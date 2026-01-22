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
Configuration for Techsupport for device resource
'''

class device_techsupport(base_resource):
	_id= ""
	_ip_address= ""
	_techsupport_filesize= ""
	_techsupport_filename= ""
	_last_updated_time= ""
	_device_name= ""
	_proxy_server= ""
	_case_or_service_request_number= ""
	_techsupport_password= ""
	_encrypted= ""
	_citrix_username= ""
	_ts_scope= ""
	_ns_auth_token= ""
	_citrix_password= ""
	_ts_partition_name= ""
	_is_upload_file= ""
	_file_name= ""
	_ts_description= ""
	_ts_time= ""
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
			return "device_techsupport"
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
			return "device_techsupports"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for techSupport bundle files
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for techSupport bundle files
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
	get Device IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
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
	get Techsupport file size
	'''
	@property
	def techsupport_filesize(self) :
		try:
			return self._techsupport_filesize
		except Exception as e :
			raise e
	'''
	set Techsupport file size
	'''
	@techsupport_filesize.setter
	def techsupport_filesize(self,techsupport_filesize):
		try :
			if not isinstance(techsupport_filesize,long):
				raise TypeError("techsupport_filesize must be set to long value")
			self._techsupport_filesize = techsupport_filesize
		except Exception as e :
			raise e


	'''
	get Name of the techsupport file
	'''
	@property
	def techsupport_filename(self) :
		try:
			return self._techsupport_filename
		except Exception as e :
			raise e


	'''
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
		except Exception as e :
			raise e
	'''
	set Last Updated Time
	'''
	@last_updated_time.setter
	def last_updated_time(self,last_updated_time):
		try :
			if not isinstance(last_updated_time,long):
				raise TypeError("last_updated_time must be set to long value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get Device Hostname
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
		except Exception as e :
			raise e

	'''
	Proxy server ip
	'''
	@property
	def proxy_server(self):
		try:
			return self._proxy_server
		except Exception as e :
			raise e
	'''
	Proxy server ip
	'''
	@proxy_server.setter
	def proxy_server(self,proxy_server):
		try :
			if not isinstance(proxy_server,str):
				raise TypeError("proxy_server must be set to str value")
			self._proxy_server = proxy_server
		except Exception as e :
			raise e

	'''
	case or serrvice request number
	'''
	@property
	def case_or_service_request_number(self):
		try:
			return self._case_or_service_request_number
		except Exception as e :
			raise e
	'''
	case or serrvice request number
	'''
	@case_or_service_request_number.setter
	def case_or_service_request_number(self,case_or_service_request_number):
		try :
			if not isinstance(case_or_service_request_number,str):
				raise TypeError("case_or_service_request_number must be set to str value")
			self._case_or_service_request_number = case_or_service_request_number
		except Exception as e :
			raise e

	'''
	Techsupport Password
	'''
	@property
	def techsupport_password(self):
		try:
			return self._techsupport_password
		except Exception as e :
			raise e
	'''
	Techsupport Password
	'''
	@techsupport_password.setter
	def techsupport_password(self,techsupport_password):
		try :
			if not isinstance(techsupport_password,str):
				raise TypeError("techsupport_password must be set to str value")
			self._techsupport_password = techsupport_password
		except Exception as e :
			raise e

	'''
	Indicates if the techsupport file is encrypted.
	'''
	@property
	def encrypted(self):
		try:
			return self._encrypted
		except Exception as e :
			raise e
	'''
	Indicates if the techsupport file is encrypted.
	'''
	@encrypted.setter
	def encrypted(self,encrypted):
		try :
			if not isinstance(encrypted,bool):
				raise TypeError("encrypted must be set to bool value")
			self._encrypted = encrypted
		except Exception as e :
			raise e

	'''
	Citrix username
	'''
	@property
	def citrix_username(self):
		try:
			return self._citrix_username
		except Exception as e :
			raise e
	'''
	Citrix username
	'''
	@citrix_username.setter
	def citrix_username(self,citrix_username):
		try :
			if not isinstance(citrix_username,str):
				raise TypeError("citrix_username must be set to str value")
			self._citrix_username = citrix_username
		except Exception as e :
			raise e

	'''
	Scope can be cluster or node or partition
	'''
	@property
	def ts_scope(self):
		try:
			return self._ts_scope
		except Exception as e :
			raise e
	'''
	Scope can be cluster or node or partition
	'''
	@ts_scope.setter
	def ts_scope(self,ts_scope):
		try :
			if not isinstance(ts_scope,str):
				raise TypeError("ts_scope must be set to str value")
			self._ts_scope = ts_scope
		except Exception as e :
			raise e

	'''
	Authorisation token required for uploading the file from NS
	'''
	@property
	def ns_auth_token(self):
		try:
			return self._ns_auth_token
		except Exception as e :
			raise e
	'''
	Authorisation token required for uploading the file from NS
	'''
	@ns_auth_token.setter
	def ns_auth_token(self,ns_auth_token):
		try :
			if not isinstance(ns_auth_token,str):
				raise TypeError("ns_auth_token must be set to str value")
			self._ns_auth_token = ns_auth_token
		except Exception as e :
			raise e

	'''
	Citrix password
	'''
	@property
	def citrix_password(self):
		try:
			return self._citrix_password
		except Exception as e :
			raise e
	'''
	Citrix password
	'''
	@citrix_password.setter
	def citrix_password(self,citrix_password):
		try :
			if not isinstance(citrix_password,str):
				raise TypeError("citrix_password must be set to str value")
			self._citrix_password = citrix_password
		except Exception as e :
			raise e

	'''
	Name of the partition
	'''
	@property
	def ts_partition_name(self):
		try:
			return self._ts_partition_name
		except Exception as e :
			raise e
	'''
	Name of the partition
	'''
	@ts_partition_name.setter
	def ts_partition_name(self,ts_partition_name):
		try :
			if not isinstance(ts_partition_name,str):
				raise TypeError("ts_partition_name must be set to str value")
			self._ts_partition_name = ts_partition_name
		except Exception as e :
			raise e

	'''
	To upload the collector archive
	'''
	@property
	def is_upload_file(self):
		try:
			return self._is_upload_file
		except Exception as e :
			raise e
	'''
	To upload the collector archive
	'''
	@is_upload_file.setter
	def is_upload_file(self,is_upload_file):
		try :
			if not isinstance(is_upload_file,bool):
				raise TypeError("is_upload_file must be set to bool value")
			self._is_upload_file = is_upload_file
		except Exception as e :
			raise e

	'''
	file name
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	file name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	Description for the file
	'''
	@property
	def ts_description(self):
		try:
			return self._ts_description
		except Exception as e :
			raise e
	'''
	Description for the file
	'''
	@ts_description.setter
	def ts_description(self,ts_description):
		try :
			if not isinstance(ts_description,str):
				raise TypeError("ts_description must be set to str value")
			self._ts_description = ts_description
		except Exception as e :
			raise e

	'''
	Time from which techSupport file will be generated
	'''
	@property
	def ts_time(self):
		try:
			return self._ts_time
		except Exception as e :
			raise e
	'''
	Time from which techSupport file will be generated
	'''
	@ts_time.setter
	def ts_time(self,ts_time):
		try :
			if not isinstance(ts_time,str):
				raise TypeError("ts_time must be set to str value")
			self._ts_time = ts_time
		except Exception as e :
			raise e

	'''
	Use this operation to delete tech support bundles.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					device_techsupport_obj=device_techsupport()
					return cls.delete_bulk_request(client,resource,device_techsupport_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download techsupport file.
	'''

	'''
	Use this operation to download techsupport file.
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
	Use this operation to poll tech support bundle from a device and updated the database.
	'''

	'''
	Use this operation to poll tech support bundle from a device and updated the database.
	'''
	@classmethod
	def devicetechsupport(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"devicetechsupport")
			else : 
				device_techsupport_obj= device_techsupport()
				return cls.perform_operation_bulk_request(service,"devicetechsupport", resource,device_techsupport_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload techsupport file.
	'''

	'''
	Use this operation to upload techsupport file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Get tech support bundles of devices.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				device_techsupport_obj=device_techsupport()
				response = device_techsupport_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_techsupport resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_techsupport_obj = device_techsupport()
			option_ = options()
			option_._filter=filter_
			return device_techsupport_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_techsupport resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_techsupport_obj = device_techsupport()
			option_ = options()
			option_._count=True
			response = device_techsupport_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_techsupport resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_techsupport_obj = device_techsupport()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_techsupport_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_techsupport_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_techsupport
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_techsupport_responses, response, "device_techsupport_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_techsupport_response_array
				i=0
				error = [device_techsupport() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_techsupport_response_array
			i=0
			device_techsupport_objs = [device_techsupport() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_techsupport'):
					for props in obj._device_techsupport:
						result = service.payload_formatter.string_to_bulk_resource(device_techsupport_response,self.__class__.__name__,props)
						device_techsupport_objs[i] = result.device_techsupport
						i=i+1
			return device_techsupport_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_techsupport,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_techsupport_response(base_response):
	def __init__(self,length=1) :
		self.device_techsupport= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_techsupport= [ device_techsupport() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_techsupport_responses(base_response):
	def __init__(self,length=1) :
		self.device_techsupport_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_techsupport_response_array = [ device_techsupport() for _ in range(length)]
