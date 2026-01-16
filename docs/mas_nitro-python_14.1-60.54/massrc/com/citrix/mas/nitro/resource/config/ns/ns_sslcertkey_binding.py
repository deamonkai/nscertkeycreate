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
Configuration for SSL certificate Vs entity bindings on NetScaler resource
'''

class ns_sslcertkey_binding(base_resource):
	_poll_time= ""
	_entity_name= ""
	_entity_type= ""
	_partition_name= ""
	_display_name= ""
	_ns_ip_address= ""
	_hostname= ""
	_certkeypair_name= ""
	_id= ""
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
			return "ns_sslcertkey_binding"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "ns_sslcertkey_bindings"
		except Exception as e :
			raise e



	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get Name of the SSL LB Vserver or Service or Service Group to which the certificate is bound
	'''
	@property
	def entity_name(self) :
		try:
			return self._entity_name
		except Exception as e :
			raise e


	'''
	get Entity type.Indicates sslvserver,service
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e


	'''
	get Name of Admin Partition. Blank means Default Partition
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Display Name of the device
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
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
	get Host Name of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get Cert Key Pair Name
	'''
	@property
	def certkeypair_name(self) :
		try:
			return self._certkeypair_name
		except Exception as e :
			raise e
	'''
	set Cert Key Pair Name
	'''
	@certkeypair_name.setter
	def certkeypair_name(self,certkeypair_name):
		try :
			if not isinstance(certkeypair_name,str):
				raise TypeError("certkeypair_name must be set to str value")
			self._certkeypair_name = certkeypair_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all ssl cert-keys entries. 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all ssl cert-keys entries. 
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sslcertkey_binding
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sslcertkey_binding_responses, response, "ns_sslcertkey_binding_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sslcertkey_binding_response_array
				i=0
				error = [ns_sslcertkey_binding() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sslcertkey_binding_response_array
			i=0
			ns_sslcertkey_binding_objs = [ns_sslcertkey_binding() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sslcertkey_binding'):
					for props in obj._ns_sslcertkey_binding:
						result = service.payload_formatter.string_to_bulk_resource(ns_sslcertkey_binding_response,self.__class__.__name__,props)
						ns_sslcertkey_binding_objs[i] = result.ns_sslcertkey_binding
						i=i+1
			return ns_sslcertkey_binding_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sslcertkey_binding,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sslcertkey_binding_response(base_response):
	def __init__(self,length=1) :
		self.ns_sslcertkey_binding= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sslcertkey_binding= [ ns_sslcertkey_binding() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sslcertkey_binding_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sslcertkey_binding_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sslcertkey_binding_response_array = [ ns_sslcertkey_binding() for _ in range(length)]
