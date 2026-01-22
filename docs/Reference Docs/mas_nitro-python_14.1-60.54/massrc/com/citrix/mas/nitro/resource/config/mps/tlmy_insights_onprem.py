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

class tlmy_insights_onprem(base_resource):
	_tlmy_package_version= ""
	_device_type= ""
	_time_stamp= ""
	_evergreen_download_status= ""
	_error_message= ""
	_error_code= ""
	_device_ip= ""
	_failure_step= ""
	_device_id= ""
	_telemetry_name= ""
	_token= ""
	_evergreen_download_error_details= ""
	_telemetry_level= ""
	_telemetry_status= ""
	_device_version= ""
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
			return "tlmy_insights_onprem"
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
			return "tlmy_insights_onprems"
		except Exception as e :
			raise e



	'''
	get Telemetry package version
	'''
	@property
	def tlmy_package_version(self) :
		try:
			return self._tlmy_package_version
		except Exception as e :
			raise e
	'''
	set Telemetry package version
	'''
	@tlmy_package_version.setter
	def tlmy_package_version(self,tlmy_package_version):
		try :
			if not isinstance(tlmy_package_version,str):
				raise TypeError("tlmy_package_version must be set to str value")
			self._tlmy_package_version = tlmy_package_version
		except Exception as e :
			raise e


	'''
	get Type of the device
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set Type of the device
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
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
	get Error encountered during telemetry execution
	'''
	@property
	def error_message(self) :
		try:
			return self._error_message
		except Exception as e :
			raise e
	'''
	set Error encountered during telemetry execution
	'''
	@error_message.setter
	def error_message(self,error_message):
		try :
			if not isinstance(error_message,str):
				raise TypeError("error_message must be set to str value")
			self._error_message = error_message
		except Exception as e :
			raise e


	'''
	get Error code
	'''
	@property
	def error_code(self) :
		try:
			return self._error_code
		except Exception as e :
			raise e
	'''
	set Error code
	'''
	@error_code.setter
	def error_code(self,error_code):
		try :
			if not isinstance(error_code,str):
				raise TypeError("error_code must be set to str value")
			self._error_code = error_code
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
	get Failure step of the telemetry execution
	'''
	@property
	def failure_step(self) :
		try:
			return self._failure_step
		except Exception as e :
			raise e
	'''
	set Failure step of the telemetry execution
	'''
	@failure_step.setter
	def failure_step(self,failure_step):
		try :
			if not isinstance(failure_step,str):
				raise TypeError("failure_step must be set to str value")
			self._failure_step = failure_step
		except Exception as e :
			raise e


	'''
	get ID of the device
	'''
	@property
	def device_id(self) :
		try:
			return self._device_id
		except Exception as e :
			raise e
	'''
	set ID of the device
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
	get Name/type of the telemetry collected
	'''
	@property
	def telemetry_name(self) :
		try:
			return self._telemetry_name
		except Exception as e :
			raise e
	'''
	set Name/type of the telemetry collected
	'''
	@telemetry_name.setter
	def telemetry_name(self,telemetry_name):
		try :
			if not isinstance(telemetry_name,str):
				raise TypeError("telemetry_name must be set to str value")
			self._telemetry_name = telemetry_name
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
	get Telemetry level
	'''
	@property
	def telemetry_level(self) :
		try:
			return self._telemetry_level
		except Exception as e :
			raise e
	'''
	set Telemetry level
	'''
	@telemetry_level.setter
	def telemetry_level(self,telemetry_level):
		try :
			if not isinstance(telemetry_level,str):
				raise TypeError("telemetry_level must be set to str value")
			self._telemetry_level = telemetry_level
		except Exception as e :
			raise e


	'''
	get Status of the telemetry execution - success/failure
	'''
	@property
	def telemetry_status(self) :
		try:
			return self._telemetry_status
		except Exception as e :
			raise e
	'''
	set Status of the telemetry execution - success/failure
	'''
	@telemetry_status.setter
	def telemetry_status(self,telemetry_status):
		try :
			if not isinstance(telemetry_status,str):
				raise TypeError("telemetry_status must be set to str value")
			self._telemetry_status = telemetry_status
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_insights_onprem_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tlmy_insights_onprem
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_insights_onprem_responses, response, "tlmy_insights_onprem_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tlmy_insights_onprem_response_array
				i=0
				error = [tlmy_insights_onprem() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tlmy_insights_onprem_response_array
			i=0
			tlmy_insights_onprem_objs = [tlmy_insights_onprem() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tlmy_insights_onprem'):
					for props in obj._tlmy_insights_onprem:
						result = service.payload_formatter.string_to_bulk_resource(tlmy_insights_onprem_response,self.__class__.__name__,props)
						tlmy_insights_onprem_objs[i] = result.tlmy_insights_onprem
						i=i+1
			return tlmy_insights_onprem_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tlmy_insights_onprem,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tlmy_insights_onprem_response(base_response):
	def __init__(self,length=1) :
		self.tlmy_insights_onprem= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tlmy_insights_onprem= [ tlmy_insights_onprem() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tlmy_insights_onprem_responses(base_response):
	def __init__(self,length=1) :
		self.tlmy_insights_onprem_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tlmy_insights_onprem_response_array = [ tlmy_insights_onprem() for _ in range(length)]
