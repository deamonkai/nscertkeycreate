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
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_submodule_client_data import rba_submodule_client_data
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_operation_client_data import rba_operation_client_data


'''
Configuration for This resource is used to display the feature wise permissions tree during access policy creation in GUI. resource
'''

class rba_module_client_data(base_resource):
	_submodules=[]
	_display_name= ""
	_ui_component= ""
	_id= ""
	_operation=[]
	_serial_id= ""
	_name= ""
	_parent_name= ""
	_parent_id= ""
	_child_node= ""
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
			return "rba_module_client_data"
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
			return "rba_module_client_datas"
		except Exception as e :
			raise e



	'''
	get This is used to display child nodes under a particular feature tree node in permission tree.
	'''
	@property
	def submodules(self) :
		try:
			return self._submodules
		except Exception as e :
			raise e


	'''
	get module display name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get This is used to mention if its UI component
	'''
	@property
	def ui_component(self) :
		try:
			return self._ui_component
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
	get This is used to display operations of particular node in permissions tree.
	'''
	@property
	def operation(self) :
		try:
			return self._operation
		except Exception as e :
			raise e


	'''
	get This is used to display the permissions tree in an order manner.
	'''
	@property
	def serial_id(self) :
		try:
			return self._serial_id
		except Exception as e :
			raise e


	'''
	get module name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get Parent name for UI tree node
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e


	'''
	get Parent id for UI tree node
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e


	'''
	get This is used if tree node is child node of another tree node in permission tree.
	'''
	@property
	def child_node(self) :
		try:
			return self._child_node
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_module_client_data_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_module_client_data
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_module_client_data_responses, response, "rba_module_client_data_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_module_client_data_response_array
				i=0
				error = [rba_module_client_data() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_module_client_data_response_array
			i=0
			rba_module_client_data_objs = [rba_module_client_data() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_module_client_data'):
					for props in obj._rba_module_client_data:
						result = service.payload_formatter.string_to_bulk_resource(rba_module_client_data_response,self.__class__.__name__,props)
						rba_module_client_data_objs[i] = result.rba_module_client_data
						i=i+1
			return rba_module_client_data_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_module_client_data,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_module_client_data_response(base_response):
	def __init__(self,length=1) :
		self.rba_module_client_data= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_module_client_data= [ rba_module_client_data() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_module_client_data_responses(base_response):
	def __init__(self,length=1) :
		self.rba_module_client_data_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_module_client_data_response_array = [ rba_module_client_data() for _ in range(length)]
