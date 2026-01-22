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
Configuration for Third party CA provider resource
'''

class certificate_authority_management(base_resource):
	_agent_id= ""
	_client_id= ""
	_renew_before_days= ""
	_passphrase= ""
	_access_token= ""
	_ca_provider= ""
	_policy_folder_list= ""
	_name= ""
	_refresh_token= ""
	_policy_folder= ""
	_id= ""
	_api_endpoint= ""
	_is_renew= ""
	_is_deploy= ""
	_device_folder= ""
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
			return "certificate_authority_management"
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
			return "certificate_authority_managements"
		except Exception as e :
			raise e



	'''
	get Id of the agent which connects to third party CA management server
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Id of the agent which connects to third party CA management server
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
	get Client id required to make API calls to third party CA management server
	'''
	@property
	def client_id(self) :
		try:
			return self._client_id
		except Exception as e :
			raise e
	'''
	set Client id required to make API calls to third party CA management server
	'''
	@client_id.setter
	def client_id(self,client_id):
		try :
			if not isinstance(client_id,str):
				raise TypeError("client_id must be set to str value")
			self._client_id = client_id
		except Exception as e :
			raise e


	'''
	get Number of days before which certificates managed by third party CA should be renewed by NetScaler Console.Should be set only if is_renew is true.
	'''
	@property
	def renew_before_days(self) :
		try:
			return self._renew_before_days
		except Exception as e :
			raise e
	'''
	set Number of days before which certificates managed by third party CA should be renewed by NetScaler Console.Should be set only if is_renew is true.
	'''
	@renew_before_days.setter
	def renew_before_days(self,renew_before_days):
		try :
			if not isinstance(renew_before_days,int):
				raise TypeError("renew_before_days must be set to int value")
			self._renew_before_days = renew_before_days
		except Exception as e :
			raise e


	'''
	get password with which the cert/key file will be encrypted when downloading from third party CA management server
	'''
	@property
	def passphrase(self) :
		try:
			return self._passphrase
		except Exception as e :
			raise e
	'''
	set password with which the cert/key file will be encrypted when downloading from third party CA management server
	'''
	@passphrase.setter
	def passphrase(self,passphrase):
		try :
			if not isinstance(passphrase,str):
				raise TypeError("passphrase must be set to str value")
			self._passphrase = passphrase
		except Exception as e :
			raise e


	'''
	get Access token is passed in the header of every API call
	'''
	@property
	def access_token(self) :
		try:
			return self._access_token
		except Exception as e :
			raise e
	'''
	set Access token is passed in the header of every API call
	'''
	@access_token.setter
	def access_token(self,access_token):
		try :
			if not isinstance(access_token,str):
				raise TypeError("access_token must be set to str value")
			self._access_token = access_token
		except Exception as e :
			raise e


	'''
	get CA provider.Possible values are: Venafi
	'''
	@property
	def ca_provider(self) :
		try:
			return self._ca_provider
		except Exception as e :
			raise e
	'''
	set CA provider.Possible values are: Venafi
	'''
	@ca_provider.setter
	def ca_provider(self,ca_provider):
		try :
			if not isinstance(ca_provider,str):
				raise TypeError("ca_provider must be set to str value")
			self._ca_provider = ca_provider
		except Exception as e :
			raise e


	'''
	get Comma separated list of policies available under policy_folder. Applicable only if the CA provider is Venafi.
	'''
	@property
	def policy_folder_list(self) :
		try:
			return self._policy_folder_list
		except Exception as e :
			raise e
	'''
	set Comma separated list of policies available under policy_folder. Applicable only if the CA provider is Venafi.
	'''
	@policy_folder_list.setter
	def policy_folder_list(self,policy_folder_list):
		try :
			if not isinstance(policy_folder_list,str):
				raise TypeError("policy_folder_list must be set to str value")
			self._policy_folder_list = policy_folder_list
		except Exception as e :
			raise e


	'''
	get Name to identify the third party CA management server.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name to identify the third party CA management server.
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
	get Before the access token expires, application uses the refresh token to get a new set of tokens
	'''
	@property
	def refresh_token(self) :
		try:
			return self._refresh_token
		except Exception as e :
			raise e
	'''
	set Before the access token expires, application uses the refresh token to get a new set of tokens
	'''
	@refresh_token.setter
	def refresh_token(self,refresh_token):
		try :
			if not isinstance(refresh_token,str):
				raise TypeError("refresh_token must be set to str value")
			self._refresh_token = refresh_token
		except Exception as e :
			raise e


	'''
	get Policy Folder.Applicable only if the CA provider is Venafi
	'''
	@property
	def policy_folder(self) :
		try:
			return self._policy_folder
		except Exception as e :
			raise e
	'''
	set Policy Folder.Applicable only if the CA provider is Venafi
	'''
	@policy_folder.setter
	def policy_folder(self,policy_folder):
		try :
			if not isinstance(policy_folder,str):
				raise TypeError("policy_folder must be set to str value")
			self._policy_folder = policy_folder
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all third party CA management resource.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all third party CA management resource.
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
	get WebSDK endpoint for the configured third party CA management server.
	'''
	@property
	def api_endpoint(self) :
		try:
			return self._api_endpoint
		except Exception as e :
			raise e
	'''
	set WebSDK endpoint for the configured third party CA management server.
	'''
	@api_endpoint.setter
	def api_endpoint(self,api_endpoint):
		try :
			if not isinstance(api_endpoint,str):
				raise TypeError("api_endpoint must be set to str value")
			self._api_endpoint = api_endpoint
		except Exception as e :
			raise e


	'''
	get Whether Auto renewal of certificates managed by third party CA should be done by NetScaler Console.
	'''
	@property
	def is_renew(self) :
		try:
			return self._is_renew
		except Exception as e :
			raise e
	'''
	set Whether Auto renewal of certificates managed by third party CA should be done by NetScaler Console.
	'''
	@is_renew.setter
	def is_renew(self,is_renew):
		try :
			if not isinstance(is_renew,bool):
				raise TypeError("is_renew must be set to bool value")
			self._is_renew = is_renew
		except Exception as e :
			raise e


	'''
	get Whether Auto deployment of certificates managed by third party CA should be done by NetScaler Console.Should be set only if is_renew is true.
	'''
	@property
	def is_deploy(self) :
		try:
			return self._is_deploy
		except Exception as e :
			raise e
	'''
	set Whether Auto deployment of certificates managed by third party CA should be done by NetScaler Console.Should be set only if is_renew is true.
	'''
	@is_deploy.setter
	def is_deploy(self,is_deploy):
		try :
			if not isinstance(is_deploy,bool):
				raise TypeError("is_deploy must be set to bool value")
			self._is_deploy = is_deploy
		except Exception as e :
			raise e


	'''
	get Device Folder.Applicable only if the CA provider is Venafi
	'''
	@property
	def device_folder(self) :
		try:
			return self._device_folder
		except Exception as e :
			raise e
	'''
	set Device Folder.Applicable only if the CA provider is Venafi
	'''
	@device_folder.setter
	def device_folder(self,device_folder):
		try :
			if not isinstance(device_folder,str):
				raise TypeError("device_folder must be set to str value")
			self._device_folder = device_folder
		except Exception as e :
			raise e

	'''
	Use this operation to get third party CA management resource..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				certificate_authority_management_obj=certificate_authority_management()
				response = certificate_authority_management_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Applicable only for Venafi.Use this operation to get the policy folder list..
	'''
	@classmethod
	def get_policy_folders(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"get_policy_folders")
				return res
			else : 
				certificate_authority_management_obj= certificate_authority_management()
				return cls.perform_operation_bulk_request(service,"get_policy_folders",resource,certificate_authority_management_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete third party CA management..
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
					certificate_authority_management_obj=certificate_authority_management()
					return cls.delete_bulk_request(client,resource,certificate_authority_management_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify third party CA management..
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				certificate_authority_management_obj=certificate_authority_management()
				return cls.update_bulk_request(client,resource,certificate_authority_management_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add third party CA management..
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
				certificate_authority_management_obj= certificate_authority_management()
				return cls.perform_operation_bulk_request(service,resource,certificate_authority_management_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of certificate_authority_management resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			certificate_authority_management_obj = certificate_authority_management()
			option_ = options()
			option_._filter=filter_
			return certificate_authority_management_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the certificate_authority_management resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			certificate_authority_management_obj = certificate_authority_management()
			option_ = options()
			option_._count=True
			response = certificate_authority_management_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of certificate_authority_management resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			certificate_authority_management_obj = certificate_authority_management()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = certificate_authority_management_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(certificate_authority_management_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.certificate_authority_management
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(certificate_authority_management_responses, response, "certificate_authority_management_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.certificate_authority_management_response_array
				i=0
				error = [certificate_authority_management() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.certificate_authority_management_response_array
			i=0
			certificate_authority_management_objs = [certificate_authority_management() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_certificate_authority_management'):
					for props in obj._certificate_authority_management:
						result = service.payload_formatter.string_to_bulk_resource(certificate_authority_management_response,self.__class__.__name__,props)
						certificate_authority_management_objs[i] = result.certificate_authority_management
						i=i+1
			return certificate_authority_management_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(certificate_authority_management,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class certificate_authority_management_response(base_response):
	def __init__(self,length=1) :
		self.certificate_authority_management= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.certificate_authority_management= [ certificate_authority_management() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class certificate_authority_management_responses(base_response):
	def __init__(self,length=1) :
		self.certificate_authority_management_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.certificate_authority_management_response_array = [ certificate_authority_management() for _ in range(length)]
