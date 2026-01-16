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
Configuration for adc script output file resource
'''

class adc_script_output_file(base_resource):
	_format= ""
	_file_path= ""
	_contents= ""
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
			return "adc_script_output_file"
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
			return "adc_script_output_files"
		except Exception as e :
			raise e


	'''
	format
	'''
	@property
	def format(self):
		try:
			return self._format
		except Exception as e :
			raise e
	'''
	format
	'''
	@format.setter
	def format(self,format):
		try :
			if not isinstance(format,str):
				raise TypeError("format must be set to str value")
			self._format = format
		except Exception as e :
			raise e

	'''
	file_path
	'''
	@property
	def file_path(self):
		try:
			return self._file_path
		except Exception as e :
			raise e
	'''
	file_path
	'''
	@file_path.setter
	def file_path(self,file_path):
		try :
			if not isinstance(file_path,str):
				raise TypeError("file_path must be set to str value")
			self._file_path = file_path
		except Exception as e :
			raise e

	'''
	contents
	'''
	@property
	def contents(self):
		try:
			return self._contents
		except Exception as e :
			raise e
	'''
	contents
	'''
	@contents.setter
	def contents(self,contents):
		try :
			if not isinstance(contents,str):
				raise TypeError("contents must be set to str value")
			self._contents = contents
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_script_output_file_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_script_output_file
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_script_output_file_responses, response, "adc_script_output_file_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_script_output_file_response_array
				i=0
				error = [adc_script_output_file() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_script_output_file_response_array
			i=0
			adc_script_output_file_objs = [adc_script_output_file() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_script_output_file'):
					for props in obj._adc_script_output_file:
						result = service.payload_formatter.string_to_bulk_resource(adc_script_output_file_response,self.__class__.__name__,props)
						adc_script_output_file_objs[i] = result.adc_script_output_file
						i=i+1
			return adc_script_output_file_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_script_output_file,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_script_output_file_response(base_response):
	def __init__(self,length=1) :
		self.adc_script_output_file= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_script_output_file= [ adc_script_output_file() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_script_output_file_responses(base_response):
	def __init__(self,length=1) :
		self.adc_script_output_file_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_script_output_file_response_array = [ adc_script_output_file() for _ in range(length)]
