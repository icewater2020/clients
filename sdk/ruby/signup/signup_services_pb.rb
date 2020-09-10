# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: signup/signup.proto for package 'go.micro.service.signup'

require 'grpc'
require 'signup/signup_pb'

module Go
  module Micro
    module Service
      module Signup
        module Signup
          class Service

            include GRPC::GenericService

            self.marshal_class_method = :encode
            self.unmarshal_class_method = :decode
            self.service_name = 'go.micro.service.signup.Signup'

            # Sends the verification email to the user
            rpc :SendVerificationEmail, ::Go::Micro::Service::Signup::SendVerificationEmailRequest, ::Go::Micro::Service::Signup::SendVerificationEmailResponse
            # Verify kicks off the process of verification
            rpc :Verify, ::Go::Micro::Service::Signup::VerifyRequest, ::Go::Micro::Service::Signup::VerifyResponse
            # Creates a subscription and an account
            rpc :CompleteSignup, ::Go::Micro::Service::Signup::CompleteSignupRequest, ::Go::Micro::Service::Signup::CompleteSignupResponse
            rpc :Recover, ::Go::Micro::Service::Signup::RecoverRequest, ::Go::Micro::Service::Signup::RecoverResponse
          end

          Stub = Service.rpc_stub_class
        end
      end
    end
  end
end
