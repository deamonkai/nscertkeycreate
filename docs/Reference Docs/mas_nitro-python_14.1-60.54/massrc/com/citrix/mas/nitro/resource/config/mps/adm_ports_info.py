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
Configuration for List of ports exposed to NetScaler Console resource
'''

class adm_ports_info(base_resource):
	_port_number= ""
	_description= ""
	_name= ""
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
			return "adm_ports_info"
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
			return "adm_ports_infos"
		except Exception as e :
			raise e



	'''
	get The Port number used by NetScaler Console services
	'''
	@property
	def port_number(self) :
		try:
			return self._port_number
		except Exception as e :
			raise e
	'''
	set The Port number used by NetScaler Console services
	'''
	@port_number.setter
	def port_number(self,port_number):
		try :
			if not isinstance(port_number,int):
				raise TypeError("port_number must be set to int value")
			self._port_number = port_number
		except Exception as e :
			raise e


	'''
	get The Description of the port used by NetScaler Console
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set The Description of the port used by NetScaler Console
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get The Name of the NetScaler Console using any port
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set The Name of the NetScaler Console using any port
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e

	'''
	Use this operation to get information regarding all the ports of NetScaler Console.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adm_ports_info_obj=adm_ports_info()
				response = adm_ports_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adm_ports_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adm_ports_info_obj = adm_ports_info()
			option_ = options()
			option_._filter=filter_
			return adm_ports_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adm_ports_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adm_ports_info_obj = adm_ports_info()
			option_ = options()
			option_._count=True
			response = adm_ports_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adm_ports_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adm_ports_info_obj = adm_ports_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adm_ports_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adm_ports_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adm_ports_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_ports_info_responses, response, "adm_ports_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adm_ports_info_response_array
				i=0
				error = [adm_ports_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adm_ports_info_response_array
			i=0
			adm_ports_info_objs = [adm_ports_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adm_ports_info'):
					for props in obj._adm_ports_info:
						result = service.payload_formatter.string_to_bulk_resource(adm_ports_info_response,self.__class__.__name__,props)
						adm_ports_info_objs[i] = result.adm_ports_info
						i=i+1
			return adm_ports_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adm_ports_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adm_ports_info_response(base_response):
	def __init__(self,length=1) :
		self.adm_ports_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adm_ports_info= [ adm_ports_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adm_ports_info_responses(base_response):
	def __init__(self,length=1) :
		self.adm_ports_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adm_ports_info_response_array = [ adm_ports_info() for _ in range(length)]
