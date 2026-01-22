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
Configuration for Af report for ICA App timeline resource
'''

class ica_app_timeline(af_generic_api):
	_up_time= ""
	_rpt_sample_time= ""
	_active_launches= ""
	_launch_duration= ""
	_total_bytes= ""
	_ica_device_ip_address= ""
	___count= ""
	_state= ""
	_is_active= ""
	_user_count= ""
	_app_start_time= ""
	_app_enumeration_duration= ""
	_name= ""
	_app_count= ""
	_ica_user_name= ""
	_app_terminate_time= ""
	_usage_time= ""
	_id= ""
	_app_launch_count= ""
	_ica_session_id= ""
	_timeline_user_count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_app_timeline"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_app_timeline,self).get_object_id()
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
			return "ica_app_timelines"
		except Exception as e :
			raise e


	'''
	ica app up time.
	'''
	@property
	def up_time(self):
		try:
			return self._up_time
		except Exception as e :
			raise e
	'''
	ica app up time.
	'''
	@up_time.setter
	def up_time(self,up_time):
		try :
			if not isinstance(up_time,float):
				raise TypeError("up_time must be set to float value")
			self._up_time = up_time
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
	ica active_launches
	'''
	@property
	def active_launches(self):
		try:
			return self._active_launches
		except Exception as e :
			raise e
	'''
	ica active_launches
	'''
	@active_launches.setter
	def active_launches(self,active_launches):
		try :
			if not isinstance(active_launches,float):
				raise TypeError("active_launches must be set to float value")
			self._active_launches = active_launches
		except Exception as e :
			raise e

	'''
	ICA App launch duration.
	'''
	@property
	def launch_duration(self):
		try:
			return self._launch_duration
		except Exception as e :
			raise e
	'''
	ICA App launch duration.
	'''
	@launch_duration.setter
	def launch_duration(self,launch_duration):
		try :
			if not isinstance(launch_duration,float):
				raise TypeError("launch_duration must be set to float value")
			self._launch_duration = launch_duration
		except Exception as e :
			raise e

	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
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
	App state.
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	App state.
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e

	'''
	Is Active.
	'''
	@property
	def is_active(self):
		try:
			return self._is_active
		except Exception as e :
			raise e
	'''
	Is Active.
	'''
	@is_active.setter
	def is_active(self,is_active):
		try :
			if not isinstance(is_active,float):
				raise TypeError("is_active must be set to float value")
			self._is_active = is_active
		except Exception as e :
			raise e

	'''
	user_count.
	'''
	@property
	def user_count(self):
		try:
			return self._user_count
		except Exception as e :
			raise e
	'''
	user_count.
	'''
	@user_count.setter
	def user_count(self,user_count):
		try :
			if not isinstance(user_count,float):
				raise TypeError("user_count must be set to float value")
			self._user_count = user_count
		except Exception as e :
			raise e

	'''
	Application start time.
	'''
	@property
	def app_start_time(self):
		try:
			return self._app_start_time
		except Exception as e :
			raise e
	'''
	Application start time.
	'''
	@app_start_time.setter
	def app_start_time(self,app_start_time):
		try :
			if not isinstance(app_start_time,float):
				raise TypeError("app_start_time must be set to float value")
			self._app_start_time = app_start_time
		except Exception as e :
			raise e

	'''
	ica app enumeration duration.
	'''
	@property
	def app_enumeration_duration(self):
		try:
			return self._app_enumeration_duration
		except Exception as e :
			raise e
	'''
	ica app enumeration duration.
	'''
	@app_enumeration_duration.setter
	def app_enumeration_duration(self,app_enumeration_duration):
		try :
			if not isinstance(app_enumeration_duration,float):
				raise TypeError("app_enumeration_duration must be set to float value")
			self._app_enumeration_duration = app_enumeration_duration
		except Exception as e :
			raise e

	'''
	Name of ICA Device
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA Device
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
	ica app_count.
	'''
	@property
	def app_count(self):
		try:
			return self._app_count
		except Exception as e :
			raise e
	'''
	ica app_count.
	'''
	@app_count.setter
	def app_count(self,app_count):
		try :
			if not isinstance(app_count,float):
				raise TypeError("app_count must be set to float value")
			self._app_count = app_count
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
	Application terminate time.
	'''
	@property
	def app_terminate_time(self):
		try:
			return self._app_terminate_time
		except Exception as e :
			raise e
	'''
	Application terminate time.
	'''
	@app_terminate_time.setter
	def app_terminate_time(self,app_terminate_time):
		try :
			if not isinstance(app_terminate_time,float):
				raise TypeError("app_terminate_time must be set to float value")
			self._app_terminate_time = app_terminate_time
		except Exception as e :
			raise e

	'''
	ica app usages time.
	'''
	@property
	def usage_time(self):
		try:
			return self._usage_time
		except Exception as e :
			raise e
	'''
	ica app usages time.
	'''
	@usage_time.setter
	def usage_time(self,usage_time):
		try :
			if not isinstance(usage_time,float):
				raise TypeError("usage_time must be set to float value")
			self._usage_time = usage_time
		except Exception as e :
			raise e

	'''
	Id is ICA App  Name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA App  Name
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
	ica app_launch_count
	'''
	@property
	def app_launch_count(self):
		try:
			return self._app_launch_count
		except Exception as e :
			raise e
	'''
	ica app_launch_count
	'''
	@app_launch_count.setter
	def app_launch_count(self,app_launch_count):
		try :
			if not isinstance(app_launch_count,float):
				raise TypeError("app_launch_count must be set to float value")
			self._app_launch_count = app_launch_count
		except Exception as e :
			raise e

	'''
	Id is ICA Session ID
	'''
	@property
	def ica_session_id(self):
		try:
			return self._ica_session_id
		except Exception as e :
			raise e
	'''
	Id is ICA Session ID
	'''
	@ica_session_id.setter
	def ica_session_id(self,ica_session_id):
		try :
			if not isinstance(ica_session_id,str):
				raise TypeError("ica_session_id must be set to str value")
			self._ica_session_id = ica_session_id
		except Exception as e :
			raise e

	'''
	timeline_user_count.
	'''
	@property
	def timeline_user_count(self):
		try:
			return self._timeline_user_count
		except Exception as e :
			raise e
	'''
	timeline_user_count.
	'''
	@timeline_user_count.setter
	def timeline_user_count(self,timeline_user_count):
		try :
			if not isinstance(timeline_user_count,float):
				raise TypeError("timeline_user_count must be set to float value")
			self._timeline_user_count = timeline_user_count
		except Exception as e :
			raise e

	'''
	Af Report for ICA App timeline..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_app_timeline_obj=ica_app_timeline()
				response = ica_app_timeline_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_app_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_app_timeline_obj = ica_app_timeline()
			option_ = options()
			option_._filter=filter_
			return ica_app_timeline_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_app_timeline resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_app_timeline_obj = ica_app_timeline()
			option_ = options()
			option_._count=True
			response = ica_app_timeline_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_app_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_app_timeline_obj = ica_app_timeline()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_app_timeline_obj.getfiltered(service, option_)
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
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

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
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_app_timeline_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_app_timeline
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_app_timeline_responses, response, "ica_app_timeline_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_app_timeline_response_array
				i=0
				error = [ica_app_timeline() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_app_timeline_response_array
			i=0
			ica_app_timeline_objs = [ica_app_timeline() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_app_timeline:
					result = service.payload_formatter.string_to_bulk_resource(ica_app_timeline_response,self.__class__.__name__,props)
					ica_app_timeline_objs[i] = result.ica_app_timeline
					i=i+1
			return ica_app_timeline_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_app_timeline,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_app_timeline_response(base_response):
	def __init__(self,length=1) :
		self.ica_app_timeline= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_app_timeline= [ ica_app_timeline() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_app_timeline_responses(base_response):
	def __init__(self,length=1) :
		self.ica_app_timeline_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_app_timeline_response_array = [ ica_app_timeline() for _ in range(length)]
