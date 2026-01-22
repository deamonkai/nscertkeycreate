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
Configuration for Used to configure SSL zero touch param on NetScaler resource
'''

class ns_ssl_zerotouch_param(base_resource):
	_managed_device_id= ""
	_passphrase= ""
	_public_key= ""
	_id= ""
	_ip_address= ""
	_file_data= ""
	_ns_id_arr=[]
	_activity_id= ""
	_isCACertificatePresent= ""
	_ns_ip_address_arr=[]
	_file_name= ""
	_eligible_devices=[]
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
			return "ns_ssl_zerotouch_param"
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
			return "ns_ssl_zerotouch_params"
		except Exception as e :
			raise e



	'''
	get Id of the device where SSL zero touch param is enabled
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e
	'''
	set Id of the device where SSL zero touch param is enabled
	'''
	@managed_device_id.setter
	def managed_device_id(self,managed_device_id):
		try :
			if not isinstance(managed_device_id,str):
				raise TypeError("managed_device_id must be set to str value")
			self._managed_device_id = managed_device_id
		except Exception as e :
			raise e


	'''
	get Passphrase used to configure SSL zero touch param on NetScaler
	'''
	@property
	def passphrase(self) :
		try:
			return self._passphrase
		except Exception as e :
			raise e
	'''
	set Passphrase used to configure SSL zero touch param on NetScaler
	'''
	@passphrase.setter
	def passphrase(self,passphrase):
		try :
			if not isinstance(passphrase,str):
				raise TypeError("passphrase must be set to str value")
			self._passphrase = passphrase
		except Exception as e :
			raise e


	'''
	get Public key generated on the device where SSL zero touch param is configured
	'''
	@property
	def public_key(self) :
		try:
			return self._public_key
		except Exception as e :
			raise e
	'''
	set Public key generated on the device where SSL zero touch param is configured
	'''
	@public_key.setter
	def public_key(self,public_key):
		try :
			if not isinstance(public_key,str):
				raise TypeError("public_key must be set to str value")
			self._public_key = public_key
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get IP Address of the device where SSL zero touch param is enabled
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address of the device where SSL zero touch param is enabled
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
	Base64 encoded CA cert file content
	'''
	@property
	def file_data(self):
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	Base64 encoded CA cert file content
	'''
	@file_data.setter
	def file_data(self,file_data):
		try :
			if not isinstance(file_data,str):
				raise TypeError("file_data must be set to str value")
			self._file_data = file_data
		except Exception as e :
			raise e

	'''
	List of NetScaler IDs where SSL zero touch param is to be configured
	'''
	@property
	def ns_id_arr(self) :
		try:
			return self._ns_id_arr
		except Exception as e :
			raise e
	'''
	List of NetScaler IDs where SSL zero touch param is to be configured
	'''
	@ns_id_arr.setter
	def ns_id_arr(self,ns_id_arr) :
		try :
			if not isinstance(ns_id_arr,list):
				raise TypeError("ns_id_arr must be set to array of str value")
			for item in ns_id_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_id_arr = ns_id_arr
		except Exception as e :
			raise e

	'''
	Activity ID that is used by GUI to track the status of configuring SSL zero touch param on NetScaler.
	'''
	@property
	def activity_id(self):
		try:
			return self._activity_id
		except Exception as e :
			raise e

	'''
	Set to true, if the Console CA certificate is already present
	'''
	@property
	def isCACertificatePresent(self):
		try:
			return self._isCACertificatePresent
		except Exception as e :
			raise e
	'''
	Set to true, if the Console CA certificate is already present
	'''
	@isCACertificatePresent.setter
	def isCACertificatePresent(self,isCACertificatePresent):
		try :
			if not isinstance(isCACertificatePresent,bool):
				raise TypeError("isCACertificatePresent must be set to bool value")
			self._isCACertificatePresent = isCACertificatePresent
		except Exception as e :
			raise e

	'''
	List of NetScaler IP Address where SSL zero touch param is to be configured
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	List of NetScaler IP Address where SSL zero touch param is to be configured
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e

	'''
	CA file name.
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	CA file name.
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
	List of NetScaler IDs eligible for SSL zero touch param configuration
	'''
	@property
	def eligible_devices(self) :
		try:
			return self._eligible_devices
		except Exception as e :
			raise e
	'''
	List of NetScaler IDs eligible for SSL zero touch param configuration
	'''
	@eligible_devices.setter
	def eligible_devices(self,eligible_devices) :
		try :
			if not isinstance(eligible_devices,list):
				raise TypeError("eligible_devices must be set to array of str value")
			for item in eligible_devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._eligible_devices = eligible_devices
		except Exception as e :
			raise e

	'''
	Use this operation to configure SSL zero touch param on NetScaler.
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
				ns_ssl_zerotouch_param_obj= ns_ssl_zerotouch_param()
				return cls.perform_operation_bulk_request(service,resource,ns_ssl_zerotouch_param_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get list of NetScaler where SSL zero touch param is configured.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_ssl_zerotouch_param_obj=ns_ssl_zerotouch_param()
				response = ns_ssl_zerotouch_param_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_zerotouch_param resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_zerotouch_param_obj = ns_ssl_zerotouch_param()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_zerotouch_param_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_zerotouch_param resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_zerotouch_param_obj = ns_ssl_zerotouch_param()
			option_ = options()
			option_._count=True
			response = ns_ssl_zerotouch_param_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_zerotouch_param resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_zerotouch_param_obj = ns_ssl_zerotouch_param()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_zerotouch_param_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_zerotouch_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_zerotouch_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_zerotouch_param_responses, response, "ns_ssl_zerotouch_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_zerotouch_param_response_array
				i=0
				error = [ns_ssl_zerotouch_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_zerotouch_param_response_array
			i=0
			ns_ssl_zerotouch_param_objs = [ns_ssl_zerotouch_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_zerotouch_param'):
					for props in obj._ns_ssl_zerotouch_param:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_zerotouch_param_response,self.__class__.__name__,props)
						ns_ssl_zerotouch_param_objs[i] = result.ns_ssl_zerotouch_param
						i=i+1
			return ns_ssl_zerotouch_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_zerotouch_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_zerotouch_param_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_zerotouch_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_zerotouch_param= [ ns_ssl_zerotouch_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_zerotouch_param_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_zerotouch_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_zerotouch_param_response_array = [ ns_ssl_zerotouch_param() for _ in range(length)]
