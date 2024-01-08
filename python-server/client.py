from concurrent import futures
import grpc
import trace_server_pb2
import trace_server_pb2_grpc
import trace_pb2
import common_pb2
import resource_pb2

def run():
    # 创建与gRPC服务的连接
    with grpc.insecure_channel('127.0.0.1:10802') as channel:
        # 创建Stub（客户端）
        stub = trace_server_pb2_grpc.TraceServiceStub(channel)
        # 创建请求对象
        response = stub.Export(trace_server_pb2.ExportTraceServiceRequest(
            resource_spans = [
                trace_pb2.ResourceSpans(
                    resource = resource_pb2.Resource(
                        attributes = [
                            common_pb2.KeyValue(
                                key = "service.name",
                                value = common_pb2.AnyValue(string_value="envoy-yucheng-test")
                            ),
                            # common_pb2.KeyValue(
                            #     key = "k2",
                            #     value = 11
                            # )
                        ]
                    ),
                    scope_spans = [],
                )
            ]
        ))
        # 打印响应
        print(response)

if __name__ == '__main__':
    run()
