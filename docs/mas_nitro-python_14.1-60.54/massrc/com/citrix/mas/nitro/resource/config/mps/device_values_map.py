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
Configuration for Map of Device and value to be used for it resource
'''

class device_values_map(base_resource):
	_parent_id= ""
	_parent_name= ""
	_device= ""
	_value= ""
	_valuex= ""
	_device_group= ""
	_id= ""
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
			return "device_values_map"
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
			return "device_values_maps"
		except Exception as e :
			raise e



	'''
	get Parent ID
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e


	'''
	get Parent Name
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e


	'''
	get IP Address for this device
	'''
	@property
	def device(self) :
		try:
			return self._device
		except Exception as e :
			raise e
	'''
	set IP Address for this device
	'''
	@device.setter
	def device(self,device):
		try :
			if not isinstance(device,str):
				raise TypeError("device must be set to str value")
			self._device = device
		except Exception as e :
			raise e


	'''
	get Value of the Variable to be used for device ip/group
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set Value of the Variable to be used for device ip/group
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
	get Secure Value of the Variable to be used for device ip/group
	'''
	@property
	def valuex(self) :
		try:
			return self._valuex
		except Exception as e :
			raise e
	'''
	set Secure Value of the Variable to be used for device ip/group
	'''
	@valuex.setter
	def valuex(self,valuex):
		try :
			if not isinstance(valuex,str):
				raise TypeError("valuex must be set to str value")
			self._valuex = valuex
		except Exception as e :
			raise e


	'''
	get Device Group for which value is to be defined
	'''
	@property
	def device_group(self) :
		try:
			return self._device_group
		except Exception as e :
			raise e
	'''
	set Device Group for which value is to be defined
	'''
	@device_group.setter
	def device_group(self,device_group):
		try :
			if not isinstance(device_group,str):
				raise TypeError("device_group must be set to str value")
			self._device_group = device_group
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the device value mapping
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the device value mapping
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_values_map_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_values_map
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_values_map_responses, response, "device_values_map_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_values_map_response_array
				i=0
				error = [device_values_map() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_values_map_response_array
			i=0
			device_values_map_objs = [device_values_map() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_values_map'):
					for props in obj._device_values_map:
						result = service.payload_formatter.string_to_bulk_resource(device_values_map_response,self.__class__.__name__,props)
						device_values_map_objs[i] = result.device_values_map
						i=i+1
			return device_values_map_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_values_map,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_values_map_response(base_response):
	def __init__(self,length=1) :
		self.device_values_map= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_values_map= [ device_values_map() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_values_map_responses(base_response):
	def __init__(self,length=1) :
		self.device_values_map_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_values_map_response_array = [ device_values_map() for _ in range(length)]
