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

class si_security_overview(af_generic_api):
	_si_app_unit_name= ""
	_severity_type= ""
	_total_compliant_count= ""
	_safety_index= ""
	_id= ""
	_not_compliant_percentage= ""
	_name= ""
	_si_device_ip_address= ""
	_not_compliant_count= ""
	_total_attacks= ""
	_threat_index= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_security_overview"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_security_overview,self).get_object_id()
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
			return "si_security_overviews"
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
	severity_type
	'''
	@property
	def severity_type(self):
		try:
			return self._severity_type
		except Exception as e :
			raise e
	'''
	severity_type
	'''
	@severity_type.setter
	def severity_type(self,severity_type):
		try :
			if not isinstance(severity_type,str):
				raise TypeError("severity_type must be set to str value")
			self._severity_type = severity_type
		except Exception as e :
			raise e

	'''
	Total Compliant Count
	'''
	@property
	def total_compliant_count(self):
		try:
			return self._total_compliant_count
		except Exception as e :
			raise e
	'''
	Total Compliant Count
	'''
	@total_compliant_count.setter
	def total_compliant_count(self,total_compliant_count):
		try :
			if not isinstance(total_compliant_count,float):
				raise TypeError("total_compliant_count must be set to float value")
			self._total_compliant_count = total_compliant_count
		except Exception as e :
			raise e

	'''
	safety index
	'''
	@property
	def safety_index(self):
		try:
			return self._safety_index
		except Exception as e :
			raise e
	'''
	safety index
	'''
	@safety_index.setter
	def safety_index(self,safety_index):
		try :
			if not isinstance(safety_index,float):
				raise TypeError("safety_index must be set to float value")
			self._safety_index = safety_index
		except Exception as e :
			raise e

	'''
	Id is Security check violation name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is Security check violation name
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
	not_compliant_percentage
	'''
	@property
	def not_compliant_percentage(self):
		try:
			return self._not_compliant_percentage
		except Exception as e :
			raise e
	'''
	not_compliant_percentage
	'''
	@not_compliant_percentage.setter
	def not_compliant_percentage(self,not_compliant_percentage):
		try :
			if not isinstance(not_compliant_percentage,float):
				raise TypeError("not_compliant_percentage must be set to float value")
			self._not_compliant_percentage = not_compliant_percentage
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
	Not Compliant Count
	'''
	@property
	def not_compliant_count(self):
		try:
			return self._not_compliant_count
		except Exception as e :
			raise e
	'''
	Not Compliant Count
	'''
	@not_compliant_count.setter
	def not_compliant_count(self,not_compliant_count):
		try :
			if not isinstance(not_compliant_count,float):
				raise TypeError("not_compliant_count must be set to float value")
			self._not_compliant_count = not_compliant_count
		except Exception as e :
			raise e

	'''
	Total Attacks.
	'''
	@property
	def total_attacks(self):
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	Total Attacks.
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
	Threat Index
	'''
	@property
	def threat_index(self):
		try:
			return self._threat_index
		except Exception as e :
			raise e
	'''
	Threat Index
	'''
	@threat_index.setter
	def threat_index(self,threat_index):
		try :
			if not isinstance(threat_index,float):
				raise TypeError("threat_index must be set to float value")
			self._threat_index = threat_index
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
	Af Report for Security Insight Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_security_overview_obj=si_security_overview()
				response = si_security_overview_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_security_overview resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_security_overview_obj = si_security_overview()
			option_ = options()
			option_._filter=filter_
			return si_security_overview_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_security_overview resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_security_overview_obj = si_security_overview()
			option_ = options()
			option_._count=True
			response = si_security_overview_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_security_overview resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_security_overview_obj = si_security_overview()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_security_overview_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_security_overview_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_security_overview
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_security_overview_responses, response, "si_security_overview_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_security_overview_response_array
				i=0
				error = [si_security_overview() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_security_overview_response_array
			i=0
			si_security_overview_objs = [si_security_overview() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_security_overview:
					result = service.payload_formatter.string_to_bulk_resource(si_security_overview_response,self.__class__.__name__,props)
					si_security_overview_objs[i] = result.si_security_overview
					i=i+1
			return si_security_overview_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_security_overview,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_security_overview_response(base_response):
	def __init__(self,length=1) :
		self.si_security_overview= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_security_overview= [ si_security_overview() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_security_overview_responses(base_response):
	def __init__(self,length=1) :
		self.si_security_overview_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_security_overview_response_array = [ si_security_overview() for _ in range(length)]
