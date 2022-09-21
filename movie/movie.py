import uuid
import grpc
from concurrent import futures

import movie_pb2_grpc
import movie_pb2
import json

class MovieServicer(movie_pb2_grpc.MovieServicer):

    def __init__(self):
        with open('{}/data/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]
    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating="", director="", id="")

    def GetListMovies(self, request, context):
        for movie in self.db:
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
            
    def CreateMovie(self, request, context):
        #generate a new id
        movie = {
            "title": request.title,
            "rating": request.rating,
            "director": request.director,
            "id": str(uuid.uuid4())
        }
        self.db.append(movie)
        return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])


    def UpdateMovie(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                movie['title'] = request.title
                movie['rating'] = request.rating
                movie['director'] = request.director
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData(title="", rating="", director="", id="")

    
    # create DeleteMovie
    def DeleteMovie(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                self
                self.db.remove(movie)
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
                
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
