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
Configuration for Mapping between the certificates in store and the entities to which they are bound resource
'''

class cert_store_mapping(base_resource):
	_entity_id= ""
	_cert_id= ""
	_instance_host_name= ""
	_id= ""
	_instance_id= ""
	_installed_cert_data_ids= ""
	_entity_name= ""
	_entity_type= ""
	_instance_display_name= ""
	_instance_ip= ""
	_is_instances= ""
	_is_entities= ""
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
			return "cert_store_mapping"
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
			return "cert_store_mappings"
		except Exception as e :
			raise e



	'''
	get Id of the application or module to which the cert is bound
	'''
	@property
	def entity_id(self) :
		try:
			return self._entity_id
		except Exception as e :
			raise e
	'''
	set Id of the application or module to which the cert is bound
	'''
	@entity_id.setter
	def entity_id(self,entity_id):
		try :
			if not isinstance(entity_id,str):
				raise TypeError("entity_id must be set to str value")
			self._entity_id = entity_id
		except Exception as e :
			raise e


	'''
	get Id of the certificate file in cert store table
	'''
	@property
	def cert_id(self) :
		try:
			return self._cert_id
		except Exception as e :
			raise e
	'''
	set Id of the certificate file in cert store table
	'''
	@cert_id.setter
	def cert_id(self,cert_id):
		try :
			if not isinstance(cert_id,str):
				raise TypeError("cert_id must be set to str value")
			self._cert_id = cert_id
		except Exception as e :
			raise e


	'''
	get Host name of the instance in the managed_device table, in which the cert is installed
	'''
	@property
	def instance_host_name(self) :
		try:
			return self._instance_host_name
		except Exception as e :
			raise e
	'''
	set Host name of the instance in the managed_device table, in which the cert is installed
	'''
	@instance_host_name.setter
	def instance_host_name(self,instance_host_name):
		try :
			if not isinstance(instance_host_name,str):
				raise TypeError("instance_host_name must be set to str value")
			self._instance_host_name = instance_host_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all certificate story entries. 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all certificate story entries. 
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
	get Id of the instance in the managed_device table, in which the cert is installed
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e
	'''
	set Id of the instance in the managed_device table, in which the cert is installed
	'''
	@instance_id.setter
	def instance_id(self,instance_id):
		try :
			if not isinstance(instance_id,str):
				raise TypeError("instance_id must be set to str value")
			self._instance_id = instance_id
		except Exception as e :
			raise e


	'''
	get Comma separated list of cert store data ids installed
	'''
	@property
	def installed_cert_data_ids(self) :
		try:
			return self._installed_cert_data_ids
		except Exception as e :
			raise e
	'''
	set Comma separated list of cert store data ids installed
	'''
	@installed_cert_data_ids.setter
	def installed_cert_data_ids(self,installed_cert_data_ids):
		try :
			if not isinstance(installed_cert_data_ids,str):
				raise TypeError("installed_cert_data_ids must be set to str value")
			self._installed_cert_data_ids = installed_cert_data_ids
		except Exception as e :
			raise e


	'''
	get Name of the application or module to which the cert is bound
	'''
	@property
	def entity_name(self) :
		try:
			return self._entity_name
		except Exception as e :
			raise e
	'''
	set Name of the application or module to which the cert is bound
	'''
	@entity_name.setter
	def entity_name(self,entity_name):
		try :
			if not isinstance(entity_name,str):
				raise TypeError("entity_name must be set to str value")
			self._entity_name = entity_name
		except Exception as e :
			raise e


	'''
	get Type of the application or module to which the cert is bound
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	set Type of the application or module to which the cert is bound
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e


	'''
	get Display name of the instance in the managed_device table, in which the cert is installed
	'''
	@property
	def instance_display_name(self) :
		try:
			return self._instance_display_name
		except Exception as e :
			raise e
	'''
	set Display name of the instance in the managed_device table, in which the cert is installed
	'''
	@instance_display_name.setter
	def instance_display_name(self,instance_display_name):
		try :
			if not isinstance(instance_display_name,str):
				raise TypeError("instance_display_name must be set to str value")
			self._instance_display_name = instance_display_name
		except Exception as e :
			raise e


	'''
	get IP Address of the instance in the managed_device table, in which the cert is installed
	'''
	@property
	def instance_ip(self) :
		try:
			return self._instance_ip
		except Exception as e :
			raise e
	'''
	set IP Address of the instance in the managed_device table, in which the cert is installed
	'''
	@instance_ip.setter
	def instance_ip(self,instance_ip):
		try :
			if not isinstance(instance_ip,str):
				raise TypeError("instance_ip must be set to str value")
			self._instance_ip = instance_ip
		except Exception as e :
			raise e

	'''
	To retrieve only the instances associated with the provided cert_id
	'''
	@property
	def is_instances(self):
		try:
			return self._is_instances
		except Exception as e :
			raise e
	'''
	To retrieve only the instances associated with the provided cert_id
	'''
	@is_instances.setter
	def is_instances(self,is_instances):
		try :
			if not isinstance(is_instances,bool):
				raise TypeError("is_instances must be set to bool value")
			self._is_instances = is_instances
		except Exception as e :
			raise e

	'''
	To get only the entities associated with the provided cert_id
	'''
	@property
	def is_entities(self):
		try:
			return self._is_entities
		except Exception as e :
			raise e
	'''
	To get only the entities associated with the provided cert_id
	'''
	@is_entities.setter
	def is_entities(self,is_entities):
		try :
			if not isinstance(is_entities,bool):
				raise TypeError("is_entities must be set to bool value")
			self._is_entities = is_entities
		except Exception as e :
			raise e

	'''
	Use this operation to modify mapping information about certificates stored in cert store to the bound entities .
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				cert_store_mapping_obj=cert_store_mapping()
				return cls.update_bulk_request(client,resource,cert_store_mapping_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add mapping information about certificates stored in cert store to the bound entities .
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
				cert_store_mapping_obj= cert_store_mapping()
				return cls.perform_operation_bulk_request(service,resource,cert_store_mapping_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete mapping information between certificates and entities bound.
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
					cert_store_mapping_obj=cert_store_mapping()
					return cls.delete_bulk_request(client,resource,cert_store_mapping_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get bound entity details of certificates stored in cert store..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				cert_store_mapping_obj=cert_store_mapping()
				response = cert_store_mapping_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cert_store_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cert_store_mapping_obj = cert_store_mapping()
			option_ = options()
			option_._filter=filter_
			return cert_store_mapping_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cert_store_mapping resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cert_store_mapping_obj = cert_store_mapping()
			option_ = options()
			option_._count=True
			response = cert_store_mapping_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cert_store_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cert_store_mapping_obj = cert_store_mapping()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cert_store_mapping_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cert_store_mapping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cert_store_mapping
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_store_mapping_responses, response, "cert_store_mapping_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cert_store_mapping_response_array
				i=0
				error = [cert_store_mapping() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cert_store_mapping_response_array
			i=0
			cert_store_mapping_objs = [cert_store_mapping() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cert_store_mapping'):
					for props in obj._cert_store_mapping:
						result = service.payload_formatter.string_to_bulk_resource(cert_store_mapping_response,self.__class__.__name__,props)
						cert_store_mapping_objs[i] = result.cert_store_mapping
						i=i+1
			return cert_store_mapping_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cert_store_mapping,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cert_store_mapping_response(base_response):
	def __init__(self,length=1) :
		self.cert_store_mapping= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cert_store_mapping= [ cert_store_mapping() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cert_store_mapping_responses(base_response):
	def __init__(self,length=1) :
		self.cert_store_mapping_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cert_store_mapping_response_array = [ cert_store_mapping() for _ in range(length)]
