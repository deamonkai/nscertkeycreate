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
Configuration for DNS Domain Entry resource
'''

class dns_domain_entry(base_resource):
	_tenant_id= ""
	_id= ""
	_name= ""
	_description= ""
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
			return "dns_domain_entry"
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
			return "dns_domain_entrys"
		except Exception as e :
			raise e



	'''
	get Tenant Id of the DNS Domain Entries
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the DNS Domain Entries
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
	get Id is system generated key for all the DNS Domain Entries
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the DNS Domain Entries
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
	get DNS Domain Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set DNS Domain Name
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
	get Description of DNS Domain Entry
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of DNS Domain Entry
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
	Use this operation to add DNS Domain Entry(s).
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
				dns_domain_entry_obj= dns_domain_entry()
				return cls.perform_operation_bulk_request(service,resource,dns_domain_entry_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get DNS Domain Entry(s).
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				dns_domain_entry_obj=dns_domain_entry()
				response = dns_domain_entry_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete DNS Domain Entry(s).
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
					dns_domain_entry_obj=dns_domain_entry()
					return cls.delete_bulk_request(client,resource,dns_domain_entry_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify DNS Domain Entry(s).
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
				dns_domain_entry_obj=dns_domain_entry()
				return cls.update_bulk_request(client,resource,dns_domain_entry_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of dns_domain_entry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			dns_domain_entry_obj = dns_domain_entry()
			option_ = options()
			option_._filter=filter_
			return dns_domain_entry_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the dns_domain_entry resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			dns_domain_entry_obj = dns_domain_entry()
			option_ = options()
			option_._count=True
			response = dns_domain_entry_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of dns_domain_entry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			dns_domain_entry_obj = dns_domain_entry()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = dns_domain_entry_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(dns_domain_entry_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dns_domain_entry
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dns_domain_entry_responses, response, "dns_domain_entry_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dns_domain_entry_response_array
				i=0
				error = [dns_domain_entry() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dns_domain_entry_response_array
			i=0
			dns_domain_entry_objs = [dns_domain_entry() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_dns_domain_entry'):
					for props in obj._dns_domain_entry:
						result = service.payload_formatter.string_to_bulk_resource(dns_domain_entry_response,self.__class__.__name__,props)
						dns_domain_entry_objs[i] = result.dns_domain_entry
						i=i+1
			return dns_domain_entry_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dns_domain_entry,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dns_domain_entry_response(base_response):
	def __init__(self,length=1) :
		self.dns_domain_entry= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dns_domain_entry= [ dns_domain_entry() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dns_domain_entry_responses(base_response):
	def __init__(self,length=1) :
		self.dns_domain_entry_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dns_domain_entry_response_array = [ dns_domain_entry() for _ in range(length)]
