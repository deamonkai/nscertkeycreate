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
Configuration for ACME Access Parameters resource
'''

class acme_access_parameters(base_resource):
	_type= ""
	_input_option= ""
	_display_name= ""
	_notes= ""
	_value= ""
	_optional= ""
	_name= ""
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
			return "acme_access_parameters"
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
			return "acme_access_parameterss"
		except Exception as e :
			raise e



	'''
	get Type of the parameter like text, password, etc.
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of the parameter like text, password, etc.
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Some DNS providers provide alternate input options. By default 1 for all parameters but some has more than 1 input options. This is used to identify the input option for the parameter.
	'''
	@property
	def input_option(self) :
		try:
			return self._input_option
		except Exception as e :
			raise e
	'''
	set Some DNS providers provide alternate input options. By default 1 for all parameters but some has more than 1 input options. This is used to identify the input option for the parameter.
	'''
	@input_option.setter
	def input_option(self,input_option):
		try :
			if not isinstance(input_option,int):
				raise TypeError("input_option must be set to int value")
			self._input_option = input_option
		except Exception as e :
			raise e


	'''
	get Display name for the ACME parameter. This is the name that will be shown in the UI for the parameter.
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Display name for the ACME parameter. This is the name that will be shown in the UI for the parameter.
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
	get Notes for the ACME parameter. This can be used to provide additional information about the parameter.
	'''
	@property
	def notes(self) :
		try:
			return self._notes
		except Exception as e :
			raise e
	'''
	set Notes for the ACME parameter. This can be used to provide additional information about the parameter.
	'''
	@notes.setter
	def notes(self,notes):
		try :
			if not isinstance(notes,str):
				raise TypeError("notes must be set to str value")
			self._notes = notes
		except Exception as e :
			raise e


	'''
	get Value of the DNS provider parameter. This is the actual value that will be used by the DNS provider.
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set Value of the DNS provider parameter. This is the actual value that will be used by the DNS provider.
	'''
	@value.setter
	def value(self,value):
		try :
			if not isinstance(value,str):
				raise TypeError("value must be set to str value")
			self._value = value
		except Exception as e :
			raise e


	'''
	get Indicates if this parameter is optional or required for the configuration
	'''
	@property
	def optional(self) :
		try:
			return self._optional
		except Exception as e :
			raise e
	'''
	set Indicates if this parameter is optional or required for the configuration
	'''
	@optional.setter
	def optional(self,optional):
		try :
			if not isinstance(optional,bool):
				raise TypeError("optional must be set to bool value")
			self._optional = optional
		except Exception as e :
			raise e


	'''
	get Name of the ACME Parameter
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the ACME Parameter
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_access_parameters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_access_parameters
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_access_parameters_responses, response, "acme_access_parameters_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_access_parameters_response_array
				i=0
				error = [acme_access_parameters() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_access_parameters_response_array
			i=0
			acme_access_parameters_objs = [acme_access_parameters() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_access_parameters'):
					for props in obj._acme_access_parameters:
						result = service.payload_formatter.string_to_bulk_resource(acme_access_parameters_response,self.__class__.__name__,props)
						acme_access_parameters_objs[i] = result.acme_access_parameters
						i=i+1
			return acme_access_parameters_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_access_parameters,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_access_parameters_response(base_response):
	def __init__(self,length=1) :
		self.acme_access_parameters= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_access_parameters= [ acme_access_parameters() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_access_parameters_responses(base_response):
	def __init__(self,length=1) :
		self.acme_access_parameters_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_access_parameters_response_array = [ acme_access_parameters() for _ in range(length)]
