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
Configuration for RBA Statement defines the permission for a resource resource
'''

class rba_statement(base_resource):
	_parent_id= ""
	_parent_name= ""
	_access_type= ""
	_id= ""
	_operation_name= ""
	_dependent_resources= ""
	_resource_type= ""
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
			return "rba_statement"
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
			return "rba_statements"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e


	'''
	get true, if access is allowed
	'''
	@property
	def access_type(self) :
		try:
			return self._access_type
		except Exception as e :
			raise e
	'''
	set true, if access is allowed
	'''
	@access_type.setter
	def access_type(self,access_type):
		try :
			if not isinstance(access_type,bool):
				raise TypeError("access_type must be set to bool value")
			self._access_type = access_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the permission statements
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the permission statements
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
	get Operation for a resource
	'''
	@property
	def operation_name(self) :
		try:
			return self._operation_name
		except Exception as e :
			raise e
	'''
	set Operation for a resource
	'''
	@operation_name.setter
	def operation_name(self,operation_name):
		try :
			if not isinstance(operation_name,str):
				raise TypeError("operation_name must be set to str value")
			self._operation_name = operation_name
		except Exception as e :
			raise e


	'''
	get Comma separated names of resources, permission of these resources is dependent upon permission of whatever is given in resource_type.
	'''
	@property
	def dependent_resources(self) :
		try:
			return self._dependent_resources
		except Exception as e :
			raise e
	'''
	set Comma separated names of resources, permission of these resources is dependent upon permission of whatever is given in resource_type.
	'''
	@dependent_resources.setter
	def dependent_resources(self,dependent_resources):
		try :
			if not isinstance(dependent_resources,str):
				raise TypeError("dependent_resources must be set to str value")
			self._dependent_resources = dependent_resources
		except Exception as e :
			raise e


	'''
	get Resource Type
	'''
	@property
	def resource_type(self) :
		try:
			return self._resource_type
		except Exception as e :
			raise e
	'''
	set Resource Type
	'''
	@resource_type.setter
	def resource_type(self,resource_type):
		try :
			if not isinstance(resource_type,str):
				raise TypeError("resource_type must be set to str value")
			self._resource_type = resource_type
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_statement_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_statement
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_statement_responses, response, "rba_statement_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_statement_response_array
				i=0
				error = [rba_statement() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_statement_response_array
			i=0
			rba_statement_objs = [rba_statement() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_statement'):
					for props in obj._rba_statement:
						result = service.payload_formatter.string_to_bulk_resource(rba_statement_response,self.__class__.__name__,props)
						rba_statement_objs[i] = result.rba_statement
						i=i+1
			return rba_statement_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_statement,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_statement_response(base_response):
	def __init__(self,length=1) :
		self.rba_statement= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_statement= [ rba_statement() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_statement_responses(base_response):
	def __init__(self,length=1) :
		self.rba_statement_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_statement_response_array = [ rba_statement() for _ in range(length)]
