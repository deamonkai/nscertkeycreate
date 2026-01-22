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
Configuration for Af report for ICA User resource
'''

class vpn_info(af_generic_api):
	_active_sessions= ""
	_applications= ""
	___count= ""
	_rpt_sample_time= ""
	_session_count= ""
	_gateways= ""
	_id= ""
	_total_bytes= ""
	_bandwidth= ""
	_active_users= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_info,self).get_object_id()
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
			return "vpn_infos"
		except Exception as e :
			raise e


	'''
	#Active Session
	'''
	@property
	def active_sessions(self):
		try:
			return self._active_sessions
		except Exception as e :
			raise e
	'''
	#Active Session
	'''
	@active_sessions.setter
	def active_sessions(self,active_sessions):
		try :
			if not isinstance(active_sessions,float):
				raise TypeError("active_sessions must be set to float value")
			self._active_sessions = active_sessions
		except Exception as e :
			raise e

	'''
	#Applications
	'''
	@property
	def applications(self):
		try:
			return self._applications
		except Exception as e :
			raise e
	'''
	#Applications
	'''
	@applications.setter
	def applications(self,applications):
		try :
			if not isinstance(applications,float):
				raise TypeError("applications must be set to float value")
			self._applications = applications
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
	Number of sessions launched this application
	'''
	@property
	def session_count(self):
		try:
			return self._session_count
		except Exception as e :
			raise e
	'''
	Number of sessions launched this application
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
	#Gateways
	'''
	@property
	def gateways(self):
		try:
			return self._gateways
		except Exception as e :
			raise e
	'''
	#Gateways
	'''
	@gateways.setter
	def gateways(self,gateways):
		try :
			if not isinstance(gateways,float):
				raise TypeError("gateways must be set to float value")
			self._gateways = gateways
		except Exception as e :
			raise e

	'''
	Id is not dicided yet
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is not dicided yet
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
	Total bytes
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes
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
	#Active Users
	'''
	@property
	def active_users(self):
		try:
			return self._active_users
		except Exception as e :
			raise e
	'''
	#Active Users
	'''
	@active_users.setter
	def active_users(self,active_users):
		try :
			if not isinstance(active_users,float):
				raise TypeError("active_users must be set to float value")
			self._active_users = active_users
		except Exception as e :
			raise e

	'''
	Af Report for VPN Error Counts ....
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_info_obj=vpn_info()
				response = vpn_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_info_obj = vpn_info()
			option_ = options()
			option_._filter=filter_
			return vpn_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_info resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_info_obj = vpn_info()
			option_ = options()
			option_._count=True
			response = vpn_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_info_obj = vpn_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vpn_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_info_responses, response, "vpn_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_info_response_array
				i=0
				error = [vpn_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_info_response_array
			i=0
			vpn_info_objs = [vpn_info() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_info:
					result = service.payload_formatter.string_to_bulk_resource(vpn_info_response,self.__class__.__name__,props)
					vpn_info_objs[i] = result.vpn_info
					i=i+1
			return vpn_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_info_response(base_response):
	def __init__(self,length=1) :
		self.vpn_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_info= [ vpn_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_info_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_info_response_array = [ vpn_info() for _ in range(length)]
