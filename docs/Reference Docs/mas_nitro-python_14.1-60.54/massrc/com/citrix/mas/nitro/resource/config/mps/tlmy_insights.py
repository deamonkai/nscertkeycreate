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
Configuration for Telemetry Insights resource
'''

class tlmy_insights(base_resource):
	_evergreen_download_error_details= ""
	_token= ""
	_device_id= ""
	_agent_version= ""
	_device_ip= ""
	_evergreen_download_status= ""
	_time_stamp= ""
	_agent_ip= ""
	_name= ""
	_managed_by= ""
	_device_version= ""
	_status= ""
	_err_details= ""
	_exec_step= ""
	_pkg_ver= ""
	__count=""
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
			return "tlmy_insights"
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
			return "tlmy_insightss"
		except Exception as e :
			raise e



	'''
	get Error encountered during downloading telemetry package
	'''
	@property
	def evergreen_download_error_details(self) :
		try:
			return self._evergreen_download_error_details
		except Exception as e :
			raise e
	'''
	set Error encountered during downloading telemetry package
	'''
	@evergreen_download_error_details.setter
	def evergreen_download_error_details(self,evergreen_download_error_details):
		try :
			if not isinstance(evergreen_download_error_details,str):
				raise TypeError("evergreen_download_error_details must be set to str value")
			self._evergreen_download_error_details = evergreen_download_error_details
		except Exception as e :
			raise e


	'''
	get Telemetry execution token
	'''
	@property
	def token(self) :
		try:
			return self._token
		except Exception as e :
			raise e
	'''
	set Telemetry execution token
	'''
	@token.setter
	def token(self,token):
		try :
			if not isinstance(token,str):
				raise TypeError("token must be set to str value")
			self._token = token
		except Exception as e :
			raise e


	'''
	get ID of the device - foreign key to tlmy_ns_device.id column
	'''
	@property
	def device_id(self) :
		try:
			return self._device_id
		except Exception as e :
			raise e
	'''
	set ID of the device - foreign key to tlmy_ns_device.id column
	'''
	@device_id.setter
	def device_id(self,device_id):
		try :
			if not isinstance(device_id,str):
				raise TypeError("device_id must be set to str value")
			self._device_id = device_id
		except Exception as e :
			raise e


	'''
	get Version of the agent managing the device
	'''
	@property
	def agent_version(self) :
		try:
			return self._agent_version
		except Exception as e :
			raise e
	'''
	set Version of the agent managing the device
	'''
	@agent_version.setter
	def agent_version(self,agent_version):
		try :
			if not isinstance(agent_version,str):
				raise TypeError("agent_version must be set to str value")
			self._agent_version = agent_version
		except Exception as e :
			raise e


	'''
	get Ip Address of the device
	'''
	@property
	def device_ip(self) :
		try:
			return self._device_ip
		except Exception as e :
			raise e
	'''
	set Ip Address of the device
	'''
	@device_ip.setter
	def device_ip(self,device_ip):
		try :
			if not isinstance(device_ip,str):
				raise TypeError("device_ip must be set to str value")
			self._device_ip = device_ip
		except Exception as e :
			raise e


	'''
	get Status of evergreen download
	'''
	@property
	def evergreen_download_status(self) :
		try:
			return self._evergreen_download_status
		except Exception as e :
			raise e
	'''
	set Status of evergreen download
	'''
	@evergreen_download_status.setter
	def evergreen_download_status(self,evergreen_download_status):
		try :
			if not isinstance(evergreen_download_status,str):
				raise TypeError("evergreen_download_status must be set to str value")
			self._evergreen_download_status = evergreen_download_status
		except Exception as e :
			raise e


	'''
	get Timestamp of the telemetry execution
	'''
	@property
	def time_stamp(self) :
		try:
			return self._time_stamp
		except Exception as e :
			raise e
	'''
	set Timestamp of the telemetry execution
	'''
	@time_stamp.setter
	def time_stamp(self,time_stamp):
		try :
			if not isinstance(time_stamp,long):
				raise TypeError("time_stamp must be set to long value")
			self._time_stamp = time_stamp
		except Exception as e :
			raise e


	'''
	get Ip Address of the agent managing the device
	'''
	@property
	def agent_ip(self) :
		try:
			return self._agent_ip
		except Exception as e :
			raise e
	'''
	set Ip Address of the agent managing the device
	'''
	@agent_ip.setter
	def agent_ip(self,agent_ip):
		try :
			if not isinstance(agent_ip,str):
				raise TypeError("agent_ip must be set to str value")
			self._agent_ip = agent_ip
		except Exception as e :
			raise e


	'''
	get Name/type of the telemetry collected
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name/type of the telemetry collected
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
	get Type of the agent managing the device
	'''
	@property
	def managed_by(self) :
		try:
			return self._managed_by
		except Exception as e :
			raise e
	'''
	set Type of the agent managing the device
	'''
	@managed_by.setter
	def managed_by(self,managed_by):
		try :
			if not isinstance(managed_by,str):
				raise TypeError("managed_by must be set to str value")
			self._managed_by = managed_by
		except Exception as e :
			raise e


	'''
	get Version of the device
	'''
	@property
	def device_version(self) :
		try:
			return self._device_version
		except Exception as e :
			raise e
	'''
	set Version of the device
	'''
	@device_version.setter
	def device_version(self,device_version):
		try :
			if not isinstance(device_version,str):
				raise TypeError("device_version must be set to str value")
			self._device_version = device_version
		except Exception as e :
			raise e


	'''
	get Status of the telemetry execution - success/failure
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of the telemetry execution - success/failure
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Error encountered during telemetry execution
	'''
	@property
	def err_details(self) :
		try:
			return self._err_details
		except Exception as e :
			raise e
	'''
	set Error encountered during telemetry execution
	'''
	@err_details.setter
	def err_details(self,err_details):
		try :
			if not isinstance(err_details,str):
				raise TypeError("err_details must be set to str value")
			self._err_details = err_details
		except Exception as e :
			raise e


	'''
	get Step of the telemetry execution
	'''
	@property
	def exec_step(self) :
		try:
			return self._exec_step
		except Exception as e :
			raise e
	'''
	set Step of the telemetry execution
	'''
	@exec_step.setter
	def exec_step(self,exec_step):
		try :
			if not isinstance(exec_step,str):
				raise TypeError("exec_step must be set to str value")
			self._exec_step = exec_step
		except Exception as e :
			raise e


	'''
	get Telemetry package version
	'''
	@property
	def pkg_ver(self) :
		try:
			return self._pkg_ver
		except Exception as e :
			raise e
	'''
	set Telemetry package version
	'''
	@pkg_ver.setter
	def pkg_ver(self,pkg_ver):
		try :
			if not isinstance(pkg_ver,str):
				raise TypeError("pkg_ver must be set to str value")
			self._pkg_ver = pkg_ver
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_insights_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tlmy_insights
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_insights_responses, response, "tlmy_insights_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tlmy_insights_response_array
				i=0
				error = [tlmy_insights() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tlmy_insights_response_array
			i=0
			tlmy_insights_objs = [tlmy_insights() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tlmy_insights'):
					for props in obj._tlmy_insights:
						result = service.payload_formatter.string_to_bulk_resource(tlmy_insights_response,self.__class__.__name__,props)
						tlmy_insights_objs[i] = result.tlmy_insights
						i=i+1
			return tlmy_insights_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tlmy_insights,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tlmy_insights_response(base_response):
	def __init__(self,length=1) :
		self.tlmy_insights= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tlmy_insights= [ tlmy_insights() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tlmy_insights_responses(base_response):
	def __init__(self,length=1) :
		self.tlmy_insights_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tlmy_insights_response_array = [ tlmy_insights() for _ in range(length)]
