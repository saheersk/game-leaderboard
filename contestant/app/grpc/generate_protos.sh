#!/bin/bash

# Generate gRPC Python files from the .proto definition
python -m grpc_tools.protoc \
    --proto_path=app/grpc/proto \
    --python_out=app/api/v1/grpc \
    --grpc_python_out=app/api/v1/grpc \
    contestant.proto


