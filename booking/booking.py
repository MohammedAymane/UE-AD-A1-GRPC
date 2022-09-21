import grpc
import json
 
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc
from google.protobuf.json_format import MessageToJson


def check_if_date_exists(stub,date, movieid):
    print(movieid in stub.getShowTime(date).moviesId)
    return (movieid in stub.getShowTime(date).moviesId and stub.getShowTime(date).date != "Not Found")

class BookingServicer(booking_pb2_grpc.BookingServicer):
   def __init__(self):
      with open('{}/data/bookings.json'.format("."), "r") as jsf:
        self.db = json.load(jsf)["bookings"]

   def getBooking(self, request, context):
      for booking in self.db:
         if booking['userid'] == request.userid:
               return booking_pb2.BookingDataGet(userid=booking['userid'], dates=booking['dates'])
      return booking_pb2.BookingDataGet(userid="Not Found", dates="Not Found")


   def getListBookings(self, request, context):
      for booking in self.db:
         yield booking_pb2.BookingDataGet(userid=booking['userid'], dates=booking['dates'])
 
   def createBooking(self, request, context):
      print(request)
      # check if the date is available using the showtime service and grpc client
      with grpc.insecure_channel('localhost:3002') as channel: ## WITH GRPC
            
            stub = showtime_pb2_grpc.ShowTimeStub(channel)
            if(not check_if_date_exists(stub, showtime_pb2.showDate(date=request.date), request.movieid)):
               print("Date not found")
               channel.close()
               return booking_pb2.BookingDataGet(userid="", dates="")
               
      channel.close()
      for booking in self.db:
         if booking['userid'] == request.userid:
            for date in booking['dates']:
               if date['date'] == request.date:
                  date['movies'].append(request.movieid)
                  return booking_pb2.BookingDataGet(userid=booking['userid'], dates=booking['dates'])
            booking['dates'].append({"date":request.date,"movies":[request.movieid]})
            return booking_pb2.BookingDataGet(userid=booking['userid'], dates=booking['dates'])







def serve():
      server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
      booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
      server.add_insecure_port('[::]:10000')
      server.start()
      server.wait_for_termination()



if __name__ == "__main__":
   serve()
   
