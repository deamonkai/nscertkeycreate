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

from massrc.com.citrix.mas.nitro.resource.config.mps.af_generic_api import af_generic_api

'''
Configuration for AF Data Report table resource
'''

class si_safety_overview(af_generic_api):
	_total_system_security_setting= ""
	_not_configured_system_security_setting= ""
	_si_app_unit_name= ""
	_si_device_ip_address= ""
	_total_signatures= ""
	_total_security_checks= ""
	_not_configured_signatures= ""
	___count= ""
	_not_configured_security_checks= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_safety_overview"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_safety_overview,self).get_object_id()
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
			return "si_safety_overviews"
		except Exception as e :
			raise e


	'''
	Total System Security Setting
	'''
	@property
	def total_system_security_setting(self):
		try:
			return self._total_system_security_setting
		except Exception as e :
			raise e
	'''
	Total System Security Setting
	'''
	@total_system_security_setting.setter
	def total_system_security_setting(self,total_system_security_setting):
		try :
			if not isinstance(total_system_security_setting,float):
				raise TypeError("total_system_security_setting must be set to float value")
			self._total_system_security_setting = total_system_security_setting
		except Exception as e :
			raise e

	'''
	Not Configured System Security Setting
	'''
	@property
	def not_configured_system_security_setting(self):
		try:
			return self._not_configured_system_security_setting
		except Exception as e :
			raise e
	'''
	Not Configured System Security Setting
	'''
	@not_configured_system_security_setting.setter
	def not_configured_system_security_setting(self,not_configured_system_security_setting):
		try :
			if not isinstance(not_configured_system_security_setting,float):
				raise TypeError("not_configured_system_security_setting must be set to float value")
			self._not_configured_system_security_setting = not_configured_system_security_setting
		except Exception as e :
			raise e

	'''
	AppName
	'''
	@property
	def si_app_unit_name(self):
		try:
			return self._si_app_unit_name
		except Exception as e :
			raise e
	'''
	AppName
	'''
	@si_app_unit_name.setter
	def si_app_unit_name(self,si_app_unit_name):
		try :
			if not isinstance(si_app_unit_name,str):
				raise TypeError("si_app_unit_name must be set to str value")
			self._si_app_unit_name = si_app_unit_name
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def si_device_ip_address(self):
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
	'''
	@si_device_ip_address.setter
	def si_device_ip_address(self,si_device_ip_address):
		try :
			if not isinstance(si_device_ip_address,str):
				raise TypeError("si_device_ip_address must be set to str value")
			self._si_device_ip_address = si_device_ip_address
		except Exception as e :
			raise e

	'''
	Total number of Signatures
	'''
	@property
	def total_signatures(self):
		try:
			return self._total_signatures
		except Exception as e :
			raise e
	'''
	Total number of Signatures
	'''
	@total_signatures.setter
	def total_signatures(self,total_signatures):
		try :
			if not isinstance(total_signatures,float):
				raise TypeError("total_signatures must be set to float value")
			self._total_signatures = total_signatures
		except Exception as e :
			raise e

	'''
	Total number of security_checks
	'''
	@property
	def total_security_checks(self):
		try:
			return self._total_security_checks
		except Exception as e :
			raise e
	'''
	Total number of security_checks
	'''
	@total_security_checks.setter
	def total_security_checks(self,total_security_checks):
		try :
			if not isinstance(total_security_checks,float):
				raise TypeError("total_security_checks must be set to float value")
			self._total_security_checks = total_security_checks
		except Exception as e :
			raise e

	'''
	Not Configured Signatures
	'''
	@property
	def not_configured_signatures(self):
		try:
			return self._not_configured_signatures
		except Exception as e :
			raise e
	'''
	Not Configured Signatures
	'''
	@not_configured_signatures.setter
	def not_configured_signatures(self,not_configured_signatures):
		try :
			if not isinstance(not_configured_signatures,float):
				raise TypeError("not_configured_signatures must be set to float value")
			self._not_configured_signatures = not_configured_signatures
		except Exception as e :
			raise e

	'''
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	Not Configured Security Checks
	'''
	@property
	def not_configured_security_checks(self):
		try:
			return self._not_configured_security_checks
		except Exception as e :
			raise e
	'''
	Not Configured Security Checks
	'''
	@not_configured_security_checks.setter
	def not_configured_security_checks(self,not_configured_security_checks):
		try :
			if not isinstance(not_configured_security_checks,float):
				raise TypeError("not_configured_security_checks must be set to float value")
			self._not_configured_security_checks = not_configured_security_checks
		except Exception as e :
			raise e

	'''
	Af Report for Security Insight Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_safety_overview_obj=si_safety_overview()
				response = si_safety_overview_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_safety_overview resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_safety_overview_obj = si_safety_overview()
			option_ = options()
			option_._filter=filter_
			return si_safety_overview_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_safety_overview resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_safety_overview_obj = si_safety_overview()
			option_ = options()
			option_._count=True
			response = si_safety_overview_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_safety_overview resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_safety_overview_obj = si_safety_overview()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_safety_overview_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_overview_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_safety_overview
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_overview_responses, response, "si_safety_overview_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_safety_overview_response_array
				i=0
				error = [si_safety_overview() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_safety_overview_response_array
			i=0
			si_safety_overview_objs = [si_safety_overview() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_safety_overview:
					result = service.payload_formatter.string_to_bulk_resource(si_safety_overview_response,self.__class__.__name__,props)
					si_safety_overview_objs[i] = result.si_safety_overview
					i=i+1
			return si_safety_overview_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_safety_overview,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_safety_overview_response(base_response):
	def __init__(self,length=1) :
		self.si_safety_overview= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_safety_overview= [ si_safety_overview() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_safety_overview_responses(base_response):
	def __init__(self,length=1) :
		self.si_safety_overview_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_safety_overview_response_array = [ si_safety_overview() for _ in range(length)]
