# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from router import router_pb2 as router_dot_router__pb2


class RouterStub(object):
    """Router service is used by the proxy to lookup routes
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Lookup = channel.unary_unary(
                '/router.Router/Lookup',
                request_serializer=router_dot_router__pb2.LookupRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.LookupResponse.FromString,
                )
        self.Watch = channel.unary_stream(
                '/router.Router/Watch',
                request_serializer=router_dot_router__pb2.WatchRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.Event.FromString,
                )


class RouterServicer(object):
    """Router service is used by the proxy to lookup routes
    """

    def Lookup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RouterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.Lookup,
                    request_deserializer=router_dot_router__pb2.LookupRequest.FromString,
                    response_serializer=router_dot_router__pb2.LookupResponse.SerializeToString,
            ),
            'Watch': grpc.unary_stream_rpc_method_handler(
                    servicer.Watch,
                    request_deserializer=router_dot_router__pb2.WatchRequest.FromString,
                    response_serializer=router_dot_router__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'router.Router', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Router(object):
    """Router service is used by the proxy to lookup routes
    """

    @staticmethod
    def Lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/router.Router/Lookup',
            router_dot_router__pb2.LookupRequest.SerializeToString,
            router_dot_router__pb2.LookupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/router.Router/Watch',
            router_dot_router__pb2.WatchRequest.SerializeToString,
            router_dot_router__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TableStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/router.Table/Create',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.CreateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/router.Table/Delete',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.DeleteResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/router.Table/Update',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.UpdateResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/router.Table/Read',
                request_serializer=router_dot_router__pb2.ReadRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.ReadResponse.FromString,
                )


class TableServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TableServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=router_dot_router__pb2.Route.FromString,
                    response_serializer=router_dot_router__pb2.CreateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=router_dot_router__pb2.Route.FromString,
                    response_serializer=router_dot_router__pb2.DeleteResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=router_dot_router__pb2.Route.FromString,
                    response_serializer=router_dot_router__pb2.UpdateResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=router_dot_router__pb2.ReadRequest.FromString,
                    response_serializer=router_dot_router__pb2.ReadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'router.Table', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Table(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/router.Table/Create',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/router.Table/Delete',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/router.Table/Update',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/router.Table/Read',
            router_dot_router__pb2.ReadRequest.SerializeToString,
            router_dot_router__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
