FROM python:3.9.19

COPY ./ /app
WORKDIR /app

RUN pip install grpcio grpcio-tools

CMD ["python3", "server.py"]

# docker build -t liuxr25/demo-app:grpc-py-traceserver .
# docker run --rm -ti -p 10802:10802 liuxr25/demo-app:grpc-py-traceserver
# docker run --rm -ti -p 10802:10802 -v $(pwd)/server.py:/app/server.py liuxr25/demo-app:grpc-py-traceserver
# docker run --rm -ti --network host liuxr25/demo-app:grpc-py-traceserver bash