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
Configuration for AF Safety System Security Data Report table resource
'''

class si_safety_system_security(base_resource):
	_system_safety_index= ""
	_sub_group= ""
	_profile_safety_index= ""
	_recommended_action= ""
	___count= ""
	_si_device_ip_address= ""
	_si_app_unit_name= ""
	_name= ""
	_num_configs= ""
	_id= ""
	_is_complaint= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_safety_system_security"
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
			return "si_safety_system_securitys"
		except Exception as e :
			raise e


	'''
	System Safety Index.
	'''
	@property
	def system_safety_index(self):
		try:
			return self._system_safety_index
		except Exception as e :
			raise e
	'''
	System Safety Index.
	'''
	@system_safety_index.setter
	def system_safety_index(self,system_safety_index):
		try :
			if not isinstance(system_safety_index,float):
				raise TypeError("system_safety_index must be set to float value")
			self._system_safety_index = system_safety_index
		except Exception as e :
			raise e

	'''
	System Sub Group Name
	'''
	@property
	def sub_group(self):
		try:
			return self._sub_group
		except Exception as e :
			raise e
	'''
	System Sub Group Name
	'''
	@sub_group.setter
	def sub_group(self,sub_group):
		try :
			if not isinstance(sub_group,str):
				raise TypeError("sub_group must be set to str value")
			self._sub_group = sub_group
		except Exception as e :
			raise e

	'''
	Profile Safety Index.
	'''
	@property
	def profile_safety_index(self):
		try:
			return self._profile_safety_index
		except Exception as e :
			raise e
	'''
	Profile Safety Index.
	'''
	@profile_safety_index.setter
	def profile_safety_index(self,profile_safety_index):
		try :
			if not isinstance(profile_safety_index,float):
				raise TypeError("profile_safety_index must be set to float value")
			self._profile_safety_index = profile_safety_index
		except Exception as e :
			raise e

	'''
	System recommended_action
	'''
	@property
	def recommended_action(self):
		try:
			return self._recommended_action
		except Exception as e :
			raise e
	'''
	System recommended_action
	'''
	@recommended_action.setter
	def recommended_action(self,recommended_action):
		try :
			if not isinstance(recommended_action,str):
				raise TypeError("recommended_action must be set to str value")
			self._recommended_action = recommended_action
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
	Profile Security Check Type Name
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Profile Security Check Type Name
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
	Number of Configs.
	'''
	@property
	def num_configs(self):
		try:
			return self._num_configs
		except Exception as e :
			raise e
	'''
	Number of Configs.
	'''
	@num_configs.setter
	def num_configs(self,num_configs):
		try :
			if not isinstance(num_configs,float):
				raise TypeError("num_configs must be set to float value")
			self._num_configs = num_configs
		except Exception as e :
			raise e

	'''
	Id is safety profile
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is safety profile
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
	System compliant
	'''
	@property
	def is_complaint(self):
		try:
			return self._is_complaint
		except Exception as e :
			raise e
	'''
	System compliant
	'''
	@is_complaint.setter
	def is_complaint(self,is_complaint):
		try :
			if not isinstance(is_complaint,str):
				raise TypeError("is_complaint must be set to str value")
			self._is_complaint = is_complaint
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
				si_safety_system_security_obj=si_safety_system_security()
				response = si_safety_system_security_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_safety_system_security resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_safety_system_security_obj = si_safety_system_security()
			option_ = options()
			option_._filter=filter_
			return si_safety_system_security_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_safety_system_security resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_safety_system_security_obj = si_safety_system_security()
			option_ = options()
			option_._count=True
			response = si_safety_system_security_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_safety_system_security resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_safety_system_security_obj = si_safety_system_security()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_safety_system_security_obj.getfiltered(service, option_)
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
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_system_security_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_safety_system_security
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_system_security_responses, response, "si_safety_system_security_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_safety_system_security_response_array
				i=0
				error = [si_safety_system_security() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_safety_system_security_response_array
			i=0
			si_safety_system_security_objs = [si_safety_system_security() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_safety_system_security:
					result = service.payload_formatter.string_to_bulk_resource(si_safety_system_security_response,self.__class__.__name__,props)
					si_safety_system_security_objs[i] = result.si_safety_system_security
					i=i+1
			return si_safety_system_security_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_safety_system_security,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_safety_system_security_response(base_response):
	def __init__(self,length=1) :
		self.si_safety_system_security= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_safety_system_security= [ si_safety_system_security() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_safety_system_security_responses(base_response):
	def __init__(self,length=1) :
		self.si_safety_system_security_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_safety_system_security_response_array = [ si_safety_system_security() for _ in range(length)]
