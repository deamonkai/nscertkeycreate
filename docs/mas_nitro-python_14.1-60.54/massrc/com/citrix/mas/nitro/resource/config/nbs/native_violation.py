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
Configuration for Native Violations Details resource
'''

class native_violation(base_resource):
	_ind_category_desc= ""
	_ip_address= ""
	_ind_recommend_desc= ""
	_severity_desc= ""
	_ind_id= ""
	_appname= ""
	_violation_count= ""
	_svcname= ""
	_ind_weight_desc= ""
	_rpt_sample_time= ""
	_ind_name_desc= ""
	_severity= ""
	_violation_ratio= ""
	_confidence= ""
	_ind_detection_time= ""
	_ctnsappname= ""
	_total_violations= ""
	_ind_detection_msg= ""
	_ind_value= ""
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
			return "/macro/v1/security/native_violation"
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
			return "native_violation"
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
			return "native_violations"
		except Exception as e :
			raise e



	'''
	get Indicator category description
	'''
	@property
	def ind_category_desc(self) :
		try:
			return self._ind_category_desc
		except Exception as e :
			raise e
	'''
	set Indicator category description
	'''
	@ind_category_desc.setter
	def ind_category_desc(self,ind_category_desc):
		try :
			if not isinstance(ind_category_desc,str):
				raise TypeError("ind_category_desc must be set to str value")
			self._ind_category_desc = ind_category_desc
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
	get Indicator Recommendation
	'''
	@property
	def ind_recommend_desc(self) :
		try:
			return self._ind_recommend_desc
		except Exception as e :
			raise e
	'''
	set Indicator Recommendation
	'''
	@ind_recommend_desc.setter
	def ind_recommend_desc(self,ind_recommend_desc):
		try :
			if not isinstance(ind_recommend_desc,str):
				raise TypeError("ind_recommend_desc must be set to str value")
			self._ind_recommend_desc = ind_recommend_desc
		except Exception as e :
			raise e


	'''
	get Severity description
	'''
	@property
	def severity_desc(self) :
		try:
			return self._severity_desc
		except Exception as e :
			raise e
	'''
	set Severity description
	'''
	@severity_desc.setter
	def severity_desc(self,severity_desc):
		try :
			if not isinstance(severity_desc,str):
				raise TypeError("severity_desc must be set to str value")
			self._severity_desc = severity_desc
		except Exception as e :
			raise e


	'''
	get Indicator Id
	'''
	@property
	def ind_id(self) :
		try:
			return self._ind_id
		except Exception as e :
			raise e
	'''
	set Indicator Id
	'''
	@ind_id.setter
	def ind_id(self,ind_id):
		try :
			if not isinstance(ind_id,long):
				raise TypeError("ind_id must be set to long value")
			self._ind_id = ind_id
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set Application Name
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
	get Violation Count
	'''
	@property
	def violation_count(self) :
		try:
			return self._violation_count
		except Exception as e :
			raise e
	'''
	set Violation Count
	'''
	@violation_count.setter
	def violation_count(self,violation_count):
		try :
			if not isinstance(violation_count,int):
				raise TypeError("violation_count must be set to int value")
			self._violation_count = violation_count
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@svcname.setter
	def svcname(self,svcname):
		try :
			if not isinstance(svcname,str):
				raise TypeError("svcname must be set to str value")
			self._svcname = svcname
		except Exception as e :
			raise e


	'''
	get Indicator Weight description
	'''
	@property
	def ind_weight_desc(self) :
		try:
			return self._ind_weight_desc
		except Exception as e :
			raise e
	'''
	set Indicator Weight description
	'''
	@ind_weight_desc.setter
	def ind_weight_desc(self,ind_weight_desc):
		try :
			if not isinstance(ind_weight_desc,str):
				raise TypeError("ind_weight_desc must be set to str value")
			self._ind_weight_desc = ind_weight_desc
		except Exception as e :
			raise e


	'''
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Indicator name description
	'''
	@property
	def ind_name_desc(self) :
		try:
			return self._ind_name_desc
		except Exception as e :
			raise e
	'''
	set Indicator name description
	'''
	@ind_name_desc.setter
	def ind_name_desc(self,ind_name_desc):
		try :
			if not isinstance(ind_name_desc,str):
				raise TypeError("ind_name_desc must be set to str value")
			self._ind_name_desc = ind_name_desc
		except Exception as e :
			raise e


	'''
	get Severity.
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity.
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,int):
				raise TypeError("severity must be set to int value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Violation Ratio
	'''
	@property
	def violation_ratio(self) :
		try:
			return self._violation_ratio
		except Exception as e :
			raise e
	'''
	set Violation Ratio
	'''
	@violation_ratio.setter
	def violation_ratio(self,violation_ratio):
		try :
			if not isinstance(violation_ratio,str):
				raise TypeError("violation_ratio must be set to str value")
			self._violation_ratio = violation_ratio
		except Exception as e :
			raise e


	'''
	get Confidence
	'''
	@property
	def confidence(self) :
		try:
			return self._confidence
		except Exception as e :
			raise e
	'''
	set Confidence
	'''
	@confidence.setter
	def confidence(self,confidence):
		try :
			if not isinstance(confidence,int):
				raise TypeError("confidence must be set to int value")
			self._confidence = confidence
		except Exception as e :
			raise e


	'''
	get Detection Time
	'''
	@property
	def ind_detection_time(self) :
		try:
			return self._ind_detection_time
		except Exception as e :
			raise e
	'''
	set Detection Time
	'''
	@ind_detection_time.setter
	def ind_detection_time(self,ind_detection_time):
		try :
			if not isinstance(ind_detection_time,long):
				raise TypeError("ind_detection_time must be set to long value")
			self._ind_detection_time = ind_detection_time
		except Exception as e :
			raise e


	'''
	get VServer Name
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set VServer Name
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
	get Total Violation
	'''
	@property
	def total_violations(self) :
		try:
			return self._total_violations
		except Exception as e :
			raise e
	'''
	set Total Violation
	'''
	@total_violations.setter
	def total_violations(self,total_violations):
		try :
			if not isinstance(total_violations,int):
				raise TypeError("total_violations must be set to int value")
			self._total_violations = total_violations
		except Exception as e :
			raise e


	'''
	get Indicator Detection Message
	'''
	@property
	def ind_detection_msg(self) :
		try:
			return self._ind_detection_msg
		except Exception as e :
			raise e
	'''
	set Indicator Detection Message
	'''
	@ind_detection_msg.setter
	def ind_detection_msg(self,ind_detection_msg):
		try :
			if not isinstance(ind_detection_msg,str):
				raise TypeError("ind_detection_msg must be set to str value")
			self._ind_detection_msg = ind_detection_msg
		except Exception as e :
			raise e


	'''
	get Indicator value
	'''
	@property
	def ind_value(self) :
		try:
			return self._ind_value
		except Exception as e :
			raise e
	'''
	set Indicator value
	'''
	@ind_value.setter
	def ind_value(self,ind_value):
		try :
			if not isinstance(ind_value,int):
				raise TypeError("ind_value must be set to int value")
			self._ind_value = ind_value
		except Exception as e :
			raise e

	'''
	Provides details of native violations..
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
				native_violation_obj=native_violation()
				response = native_violation_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of native_violation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			native_violation_obj = native_violation()
			option_ = options()
			option_._filter=filter_
			return native_violation_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the native_violation resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			native_violation_obj = native_violation()
			option_ = options()
			option_._count=True
			response = native_violation_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of native_violation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			native_violation_obj = native_violation()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = native_violation_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(native_violation_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.native_violation
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(native_violation_responses, response, "native_violation_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.native_violation_response_array
				i=0
				error = [native_violation() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.native_violation_response_array
			i=0
			native_violation_objs = [native_violation() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_native_violation'):
					for props in obj._native_violation:
						result = service.payload_formatter.string_to_bulk_resource(native_violation_response,self.__class__.__name__,props)
						native_violation_objs[i] = result.native_violation
						i=i+1
			return native_violation_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(native_violation,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class native_violation_response(base_response):
	def __init__(self,length=1) :
		self.native_violation= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.native_violation= [ native_violation() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class native_violation_responses(base_response):
	def __init__(self,length=1) :
		self.native_violation_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.native_violation_response_array = [ native_violation() for _ in range(length)]
