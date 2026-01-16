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
Configuration for AF APP Report table resource
'''

class af_generic_api(base_resource):
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_generic_api"
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
			return "af_generic_apis"
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_generic_api_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_generic_api
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_generic_api_responses, response, "af_generic_api_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_generic_api_response_array
				i=0
				error = [af_generic_api() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_generic_api_response_array
			i=0
			af_generic_api_objs = [af_generic_api() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_generic_api:
					result = service.payload_formatter.string_to_bulk_resource(af_generic_api_response,self.__class__.__name__,props)
					af_generic_api_objs[i] = result.af_generic_api
					i=i+1
			return af_generic_api_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_generic_api,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_generic_api_response(base_response):
	def __init__(self,length=1) :
		self.af_generic_api= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_generic_api= [ af_generic_api() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_generic_api_responses(base_response):
	def __init__(self,length=1) :
		self.af_generic_api_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_generic_api_response_array = [ af_generic_api() for _ in range(length)]
