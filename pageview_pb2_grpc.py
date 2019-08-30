# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pageview_pb2 as pageview__pb2


class SessionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSession = channel.unary_unary(
        '/SessionService/GetSession',
        request_serializer=pageview__pb2.PRequestInfo.SerializeToString,
        response_deserializer=pageview__pb2.PSession.FromString,
        )
    self.Ping = channel.unary_unary(
        '/SessionService/Ping',
        request_serializer=pageview__pb2.PingRequest.SerializeToString,
        response_deserializer=pageview__pb2.PingResponse.FromString,
        )


class SessionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SessionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSession': grpc.unary_unary_rpc_method_handler(
          servicer.GetSession,
          request_deserializer=pageview__pb2.PRequestInfo.FromString,
          response_serializer=pageview__pb2.PSession.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=pageview__pb2.PingRequest.FromString,
          response_serializer=pageview__pb2.PingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SessionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ArticleContextServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetArticleContext = channel.unary_unary(
        '/ArticleContextService/GetArticleContext',
        request_serializer=pageview__pb2.ArticleRequest.SerializeToString,
        response_deserializer=pageview__pb2.ArticleContext.FromString,
        )
    self.GetLastNClick = channel.unary_unary(
        '/ArticleContextService/GetLastNClick',
        request_serializer=pageview__pb2.LastNClickRequest.SerializeToString,
        response_deserializer=pageview__pb2.LastNClick.FromString,
        )


class ArticleContextServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetArticleContext(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLastNClick(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ArticleContextServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetArticleContext': grpc.unary_unary_rpc_method_handler(
          servicer.GetArticleContext,
          request_deserializer=pageview__pb2.ArticleRequest.FromString,
          response_serializer=pageview__pb2.ArticleContext.SerializeToString,
      ),
      'GetLastNClick': grpc.unary_unary_rpc_method_handler(
          servicer.GetLastNClick,
          request_deserializer=pageview__pb2.LastNClickRequest.FromString,
          response_serializer=pageview__pb2.LastNClick.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ArticleContextService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
