from concurrent import futures
import grpc
import trace_server_pb2
import trace_server_pb2_grpc
import trace_pb2
import common_pb2
import resource_pb2
import time


def run():
    # 创建与gRPC服务的连接
    with grpc.insecure_channel('127.0.0.1:10802') as channel:
        # 创建Stub（客户端）
        stub = trace_server_pb2_grpc.TraceServiceStub(channel)
        # 创建请求对象
        response = stub.Export(
            trace_server_pb2.ExportTraceServiceRequest(
                resource_spans = [
                    trace_pb2.ResourceSpans(
                        resource = resource_pb2.Resource(
                            attributes = [
                                common_pb2.KeyValue(
                                    key = "service.name",
                                    value = common_pb2.AnyValue(string_value="envoy-yucheng-test")
                                ),
                            ]
                        ),
                        scope_spans = [],
                    )
                ]
            ),
            metadata=(
                ("authentication", "test"),
                ("x-envoy-internal", "true"),
                ("x-forwarded-for", "172.17.0.2"),
                ("user-agent", "envoy-local"),
            )
        )
        # 打印响应
        print(response)

if __name__ == '__main__':
    run()
