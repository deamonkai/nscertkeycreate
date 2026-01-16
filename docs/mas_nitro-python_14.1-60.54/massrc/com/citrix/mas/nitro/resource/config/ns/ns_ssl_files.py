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
Configuration for NetScaler SSL Files resource
'''

class ns_ssl_files(base_resource):
	_ns_ip_address= ""
	_file_size= ""
	_display_name= ""
	_id= ""
	_file_location_path= ""
	_file_last_modified= ""
	_file_name= ""
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
			return "ns_ssl_files"
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
			return self._file_location_path
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "ns_ssl_filess"
		except Exception as e :
			raise e



	'''
	get device ip on on which ssl file is present
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set device ip on on which ssl file is present
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get file_size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get display name of device on which ssl file is present
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set display name of device on which ssl file is present
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the ns ssl files
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the ns ssl files
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
	get File Location of ssl file on ADC
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location of ssl file on ADC
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
	get Last Modified
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
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
	Activity ID that is used by GUI to track the polling status.
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e
	'''
	Activity ID that is used by GUI to track the polling status.
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	Use this operation to download ns ssl files.
	'''

	'''
	Use this operation to download ns ssl files.
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
	Use this operation to delete ns ssl files.
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
					ns_ssl_files_obj=ns_ssl_files()
					return cls.delete_bulk_request(client,resource,ns_ssl_files_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get ns ssl files.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_ssl_files_obj=ns_ssl_files()
				response = ns_ssl_files_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to poll all SSL certificates from all NetScaler and update the database.
	'''
	@classmethod
	def do_poll(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"do_poll")
				return res
			else : 
				ns_ssl_files_obj= ns_ssl_files()
				return cls.perform_operation_bulk_request(service,"do_poll",resource,ns_ssl_files_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_files resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_files_obj = ns_ssl_files()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_files_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_files resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_files_obj = ns_ssl_files()
			option_ = options()
			option_._count=True
			response = ns_ssl_files_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_files resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_files_obj = ns_ssl_files()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_files_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_files_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_files
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_files_responses, response, "ns_ssl_files_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_files_response_array
				i=0
				error = [ns_ssl_files() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_files_response_array
			i=0
			ns_ssl_files_objs = [ns_ssl_files() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_files'):
					for props in obj._ns_ssl_files:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_files_response,self.__class__.__name__,props)
						ns_ssl_files_objs[i] = result.ns_ssl_files
						i=i+1
			return ns_ssl_files_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_files,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_files_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_files= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_files= [ ns_ssl_files() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_files_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_files_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_files_response_array = [ ns_ssl_files() for _ in range(length)]
