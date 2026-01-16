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
Configuration for Account Takeover Configuration from GUI resource
'''

class account_takeover_config(base_resource):
	_method= ""
	_url= ""
	_parent_name= ""
	_parent_id= ""
	_id= ""
	_success_response_code= ""
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
			return "account_takeover_config"
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
			return "account_takeover_configs"
		except Exception as e :
			raise e



	'''
	get response code for failure and login
	'''
	@property
	def method(self) :
		try:
			return self._method
		except Exception as e :
			raise e
	'''
	set response code for failure and login
	'''
	@method.setter
	def method(self,method):
		try :
			if not isinstance(method,str):
				raise TypeError("method must be set to str value")
			self._method = method
		except Exception as e :
			raise e


	'''
	get Url for login
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set Url for login
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e


	'''
	get Resource name of parent resource
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Resource name of parent resource
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Id of the parent resource
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id of the parent resource
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Primary key for this table.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Primary key for this table.
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
	get response code for failure and login
	'''
	@property
	def success_response_code(self) :
		try:
			return self._success_response_code
		except Exception as e :
			raise e
	'''
	set response code for failure and login
	'''
	@success_response_code.setter
	def success_response_code(self,success_response_code):
		try :
			if not isinstance(success_response_code,str):
				raise TypeError("success_response_code must be set to str value")
			self._success_response_code = success_response_code
		except Exception as e :
			raise e

	'''
	Use this operation to delete configuration.
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
					account_takeover_config_obj=account_takeover_config()
					return cls.delete_bulk_request(client,resource,account_takeover_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify configuration.
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
				account_takeover_config_obj=account_takeover_config()
				return cls.update_bulk_request(client,resource,account_takeover_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add configuration.
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
				account_takeover_config_obj= account_takeover_config()
				return cls.perform_operation_bulk_request(service,resource,account_takeover_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to fetch configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				account_takeover_config_obj=account_takeover_config()
				response = account_takeover_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of account_takeover_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			account_takeover_config_obj = account_takeover_config()
			option_ = options()
			option_._filter=filter_
			return account_takeover_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the account_takeover_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			account_takeover_config_obj = account_takeover_config()
			option_ = options()
			option_._count=True
			response = account_takeover_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of account_takeover_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			account_takeover_config_obj = account_takeover_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = account_takeover_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(account_takeover_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.account_takeover_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(account_takeover_config_responses, response, "account_takeover_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.account_takeover_config_response_array
				i=0
				error = [account_takeover_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.account_takeover_config_response_array
			i=0
			account_takeover_config_objs = [account_takeover_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_account_takeover_config'):
					for props in obj._account_takeover_config:
						result = service.payload_formatter.string_to_bulk_resource(account_takeover_config_response,self.__class__.__name__,props)
						account_takeover_config_objs[i] = result.account_takeover_config
						i=i+1
			return account_takeover_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(account_takeover_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class account_takeover_config_response(base_response):
	def __init__(self,length=1) :
		self.account_takeover_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.account_takeover_config= [ account_takeover_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class account_takeover_config_responses(base_response):
	def __init__(self,length=1) :
		self.account_takeover_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.account_takeover_config_response_array = [ account_takeover_config() for _ in range(length)]
