package org.example;


import io.grpc.stub.StreamObserver;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.opentelemetry.proto.collector.trace.v1.ExportTraceServiceRequest;
import io.opentelemetry.proto.collector.trace.v1.ExportTraceServiceResponse;
import io.opentelemetry.proto.collector.trace.v1.TraceServiceGrpc;

import java.io.File;
import java.io.IOException;

public class OtlpTraceService extends TraceServiceGrpc.TraceServiceImplBase {

    public static void main(String[] args) throws IOException, InterruptedException {
        new OtlpTraceService().start(args);
    }

    private void start(String[] args) throws IOException, InterruptedException {
        int port = 10802;
        Server server = ServerBuilder.forPort(port)
//                .useTransportSecurity(new File("/Users/liuxiaorui/Documents/codes/self-certs/certificate.crt"), new File("/Users/liuxiaorui/Documents/codes/self-certs/server.pem"))
                .addService(this)
                .build();
        server.start();
        server.awaitTermination();
    }

    @Override
    public void export(ExportTraceServiceRequest request, StreamObserver<ExportTraceServiceResponse> responseObserver) {
        System.out.println("otlp-trace-service export");
        responseObserver.onCompleted();
    }
}