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
from massrc.com.citrix.mas.nitro.resource.config.mps.device_telemetry_status_summary import device_telemetry_status_summary


'''
Configuration for Telemetry history of latest run resource
'''

class telemetry_execution_status(base_resource):
	_execution_time= ""
	_safehaven_connectivity_error_details= ""
	_device_telemetry_status_list=[]
	_evergreen_download_error_details= ""
	_download_connectivity_error_details= ""
	_safehaven_connectivity_status= ""
	_evergreen_download_status= ""
	_overall_execution_status= ""
	_download_connectivity_status= ""
	_package_version= ""
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
			return "telemetry_execution_status"
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
			return "telemetry_execution_statuss"
		except Exception as e :
			raise e


	'''
	Execution time of telemetry
	'''
	@property
	def execution_time(self):
		try:
			return self._execution_time
		except Exception as e :
			raise e
	'''
	Execution time of telemetry
	'''
	@execution_time.setter
	def execution_time(self,execution_time):
		try :
			if not isinstance(execution_time,long):
				raise TypeError("execution_time must be set to long value")
			self._execution_time = execution_time
		except Exception as e :
			raise e

	'''
	Error encountered during safehaven connectivity check
	'''
	@property
	def safehaven_connectivity_error_details(self):
		try:
			return self._safehaven_connectivity_error_details
		except Exception as e :
			raise e
	'''
	Error encountered during safehaven connectivity check
	'''
	@safehaven_connectivity_error_details.setter
	def safehaven_connectivity_error_details(self,safehaven_connectivity_error_details):
		try :
			if not isinstance(safehaven_connectivity_error_details,str):
				raise TypeError("safehaven_connectivity_error_details must be set to str value")
			self._safehaven_connectivity_error_details = safehaven_connectivity_error_details
		except Exception as e :
			raise e

	'''
	Status of devices
	'''
	@property
	def device_telemetry_status_list(self) :
		try:
			return self._device_telemetry_status_list
		except Exception as e :
			raise e
	'''
	Status of devices
	'''
	@device_telemetry_status_list.setter
	def device_telemetry_status_list(self,device_telemetry_status_list) :
		try :
			if not isinstance(device_telemetry_status_list,list):
				raise TypeError("device_telemetry_status_list must be set to array of device_telemetry_status_summary value")
			for item in device_telemetry_status_list :
				if not isinstance(item,device_telemetry_status_summary):
					raise TypeError("item must be set to device_telemetry_status_summary value")
			self._device_telemetry_status_list = device_telemetry_status_list
		except Exception as e :
			raise e

	'''
	Error encountered during downloading telemetry package
	'''
	@property
	def evergreen_download_error_details(self):
		try:
			return self._evergreen_download_error_details
		except Exception as e :
			raise e
	'''
	Error encountered during downloading telemetry package
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
	Error encountered during download connectivity check
	'''
	@property
	def download_connectivity_error_details(self):
		try:
			return self._download_connectivity_error_details
		except Exception as e :
			raise e
	'''
	Error encountered during download connectivity check
	'''
	@download_connectivity_error_details.setter
	def download_connectivity_error_details(self,download_connectivity_error_details):
		try :
			if not isinstance(download_connectivity_error_details,str):
				raise TypeError("download_connectivity_error_details must be set to str value")
			self._download_connectivity_error_details = download_connectivity_error_details
		except Exception as e :
			raise e

	'''
	Status of Safehaven connectivity. Returns 0 for success and non-zero for failure
	'''
	@property
	def safehaven_connectivity_status(self):
		try:
			return self._safehaven_connectivity_status
		except Exception as e :
			raise e
	'''
	Status of Safehaven connectivity. Returns 0 for success and non-zero for failure
	'''
	@safehaven_connectivity_status.setter
	def safehaven_connectivity_status(self,safehaven_connectivity_status):
		try :
			if not isinstance(safehaven_connectivity_status,int):
				raise TypeError("safehaven_connectivity_status must be set to int value")
			self._safehaven_connectivity_status = safehaven_connectivity_status
		except Exception as e :
			raise e

	'''
	Status of evergreen download. Returns 0 for success and non-zero for failure
	'''
	@property
	def evergreen_download_status(self):
		try:
			return self._evergreen_download_status
		except Exception as e :
			raise e
	'''
	Status of evergreen download. Returns 0 for success and non-zero for failure
	'''
	@evergreen_download_status.setter
	def evergreen_download_status(self,evergreen_download_status):
		try :
			if not isinstance(evergreen_download_status,int):
				raise TypeError("evergreen_download_status must be set to int value")
			self._evergreen_download_status = evergreen_download_status
		except Exception as e :
			raise e

	'''
	Overall telemetry execution status
	'''
	@property
	def overall_execution_status(self):
		try:
			return self._overall_execution_status
		except Exception as e :
			raise e
	'''
	Overall telemetry execution status
	'''
	@overall_execution_status.setter
	def overall_execution_status(self,overall_execution_status):
		try :
			if not isinstance(overall_execution_status,str):
				raise TypeError("overall_execution_status must be set to str value")
			self._overall_execution_status = overall_execution_status
		except Exception as e :
			raise e

	'''
	Status of download URL check. Returns 0 for success and non-zero for failure
	'''
	@property
	def download_connectivity_status(self):
		try:
			return self._download_connectivity_status
		except Exception as e :
			raise e
	'''
	Status of download URL check. Returns 0 for success and non-zero for failure
	'''
	@download_connectivity_status.setter
	def download_connectivity_status(self,download_connectivity_status):
		try :
			if not isinstance(download_connectivity_status,int):
				raise TypeError("download_connectivity_status must be set to int value")
			self._download_connectivity_status = download_connectivity_status
		except Exception as e :
			raise e

	'''
	Telemetry package version
	'''
	@property
	def package_version(self):
		try:
			return self._package_version
		except Exception as e :
			raise e
	'''
	Telemetry package version
	'''
	@package_version.setter
	def package_version(self,package_version):
		try :
			if not isinstance(package_version,str):
				raise TypeError("package_version must be set to str value")
			self._package_version = package_version
		except Exception as e :
			raise e

	'''
	Use this operation to get telemetry execution details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				telemetry_execution_status_obj=telemetry_execution_status()
				response = telemetry_execution_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of telemetry_execution_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			telemetry_execution_status_obj = telemetry_execution_status()
			option_ = options()
			option_._filter=filter_
			return telemetry_execution_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the telemetry_execution_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			telemetry_execution_status_obj = telemetry_execution_status()
			option_ = options()
			option_._count=True
			response = telemetry_execution_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of telemetry_execution_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			telemetry_execution_status_obj = telemetry_execution_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = telemetry_execution_status_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(telemetry_execution_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.telemetry_execution_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(telemetry_execution_status_responses, response, "telemetry_execution_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.telemetry_execution_status_response_array
				i=0
				error = [telemetry_execution_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.telemetry_execution_status_response_array
			i=0
			telemetry_execution_status_objs = [telemetry_execution_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_telemetry_execution_status'):
					for props in obj._telemetry_execution_status:
						result = service.payload_formatter.string_to_bulk_resource(telemetry_execution_status_response,self.__class__.__name__,props)
						telemetry_execution_status_objs[i] = result.telemetry_execution_status
						i=i+1
			return telemetry_execution_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(telemetry_execution_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class telemetry_execution_status_response(base_response):
	def __init__(self,length=1) :
		self.telemetry_execution_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.telemetry_execution_status= [ telemetry_execution_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class telemetry_execution_status_responses(base_response):
	def __init__(self,length=1) :
		self.telemetry_execution_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.telemetry_execution_status_response_array = [ telemetry_execution_status() for _ in range(length)]
