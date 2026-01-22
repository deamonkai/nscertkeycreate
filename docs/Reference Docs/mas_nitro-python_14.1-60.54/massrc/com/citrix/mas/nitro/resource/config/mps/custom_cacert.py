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
Configuration for Custom CACert resource
'''

class custom_cacert(base_resource):
	_file_name= ""
	_file_data= ""
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
			return "custom_cacert"
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
			return "custom_cacerts"
		except Exception as e :
			raise e


	'''
	CA Cert file name
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	CA Cert file name
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
	Base64 encoded CA Cert file contents
	'''
	@property
	def file_data(self):
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	Base64 encoded CA Cert file contents
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
	Use this operation to get custom cacert file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				custom_cacert_obj=custom_cacert()
				response = custom_cacert_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to upload custom cacert file.
	'''

	'''
	Use this operation to upload custom cacert file.
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
	Use this operation to delete custom cacert file.
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
					custom_cacert_obj=custom_cacert()
					return cls.delete_bulk_request(client,resource,custom_cacert_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of custom_cacert resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			custom_cacert_obj = custom_cacert()
			option_ = options()
			option_._filter=filter_
			return custom_cacert_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the custom_cacert resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			custom_cacert_obj = custom_cacert()
			option_ = options()
			option_._count=True
			response = custom_cacert_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of custom_cacert resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			custom_cacert_obj = custom_cacert()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = custom_cacert_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(custom_cacert_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.custom_cacert
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(custom_cacert_responses, response, "custom_cacert_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.custom_cacert_response_array
				i=0
				error = [custom_cacert() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.custom_cacert_response_array
			i=0
			custom_cacert_objs = [custom_cacert() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_custom_cacert'):
					for props in obj._custom_cacert:
						result = service.payload_formatter.string_to_bulk_resource(custom_cacert_response,self.__class__.__name__,props)
						custom_cacert_objs[i] = result.custom_cacert
						i=i+1
			return custom_cacert_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(custom_cacert,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class custom_cacert_response(base_response):
	def __init__(self,length=1) :
		self.custom_cacert= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.custom_cacert= [ custom_cacert() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class custom_cacert_responses(base_response):
	def __init__(self,length=1) :
		self.custom_cacert_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.custom_cacert_response_array = [ custom_cacert() for _ in range(length)]
