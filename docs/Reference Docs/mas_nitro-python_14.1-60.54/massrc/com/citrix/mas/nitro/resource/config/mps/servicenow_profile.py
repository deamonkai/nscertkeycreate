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
Configuration for Servicenow details. resource
'''

class servicenow_profile(base_resource):
	_profile_name= ""
	_tenant_id= ""
	_id= ""
	_is_enabled= ""
	_domain= ""
	_url= ""
	_is_validated= ""
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
			return "servicenow_profile"
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
			return "servicenow_profiles"
		except Exception as e :
			raise e



	'''
	get Profile name through which servicenow messages will be sent.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name through which servicenow messages will be sent.
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
	get Tenant Id of the servicenow profile
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the servicenow profile
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the sent servicenow messages.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sent servicenow messages.
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
	get true if this profile has been enabled
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set true if this profile has been enabled
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get Domain for ServiceNow Endpoint
	'''
	@property
	def domain(self) :
		try:
			return self._domain
		except Exception as e :
			raise e
	'''
	set Domain for ServiceNow Endpoint
	'''
	@domain.setter
	def domain(self,domain):
		try :
			if not isinstance(domain,str):
				raise TypeError("domain must be set to str value")
			self._domain = domain
		except Exception as e :
			raise e


	'''
	get URL for ServiceNow Endpoint
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set URL for ServiceNow Endpoint
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e


	'''
	get true if this profile has been validated and can be used to raise the ticket
	'''
	@property
	def is_validated(self) :
		try:
			return self._is_validated
		except Exception as e :
			raise e
	'''
	set true if this profile has been validated and can be used to raise the ticket
	'''
	@is_validated.setter
	def is_validated(self,is_validated):
		try :
			if not isinstance(is_validated,bool):
				raise TypeError("is_validated must be set to bool value")
			self._is_validated = is_validated
		except Exception as e :
			raise e

	'''
	Use this operation to get servicenow profile..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				servicenow_profile_obj=servicenow_profile()
				response = servicenow_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add servicenow profile..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				servicenow_profile_obj= servicenow_profile()
				return cls.perform_operation_bulk_request(service,resource,servicenow_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete servicenow profile..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					servicenow_profile_obj=servicenow_profile()
					return cls.delete_bulk_request(client,resource,servicenow_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of servicenow_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			servicenow_profile_obj = servicenow_profile()
			option_ = options()
			option_._filter=filter_
			return servicenow_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the servicenow_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			servicenow_profile_obj = servicenow_profile()
			option_ = options()
			option_._count=True
			response = servicenow_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of servicenow_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			servicenow_profile_obj = servicenow_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = servicenow_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(servicenow_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicenow_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(servicenow_profile_responses, response, "servicenow_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.servicenow_profile_response_array
				i=0
				error = [servicenow_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.servicenow_profile_response_array
			i=0
			servicenow_profile_objs = [servicenow_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_servicenow_profile'):
					for props in obj._servicenow_profile:
						result = service.payload_formatter.string_to_bulk_resource(servicenow_profile_response,self.__class__.__name__,props)
						servicenow_profile_objs[i] = result.servicenow_profile
						i=i+1
			return servicenow_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(servicenow_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class servicenow_profile_response(base_response):
	def __init__(self,length=1) :
		self.servicenow_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.servicenow_profile= [ servicenow_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class servicenow_profile_responses(base_response):
	def __init__(self,length=1) :
		self.servicenow_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.servicenow_profile_response_array = [ servicenow_profile() for _ in range(length)]
