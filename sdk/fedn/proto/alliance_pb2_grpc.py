# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fedn.proto import alliance_pb2 as fedn_dot_proto_dot_alliance__pb2


class ModelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.stream_unary(
                '/grpc.ModelService/Upload',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelResponse.FromString,
                )
        self.Download = channel.unary_stream(
                '/grpc.ModelService/Download',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelResponse.FromString,
                )


class ModelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.stream_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelResponse.SerializeToString,
            ),
            'Download': grpc.unary_stream_rpc_method_handler(
                    servicer.Download,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ModelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/grpc.ModelService/Upload',
            fedn_dot_proto_dot_alliance__pb2.ModelRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.ModelService/Download',
            fedn_dot_proto_dot_alliance__pb2.ModelRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class ReducerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGlobalModel = channel.unary_unary(
                '/grpc.Reducer/GetGlobalModel',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.GetGlobalModelRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.GetGlobalModelResponse.FromString,
                )


class ReducerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetGlobalModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReducerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGlobalModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGlobalModel,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.GetGlobalModelRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.GetGlobalModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.Reducer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reducer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetGlobalModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Reducer/GetGlobalModel',
            fedn_dot_proto_dot_alliance__pb2.GetGlobalModelRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.GetGlobalModelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class ConnectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AllianceStatusStream = channel.unary_stream(
                '/grpc.Connector/AllianceStatusStream',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Status.FromString,
                )
        self.SendStatus = channel.unary_unary(
                '/grpc.Connector/SendStatus',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.Status.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.ListActiveClients = channel.unary_unary(
                '/grpc.Connector/ListActiveClients',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ListClientsRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientList.FromString,
                )
        self.SendHeartbeat = channel.unary_unary(
                '/grpc.Connector/SendHeartbeat',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.Heartbeat.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.ReassignClient = channel.unary_unary(
                '/grpc.Connector/ReassignClient',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ReassignRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.ReconnectClient = channel.unary_unary(
                '/grpc.Connector/ReconnectClient',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ReconnectRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )


class ConnectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AllianceStatusStream(self, request, context):
        """Stream endpoint for status updates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendStatus(self, request, context):
        """Report endpoint
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListActiveClients(self, request, context):
        """rpc RegisterClient (ClientAvailableMessage) returns (Response);
        List active clients endpoint
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendHeartbeat(self, request, context):
        """Client messaging to stay engaged.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReassignClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReconnectClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AllianceStatusStream': grpc.unary_stream_rpc_method_handler(
                    servicer.AllianceStatusStream,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Status.SerializeToString,
            ),
            'SendStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SendStatus,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.Status.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'ListActiveClients': grpc.unary_unary_rpc_method_handler(
                    servicer.ListActiveClients,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ListClientsRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ClientList.SerializeToString,
            ),
            'SendHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartbeat,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.Heartbeat.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'ReassignClient': grpc.unary_unary_rpc_method_handler(
                    servicer.ReassignClient,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ReassignRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'ReconnectClient': grpc.unary_unary_rpc_method_handler(
                    servicer.ReconnectClient,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ReconnectRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.Connector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Connector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AllianceStatusStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Connector/AllianceStatusStream',
            fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Status.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Connector/SendStatus',
            fedn_dot_proto_dot_alliance__pb2.Status.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListActiveClients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Connector/ListActiveClients',
            fedn_dot_proto_dot_alliance__pb2.ListClientsRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ClientList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Connector/SendHeartbeat',
            fedn_dot_proto_dot_alliance__pb2.Heartbeat.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReassignClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Connector/ReassignClient',
            fedn_dot_proto_dot_alliance__pb2.ReassignRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReconnectClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Connector/ReconnectClient',
            fedn_dot_proto_dot_alliance__pb2.ReconnectRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class CombinerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ModelUpdateRequestStream = channel.unary_stream(
                '/grpc.Combiner/ModelUpdateRequestStream',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.FromString,
                )
        self.ModelUpdateStream = channel.unary_stream(
                '/grpc.Combiner/ModelUpdateStream',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdate.FromString,
                )
        self.ModelValidationRequestStream = channel.unary_stream(
                '/grpc.Combiner/ModelValidationRequestStream',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.FromString,
                )
        self.ModelValidationStream = channel.unary_stream(
                '/grpc.Combiner/ModelValidationStream',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelValidation.FromString,
                )
        self.SendModelUpdateRequest = channel.unary_unary(
                '/grpc.Combiner/SendModelUpdateRequest',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.SendModelUpdate = channel.unary_unary(
                '/grpc.Combiner/SendModelUpdate',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdate.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.SendModelValidationRequest = channel.unary_unary(
                '/grpc.Combiner/SendModelValidationRequest',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )
        self.SendModelValidation = channel.unary_unary(
                '/grpc.Combiner/SendModelValidation',
                request_serializer=fedn_dot_proto_dot_alliance__pb2.ModelValidation.SerializeToString,
                response_deserializer=fedn_dot_proto_dot_alliance__pb2.Response.FromString,
                )


class CombinerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ModelUpdateRequestStream(self, request, context):
        """Stream endpoints for training/validation pub/sub
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModelUpdateStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModelValidationRequestStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModelValidationStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendModelUpdateRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendModelUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendModelValidationRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendModelValidation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CombinerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ModelUpdateRequestStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ModelUpdateRequestStream,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.SerializeToString,
            ),
            'ModelUpdateStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ModelUpdateStream,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdate.SerializeToString,
            ),
            'ModelValidationRequestStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ModelValidationRequestStream,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.SerializeToString,
            ),
            'ModelValidationStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ModelValidationStream,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.ModelValidation.SerializeToString,
            ),
            'SendModelUpdateRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendModelUpdateRequest,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'SendModelUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.SendModelUpdate,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelUpdate.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'SendModelValidationRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendModelValidationRequest,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
            'SendModelValidation': grpc.unary_unary_rpc_method_handler(
                    servicer.SendModelValidation,
                    request_deserializer=fedn_dot_proto_dot_alliance__pb2.ModelValidation.FromString,
                    response_serializer=fedn_dot_proto_dot_alliance__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.Combiner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Combiner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ModelUpdateRequestStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Combiner/ModelUpdateRequestStream',
            fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModelUpdateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Combiner/ModelUpdateStream',
            fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelUpdate.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModelValidationRequestStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Combiner/ModelValidationRequestStream',
            fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModelValidationStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Combiner/ModelValidationStream',
            fedn_dot_proto_dot_alliance__pb2.ClientAvailableMessage.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.ModelValidation.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendModelUpdateRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Combiner/SendModelUpdateRequest',
            fedn_dot_proto_dot_alliance__pb2.ModelUpdateRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendModelUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Combiner/SendModelUpdate',
            fedn_dot_proto_dot_alliance__pb2.ModelUpdate.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendModelValidationRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Combiner/SendModelValidationRequest',
            fedn_dot_proto_dot_alliance__pb2.ModelValidationRequest.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendModelValidation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Combiner/SendModelValidation',
            fedn_dot_proto_dot_alliance__pb2.ModelValidation.SerializeToString,
            fedn_dot_proto_dot_alliance__pb2.Response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
