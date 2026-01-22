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
Configuration for Mapping Appsec profile config with Model settings resource
'''

class model_settings_info(base_resource):
	_id= ""
	_model_sensitivity= ""
	_parent_name= ""
	_parent_id= ""
	_model_id= ""
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
			return "model_settings_info"
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
			return "model_settings_infos"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for model settings
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for model settings
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
	get 0 for low, 1 for medium and 2 for strict. -1 if not enabled
	'''
	@property
	def model_sensitivity(self) :
		try:
			return self._model_sensitivity
		except Exception as e :
			raise e
	'''
	set 0 for low, 1 for medium and 2 for strict. -1 if not enabled
	'''
	@model_sensitivity.setter
	def model_sensitivity(self,model_sensitivity):
		try :
			if not isinstance(model_sensitivity,int):
				raise TypeError("model_sensitivity must be set to int value")
			self._model_sensitivity = model_sensitivity
		except Exception as e :
			raise e


	'''
	get Resource name of parent resource
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Resource name of parent resource
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Id of the parent resource
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id of the parent resource
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Appse Model Id maps to each appsec usecase like large upload volume, excessive client connections, etc.,
	'''
	@property
	def model_id(self) :
		try:
			return self._model_id
		except Exception as e :
			raise e
	'''
	set Appse Model Id maps to each appsec usecase like large upload volume, excessive client connections, etc.,
	'''
	@model_id.setter
	def model_id(self,model_id):
		try :
			if not isinstance(model_id,int):
				raise TypeError("model_id must be set to int value")
			self._model_id = model_id
		except Exception as e :
			raise e

	'''
	Use this operation to modify Model settings..
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
				model_settings_info_obj=model_settings_info()
				return cls.update_bulk_request(client,resource,model_settings_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to display Model settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				model_settings_info_obj=model_settings_info()
				response = model_settings_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of model_settings_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			model_settings_info_obj = model_settings_info()
			option_ = options()
			option_._filter=filter_
			return model_settings_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the model_settings_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			model_settings_info_obj = model_settings_info()
			option_ = options()
			option_._count=True
			response = model_settings_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of model_settings_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			model_settings_info_obj = model_settings_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = model_settings_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(model_settings_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.model_settings_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(model_settings_info_responses, response, "model_settings_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.model_settings_info_response_array
				i=0
				error = [model_settings_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.model_settings_info_response_array
			i=0
			model_settings_info_objs = [model_settings_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_model_settings_info'):
					for props in obj._model_settings_info:
						result = service.payload_formatter.string_to_bulk_resource(model_settings_info_response,self.__class__.__name__,props)
						model_settings_info_objs[i] = result.model_settings_info
						i=i+1
			return model_settings_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(model_settings_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class model_settings_info_response(base_response):
	def __init__(self,length=1) :
		self.model_settings_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.model_settings_info= [ model_settings_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class model_settings_info_responses(base_response):
	def __init__(self,length=1) :
		self.model_settings_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.model_settings_info_response_array = [ model_settings_info() for _ in range(length)]
