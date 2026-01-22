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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for StyleBooks Configuration resource
'''

class stylebooks(base_resource):
	_source= ""
	_name= ""
	_display_name= ""
	_version= ""
	_namespace= ""
	__count=""

	'''
	get the api_basepath url
	'''
	def get_api_basepath(self) :
		try:
			return "/stylebook/"
		except Exception as e :
			raise e


	'''
	get the namespace_url
	Multilevel object types and object ids are defined as 
	object_types = [<parent level object type>,<child level object type>]
	object_ids = [<parent object id>,<child object id>]
	An object id is list of current object attributes say ["namespace","version"] then it is
	object_ids = [<parent object id>,<child object id>]
	coverted as object str <namespace value>/<version value>
	'''
	def get_namespace_url(self) :
		try:
			namespace_url = ""
			object_types_list = ["stylebooks"]
			object_ids_list = [[self.namespace,self.version,self.name]]
			if not( len(object_types_list) == len(object_ids_list)):
				raise  Exception('Invalid Json definition ,mismatched namespace depth and  object ids '+self.__class__.__name__)
			namespace_depth = len(object_types_list)
			depth_count = 0
			for object_type,object_id  in zip(object_types_list,object_ids_list):
				depth_count = depth_count+1
				object_id_str=""
				if all(object_id):
					object_id_str = "/"+"/".join(str(x) for x in object_id)
					namespace_url = namespace_url + "/" + object_type + object_id_str
				elif depth_count == namespace_depth:
					namespace_url = namespace_url+"/"+object_type
				else:
					raise  Exception('Parent object id is missing '+self.__class__.__name__)
			return namespace_url
		except Exception as e :
			raise e
		except Exception as e :
			raise e

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
			return "stylebooks"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "stylebookss"
		except Exception as e :
			raise e



	'''
	get Source definition of the StyleBook
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source definition of the StyleBook
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e


	'''
	get Name of the StyleBook
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the StyleBook
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
	get Display name of the StyleBook
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Display name of the StyleBook
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
	get Version of the StyleBook
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Version of the StyleBook
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Namespace of the StyleBook
	'''
	@property
	def namespace(self) :
		try:
			return self._namespace
		except Exception as e :
			raise e
	'''
	set Namespace of the StyleBook
	'''
	@namespace.setter
	def namespace(self,namespace):
		try :
			if not isinstance(namespace,str):
				raise TypeError("namespace must be set to str value")
			self._namespace = namespace
		except Exception as e :
			raise e

	'''
	Use this operation to import a StyleBook.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "stylebook"
			cls._url_filter = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["source"]
			cls._response_params = ["namespace","version","name"]
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				stylebooks_obj= stylebooks()
				return cls.perform_operation_bulk_request(service,resource,stylebooks_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get stylebook  details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "stylebook"
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				stylebooks_obj=stylebooks()
				response = stylebooks_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to remove StyleBook.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "stylebook"
			cls._url_filter = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._response_params = ["namespace","version","name"]
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					stylebooks_obj=stylebooks()
					return cls.delete_bulk_request(client,resource,stylebooks_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of stylebooks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._response_params = ["namespace","version","name"]
			stylebooks_obj = stylebooks()
			option_ = options()
			option_._filter=filter_
			return stylebooks_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the stylebooks resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._response_params = ["namespace","version","name"]
			stylebooks_obj = stylebooks()
			option_ = options()
			option_._count=True
			response = stylebooks_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of stylebooks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._response_params = ["namespace","version","name"]
			stylebooks_obj = stylebooks()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = stylebooks_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(stylebooks_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.stylebooks
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(stylebooks_responses, response, "stylebooks_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.stylebooks_response_array
				i=0
				error = [stylebooks() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.stylebooks_response_array
			i=0
			stylebooks_objs = [stylebooks() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_stylebooks'):
					for props in obj._stylebooks:
						result = service.payload_formatter.string_to_bulk_resource(stylebooks_response,self.__class__.__name__,props)
						stylebooks_objs[i] = result.stylebooks
						i=i+1
			return stylebooks_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(stylebooks,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class stylebooks_response(base_response):
	def __init__(self,length=1) :
		self.stylebooks= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.stylebooks= [ stylebooks() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class stylebooks_responses(base_response):
	def __init__(self,length=1) :
		self.stylebooks_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.stylebooks_response_array = [ stylebooks() for _ in range(length)]
