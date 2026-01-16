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
Configuration for Af report for VPN User resource
'''

class vpn_user_info(af_generic_api):
	_logon_duration= ""
	_bandwidth= ""
	_name= ""
	_session_count= ""
	_id= ""
	_total_bytes= ""
	_rpt_sample_time= ""
	___count= ""
	_active_session= ""
	_session_used= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_user_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_user_info,self).get_object_id()
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
			return "vpn_user_infos"
		except Exception as e :
			raise e


	'''
	Logon duration of user in seconds
	'''
	@property
	def logon_duration(self):
		try:
			return self._logon_duration
		except Exception as e :
			raise e
	'''
	Logon duration of user in seconds
	'''
	@logon_duration.setter
	def logon_duration(self,logon_duration):
		try :
			if not isinstance(logon_duration,long):
				raise TypeError("logon_duration must be set to long value")
			self._logon_duration = logon_duration
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
	Name of ICA User
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA User
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
	Number of sessions launched by user
	'''
	@property
	def session_count(self):
		try:
			return self._session_count
		except Exception as e :
			raise e
	'''
	Number of sessions launched by user
	'''
	@session_count.setter
	def session_count(self,session_count):
		try :
			if not isinstance(session_count,float):
				raise TypeError("session_count must be set to float value")
			self._session_count = session_count
		except Exception as e :
			raise e

	'''
	Id is ICA User Name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA User Name
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
	Total bytes in sampled timeframe used by all users.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes in sampled timeframe used by all users.
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
	Number of active sessions launched by user
	'''
	@property
	def active_session(self):
		try:
			return self._active_session
		except Exception as e :
			raise e
	'''
	Number of active sessions launched by user
	'''
	@active_session.setter
	def active_session(self,active_session):
		try :
			if not isinstance(active_session,float):
				raise TypeError("active_session must be set to float value")
			self._active_session = active_session
		except Exception as e :
			raise e

	'''
	Number of  sessions used by user
	'''
	@property
	def session_used(self):
		try:
			return self._session_used
		except Exception as e :
			raise e
	'''
	Number of  sessions used by user
	'''
	@session_used.setter
	def session_used(self,session_used):
		try :
			if not isinstance(session_used,float):
				raise TypeError("session_used must be set to float value")
			self._session_used = session_used
		except Exception as e :
			raise e

	'''
	Af Report for ICA User..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_user_info_obj=vpn_user_info()
				response = vpn_user_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_user_info_obj = vpn_user_info()
			option_ = options()
			option_._filter=filter_
			return vpn_user_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_user_info resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_user_info_obj = vpn_user_info()
			option_ = options()
			option_._count=True
			response = vpn_user_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_user_info_obj = vpn_user_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_user_info_obj.getfiltered(service, option_)
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_user_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_user_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_user_info_responses, response, "vpn_user_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_user_info_response_array
				i=0
				error = [vpn_user_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_user_info_response_array
			i=0
			vpn_user_info_objs = [vpn_user_info() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_user_info:
					result = service.payload_formatter.string_to_bulk_resource(vpn_user_info_response,self.__class__.__name__,props)
					vpn_user_info_objs[i] = result.vpn_user_info
					i=i+1
			return vpn_user_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_user_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_user_info_response(base_response):
	def __init__(self,length=1) :
		self.vpn_user_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_user_info= [ vpn_user_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_user_info_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_user_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_user_info_response_array = [ vpn_user_info() for _ in range(length)]
