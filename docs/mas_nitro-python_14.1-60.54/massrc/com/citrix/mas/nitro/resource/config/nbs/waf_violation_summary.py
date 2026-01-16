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
Configuration for WAF Violation Summary resource
'''

class waf_violation_summary(base_resource):
	_threshold_breach= ""
	_total_violations= ""
	_ip_address= ""
	_safety_index= ""
	_ctnsappname= ""
	_threat_index= ""
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
			return "/macro/v1/security/waf_violation_summary"
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
			return "waf_violation_summary"
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
			return "waf_violation_summarys"
		except Exception as e :
			raise e



	'''
	get Total Requests
	'''
	@property
	def threshold_breach(self) :
		try:
			return self._threshold_breach
		except Exception as e :
			raise e
	'''
	set Total Requests
	'''
	@threshold_breach.setter
	def threshold_breach(self,threshold_breach):
		try :
			if not isinstance(threshold_breach,int):
				raise TypeError("threshold_breach must be set to int value")
			self._threshold_breach = threshold_breach
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
	get Safety Index
	'''
	@property
	def safety_index(self) :
		try:
			return self._safety_index
		except Exception as e :
			raise e
	'''
	set Safety Index
	'''
	@safety_index.setter
	def safety_index(self,safety_index):
		try :
			if not isinstance(safety_index,int):
				raise TypeError("safety_index must be set to int value")
			self._safety_index = safety_index
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
	get Threat Index
	'''
	@property
	def threat_index(self) :
		try:
			return self._threat_index
		except Exception as e :
			raise e
	'''
	set Threat Index
	'''
	@threat_index.setter
	def threat_index(self,threat_index):
		try :
			if not isinstance(threat_index,int):
				raise TypeError("threat_index must be set to int value")
			self._threat_index = threat_index
		except Exception as e :
			raise e

	'''
	WAF Violation Summary.
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
				waf_violation_summary_obj=waf_violation_summary()
				response = waf_violation_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of waf_violation_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_violation_summary_obj = waf_violation_summary()
			option_ = options()
			option_._filter=filter_
			return waf_violation_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the waf_violation_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_violation_summary_obj = waf_violation_summary()
			option_ = options()
			option_._count=True
			response = waf_violation_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of waf_violation_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_violation_summary_obj = waf_violation_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = waf_violation_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(waf_violation_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.waf_violation_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(waf_violation_summary_responses, response, "waf_violation_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.waf_violation_summary_response_array
				i=0
				error = [waf_violation_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.waf_violation_summary_response_array
			i=0
			waf_violation_summary_objs = [waf_violation_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_waf_violation_summary'):
					for props in obj._waf_violation_summary:
						result = service.payload_formatter.string_to_bulk_resource(waf_violation_summary_response,self.__class__.__name__,props)
						waf_violation_summary_objs[i] = result.waf_violation_summary
						i=i+1
			return waf_violation_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(waf_violation_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class waf_violation_summary_response(base_response):
	def __init__(self,length=1) :
		self.waf_violation_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.waf_violation_summary= [ waf_violation_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class waf_violation_summary_responses(base_response):
	def __init__(self,length=1) :
		self.waf_violation_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.waf_violation_summary_response_array = [ waf_violation_summary() for _ in range(length)]
