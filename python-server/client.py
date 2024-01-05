from concurrent import futures
import grpc
import trace_server_pb2
import trace_server_pb2_grpc
import trace_pb2
import common_pb2
import resource_pb2

def run():
    # 创建与gRPC服务的连接
    with grpc.insecure_channel('localhost:10802') as channel:
        # 创建Stub（客户端）
        stub = trace_server_pb2_grpc.TraceServiceStub(channel)
        # 创建请求对象
        response = stub.Export(trace_server_pb2.ExportTraceServiceRequest(
            resource_spans = [
                trace_pb2.ResourceSpans(
                    resource = resource_pb2.Resource(
                        attributes = [
                            # common_pb2.KeyValue(
                            #     key = "k1",
                            #     value = 10
                            # ),
                            # common_pb2.KeyValue(
                            #     key = "k2",
                            #     value = 11
                            # )
                        ],
                        dropped_attributes_count = 0
                    ),
                    scope_spans = [],
                    schema_url = "test"
                )
            ]
        ))
        # 打印响应
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
