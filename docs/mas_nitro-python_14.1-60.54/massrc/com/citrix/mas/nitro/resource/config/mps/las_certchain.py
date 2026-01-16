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
Configuration for las_certchain resource
'''

class las_certchain(base_resource):
	_previous=[]
	_current=[]
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
			return "las_certchain"
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
			return "las_certchains"
		except Exception as e :
			raise e



	'''
	get List of previous las certchain
	'''
	@property
	def previous(self) :
		try:
			return self._previous
		except Exception as e :
			raise e
	'''
	set List of previous las certchain
	'''
	@previous.setter
	def previous(self,previous) :
		try :
			if not isinstance(previous,list):
				raise TypeError("previous must be set to array of str value")
			for item in previous :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._previous = previous
		except Exception as e :
			raise e


	'''
	get List of current las certchain
	'''
	@property
	def current(self) :
		try:
			return self._current
		except Exception as e :
			raise e
	'''
	set List of current las certchain
	'''
	@current.setter
	def current(self,current) :
		try :
			if not isinstance(current,list):
				raise TypeError("current must be set to array of str value")
			for item in current :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._current = current
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_certchain_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_certchain
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_certchain_responses, response, "las_certchain_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_certchain_response_array
				i=0
				error = [las_certchain() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_certchain_response_array
			i=0
			las_certchain_objs = [las_certchain() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_certchain'):
					for props in obj._las_certchain:
						result = service.payload_formatter.string_to_bulk_resource(las_certchain_response,self.__class__.__name__,props)
						las_certchain_objs[i] = result.las_certchain
						i=i+1
			return las_certchain_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_certchain,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_certchain_response(base_response):
	def __init__(self,length=1) :
		self.las_certchain= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_certchain= [ las_certchain() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_certchain_responses(base_response):
	def __init__(self,length=1) :
		self.las_certchain_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_certchain_response_array = [ las_certchain() for _ in range(length)]
