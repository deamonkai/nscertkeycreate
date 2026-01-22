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
Configuration for Network function to application mapping resource
'''

class adcaas_app_network_function_map(base_resource):
	_created_at= ""
	_network_function_id= ""
	_state= ""
	_updated_at= ""
	_app_id= ""
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
			return "adcaas_app_network_function_map"
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
			return "adcaas_app_network_function_maps"
		except Exception as e :
			raise e



	'''
	get Created_at timestamp
	'''
	@property
	def created_at(self) :
		try:
			return self._created_at
		except Exception as e :
			raise e
	'''
	set Created_at timestamp
	'''
	@created_at.setter
	def created_at(self,created_at):
		try :
			if not isinstance(created_at,str):
				raise TypeError("created_at must be set to str value")
			self._created_at = created_at
		except Exception as e :
			raise e


	'''
	get Network function ID
	'''
	@property
	def network_function_id(self) :
		try:
			return self._network_function_id
		except Exception as e :
			raise e
	'''
	set Network function ID
	'''
	@network_function_id.setter
	def network_function_id(self,network_function_id):
		try :
			if not isinstance(network_function_id,str):
				raise TypeError("network_function_id must be set to str value")
			self._network_function_id = network_function_id
		except Exception as e :
			raise e


	'''
	get State of the network function
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of the network function
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get Created_at timestamp
	'''
	@property
	def updated_at(self) :
		try:
			return self._updated_at
		except Exception as e :
			raise e
	'''
	set Created_at timestamp
	'''
	@updated_at.setter
	def updated_at(self,updated_at):
		try :
			if not isinstance(updated_at,str):
				raise TypeError("updated_at must be set to str value")
			self._updated_at = updated_at
		except Exception as e :
			raise e


	'''
	get Application ID
	'''
	@property
	def app_id(self) :
		try:
			return self._app_id
		except Exception as e :
			raise e
	'''
	set Application ID
	'''
	@app_id.setter
	def app_id(self,app_id):
		try :
			if not isinstance(app_id,str):
				raise TypeError("app_id must be set to str value")
			self._app_id = app_id
		except Exception as e :
			raise e

	'''
	Use this operation to get network function.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adcaas_app_network_function_map_obj=adcaas_app_network_function_map()
				response = adcaas_app_network_function_map_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adcaas_app_network_function_map resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adcaas_app_network_function_map_obj = adcaas_app_network_function_map()
			option_ = options()
			option_._filter=filter_
			return adcaas_app_network_function_map_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adcaas_app_network_function_map resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adcaas_app_network_function_map_obj = adcaas_app_network_function_map()
			option_ = options()
			option_._count=True
			response = adcaas_app_network_function_map_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adcaas_app_network_function_map resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adcaas_app_network_function_map_obj = adcaas_app_network_function_map()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adcaas_app_network_function_map_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adcaas_app_network_function_map_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adcaas_app_network_function_map
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adcaas_app_network_function_map_responses, response, "adcaas_app_network_function_map_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adcaas_app_network_function_map_response_array
				i=0
				error = [adcaas_app_network_function_map() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adcaas_app_network_function_map_response_array
			i=0
			adcaas_app_network_function_map_objs = [adcaas_app_network_function_map() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adcaas_app_network_function_map'):
					for props in obj._adcaas_app_network_function_map:
						result = service.payload_formatter.string_to_bulk_resource(adcaas_app_network_function_map_response,self.__class__.__name__,props)
						adcaas_app_network_function_map_objs[i] = result.adcaas_app_network_function_map
						i=i+1
			return adcaas_app_network_function_map_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adcaas_app_network_function_map,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adcaas_app_network_function_map_response(base_response):
	def __init__(self,length=1) :
		self.adcaas_app_network_function_map= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adcaas_app_network_function_map= [ adcaas_app_network_function_map() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adcaas_app_network_function_map_responses(base_response):
	def __init__(self,length=1) :
		self.adcaas_app_network_function_map_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adcaas_app_network_function_map_response_array = [ adcaas_app_network_function_map() for _ in range(length)]
