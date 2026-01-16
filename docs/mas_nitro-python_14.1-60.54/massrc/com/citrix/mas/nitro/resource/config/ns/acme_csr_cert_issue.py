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
Configuration for ACME CSR cert issue configuration resource
'''

class acme_csr_cert_issue(base_resource):
	_activity_id= ""
	_store_type= ""
	_domain= ""
	_key_length= ""
	_key_file= ""
	_key_data= ""
	_is_auto_renewal= ""
	_file_name= ""
	_key_csr_available_on_server= ""
	_name= ""
	_acme_ca_config_id= ""
	_dns_provider_id= ""
	_file_data= ""
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
			return "acme_csr_cert_issue"
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
			return "acme_csr_cert_issues"
		except Exception as e :
			raise e



	'''
	get Activity ID of the certificate issue operation.
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Activity ID of the certificate issue operation.
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
		except Exception as e :
			raise e


	'''
	get Type of store where the certificate will be stored. It can be 'cert_store' or 'zero_touch'.
	'''
	@property
	def store_type(self) :
		try:
			return self._store_type
		except Exception as e :
			raise e
	'''
	set Type of store where the certificate will be stored. It can be 'cert_store' or 'zero_touch'.
	'''
	@store_type.setter
	def store_type(self,store_type):
		try :
			if not isinstance(store_type,str):
				raise TypeError("store_type must be set to str value")
			self._store_type = store_type
		except Exception as e :
			raise e


	'''
	get Domain name from the subject of the certificate
	'''
	@property
	def domain(self) :
		try:
			return self._domain
		except Exception as e :
			raise e
	'''
	set Domain name from the subject of the certificate
	'''
	@domain.setter
	def domain(self,domain):
		try :
			if not isinstance(domain,str):
				raise TypeError("domain must be set to str value")
			self._domain = domain
		except Exception as e :
			raise e


	'''
	get Key length used for the ACME CA configuration. Values: 1.2048, 2.4096, 3.ec-256, 4.ec-384.
	'''
	@property
	def key_length(self) :
		try:
			return self._key_length
		except Exception as e :
			raise e
	'''
	set Key length used for the ACME CA configuration. Values: 1.2048, 2.4096, 3.ec-256, 4.ec-384.
	'''
	@key_length.setter
	def key_length(self,key_length):
		try :
			if not isinstance(key_length,str):
				raise TypeError("key_length must be set to str value")
			self._key_length = key_length
		except Exception as e :
			raise e


	'''
	get Key file name
	'''
	@property
	def key_file(self) :
		try:
			return self._key_file
		except Exception as e :
			raise e
	'''
	set Key file name
	'''
	@key_file.setter
	def key_file(self,key_file):
		try :
			if not isinstance(key_file,str):
				raise TypeError("key_file must be set to str value")
			self._key_file = key_file
		except Exception as e :
			raise e


	'''
	get Base64 encoded key file contents.
	'''
	@property
	def key_data(self) :
		try:
			return self._key_data
		except Exception as e :
			raise e
	'''
	set Base64 encoded key file contents.
	'''
	@key_data.setter
	def key_data(self,key_data):
		try :
			if not isinstance(key_data,str):
				raise TypeError("key_data must be set to str value")
			self._key_data = key_data
		except Exception as e :
			raise e


	'''
	get Set to true, if the certificate should be automatically renewed before expiry.
	'''
	@property
	def is_auto_renewal(self) :
		try:
			return self._is_auto_renewal
		except Exception as e :
			raise e
	'''
	set Set to true, if the certificate should be automatically renewed before expiry.
	'''
	@is_auto_renewal.setter
	def is_auto_renewal(self,is_auto_renewal):
		try :
			if not isinstance(is_auto_renewal,bool):
				raise TypeError("is_auto_renewal must be set to bool value")
			self._is_auto_renewal = is_auto_renewal
		except Exception as e :
			raise e


	'''
	get Certificate file name.
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Certificate file name.
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Indicates whether the CSR and key have been already uploaded to the server under the default location. The same will be referred for certificate creation.
	'''
	@property
	def key_csr_available_on_server(self) :
		try:
			return self._key_csr_available_on_server
		except Exception as e :
			raise e
	'''
	set Indicates whether the CSR and key have been already uploaded to the server under the default location. The same will be referred for certificate creation.
	'''
	@key_csr_available_on_server.setter
	def key_csr_available_on_server(self,key_csr_available_on_server):
		try :
			if not isinstance(key_csr_available_on_server,bool):
				raise TypeError("key_csr_available_on_server must be set to bool value")
			self._key_csr_available_on_server = key_csr_available_on_server
		except Exception as e :
			raise e


	'''
	get Name of the new certificate issue configuration.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the new certificate issue configuration.
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get ID of the CA config that is used to issue the certificate
	'''
	@property
	def acme_ca_config_id(self) :
		try:
			return self._acme_ca_config_id
		except Exception as e :
			raise e
	'''
	set ID of the CA config that is used to issue the certificate
	'''
	@acme_ca_config_id.setter
	def acme_ca_config_id(self,acme_ca_config_id):
		try :
			if not isinstance(acme_ca_config_id,str):
				raise TypeError("acme_ca_config_id must be set to str value")
			self._acme_ca_config_id = acme_ca_config_id
		except Exception as e :
			raise e


	'''
	get ID of the DNS provider configuration used for DNS challenges.
	'''
	@property
	def dns_provider_id(self) :
		try:
			return self._dns_provider_id
		except Exception as e :
			raise e
	'''
	set ID of the DNS provider configuration used for DNS challenges.
	'''
	@dns_provider_id.setter
	def dns_provider_id(self,dns_provider_id):
		try :
			if not isinstance(dns_provider_id,str):
				raise TypeError("dns_provider_id must be set to str value")
			self._dns_provider_id = dns_provider_id
		except Exception as e :
			raise e


	'''
	get Base64 encoded CSR contents.
	'''
	@property
	def file_data(self) :
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	set Base64 encoded CSR contents.
	'''
	@file_data.setter
	def file_data(self,file_data):
		try :
			if not isinstance(file_data,str):
				raise TypeError("file_data must be set to str value")
			self._file_data = file_data
		except Exception as e :
			raise e

	'''
	Add a new ACME CSR cert issue configuration.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				acme_csr_cert_issue_obj= acme_csr_cert_issue()
				return cls.perform_operation_bulk_request(service,resource,acme_csr_cert_issue_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_csr_cert_issue_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_csr_cert_issue
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_csr_cert_issue_responses, response, "acme_csr_cert_issue_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_csr_cert_issue_response_array
				i=0
				error = [acme_csr_cert_issue() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_csr_cert_issue_response_array
			i=0
			acme_csr_cert_issue_objs = [acme_csr_cert_issue() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_csr_cert_issue'):
					for props in obj._acme_csr_cert_issue:
						result = service.payload_formatter.string_to_bulk_resource(acme_csr_cert_issue_response,self.__class__.__name__,props)
						acme_csr_cert_issue_objs[i] = result.acme_csr_cert_issue
						i=i+1
			return acme_csr_cert_issue_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_csr_cert_issue,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_csr_cert_issue_response(base_response):
	def __init__(self,length=1) :
		self.acme_csr_cert_issue= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_csr_cert_issue= [ acme_csr_cert_issue() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_csr_cert_issue_responses(base_response):
	def __init__(self,length=1) :
		self.acme_csr_cert_issue_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_csr_cert_issue_response_array = [ acme_csr_cert_issue() for _ in range(length)]
