'''
Copyright (c) 2008-2020 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for NetScaler SSL Certificate Link resource
'''

class ns_ssl_certlink(base_resource):
	_certkey= ""
	_linkcertkeyname= ""
	_ns_ip_address= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ns_ssl_certlink"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "ns_ssl_certlinks"
		except Exception as e :
			raise e



	'''
	get Certificate Name
	'''
	@property
	def certkey(self) :
		try:
			return self._certkey
		except Exception as e :
			raise e
	'''
	set Certificate Name
	'''
	@certkey.setter
	def certkey(self,certkey):
		try :
			if not isinstance(certkey,str):
				raise TypeError("certkey must be set to str value")
			self._certkey = certkey
		except Exception as e :
			raise e


	'''
	get Certificate Name To Link
	'''
	@property
	def linkcertkeyname(self) :
		try:
			return self._linkcertkeyname
		except Exception as e :
			raise e
	'''
	set Certificate Name To Link
	'''
	@linkcertkeyname.setter
	def linkcertkeyname(self,linkcertkeyname):
		try :
			if not isinstance(linkcertkeyname,str):
				raise TypeError("linkcertkeyname must be set to str value")
			self._linkcertkeyname = linkcertkeyname
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to link certificate.
	'''
	@classmethod
	def link(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"link")
				return res
			else : 
				ns_ssl_certlink_obj= ns_ssl_certlink()
				return cls.perform_operation_bulk_request(service,"link",resource,ns_ssl_certlink_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to unlink certificate.
	'''
	@classmethod
	def unlink(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"unlink")
				return res
			else : 
				ns_ssl_certlink_obj= ns_ssl_certlink()
				return cls.perform_operation_bulk_request(service,"unlink",resource,ns_ssl_certlink_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_certlink_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_certlink
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_certlink_responses, response, "ns_ssl_certlink_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_certlink_response_array
				i=0
				error = [ns_ssl_certlink() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_certlink_response_array
			i=0
			ns_ssl_certlink_objs = [ns_ssl_certlink() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_certlink'):
					for props in obj._ns_ssl_certlink:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_certlink_response,self.__class__.__name__,props)
						ns_ssl_certlink_objs[i] = result.ns_ssl_certlink
						i=i+1
			return ns_ssl_certlink_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_certlink,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_certlink_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certlink= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_certlink= [ ns_ssl_certlink() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_certlink_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certlink_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_certlink_response_array = [ ns_ssl_certlink() for _ in range(length)]
