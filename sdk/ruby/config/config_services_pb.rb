# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: config/config.proto for package 'config'

require 'grpc'
require 'config/config_pb'

module Config
  module Config
    class Service

      include GRPC::GenericService

      self.marshal_class_method = :encode
      self.unmarshal_class_method = :decode
      self.service_name = 'config.Config'

      rpc :Create, ::Config::CreateRequest, ::Config::CreateResponse
      rpc :Update, ::Config::UpdateRequest, ::Config::UpdateResponse
      rpc :Delete, ::Config::DeleteRequest, ::Config::DeleteResponse
      rpc :List, ::Config::ListRequest, ::Config::ListResponse
      rpc :Read, ::Config::ReadRequest, ::Config::ReadResponse
      rpc :Watch, ::Config::WatchRequest, stream(::Config::WatchResponse)
    end

    Stub = Service.rpc_stub_class
  end
end
