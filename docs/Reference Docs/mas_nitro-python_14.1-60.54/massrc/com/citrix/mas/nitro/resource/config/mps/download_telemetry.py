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
Configuration for Download Telemetry resource
'''

class download_telemetry(base_resource):
	_file_last_modified= ""
	_file_name= ""
	_file_size= ""
	_file_location_path= ""
	_id= ""
	_tenant_id= ""
	_act_id= ""
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
			return "download_telemetry"
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
			return "download_telemetrys"
		except Exception as e :
			raise e



	'''
	get Download date of the telemetry data
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get Compressed fie of the telemetry data
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e


	'''
	get File Size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get File Location on Client for upload/download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e


	'''
	get Id is system generated key for the record
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for the record
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
	get Tenant Id of the owner tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the owner tenant
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	Use this operation to get download bundle.
	'''

	'''
	Use this operation to get download bundle.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to authenticate cloud profile settings..
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
				download_telemetry_obj= download_telemetry()
				return cls.perform_operation_bulk_request(service,resource,download_telemetry_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get backup file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				download_telemetry_obj=download_telemetry()
				response = download_telemetry_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to get download bundle.
	'''
	@classmethod
	def generate(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				download_telemetry_obj=download_telemetry()
				response = download_telemetry_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to get download bundle.
	'''
	@classmethod
	def generate(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				download_telemetry_obj=download_telemetry()
				response = download_telemetry_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of download_telemetry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			download_telemetry_obj = download_telemetry()
			option_ = options()
			option_._filter=filter_
			return download_telemetry_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the download_telemetry resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			download_telemetry_obj = download_telemetry()
			option_ = options()
			option_._count=True
			response = download_telemetry_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of download_telemetry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			download_telemetry_obj = download_telemetry()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = download_telemetry_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(download_telemetry_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.download_telemetry
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(download_telemetry_responses, response, "download_telemetry_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.download_telemetry_response_array
				i=0
				error = [download_telemetry() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.download_telemetry_response_array
			i=0
			download_telemetry_objs = [download_telemetry() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_download_telemetry'):
					for props in obj._download_telemetry:
						result = service.payload_formatter.string_to_bulk_resource(download_telemetry_response,self.__class__.__name__,props)
						download_telemetry_objs[i] = result.download_telemetry
						i=i+1
			return download_telemetry_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(download_telemetry,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class download_telemetry_response(base_response):
	def __init__(self,length=1) :
		self.download_telemetry= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.download_telemetry= [ download_telemetry() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class download_telemetry_responses(base_response):
	def __init__(self,length=1) :
		self.download_telemetry_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.download_telemetry_response_array = [ download_telemetry() for _ in range(length)]
