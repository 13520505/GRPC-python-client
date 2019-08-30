import grpc
import pageview_pb2_grpc
import pageview_pb2
def run():
    with grpc.insecure_channel('localhost:8059') as channel:
        stub = pageview_pb2_grpc.ArticleContextServiceStub(channel)
        request = pageview_pb2.LastNClickRequest(n=10000)
        stub.GetLastNClick(request)
if __name__ == '__main__':
    run()
