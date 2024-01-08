from concurrent import futures
import grpc
import trace_server_pb2
import trace_server_pb2_grpc


class Server(trace_server_pb2_grpc.TraceServiceServicer):

    def Export(self, request, context):
        print(request)
        return trace_server_pb2.ExportTraceServiceResponse(
            partial_success = trace_server_pb2.ExportTracePartialSuccess(
                rejected_spans = 0
            )
        )
    
if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    trace_server_pb2_grpc.add_TraceServiceServicer_to_server(Server(),server)
    server.add_insecure_port('[::]:10802')
    server.start()
    server.wait_for_termination()