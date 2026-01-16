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
Configuration for Telemetry Information resource
'''

class telemetry_info(base_resource):
	_telemetry_mode= ""
	_enable_security_advisory= ""
	_id= ""
	_manual_mode_selection_date= ""
	_enable_basic_telemetry= ""
	_enable_optional_telemetry= ""
	_host_id= ""
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
			return "telemetry_info"
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
			return "telemetry_infos"
		except Exception as e :
			raise e



	'''
	get Telemetry Mode (MANUAL or AUTOMATED)
	'''
	@property
	def telemetry_mode(self) :
		try:
			return self._telemetry_mode
		except Exception as e :
			raise e
	'''
	set Telemetry Mode (MANUAL or AUTOMATED)
	'''
	@telemetry_mode.setter
	def telemetry_mode(self,telemetry_mode):
		try :
			if not isinstance(telemetry_mode,str):
				raise TypeError("telemetry_mode must be set to str value")
			self._telemetry_mode = telemetry_mode
		except Exception as e :
			raise e


	'''
	get Enable Security Advisory
	'''
	@property
	def enable_security_advisory(self) :
		try:
			return self._enable_security_advisory
		except Exception as e :
			raise e
	'''
	set Enable Security Advisory
	'''
	@enable_security_advisory.setter
	def enable_security_advisory(self,enable_security_advisory):
		try :
			if not isinstance(enable_security_advisory,bool):
				raise TypeError("enable_security_advisory must be set to bool value")
			self._enable_security_advisory = enable_security_advisory
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the cloud profiles
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the cloud profiles
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
	get Date Manual mode was selected (EPOCH)
	'''
	@property
	def manual_mode_selection_date(self) :
		try:
			return self._manual_mode_selection_date
		except Exception as e :
			raise e


	'''
	get Enable Basic Telemetry
	'''
	@property
	def enable_basic_telemetry(self) :
		try:
			return self._enable_basic_telemetry
		except Exception as e :
			raise e
	'''
	set Enable Basic Telemetry
	'''
	@enable_basic_telemetry.setter
	def enable_basic_telemetry(self,enable_basic_telemetry):
		try :
			if not isinstance(enable_basic_telemetry,bool):
				raise TypeError("enable_basic_telemetry must be set to bool value")
			self._enable_basic_telemetry = enable_basic_telemetry
		except Exception as e :
			raise e


	'''
	get Enable Optional Telemetry
	'''
	@property
	def enable_optional_telemetry(self) :
		try:
			return self._enable_optional_telemetry
		except Exception as e :
			raise e
	'''
	set Enable Optional Telemetry
	'''
	@enable_optional_telemetry.setter
	def enable_optional_telemetry(self,enable_optional_telemetry):
		try :
			if not isinstance(enable_optional_telemetry,bool):
				raise TypeError("enable_optional_telemetry must be set to bool value")
			self._enable_optional_telemetry = enable_optional_telemetry
		except Exception as e :
			raise e

	'''
	ADM Host id
	'''
	@property
	def host_id(self):
		try:
			return self._host_id
		except Exception as e :
			raise e
	'''
	ADM Host id
	'''
	@host_id.setter
	def host_id(self,host_id):
		try :
			if not isinstance(host_id,str):
				raise TypeError("host_id must be set to str value")
			self._host_id = host_id
		except Exception as e :
			raise e

	'''
	Telemetry Package version
	'''
	@property
	def package_version(self):
		try:
			return self._package_version
		except Exception as e :
			raise e
	'''
	Telemetry Package version
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
	Use this operation to get telemetry information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				telemetry_info_obj=telemetry_info()
				response = telemetry_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify telemetry information..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				telemetry_info_obj=telemetry_info()
				return cls.update_bulk_request(client,resource,telemetry_info_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of telemetry_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			telemetry_info_obj = telemetry_info()
			option_ = options()
			option_._filter=filter_
			return telemetry_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the telemetry_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			telemetry_info_obj = telemetry_info()
			option_ = options()
			option_._count=True
			response = telemetry_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of telemetry_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			telemetry_info_obj = telemetry_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = telemetry_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(telemetry_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.telemetry_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(telemetry_info_responses, response, "telemetry_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.telemetry_info_response_array
				i=0
				error = [telemetry_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.telemetry_info_response_array
			i=0
			telemetry_info_objs = [telemetry_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_telemetry_info'):
					for props in obj._telemetry_info:
						result = service.payload_formatter.string_to_bulk_resource(telemetry_info_response,self.__class__.__name__,props)
						telemetry_info_objs[i] = result.telemetry_info
						i=i+1
			return telemetry_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(telemetry_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class telemetry_info_response(base_response):
	def __init__(self,length=1) :
		self.telemetry_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.telemetry_info= [ telemetry_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class telemetry_info_responses(base_response):
	def __init__(self,length=1) :
		self.telemetry_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.telemetry_info_response_array = [ telemetry_info() for _ in range(length)]
