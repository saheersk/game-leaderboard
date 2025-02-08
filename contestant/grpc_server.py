import logging
import grpc
from concurrent import futures

from app.api.v1.grpc import contestant_pb2_grpc, contestant

logging.basicConfig(level=logging.INFO)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    contestant_pb2_grpc.add_ContestantServiceServicer_to_server(
        contestant.ContestantService(), server
    )
    server.add_insecure_port("[::]:50051")
    logging.info("gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
