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
Configuration for API to convert analytics appflow config from policy to profile based resource
'''

class analytics_policy_to_profile(base_resource):
	_act_id= ""
	_devices=[]
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
			return "analytics_policy_to_profile"
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
			return "analytics_policy_to_profiles"
		except Exception as e :
			raise e


	'''
	Activity ID that is used by GUI to track the polling status.
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e
	'''
	Activity ID that is used by GUI to track the polling status.
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	List of Devices
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	List of Devices
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e

	'''
	Use this operation to modify the analytics appflow config from policy to profile based..
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
				analytics_policy_to_profile_obj=analytics_policy_to_profile()
				return cls.update_bulk_request(client,resource,analytics_policy_to_profile_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(analytics_policy_to_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.analytics_policy_to_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(analytics_policy_to_profile_responses, response, "analytics_policy_to_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.analytics_policy_to_profile_response_array
				i=0
				error = [analytics_policy_to_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.analytics_policy_to_profile_response_array
			i=0
			analytics_policy_to_profile_objs = [analytics_policy_to_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_analytics_policy_to_profile'):
					for props in obj._analytics_policy_to_profile:
						result = service.payload_formatter.string_to_bulk_resource(analytics_policy_to_profile_response,self.__class__.__name__,props)
						analytics_policy_to_profile_objs[i] = result.analytics_policy_to_profile
						i=i+1
			return analytics_policy_to_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(analytics_policy_to_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class analytics_policy_to_profile_response(base_response):
	def __init__(self,length=1) :
		self.analytics_policy_to_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.analytics_policy_to_profile= [ analytics_policy_to_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class analytics_policy_to_profile_responses(base_response):
	def __init__(self,length=1) :
		self.analytics_policy_to_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.analytics_policy_to_profile_response_array = [ analytics_policy_to_profile() for _ in range(length)]
