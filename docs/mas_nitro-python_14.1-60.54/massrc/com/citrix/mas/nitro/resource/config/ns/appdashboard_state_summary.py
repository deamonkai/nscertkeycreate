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
Configuration for Provides the app state filter summary resource
'''

class appdashboard_state_summary(base_resource):
	_filter_count= ""
	_filter_key= ""
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
			return "appdashboard_state_summary"
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
			return "appdashboard_state_summarys"
		except Exception as e :
			raise e


	'''
	Number of applications with current filter value
	'''
	@property
	def filter_count(self):
		try:
			return self._filter_count
		except Exception as e :
			raise e
	'''
	Number of applications with current filter value
	'''
	@filter_count.setter
	def filter_count(self,filter_count):
		try :
			if not isinstance(filter_count,long):
				raise TypeError("filter_count must be set to long value")
			self._filter_count = filter_count
		except Exception as e :
			raise e

	'''
	Filter key
	'''
	@property
	def filter_key(self):
		try:
			return self._filter_key
		except Exception as e :
			raise e
	'''
	Filter key
	'''
	@filter_key.setter
	def filter_key(self,filter_key):
		try :
			if not isinstance(filter_key,str):
				raise TypeError("filter_key must be set to str value")
			self._filter_key = filter_key
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appdashboard_state_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appdashboard_state_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appdashboard_state_summary_responses, response, "appdashboard_state_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.appdashboard_state_summary_response_array
				i=0
				error = [appdashboard_state_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.appdashboard_state_summary_response_array
			i=0
			appdashboard_state_summary_objs = [appdashboard_state_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_appdashboard_state_summary'):
					for props in obj._appdashboard_state_summary:
						result = service.payload_formatter.string_to_bulk_resource(appdashboard_state_summary_response,self.__class__.__name__,props)
						appdashboard_state_summary_objs[i] = result.appdashboard_state_summary
						i=i+1
			return appdashboard_state_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(appdashboard_state_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class appdashboard_state_summary_response(base_response):
	def __init__(self,length=1) :
		self.appdashboard_state_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.appdashboard_state_summary= [ appdashboard_state_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class appdashboard_state_summary_responses(base_response):
	def __init__(self,length=1) :
		self.appdashboard_state_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.appdashboard_state_summary_response_array = [ appdashboard_state_summary() for _ in range(length)]
