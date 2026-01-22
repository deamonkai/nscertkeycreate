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
Configuration for OnpremDiag resource
'''

class onprem_diag(base_resource):
	_download_connectivity_status= ""
	_is_user_triggered= ""
	_status= ""
	_adm= ""
	_safehaven_connectivity_status= ""
	_safehaven_connectivity_error_details= ""
	_id= ""
	_start_time= ""
	_download= ""
	_end_time= ""
	_safehaven= ""
	_managed_device_status= ""
	_download_connectivity_error_details= ""
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
			return "onprem_diag"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "onprem_diags"
		except Exception as e :
			raise e



	'''
	get Status of download URL check. Returns 0 for success and non-zero for failure
	'''
	@property
	def download_connectivity_status(self) :
		try:
			return self._download_connectivity_status
		except Exception as e :
			raise e
	'''
	set Status of download URL check. Returns 0 for success and non-zero for failure
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
	get is triggered by user
	'''
	@property
	def is_user_triggered(self) :
		try:
			return self._is_user_triggered
		except Exception as e :
			raise e
	'''
	set is triggered by user
	'''
	@is_user_triggered.setter
	def is_user_triggered(self,is_user_triggered):
		try :
			if not isinstance(is_user_triggered,bool):
				raise TypeError("is_user_triggered must be set to bool value")
			self._is_user_triggered = is_user_triggered
		except Exception as e :
			raise e


	'''
	get Diagnostics status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Diagnostics status
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
	get check if is ADM reachable
	'''
	@property
	def adm(self) :
		try:
			return self._adm
		except Exception as e :
			raise e
	'''
	set check if is ADM reachable
	'''
	@adm.setter
	def adm(self,adm):
		try :
			if not isinstance(adm,str):
				raise TypeError("adm must be set to str value")
			self._adm = adm
		except Exception as e :
			raise e


	'''
	get Status of Safehaven connectivity. Returns 0 for success and non-zero for failure
	'''
	@property
	def safehaven_connectivity_status(self) :
		try:
			return self._safehaven_connectivity_status
		except Exception as e :
			raise e
	'''
	set Status of Safehaven connectivity. Returns 0 for success and non-zero for failure
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
	get Error encountered during safehaven connectivity check
	'''
	@property
	def safehaven_connectivity_error_details(self) :
		try:
			return self._safehaven_connectivity_error_details
		except Exception as e :
			raise e
	'''
	set Error encountered during safehaven connectivity check
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
	get ID of Security Advisory scan
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID of Security Advisory scan
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
	get Start time of diagnostics test
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e
	'''
	set Start time of diagnostics test
	'''
	@start_time.setter
	def start_time(self,start_time):
		try :
			if not isinstance(start_time,long):
				raise TypeError("start_time must be set to long value")
			self._start_time = start_time
		except Exception as e :
			raise e


	'''
	get Check if Download server is reachable
	'''
	@property
	def download(self) :
		try:
			return self._download
		except Exception as e :
			raise e
	'''
	set Check if Download server is reachable
	'''
	@download.setter
	def download(self,download):
		try :
			if not isinstance(download,str):
				raise TypeError("download must be set to str value")
			self._download = download
		except Exception as e :
			raise e


	'''
	get End time of diagnostics test
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set End time of diagnostics test
	'''
	@end_time.setter
	def end_time(self,end_time):
		try :
			if not isinstance(end_time,long):
				raise TypeError("end_time must be set to long value")
			self._end_time = end_time
		except Exception as e :
			raise e


	'''
	get check if is Safehaven reachable
	'''
	@property
	def safehaven(self) :
		try:
			return self._safehaven
		except Exception as e :
			raise e
	'''
	set check if is Safehaven reachable
	'''
	@safehaven.setter
	def safehaven(self,safehaven):
		try :
			if not isinstance(safehaven,str):
				raise TypeError("safehaven must be set to str value")
			self._safehaven = safehaven
		except Exception as e :
			raise e


	'''
	get Devices list with IP Address and status
	'''
	@property
	def managed_device_status(self) :
		try:
			return self._managed_device_status
		except Exception as e :
			raise e
	'''
	set Devices list with IP Address and status
	'''
	@managed_device_status.setter
	def managed_device_status(self,managed_device_status):
		try :
			if not isinstance(managed_device_status,str):
				raise TypeError("managed_device_status must be set to str value")
			self._managed_device_status = managed_device_status
		except Exception as e :
			raise e


	'''
	get Error encountered during download connectivity check
	'''
	@property
	def download_connectivity_error_details(self) :
		try:
			return self._download_connectivity_error_details
		except Exception as e :
			raise e
	'''
	set Error encountered during download connectivity check
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
	Use this operation to run onprem diagnostics.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				onprem_diag_obj= onprem_diag()
				return cls.perform_operation_bulk_request(service,resource,onprem_diag_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get onprem diagnostics status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				onprem_diag_obj=onprem_diag()
				response = onprem_diag_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of onprem_diag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			onprem_diag_obj = onprem_diag()
			option_ = options()
			option_._filter=filter_
			return onprem_diag_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the onprem_diag resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			onprem_diag_obj = onprem_diag()
			option_ = options()
			option_._count=True
			response = onprem_diag_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of onprem_diag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			onprem_diag_obj = onprem_diag()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = onprem_diag_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(onprem_diag_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.onprem_diag
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(onprem_diag_responses, response, "onprem_diag_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.onprem_diag_response_array
				i=0
				error = [onprem_diag() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.onprem_diag_response_array
			i=0
			onprem_diag_objs = [onprem_diag() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_onprem_diag'):
					for props in obj._onprem_diag:
						result = service.payload_formatter.string_to_bulk_resource(onprem_diag_response,self.__class__.__name__,props)
						onprem_diag_objs[i] = result.onprem_diag
						i=i+1
			return onprem_diag_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(onprem_diag,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class onprem_diag_response(base_response):
	def __init__(self,length=1) :
		self.onprem_diag= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.onprem_diag= [ onprem_diag() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class onprem_diag_responses(base_response):
	def __init__(self,length=1) :
		self.onprem_diag_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.onprem_diag_response_array = [ onprem_diag() for _ in range(length)]
