# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
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
                '/go.micro.router.Router/Lookup',
                request_serializer=router_dot_router__pb2.LookupRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.LookupResponse.FromString,
                )
        self.Watch = channel.unary_stream(
                '/go.micro.router.Router/Watch',
                request_serializer=router_dot_router__pb2.WatchRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.Event.FromString,
                )
        self.Advertise = channel.unary_stream(
                '/go.micro.router.Router/Advertise',
                request_serializer=router_dot_router__pb2.Request.SerializeToString,
                response_deserializer=router_dot_router__pb2.Advert.FromString,
                )
        self.Process = channel.unary_unary(
                '/go.micro.router.Router/Process',
                request_serializer=router_dot_router__pb2.Advert.SerializeToString,
                response_deserializer=router_dot_router__pb2.ProcessResponse.FromString,
                )


class RouterServicer(object):
    """Router service is used by the proxy to lookup routes
    """

    def Lookup(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Advertise(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Process(self, request, context):
        """Missing associated documentation comment in .proto file"""
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
            'Advertise': grpc.unary_stream_rpc_method_handler(
                    servicer.Advertise,
                    request_deserializer=router_dot_router__pb2.Request.FromString,
                    response_serializer=router_dot_router__pb2.Advert.SerializeToString,
            ),
            'Process': grpc.unary_unary_rpc_method_handler(
                    servicer.Process,
                    request_deserializer=router_dot_router__pb2.Advert.FromString,
                    response_serializer=router_dot_router__pb2.ProcessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'go.micro.router.Router', rpc_method_handlers)
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
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Router/Lookup',
            router_dot_router__pb2.LookupRequest.SerializeToString,
            router_dot_router__pb2.LookupResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/go.micro.router.Router/Watch',
            router_dot_router__pb2.WatchRequest.SerializeToString,
            router_dot_router__pb2.Event.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Advertise(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/go.micro.router.Router/Advertise',
            router_dot_router__pb2.Request.SerializeToString,
            router_dot_router__pb2.Advert.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Process(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Router/Process',
            router_dot_router__pb2.Advert.SerializeToString,
            router_dot_router__pb2.ProcessResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class TableStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/go.micro.router.Table/Create',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.CreateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/go.micro.router.Table/Delete',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.DeleteResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/go.micro.router.Table/Update',
                request_serializer=router_dot_router__pb2.Route.SerializeToString,
                response_deserializer=router_dot_router__pb2.UpdateResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/go.micro.router.Table/List',
                request_serializer=router_dot_router__pb2.Request.SerializeToString,
                response_deserializer=router_dot_router__pb2.ListResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/go.micro.router.Table/Query',
                request_serializer=router_dot_router__pb2.QueryRequest.SerializeToString,
                response_deserializer=router_dot_router__pb2.QueryResponse.FromString,
                )


class TableServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file"""
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
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=router_dot_router__pb2.Request.FromString,
                    response_serializer=router_dot_router__pb2.ListResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=router_dot_router__pb2.QueryRequest.FromString,
                    response_serializer=router_dot_router__pb2.QueryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'go.micro.router.Table', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Table(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Table/Create',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.CreateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Table/Delete',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Table/Update',
            router_dot_router__pb2.Route.SerializeToString,
            router_dot_router__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Table/List',
            router_dot_router__pb2.Request.SerializeToString,
            router_dot_router__pb2.ListResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/go.micro.router.Table/Query',
            router_dot_router__pb2.QueryRequest.SerializeToString,
            router_dot_router__pb2.QueryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)