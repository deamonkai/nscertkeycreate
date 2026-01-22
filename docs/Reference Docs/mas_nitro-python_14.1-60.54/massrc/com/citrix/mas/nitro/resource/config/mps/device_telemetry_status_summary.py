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
Configuration for Telemetry summary per device resource
'''

class device_telemetry_status_summary(base_resource):
	_ip_address= ""
	_telemetry_status= ""
	_error_details= ""
	_device_type= ""
	_ssh_state= ""
	_instance_state= ""
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
			return "device_telemetry_status_summary"
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
			return "device_telemetry_status_summarys"
		except Exception as e :
			raise e



	'''
	get Ip Address of the device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Ip Address of the device
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Status of telemetry collection. Returns 0 for success and non-zero for failure
	'''
	@property
	def telemetry_status(self) :
		try:
			return self._telemetry_status
		except Exception as e :
			raise e
	'''
	set Status of telemetry collection. Returns 0 for success and non-zero for failure
	'''
	@telemetry_status.setter
	def telemetry_status(self,telemetry_status):
		try :
			if not isinstance(telemetry_status,int):
				raise TypeError("telemetry_status must be set to int value")
			self._telemetry_status = telemetry_status
		except Exception as e :
			raise e


	'''
	get Details of the error if telemetry collection/SSH failed
	'''
	@property
	def error_details(self) :
		try:
			return self._error_details
		except Exception as e :
			raise e
	'''
	set Details of the error if telemetry collection/SSH failed
	'''
	@error_details.setter
	def error_details(self,error_details):
		try :
			if not isinstance(error_details,str):
				raise TypeError("error_details must be set to str value")
			self._error_details = error_details
		except Exception as e :
			raise e


	'''
	get Device type
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set Device type
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
	get State of SSH connection
	'''
	@property
	def ssh_state(self) :
		try:
			return self._ssh_state
		except Exception as e :
			raise e
	'''
	set State of SSH connection
	'''
	@ssh_state.setter
	def ssh_state(self,ssh_state):
		try :
			if not isinstance(ssh_state,str):
				raise TypeError("ssh_state must be set to str value")
			self._ssh_state = ssh_state
		except Exception as e :
			raise e


	'''
	get State of the instance
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
		except Exception as e :
			raise e
	'''
	set State of the instance
	'''
	@instance_state.setter
	def instance_state(self,instance_state):
		try :
			if not isinstance(instance_state,str):
				raise TypeError("instance_state must be set to str value")
			self._instance_state = instance_state
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_telemetry_status_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_telemetry_status_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_telemetry_status_summary_responses, response, "device_telemetry_status_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_telemetry_status_summary_response_array
				i=0
				error = [device_telemetry_status_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_telemetry_status_summary_response_array
			i=0
			device_telemetry_status_summary_objs = [device_telemetry_status_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_telemetry_status_summary'):
					for props in obj._device_telemetry_status_summary:
						result = service.payload_formatter.string_to_bulk_resource(device_telemetry_status_summary_response,self.__class__.__name__,props)
						device_telemetry_status_summary_objs[i] = result.device_telemetry_status_summary
						i=i+1
			return device_telemetry_status_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_telemetry_status_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_telemetry_status_summary_response(base_response):
	def __init__(self,length=1) :
		self.device_telemetry_status_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_telemetry_status_summary= [ device_telemetry_status_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_telemetry_status_summary_responses(base_response):
	def __init__(self,length=1) :
		self.device_telemetry_status_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_telemetry_status_summary_response_array = [ device_telemetry_status_summary() for _ in range(length)]
