import grpc

import hello_world_pb2
import hello_world_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as target:
        stub = hello_world_pb2_grpc.GreeterStub(target)
        response = stub.SayHello(hello_world_pb2.HelloRequest(name='you'))
    print("GREE" + response.message)


if __name__ == "__main__":
    run()