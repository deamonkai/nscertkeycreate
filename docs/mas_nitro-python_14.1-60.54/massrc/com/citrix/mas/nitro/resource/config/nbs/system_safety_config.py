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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for System Safety Config resource
'''

class system_safety_config(base_resource):
	_not_compliant= ""
	_compliant= ""
	_ip_address= ""
	_sys_group_desc= ""
	_recommended_action_desc= ""
	_sub_group_desc= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/security/system_safety_config"
		except Exception as e :
			raise e

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
			return "system_safety_config"
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
			return "system_safety_configs"
		except Exception as e :
			raise e



	'''
	get not_compliant.
	'''
	@property
	def not_compliant(self) :
		try:
			return self._not_compliant
		except Exception as e :
			raise e
	'''
	set not_compliant.
	'''
	@not_compliant.setter
	def not_compliant(self,not_compliant):
		try :
			if not isinstance(not_compliant,int):
				raise TypeError("not_compliant must be set to int value")
			self._not_compliant = not_compliant
		except Exception as e :
			raise e


	'''
	get compliant.
	'''
	@property
	def compliant(self) :
		try:
			return self._compliant
		except Exception as e :
			raise e
	'''
	set compliant.
	'''
	@compliant.setter
	def compliant(self,compliant):
		try :
			if not isinstance(compliant,int):
				raise TypeError("compliant must be set to int value")
			self._compliant = compliant
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get System Group Desc
	'''
	@property
	def sys_group_desc(self) :
		try:
			return self._sys_group_desc
		except Exception as e :
			raise e
	'''
	set System Group Desc
	'''
	@sys_group_desc.setter
	def sys_group_desc(self,sys_group_desc):
		try :
			if not isinstance(sys_group_desc,str):
				raise TypeError("sys_group_desc must be set to str value")
			self._sys_group_desc = sys_group_desc
		except Exception as e :
			raise e


	'''
	get Recommended Action Desc
	'''
	@property
	def recommended_action_desc(self) :
		try:
			return self._recommended_action_desc
		except Exception as e :
			raise e
	'''
	set Recommended Action Desc
	'''
	@recommended_action_desc.setter
	def recommended_action_desc(self,recommended_action_desc):
		try :
			if not isinstance(recommended_action_desc,str):
				raise TypeError("recommended_action_desc must be set to str value")
			self._recommended_action_desc = recommended_action_desc
		except Exception as e :
			raise e


	'''
	get Sub Group Desc
	'''
	@property
	def sub_group_desc(self) :
		try:
			return self._sub_group_desc
		except Exception as e :
			raise e
	'''
	set Sub Group Desc
	'''
	@sub_group_desc.setter
	def sub_group_desc(self,sub_group_desc):
		try :
			if not isinstance(sub_group_desc,str):
				raise TypeError("sub_group_desc must be set to str value")
			self._sub_group_desc = sub_group_desc
		except Exception as e :
			raise e

	'''
	Latest Safety config information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				system_safety_config_obj=system_safety_config()
				response = system_safety_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of system_safety_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			system_safety_config_obj = system_safety_config()
			option_ = options()
			option_._filter=filter_
			return system_safety_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the system_safety_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			system_safety_config_obj = system_safety_config()
			option_ = options()
			option_._count=True
			response = system_safety_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of system_safety_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			system_safety_config_obj = system_safety_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = system_safety_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(system_safety_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.system_safety_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(system_safety_config_responses, response, "system_safety_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.system_safety_config_response_array
				i=0
				error = [system_safety_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.system_safety_config_response_array
			i=0
			system_safety_config_objs = [system_safety_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_system_safety_config'):
					for props in obj._system_safety_config:
						result = service.payload_formatter.string_to_bulk_resource(system_safety_config_response,self.__class__.__name__,props)
						system_safety_config_objs[i] = result.system_safety_config
						i=i+1
			return system_safety_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(system_safety_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class system_safety_config_response(base_response):
	def __init__(self,length=1) :
		self.system_safety_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.system_safety_config= [ system_safety_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class system_safety_config_responses(base_response):
	def __init__(self,length=1) :
		self.system_safety_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.system_safety_config_response_array = [ system_safety_config() for _ in range(length)]
