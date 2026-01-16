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
Configuration for AF IP Reputation Report resource
'''

class si_ip_reputation(af_generic_api):
	_iprep_http_method= ""
	_si_device_ip_address= ""
	_total_attacks= ""
	_iprep_reputation_score= ""
	___count= ""
	_source_ip_address= ""
	_name= ""
	_iprep_category= ""
	_iprep_app_threat_index= ""
	_rpt_sample_time= ""
	_violation_type= ""
	_violation_action= ""
	_iprep_severity= ""
	_iprep_attack_time= ""
	_attack_category= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_ip_reputation"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_ip_reputation,self).get_object_id()
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
			return "si_ip_reputations"
		except Exception as e :
			raise e


	'''
	HTTP Req method
	'''
	@property
	def iprep_http_method(self):
		try:
			return self._iprep_http_method
		except Exception as e :
			raise e
	'''
	HTTP Req method
	'''
	@iprep_http_method.setter
	def iprep_http_method(self,iprep_http_method):
		try :
			if not isinstance(iprep_http_method,str):
				raise TypeError("iprep_http_method must be set to str value")
			self._iprep_http_method = iprep_http_method
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
	total attacks.
	'''
	@property
	def total_attacks(self):
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	total attacks.
	'''
	@total_attacks.setter
	def total_attacks(self,total_attacks):
		try :
			if not isinstance(total_attacks,float):
				raise TypeError("total_attacks must be set to float value")
			self._total_attacks = total_attacks
		except Exception as e :
			raise e

	'''
	Reputation Score of IP
	'''
	@property
	def iprep_reputation_score(self):
		try:
			return self._iprep_reputation_score
		except Exception as e :
			raise e
	'''
	Reputation Score of IP
	'''
	@iprep_reputation_score.setter
	def iprep_reputation_score(self,iprep_reputation_score):
		try :
			if not isinstance(iprep_reputation_score,float):
				raise TypeError("iprep_reputation_score must be set to float value")
			self._iprep_reputation_score = iprep_reputation_score
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
	source_ip_address
	'''
	@property
	def source_ip_address(self):
		try:
			return self._source_ip_address
		except Exception as e :
			raise e
	'''
	source_ip_address
	'''
	@source_ip_address.setter
	def source_ip_address(self,source_ip_address):
		try :
			if not isinstance(source_ip_address,str):
				raise TypeError("source_ip_address must be set to str value")
			self._source_ip_address = source_ip_address
		except Exception as e :
			raise e

	'''
	AppName
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	AppName
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
	Category of the IPREP
	'''
	@property
	def iprep_category(self):
		try:
			return self._iprep_category
		except Exception as e :
			raise e
	'''
	Category of the IPREP
	'''
	@iprep_category.setter
	def iprep_category(self,iprep_category):
		try :
			if not isinstance(iprep_category,str):
				raise TypeError("iprep_category must be set to str value")
			self._iprep_category = iprep_category
		except Exception as e :
			raise e

	'''
	App Threat Index
	'''
	@property
	def iprep_app_threat_index(self):
		try:
			return self._iprep_app_threat_index
		except Exception as e :
			raise e
	'''
	App Threat Index
	'''
	@iprep_app_threat_index.setter
	def iprep_app_threat_index(self,iprep_app_threat_index):
		try :
			if not isinstance(iprep_app_threat_index,float):
				raise TypeError("iprep_app_threat_index must be set to float value")
			self._iprep_app_threat_index = iprep_app_threat_index
		except Exception as e :
			raise e

	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Violation Type
	'''
	@property
	def violation_type(self):
		try:
			return self._violation_type
		except Exception as e :
			raise e
	'''
	Violation Type
	'''
	@violation_type.setter
	def violation_type(self,violation_type):
		try :
			if not isinstance(violation_type,str):
				raise TypeError("violation_type must be set to str value")
			self._violation_type = violation_type
		except Exception as e :
			raise e

	'''
	Violation Action
	'''
	@property
	def violation_action(self):
		try:
			return self._violation_action
		except Exception as e :
			raise e
	'''
	Violation Action
	'''
	@violation_action.setter
	def violation_action(self,violation_action):
		try :
			if not isinstance(violation_action,str):
				raise TypeError("violation_action must be set to str value")
			self._violation_action = violation_action
		except Exception as e :
			raise e

	'''
	Severity
	'''
	@property
	def iprep_severity(self):
		try:
			return self._iprep_severity
		except Exception as e :
			raise e
	'''
	Severity
	'''
	@iprep_severity.setter
	def iprep_severity(self,iprep_severity):
		try :
			if not isinstance(iprep_severity,str):
				raise TypeError("iprep_severity must be set to str value")
			self._iprep_severity = iprep_severity
		except Exception as e :
			raise e

	'''
	Time of Attack
	'''
	@property
	def iprep_attack_time(self):
		try:
			return self._iprep_attack_time
		except Exception as e :
			raise e
	'''
	Time of Attack
	'''
	@iprep_attack_time.setter
	def iprep_attack_time(self,iprep_attack_time):
		try :
			if not isinstance(iprep_attack_time,float):
				raise TypeError("iprep_attack_time must be set to float value")
			self._iprep_attack_time = iprep_attack_time
		except Exception as e :
			raise e

	'''
	Attack Category
	'''
	@property
	def attack_category(self):
		try:
			return self._attack_category
		except Exception as e :
			raise e
	'''
	Attack Category
	'''
	@attack_category.setter
	def attack_category(self,attack_category):
		try :
			if not isinstance(attack_category,str):
				raise TypeError("attack_category must be set to str value")
			self._attack_category = attack_category
		except Exception as e :
			raise e

	'''
	Af Report for IP Reputation..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_ip_reputation_obj=si_ip_reputation()
				response = si_ip_reputation_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_ip_reputation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_ip_reputation_obj = si_ip_reputation()
			option_ = options()
			option_._filter=filter_
			return si_ip_reputation_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_ip_reputation resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_ip_reputation_obj = si_ip_reputation()
			option_ = options()
			option_._count=True
			response = si_ip_reputation_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_ip_reputation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_ip_reputation_obj = si_ip_reputation()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_ip_reputation_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_ip_reputation_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_ip_reputation
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_ip_reputation_responses, response, "si_ip_reputation_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_ip_reputation_response_array
				i=0
				error = [si_ip_reputation() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_ip_reputation_response_array
			i=0
			si_ip_reputation_objs = [si_ip_reputation() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_ip_reputation:
					result = service.payload_formatter.string_to_bulk_resource(si_ip_reputation_response,self.__class__.__name__,props)
					si_ip_reputation_objs[i] = result.si_ip_reputation
					i=i+1
			return si_ip_reputation_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_ip_reputation,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_ip_reputation_response(base_response):
	def __init__(self,length=1) :
		self.si_ip_reputation= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_ip_reputation= [ si_ip_reputation() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_ip_reputation_responses(base_response):
	def __init__(self,length=1) :
		self.si_ip_reputation_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_ip_reputation_response_array = [ si_ip_reputation() for _ in range(length)]
