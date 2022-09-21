import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json
from google.protobuf.json_format import MessageToJson
class ShowtimeServicer(showtime_pb2_grpc.ShowTimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]
    # create getListShowTime
    def getListShowTime(self, request, context):
        for showtime in self.db:
            yield showtime_pb2.ShowTimeData(date=showtime['date'], moviesId=showtime['movies'])
    def getShowTime(self, request, context):
        for showtime in self.db:
            if showtime['date'] == request.date:
                return showtime_pb2.ShowTimeData(date=showtime['date'], moviesId=showtime['movies'])

        return showtime_pb2.ShowTimeData(date="Not Found", moviesId="Not Found")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowTimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
