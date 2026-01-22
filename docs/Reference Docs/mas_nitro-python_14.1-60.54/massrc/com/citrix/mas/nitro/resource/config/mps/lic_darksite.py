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
Configuration for generate offline license request package resource
'''

class lic_darksite(base_resource):
	_package_name= ""
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
			return "lic_darksite"
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
			return "lic_darksites"
		except Exception as e :
			raise e


	'''
	generated package full path
	'''
	@property
	def package_name(self):
		try:
			return self._package_name
		except Exception as e :
			raise e
	'''
	generated package full path
	'''
	@package_name.setter
	def package_name(self,package_name):
		try :
			if not isinstance(package_name,str):
				raise TypeError("package_name must be set to str value")
			self._package_name = package_name
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(lic_darksite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lic_darksite
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(lic_darksite_responses, response, "lic_darksite_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.lic_darksite_response_array
				i=0
				error = [lic_darksite() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.lic_darksite_response_array
			i=0
			lic_darksite_objs = [lic_darksite() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_lic_darksite'):
					for props in obj._lic_darksite:
						result = service.payload_formatter.string_to_bulk_resource(lic_darksite_response,self.__class__.__name__,props)
						lic_darksite_objs[i] = result.lic_darksite
						i=i+1
			return lic_darksite_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(lic_darksite,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class lic_darksite_response(base_response):
	def __init__(self,length=1) :
		self.lic_darksite= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.lic_darksite= [ lic_darksite() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class lic_darksite_responses(base_response):
	def __init__(self,length=1) :
		self.lic_darksite_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.lic_darksite_response_array = [ lic_darksite() for _ in range(length)]
