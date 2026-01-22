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
from massrc.com.citrix.mas.nitro.resource.config.mps.acme_access_parameters import acme_access_parameters


'''
Configuration for ACME CA Configuration resource
'''

class acme_ca_config(base_resource):
	_id= ""
	_agent_type= ""
	_acme_server_config_map=[]
	_key_length= ""
	_email_id= ""
	_status= ""
	_renew_interval= ""
	_updated_time= ""
	_acme_ca_server_type= ""
	_challenge_type= ""
	_agent_id= ""
	_is_enabled= ""
	_name= ""
	_created_time= ""
	_get_by_draft_status= ""
	_is_incomplete_deployment= ""
	_supported_ca_list= ""
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
			return "acme_ca_config"
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
			return "acme_ca_configs"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for all ACME CA entries.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all ACME CA entries.
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
	get Type of agent. Values: 1.External_Agent, 2. Inbuilt_Agent
	'''
	@property
	def agent_type(self) :
		try:
			return self._agent_type
		except Exception as e :
			raise e


	'''
	get Array of key and value for acme server configuration
	'''
	@property
	def acme_server_config_map(self) :
		try:
			return self._acme_server_config_map
		except Exception as e :
			raise e
	'''
	set Array of key and value for acme server configuration
	'''
	@acme_server_config_map.setter
	def acme_server_config_map(self,acme_server_config_map) :
		try :
			if not isinstance(acme_server_config_map,list):
				raise TypeError("acme_server_config_map must be set to array of acme_access_parameters value")
			for item in acme_server_config_map :
				if not isinstance(item,acme_access_parameters):
					raise TypeError("item must be set to acme_access_parameters value")
			self._acme_server_config_map = acme_server_config_map
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
	get Email Address used for ACME CA configuration
	'''
	@property
	def email_id(self) :
		try:
			return self._email_id
		except Exception as e :
			raise e
	'''
	set Email Address used for ACME CA configuration
	'''
	@email_id.setter
	def email_id(self,email_id):
		try :
			if not isinstance(email_id,str):
				raise TypeError("email_id must be set to str value")
			self._email_id = email_id
		except Exception as e :
			raise e


	'''
	get DRAFT/COMPLETE. Status of the ACME CA configuration. DRAFT means the configuration is not yet complete and cannot be used for certificate issue/renew. COMPLETE means the configuration is complete and can be used for certificate issue/renew.
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set DRAFT/COMPLETE. Status of the ACME CA configuration. DRAFT means the configuration is not yet complete and cannot be used for certificate issue/renew. COMPLETE means the configuration is complete and can be used for certificate issue/renew.
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Expiry day for renewing the certificate
	'''
	@property
	def renew_interval(self) :
		try:
			return self._renew_interval
		except Exception as e :
			raise e
	'''
	set Expiry day for renewing the certificate
	'''
	@renew_interval.setter
	def renew_interval(self,renew_interval):
		try :
			if not isinstance(renew_interval,int):
				raise TypeError("renew_interval must be set to int value")
			self._renew_interval = renew_interval
		except Exception as e :
			raise e


	'''
	get Time when the ACME CA configuration was last updated in seconds
	'''
	@property
	def updated_time(self) :
		try:
			return self._updated_time
		except Exception as e :
			raise e
	'''
	set Time when the ACME CA configuration was last updated in seconds
	'''
	@updated_time.setter
	def updated_time(self,updated_time):
		try :
			if not isinstance(updated_time,float):
				raise TypeError("updated_time must be set to float value")
			self._updated_time = updated_time
		except Exception as e :
			raise e


	'''
	get ACME CA Server Type. Values: 1.LETS_ENCRYPT, 2. DIGICERT
	'''
	@property
	def acme_ca_server_type(self) :
		try:
			return self._acme_ca_server_type
		except Exception as e :
			raise e
	'''
	set ACME CA Server Type. Values: 1.LETS_ENCRYPT, 2. DIGICERT
	'''
	@acme_ca_server_type.setter
	def acme_ca_server_type(self,acme_ca_server_type):
		try :
			if not isinstance(acme_ca_server_type,str):
				raise TypeError("acme_ca_server_type must be set to str value")
			self._acme_ca_server_type = acme_ca_server_type
		except Exception as e :
			raise e


	'''
	get Challenge type used for ACME CA configuration. Values: 1.HTTP-01, 2.DNS-01, 3.TLS-ALPN-01
	'''
	@property
	def challenge_type(self) :
		try:
			return self._challenge_type
		except Exception as e :
			raise e
	'''
	set Challenge type used for ACME CA configuration. Values: 1.HTTP-01, 2.DNS-01, 3.TLS-ALPN-01
	'''
	@challenge_type.setter
	def challenge_type(self,challenge_type):
		try :
			if not isinstance(challenge_type,str):
				raise TypeError("challenge_type must be set to str value")
			self._challenge_type = challenge_type
		except Exception as e :
			raise e


	'''
	get ID of the agent that is used to connect to ACME CA server
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set ID of the agent that is used to connect to ACME CA server
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get Set to true, if the CA is enabled for certificate issue/renew
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set Set to true, if the CA is enabled for certificate issue/renew
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get Name of the CA Configuration. This is a user defined name for the ACME CA configuration.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the CA Configuration. This is a user defined name for the ACME CA configuration.
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
	get Time when the ACME CA configuration was created in seconds
	'''
	@property
	def created_time(self) :
		try:
			return self._created_time
		except Exception as e :
			raise e
	'''
	set Time when the ACME CA configuration was created in seconds
	'''
	@created_time.setter
	def created_time(self,created_time):
		try :
			if not isinstance(created_time,float):
				raise TypeError("created_time must be set to float value")
			self._created_time = created_time
		except Exception as e :
			raise e

	'''
	Set to true, if only DRAFT status ACME CA configurations need to be fetched
	'''
	@property
	def get_by_draft_status(self):
		try:
			return self._get_by_draft_status
		except Exception as e :
			raise e
	'''
	Set to true, if only DRAFT status ACME CA configurations need to be fetched
	'''
	@get_by_draft_status.setter
	def get_by_draft_status(self,get_by_draft_status):
		try :
			if not isinstance(get_by_draft_status,bool):
				raise TypeError("get_by_draft_status must be set to bool value")
			self._get_by_draft_status = get_by_draft_status
		except Exception as e :
			raise e

	'''
	Set to true, if the CA configuration is incomplete and cannot be used for certificate issue/renew
	'''
	@property
	def is_incomplete_deployment(self):
		try:
			return self._is_incomplete_deployment
		except Exception as e :
			raise e
	'''
	Set to true, if the CA configuration is incomplete and cannot be used for certificate issue/renew
	'''
	@is_incomplete_deployment.setter
	def is_incomplete_deployment(self,is_incomplete_deployment):
		try :
			if not isinstance(is_incomplete_deployment,bool):
				raise TypeError("is_incomplete_deployment must be set to bool value")
			self._is_incomplete_deployment = is_incomplete_deployment
		except Exception as e :
			raise e

	'''
	Set to true, if only password needs to be updated during update operation
	'''
	@property
	def supported_ca_list(self):
		try:
			return self._supported_ca_list
		except Exception as e :
			raise e
	'''
	Set to true, if only password needs to be updated during update operation
	'''
	@supported_ca_list.setter
	def supported_ca_list(self,supported_ca_list):
		try :
			if not isinstance(supported_ca_list,bool):
				raise TypeError("supported_ca_list must be set to bool value")
			self._supported_ca_list = supported_ca_list
		except Exception as e :
			raise e

	'''
	Delete ACME CA configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					acme_ca_config_obj=acme_ca_config()
					return cls.delete_bulk_request(client,resource,acme_ca_config_obj)
		except Exception as e :
			raise e

	'''
	get ACME CA configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				acme_ca_config_obj=acme_ca_config()
				response = acme_ca_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify ACME CA configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				acme_ca_config_obj=acme_ca_config()
				return cls.update_bulk_request(client,resource,acme_ca_config_obj)
		except Exception as e :
			raise e

	'''
	add ACME CA configuration.
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
				acme_ca_config_obj= acme_ca_config()
				return cls.perform_operation_bulk_request(service,resource,acme_ca_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of acme_ca_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			acme_ca_config_obj = acme_ca_config()
			option_ = options()
			option_._filter=filter_
			return acme_ca_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the acme_ca_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			acme_ca_config_obj = acme_ca_config()
			option_ = options()
			option_._count=True
			response = acme_ca_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of acme_ca_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			acme_ca_config_obj = acme_ca_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = acme_ca_config_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_ca_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_ca_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_ca_config_responses, response, "acme_ca_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_ca_config_response_array
				i=0
				error = [acme_ca_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_ca_config_response_array
			i=0
			acme_ca_config_objs = [acme_ca_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_ca_config'):
					for props in obj._acme_ca_config:
						result = service.payload_formatter.string_to_bulk_resource(acme_ca_config_response,self.__class__.__name__,props)
						acme_ca_config_objs[i] = result.acme_ca_config
						i=i+1
			return acme_ca_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_ca_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_ca_config_response(base_response):
	def __init__(self,length=1) :
		self.acme_ca_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_ca_config= [ acme_ca_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_ca_config_responses(base_response):
	def __init__(self,length=1) :
		self.acme_ca_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_ca_config_response_array = [ acme_ca_config() for _ in range(length)]
