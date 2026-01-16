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
Configuration for Af report for ICA Channel resource
'''

class ica_channel(af_generic_api):
	_channel_count= ""
	___count= ""
	_ica_app_name= ""
	_name= ""
	_ica_user_name= ""
	_id= ""
	_description= ""
	_rpt_sample_time= ""
	_bandwidth= ""
	_total_bytes= ""
	_ica_device_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_channel"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_channel,self).get_object_id()
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
			return "ica_channels"
		except Exception as e :
			raise e


	'''
	no_of_channels.
	'''
	@property
	def channel_count(self):
		try:
			return self._channel_count
		except Exception as e :
			raise e
	'''
	no_of_channels.
	'''
	@channel_count.setter
	def channel_count(self,channel_count):
		try :
			if not isinstance(channel_count,float):
				raise TypeError("channel_count must be set to float value")
			self._channel_count = channel_count
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
	Name of ICA app
	'''
	@property
	def ica_app_name(self):
		try:
			return self._ica_app_name
		except Exception as e :
			raise e
	'''
	Name of ICA app
	'''
	@ica_app_name.setter
	def ica_app_name(self,ica_app_name):
		try :
			if not isinstance(ica_app_name,str):
				raise TypeError("ica_app_name must be set to str value")
			self._ica_app_name = ica_app_name
		except Exception as e :
			raise e

	'''
	Name of ICA Channel
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA Channel
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
	Name of ICA User
	'''
	@property
	def ica_user_name(self):
		try:
			return self._ica_user_name
		except Exception as e :
			raise e
	'''
	Name of ICA User
	'''
	@ica_user_name.setter
	def ica_user_name(self,ica_user_name):
		try :
			if not isinstance(ica_user_name,str):
				raise TypeError("ica_user_name must be set to str value")
			self._ica_user_name = ica_user_name
		except Exception as e :
			raise e

	'''
	Id is ICA Channel
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Channel
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
	Description of ICA Channel
	'''
	@property
	def description(self):
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	Description of ICA Channel
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
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
	Avg Bandwidth.
	'''
	@property
	def bandwidth(self):
		try:
			return self._bandwidth
		except Exception as e :
			raise e
	'''
	Avg Bandwidth.
	'''
	@bandwidth.setter
	def bandwidth(self,bandwidth):
		try :
			if not isinstance(bandwidth,float):
				raise TypeError("bandwidth must be set to float value")
			self._bandwidth = bandwidth
		except Exception as e :
			raise e

	'''
	Total bytes accounted by ICA Channel in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by ICA Channel in sampled timeframe.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,float):
				raise TypeError("total_bytes must be set to float value")
			self._total_bytes = total_bytes
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
	Af Report for ICA Channel..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_channel_obj=ica_channel()
				response = ica_channel_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_channel resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_channel_obj = ica_channel()
			option_ = options()
			option_._filter=filter_
			return ica_channel_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_channel resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_channel_obj = ica_channel()
			option_ = options()
			option_._count=True
			response = ica_channel_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_channel resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_channel_obj = ica_channel()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_channel_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_channel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_channel
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_channel_responses, response, "ica_channel_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_channel_response_array
				i=0
				error = [ica_channel() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_channel_response_array
			i=0
			ica_channel_objs = [ica_channel() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_channel:
					result = service.payload_formatter.string_to_bulk_resource(ica_channel_response,self.__class__.__name__,props)
					ica_channel_objs[i] = result.ica_channel
					i=i+1
			return ica_channel_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_channel,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_channel_response(base_response):
	def __init__(self,length=1) :
		self.ica_channel= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_channel= [ ica_channel() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_channel_responses(base_response):
	def __init__(self,length=1) :
		self.ica_channel_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_channel_response_array = [ ica_channel() for _ in range(length)]
