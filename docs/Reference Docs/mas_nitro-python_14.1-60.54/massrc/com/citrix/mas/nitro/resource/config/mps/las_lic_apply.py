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
Configuration for get-post las license apply resource
'''

class las_lic_apply(base_resource):
	_las_token_file_name= ""
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
			return "las_lic_apply"
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
			return "las_lic_applys"
		except Exception as e :
			raise e


	'''
	LAS token file name
	'''
	@property
	def las_token_file_name(self):
		try:
			return self._las_token_file_name
		except Exception as e :
			raise e
	'''
	LAS token file name
	'''
	@las_token_file_name.setter
	def las_token_file_name(self,las_token_file_name):
		try :
			if not isinstance(las_token_file_name,str):
				raise TypeError("las_token_file_name must be set to str value")
			self._las_token_file_name = las_token_file_name
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_apply_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_lic_apply
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_apply_responses, response, "las_lic_apply_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_lic_apply_response_array
				i=0
				error = [las_lic_apply() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_lic_apply_response_array
			i=0
			las_lic_apply_objs = [las_lic_apply() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_lic_apply'):
					for props in obj._las_lic_apply:
						result = service.payload_formatter.string_to_bulk_resource(las_lic_apply_response,self.__class__.__name__,props)
						las_lic_apply_objs[i] = result.las_lic_apply
						i=i+1
			return las_lic_apply_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_lic_apply,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_lic_apply_response(base_response):
	def __init__(self,length=1) :
		self.las_lic_apply= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_lic_apply= [ las_lic_apply() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_lic_apply_responses(base_response):
	def __init__(self,length=1) :
		self.las_lic_apply_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_lic_apply_response_array = [ las_lic_apply() for _ in range(length)]
