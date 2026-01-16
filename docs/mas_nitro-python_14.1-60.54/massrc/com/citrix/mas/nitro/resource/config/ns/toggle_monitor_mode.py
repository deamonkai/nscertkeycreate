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
Configuration for toggle_monitor_mode resource
'''

class toggle_monitor_mode(base_resource):
	_enable_monitor_mode= ""
	_profile_name= ""
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
			return "toggle_monitor_mode"
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
			return "toggle_monitor_modes"
		except Exception as e :
			raise e


	'''
	Enable Monitor mode toggle
	'''
	@property
	def enable_monitor_mode(self):
		try:
			return self._enable_monitor_mode
		except Exception as e :
			raise e
	'''
	Enable Monitor mode toggle
	'''
	@enable_monitor_mode.setter
	def enable_monitor_mode(self,enable_monitor_mode):
		try :
			if not isinstance(enable_monitor_mode,bool):
				raise TypeError("enable_monitor_mode must be set to bool value")
			self._enable_monitor_mode = enable_monitor_mode
		except Exception as e :
			raise e

	'''
	appsec profile name
	'''
	@property
	def profile_name(self):
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	appsec profile name
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Use this operation to modify Appsec Config profile.
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
				toggle_monitor_mode_obj=toggle_monitor_mode()
				return cls.update_bulk_request(client,resource,toggle_monitor_mode_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(toggle_monitor_mode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.toggle_monitor_mode
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(toggle_monitor_mode_responses, response, "toggle_monitor_mode_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.toggle_monitor_mode_response_array
				i=0
				error = [toggle_monitor_mode() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.toggle_monitor_mode_response_array
			i=0
			toggle_monitor_mode_objs = [toggle_monitor_mode() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_toggle_monitor_mode'):
					for props in obj._toggle_monitor_mode:
						result = service.payload_formatter.string_to_bulk_resource(toggle_monitor_mode_response,self.__class__.__name__,props)
						toggle_monitor_mode_objs[i] = result.toggle_monitor_mode
						i=i+1
			return toggle_monitor_mode_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(toggle_monitor_mode,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class toggle_monitor_mode_response(base_response):
	def __init__(self,length=1) :
		self.toggle_monitor_mode= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.toggle_monitor_mode= [ toggle_monitor_mode() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class toggle_monitor_mode_responses(base_response):
	def __init__(self,length=1) :
		self.toggle_monitor_mode_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.toggle_monitor_mode_response_array = [ toggle_monitor_mode() for _ in range(length)]
