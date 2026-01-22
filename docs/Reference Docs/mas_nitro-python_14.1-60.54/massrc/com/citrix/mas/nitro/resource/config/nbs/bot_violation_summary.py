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
Configuration for Bot Violation Summary resource
'''

class bot_violation_summary(base_resource):
	_ctnsappname= ""
	_total_bots= ""
	_total_violations= ""
	_appname= ""
	_backend_appname= ""
	_host_name= ""
	_ip_address= ""
	_bot_human_ratio= ""
	_backend_vserver= ""
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
			return "/macro/v1/security/bot_violation_summary"
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
			return "bot_violation_summary"
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
			return "bot_violation_summarys"
		except Exception as e :
			raise e



	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Total Bots
	'''
	@property
	def total_bots(self) :
		try:
			return self._total_bots
		except Exception as e :
			raise e
	'''
	set Total Bots
	'''
	@total_bots.setter
	def total_bots(self,total_bots):
		try :
			if not isinstance(total_bots,int):
				raise TypeError("total_bots must be set to int value")
			self._total_bots = total_bots
		except Exception as e :
			raise e


	'''
	get Total Violations
	'''
	@property
	def total_violations(self) :
		try:
			return self._total_violations
		except Exception as e :
			raise e
	'''
	set Total Violations
	'''
	@total_violations.setter
	def total_violations(self,total_violations):
		try :
			if not isinstance(total_violations,long):
				raise TypeError("total_violations must be set to long value")
			self._total_violations = total_violations
		except Exception as e :
			raise e


	'''
	get App Name
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set App Name
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get Backend App Name
	'''
	@property
	def backend_appname(self) :
		try:
			return self._backend_appname
		except Exception as e :
			raise e
	'''
	set Backend App Name
	'''
	@backend_appname.setter
	def backend_appname(self,backend_appname):
		try :
			if not isinstance(backend_appname,str):
				raise TypeError("backend_appname must be set to str value")
			self._backend_appname = backend_appname
		except Exception as e :
			raise e


	'''
	get HostName
	'''
	@property
	def host_name(self) :
		try:
			return self._host_name
		except Exception as e :
			raise e
	'''
	set HostName
	'''
	@host_name.setter
	def host_name(self,host_name):
		try :
			if not isinstance(host_name,str):
				raise TypeError("host_name must be set to str value")
			self._host_name = host_name
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
	get Bot Human Ratio
	'''
	@property
	def bot_human_ratio(self) :
		try:
			return self._bot_human_ratio
		except Exception as e :
			raise e
	'''
	set Bot Human Ratio
	'''
	@bot_human_ratio.setter
	def bot_human_ratio(self,bot_human_ratio):
		try :
			if not isinstance(bot_human_ratio,str):
				raise TypeError("bot_human_ratio must be set to str value")
			self._bot_human_ratio = bot_human_ratio
		except Exception as e :
			raise e


	'''
	get Backend Vserver Name
	'''
	@property
	def backend_vserver(self) :
		try:
			return self._backend_vserver
		except Exception as e :
			raise e
	'''
	set Backend Vserver Name
	'''
	@backend_vserver.setter
	def backend_vserver(self,backend_vserver):
		try :
			if not isinstance(backend_vserver,str):
				raise TypeError("backend_vserver must be set to str value")
			self._backend_vserver = backend_vserver
		except Exception as e :
			raise e

	'''
	Bot Violation Summary.
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
				bot_violation_summary_obj=bot_violation_summary()
				response = bot_violation_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of bot_violation_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_summary_obj = bot_violation_summary()
			option_ = options()
			option_._filter=filter_
			return bot_violation_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the bot_violation_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_summary_obj = bot_violation_summary()
			option_ = options()
			option_._count=True
			response = bot_violation_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of bot_violation_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_summary_obj = bot_violation_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = bot_violation_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(bot_violation_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bot_violation_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(bot_violation_summary_responses, response, "bot_violation_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.bot_violation_summary_response_array
				i=0
				error = [bot_violation_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.bot_violation_summary_response_array
			i=0
			bot_violation_summary_objs = [bot_violation_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_bot_violation_summary'):
					for props in obj._bot_violation_summary:
						result = service.payload_formatter.string_to_bulk_resource(bot_violation_summary_response,self.__class__.__name__,props)
						bot_violation_summary_objs[i] = result.bot_violation_summary
						i=i+1
			return bot_violation_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(bot_violation_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class bot_violation_summary_response(base_response):
	def __init__(self,length=1) :
		self.bot_violation_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.bot_violation_summary= [ bot_violation_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class bot_violation_summary_responses(base_response):
	def __init__(self,length=1) :
		self.bot_violation_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.bot_violation_summary_response_array = [ bot_violation_summary() for _ in range(length)]
