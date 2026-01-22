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
Configuration for Skip flow Information resource
'''

class ica_device_skip_flow(base_resource):
	_skipflow_reason_id= ""
	_id= ""
	_ica_device_ip_address= ""
	_skipflow_description= ""
	_name= ""
	_group_reason_id= ""
	_skipflow_count= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_device_skip_flow"
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
			return "ica_device_skip_flows"
		except Exception as e :
			raise e


	'''
	Skip flow reason id.
	'''
	@property
	def skipflow_reason_id(self):
		try:
			return self._skipflow_reason_id
		except Exception as e :
			raise e
	'''
	Skip flow reason id.
	'''
	@skipflow_reason_id.setter
	def skipflow_reason_id(self,skipflow_reason_id):
		try :
			if not isinstance(skipflow_reason_id,float):
				raise TypeError("skipflow_reason_id must be set to float value")
			self._skipflow_reason_id = skipflow_reason_id
		except Exception as e :
			raise e

	'''
	Id is ICA Device IPAddress
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Device IPAddress
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
	ICA Device IP Address.
	'''
	@property
	def ica_device_ip_address(self):
		try:
			return self._ica_device_ip_address
		except Exception as e :
			raise e
	'''
	ICA Device IP Address.
	'''
	@ica_device_ip_address.setter
	def ica_device_ip_address(self,ica_device_ip_address):
		try :
			if not isinstance(ica_device_ip_address,str):
				raise TypeError("ica_device_ip_address must be set to str value")
			self._ica_device_ip_address = ica_device_ip_address
		except Exception as e :
			raise e

	'''
	Reason for skip flow.
	'''
	@property
	def skipflow_description(self):
		try:
			return self._skipflow_description
		except Exception as e :
			raise e
	'''
	Reason for skip flow.
	'''
	@skipflow_description.setter
	def skipflow_description(self,skipflow_description):
		try :
			if not isinstance(skipflow_description,str):
				raise TypeError("skipflow_description must be set to str value")
			self._skipflow_description = skipflow_description
		except Exception as e :
			raise e

	'''
	Name of ICA Device.
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA Device.
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
	Skip flow group reason id.
	'''
	@property
	def group_reason_id(self):
		try:
			return self._group_reason_id
		except Exception as e :
			raise e
	'''
	Skip flow group reason id.
	'''
	@group_reason_id.setter
	def group_reason_id(self,group_reason_id):
		try :
			if not isinstance(group_reason_id,float):
				raise TypeError("group_reason_id must be set to float value")
			self._group_reason_id = group_reason_id
		except Exception as e :
			raise e

	'''
	Skip flow count..
	'''
	@property
	def skipflow_count(self):
		try:
			return self._skipflow_count
		except Exception as e :
			raise e
	'''
	Skip flow count..
	'''
	@skipflow_count.setter
	def skipflow_count(self,skipflow_count):
		try :
			if not isinstance(skipflow_count,float):
				raise TypeError("skipflow_count must be set to float value")
			self._skipflow_count = skipflow_count
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
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
	Af Report for ICA Device Skip flow..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_device_skip_flow_obj=ica_device_skip_flow()
				response = ica_device_skip_flow_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_device_skip_flow resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_device_skip_flow_obj = ica_device_skip_flow()
			option_ = options()
			option_._filter=filter_
			return ica_device_skip_flow_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_device_skip_flow resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_device_skip_flow_obj = ica_device_skip_flow()
			option_ = options()
			option_._count=True
			response = ica_device_skip_flow_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_device_skip_flow resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_device_skip_flow_obj = ica_device_skip_flow()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_device_skip_flow_obj.getfiltered(service, option_)
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
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_device_skip_flow_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_device_skip_flow
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_device_skip_flow_responses, response, "ica_device_skip_flow_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_device_skip_flow_response_array
				i=0
				error = [ica_device_skip_flow() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_device_skip_flow_response_array
			i=0
			ica_device_skip_flow_objs = [ica_device_skip_flow() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_device_skip_flow:
					result = service.payload_formatter.string_to_bulk_resource(ica_device_skip_flow_response,self.__class__.__name__,props)
					ica_device_skip_flow_objs[i] = result.ica_device_skip_flow
					i=i+1
			return ica_device_skip_flow_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_device_skip_flow,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_device_skip_flow_response(base_response):
	def __init__(self,length=1) :
		self.ica_device_skip_flow= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_device_skip_flow= [ ica_device_skip_flow() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_device_skip_flow_responses(base_response):
	def __init__(self,length=1) :
		self.ica_device_skip_flow_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_device_skip_flow_response_array = [ ica_device_skip_flow() for _ in range(length)]
