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
Configuration for NetScaler Pooled Saas license access codes info resource
'''

class pooled_saas_lac_info(base_resource):
	_lac_proc_state= ""
	_lac_last_proc= ""
	_activation_id_list= ""
	_license_access_codes= ""
	_customer_id= ""
	_id= ""
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
			return "pooled_saas_lac_info"
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
			return "pooled_saas_lac_infos"
		except Exception as e :
			raise e



	'''
	get LAC processing state
	'''
	@property
	def lac_proc_state(self) :
		try:
			return self._lac_proc_state
		except Exception as e :
			raise e
	'''
	set LAC processing state
	'''
	@lac_proc_state.setter
	def lac_proc_state(self,lac_proc_state):
		try :
			if not isinstance(lac_proc_state,str):
				raise TypeError("lac_proc_state must be set to str value")
			self._lac_proc_state = lac_proc_state
		except Exception as e :
			raise e


	'''
	get Last scan of lac in UTC
	'''
	@property
	def lac_last_proc(self) :
		try:
			return self._lac_last_proc
		except Exception as e :
			raise e
	'''
	set Last scan of lac in UTC
	'''
	@lac_last_proc.setter
	def lac_last_proc(self,lac_last_proc):
		try :
			if not isinstance(lac_last_proc,str):
				raise TypeError("lac_last_proc must be set to str value")
			self._lac_last_proc = lac_last_proc
		except Exception as e :
			raise e


	'''
	get All activation IDs of the LAC
	'''
	@property
	def activation_id_list(self) :
		try:
			return self._activation_id_list
		except Exception as e :
			raise e
	'''
	set All activation IDs of the LAC
	'''
	@activation_id_list.setter
	def activation_id_list(self,activation_id_list):
		try :
			if not isinstance(activation_id_list,str):
				raise TypeError("activation_id_list must be set to str value")
			self._activation_id_list = activation_id_list
		except Exception as e :
			raise e


	'''
	get ADS pooled license access codes
	'''
	@property
	def license_access_codes(self) :
		try:
			return self._license_access_codes
		except Exception as e :
			raise e
	'''
	set ADS pooled license access codes
	'''
	@license_access_codes.setter
	def license_access_codes(self,license_access_codes):
		try :
			if not isinstance(license_access_codes,str):
				raise TypeError("license_access_codes must be set to str value")
			self._license_access_codes = license_access_codes
		except Exception as e :
			raise e


	'''
	get Customer Id for the tenant who has purchased the license
	'''
	@property
	def customer_id(self) :
		try:
			return self._customer_id
		except Exception as e :
			raise e
	'''
	set Customer Id for the tenant who has purchased the license
	'''
	@customer_id.setter
	def customer_id(self,customer_id):
		try :
			if not isinstance(customer_id,str):
				raise TypeError("customer_id must be set to str value")
			self._customer_id = customer_id
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
	get All properties
	'''
	@property
	def properties(self) :
		try:
			return self._properties
		except Exception as e :
			raise e
	'''
	set All properties
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
			result=service.payload_formatter.string_to_resource(pooled_saas_lac_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pooled_saas_lac_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(pooled_saas_lac_info_responses, response, "pooled_saas_lac_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.pooled_saas_lac_info_response_array
				i=0
				error = [pooled_saas_lac_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.pooled_saas_lac_info_response_array
			i=0
			pooled_saas_lac_info_objs = [pooled_saas_lac_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_pooled_saas_lac_info'):
					for props in obj._pooled_saas_lac_info:
						result = service.payload_formatter.string_to_bulk_resource(pooled_saas_lac_info_response,self.__class__.__name__,props)
						pooled_saas_lac_info_objs[i] = result.pooled_saas_lac_info
						i=i+1
			return pooled_saas_lac_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(pooled_saas_lac_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class pooled_saas_lac_info_response(base_response):
	def __init__(self,length=1) :
		self.pooled_saas_lac_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.pooled_saas_lac_info= [ pooled_saas_lac_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class pooled_saas_lac_info_responses(base_response):
	def __init__(self,length=1) :
		self.pooled_saas_lac_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.pooled_saas_lac_info_response_array = [ pooled_saas_lac_info() for _ in range(length)]
