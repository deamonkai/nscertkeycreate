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
Configuration for NetScaler Console MSP type tenant resource
'''

class msp_tenant(base_resource):
	_id= ""
	_enable_msp_mode= ""
	_properties= ""
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
			return "msp_tenant"
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
			return "msp_tenants"
		except Exception as e :
			raise e



	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Signifies if a tenant is running in MSP mode 
	'''
	@property
	def enable_msp_mode(self) :
		try:
			return self._enable_msp_mode
		except Exception as e :
			raise e
	'''
	set Signifies if a tenant is running in MSP mode 
	'''
	@enable_msp_mode.setter
	def enable_msp_mode(self,enable_msp_mode):
		try :
			if not isinstance(enable_msp_mode,bool):
				raise TypeError("enable_msp_mode must be set to bool value")
			self._enable_msp_mode = enable_msp_mode
		except Exception as e :
			raise e


	'''
	get Misc content goes here
	'''
	@property
	def properties(self) :
		try:
			return self._properties
		except Exception as e :
			raise e
	'''
	set Misc content goes here
	'''
	@properties.setter
	def properties(self,properties):
		try :
			if not isinstance(properties,str):
				raise TypeError("properties must be set to str value")
			self._properties = properties
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(msp_tenant_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.msp_tenant
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(msp_tenant_responses, response, "msp_tenant_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.msp_tenant_response_array
				i=0
				error = [msp_tenant() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.msp_tenant_response_array
			i=0
			msp_tenant_objs = [msp_tenant() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_msp_tenant'):
					for props in obj._msp_tenant:
						result = service.payload_formatter.string_to_bulk_resource(msp_tenant_response,self.__class__.__name__,props)
						msp_tenant_objs[i] = result.msp_tenant
						i=i+1
			return msp_tenant_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(msp_tenant,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class msp_tenant_response(base_response):
	def __init__(self,length=1) :
		self.msp_tenant= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.msp_tenant= [ msp_tenant() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class msp_tenant_responses(base_response):
	def __init__(self,length=1) :
		self.msp_tenant_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.msp_tenant_response_array = [ msp_tenant() for _ in range(length)]
