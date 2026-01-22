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
Configuration for Profile Safety Config resource
'''

class profile_safety_config(base_resource):
	_profile_sig_name= ""
	_sig_rule_id= ""
	_sig_rule_logstring= ""
	_security_type_desc= ""
	_log_flag= ""
	_sig_rule_category= ""
	_stat_flag= ""
	_block_flag= ""
	_none_flag= ""
	_security_type= ""
	_ip_address= ""
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
			return "/macro/v1/security/profile_safety_config"
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
			return "profile_safety_config"
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
			return "profile_safety_configs"
		except Exception as e :
			raise e



	'''
	get profile_sig_name
	'''
	@property
	def profile_sig_name(self) :
		try:
			return self._profile_sig_name
		except Exception as e :
			raise e
	'''
	set profile_sig_name
	'''
	@profile_sig_name.setter
	def profile_sig_name(self,profile_sig_name):
		try :
			if not isinstance(profile_sig_name,str):
				raise TypeError("profile_sig_name must be set to str value")
			self._profile_sig_name = profile_sig_name
		except Exception as e :
			raise e


	'''
	get Signature Rule ID
	'''
	@property
	def sig_rule_id(self) :
		try:
			return self._sig_rule_id
		except Exception as e :
			raise e
	'''
	set Signature Rule ID
	'''
	@sig_rule_id.setter
	def sig_rule_id(self,sig_rule_id):
		try :
			if not isinstance(sig_rule_id,long):
				raise TypeError("sig_rule_id must be set to long value")
			self._sig_rule_id = sig_rule_id
		except Exception as e :
			raise e


	'''
	get signature rule logstring
	'''
	@property
	def sig_rule_logstring(self) :
		try:
			return self._sig_rule_logstring
		except Exception as e :
			raise e
	'''
	set signature rule logstring
	'''
	@sig_rule_logstring.setter
	def sig_rule_logstring(self,sig_rule_logstring):
		try :
			if not isinstance(sig_rule_logstring,str):
				raise TypeError("sig_rule_logstring must be set to str value")
			self._sig_rule_logstring = sig_rule_logstring
		except Exception as e :
			raise e


	'''
	get Security Type Description
	'''
	@property
	def security_type_desc(self) :
		try:
			return self._security_type_desc
		except Exception as e :
			raise e
	'''
	set Security Type Description
	'''
	@security_type_desc.setter
	def security_type_desc(self,security_type_desc):
		try :
			if not isinstance(security_type_desc,str):
				raise TypeError("security_type_desc must be set to str value")
			self._security_type_desc = security_type_desc
		except Exception as e :
			raise e


	'''
	get log_flag.
	'''
	@property
	def log_flag(self) :
		try:
			return self._log_flag
		except Exception as e :
			raise e
	'''
	set log_flag.
	'''
	@log_flag.setter
	def log_flag(self,log_flag):
		try :
			if not isinstance(log_flag,int):
				raise TypeError("log_flag must be set to int value")
			self._log_flag = log_flag
		except Exception as e :
			raise e


	'''
	get signature rule category
	'''
	@property
	def sig_rule_category(self) :
		try:
			return self._sig_rule_category
		except Exception as e :
			raise e
	'''
	set signature rule category
	'''
	@sig_rule_category.setter
	def sig_rule_category(self,sig_rule_category):
		try :
			if not isinstance(sig_rule_category,str):
				raise TypeError("sig_rule_category must be set to str value")
			self._sig_rule_category = sig_rule_category
		except Exception as e :
			raise e


	'''
	get stat_flag
	'''
	@property
	def stat_flag(self) :
		try:
			return self._stat_flag
		except Exception as e :
			raise e
	'''
	set stat_flag
	'''
	@stat_flag.setter
	def stat_flag(self,stat_flag):
		try :
			if not isinstance(stat_flag,int):
				raise TypeError("stat_flag must be set to int value")
			self._stat_flag = stat_flag
		except Exception as e :
			raise e


	'''
	get block_flag.
	'''
	@property
	def block_flag(self) :
		try:
			return self._block_flag
		except Exception as e :
			raise e
	'''
	set block_flag.
	'''
	@block_flag.setter
	def block_flag(self,block_flag):
		try :
			if not isinstance(block_flag,int):
				raise TypeError("block_flag must be set to int value")
			self._block_flag = block_flag
		except Exception as e :
			raise e


	'''
	get none_flag
	'''
	@property
	def none_flag(self) :
		try:
			return self._none_flag
		except Exception as e :
			raise e
	'''
	set none_flag
	'''
	@none_flag.setter
	def none_flag(self,none_flag):
		try :
			if not isinstance(none_flag,int):
				raise TypeError("none_flag must be set to int value")
			self._none_flag = none_flag
		except Exception as e :
			raise e


	'''
	get severity.
	'''
	@property
	def security_type(self) :
		try:
			return self._security_type
		except Exception as e :
			raise e
	'''
	set severity.
	'''
	@security_type.setter
	def security_type(self,security_type):
		try :
			if not isinstance(security_type,int):
				raise TypeError("security_type must be set to int value")
			self._security_type = security_type
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
	Latest Profile safety config information..
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
				profile_safety_config_obj=profile_safety_config()
				response = profile_safety_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of profile_safety_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			profile_safety_config_obj = profile_safety_config()
			option_ = options()
			option_._filter=filter_
			return profile_safety_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the profile_safety_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			profile_safety_config_obj = profile_safety_config()
			option_ = options()
			option_._count=True
			response = profile_safety_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of profile_safety_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			profile_safety_config_obj = profile_safety_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = profile_safety_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(profile_safety_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.profile_safety_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(profile_safety_config_responses, response, "profile_safety_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.profile_safety_config_response_array
				i=0
				error = [profile_safety_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.profile_safety_config_response_array
			i=0
			profile_safety_config_objs = [profile_safety_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_profile_safety_config'):
					for props in obj._profile_safety_config:
						result = service.payload_formatter.string_to_bulk_resource(profile_safety_config_response,self.__class__.__name__,props)
						profile_safety_config_objs[i] = result.profile_safety_config
						i=i+1
			return profile_safety_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(profile_safety_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class profile_safety_config_response(base_response):
	def __init__(self,length=1) :
		self.profile_safety_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.profile_safety_config= [ profile_safety_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class profile_safety_config_responses(base_response):
	def __init__(self,length=1) :
		self.profile_safety_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.profile_safety_config_response_array = [ profile_safety_config() for _ in range(length)]
