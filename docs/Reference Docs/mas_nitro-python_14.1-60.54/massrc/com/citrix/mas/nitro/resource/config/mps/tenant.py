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
from massrc.com.citrix.mas.nitro.resource.config.mps.tenant_system_resource import tenant_system_resource
from massrc.com.citrix.mas.nitro.resource.config.mps.tenant_company_info import tenant_company_info


'''
Configuration for Tenants resource
'''

class tenant(base_resource):
	_user_name= ""
	_preauthtoken= ""
	_tenant_user_name= ""
	_is_pool_lic_user= ""
	_password= ""
	_service_type= ""
	_id= ""
	_parent_id= ""
	_name= ""
	_dbrole_name= ""
	_system_resource= ""
	_schema_name= ""
	_access_to_parent= ""
	_light_tenant= ""
	_company_info= ""
	_entitlement= ""
	_act_id= ""
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
			return "tenant"
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
			return "tenants"
		except Exception as e :
			raise e



	'''
	get User Name for tenant
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set User Name for tenant
	'''
	@user_name.setter
	def user_name(self,user_name):
		try :
			if not isinstance(user_name,str):
				raise TypeError("user_name must be set to str value")
			self._user_name = user_name
		except Exception as e :
			raise e


	'''
	get Preauth token for a tenant
	'''
	@property
	def preauthtoken(self) :
		try:
			return self._preauthtoken
		except Exception as e :
			raise e
	'''
	set Preauth token for a tenant
	'''
	@preauthtoken.setter
	def preauthtoken(self,preauthtoken):
		try :
			if not isinstance(preauthtoken,str):
				raise TypeError("preauthtoken must be set to str value")
			self._preauthtoken = preauthtoken
		except Exception as e :
			raise e


	'''
	get User Name for tenant
	'''
	@property
	def tenant_user_name(self) :
		try:
			return self._tenant_user_name
		except Exception as e :
			raise e
	'''
	set User Name for tenant
	'''
	@tenant_user_name.setter
	def tenant_user_name(self,tenant_user_name):
		try :
			if not isinstance(tenant_user_name,str):
				raise TypeError("tenant_user_name must be set to str value")
			self._tenant_user_name = tenant_user_name
		except Exception as e :
			raise e


	'''
	get Check if the customer is a pooled/ flexed licensing user
	'''
	@property
	def is_pool_lic_user(self) :
		try:
			return self._is_pool_lic_user
		except Exception as e :
			raise e
	'''
	set Check if the customer is a pooled/ flexed licensing user
	'''
	@is_pool_lic_user.setter
	def is_pool_lic_user(self,is_pool_lic_user):
		try :
			if not isinstance(is_pool_lic_user,bool):
				raise TypeError("is_pool_lic_user must be set to bool value")
			self._is_pool_lic_user = is_pool_lic_user
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Type of service, Setting the bits for NetScaler Console, NGS, WAF
	'''
	@property
	def service_type(self) :
		try:
			return self._service_type
		except Exception as e :
			raise e
	'''
	set Type of service, Setting the bits for NetScaler Console, NGS, WAF
	'''
	@service_type.setter
	def service_type(self,service_type):
		try :
			if not isinstance(service_type,long):
				raise TypeError("service_type must be set to long value")
			self._service_type = service_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the Tenants
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Tenants
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
	get Tenant ID of the parent Tenant.
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Tenant ID of the parent Tenant.
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Name of the Tenant
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the Tenant
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
	get Database Role Name for tenant
	'''
	@property
	def dbrole_name(self) :
		try:
			return self._dbrole_name
		except Exception as e :
			raise e
	'''
	set Database Role Name for tenant
	'''
	@dbrole_name.setter
	def dbrole_name(self,dbrole_name):
		try :
			if not isinstance(dbrole_name,str):
				raise TypeError("dbrole_name must be set to str value")
			self._dbrole_name = dbrole_name
		except Exception as e :
			raise e


	'''
	get Tenant System Resource
	'''
	@property
	def system_resource(self) :
		try:
			return self._system_resource
		except Exception as e :
			raise e
	'''
	set Tenant System Resource
	'''
	@system_resource.setter
	def system_resource(self,system_resource):
		try :
			if not isinstance(system_resource,tenant_system_resource):
				raise TypeError("system_resource must be set to tenant_system_resource value")
			self._system_resource = system_resource
		except Exception as e :
			raise e


	'''
	get Schema Name for tenant
	'''
	@property
	def schema_name(self) :
		try:
			return self._schema_name
		except Exception as e :
			raise e
	'''
	set Schema Name for tenant
	'''
	@schema_name.setter
	def schema_name(self,schema_name):
		try :
			if not isinstance(schema_name,str):
				raise TypeError("schema_name must be set to str value")
			self._schema_name = schema_name
		except Exception as e :
			raise e


	'''
	get Enable Shell access for non-nsroot User(s)
	'''
	@property
	def access_to_parent(self) :
		try:
			return self._access_to_parent
		except Exception as e :
			raise e
	'''
	set Enable Shell access for non-nsroot User(s)
	'''
	@access_to_parent.setter
	def access_to_parent(self,access_to_parent):
		try :
			if not isinstance(access_to_parent,bool):
				raise TypeError("access_to_parent must be set to bool value")
			self._access_to_parent = access_to_parent
		except Exception as e :
			raise e


	'''
	get Type of tenant schema, Setting the bits for full tenant with all tables
	'''
	@property
	def light_tenant(self) :
		try:
			return self._light_tenant
		except Exception as e :
			raise e
	'''
	set Type of tenant schema, Setting the bits for full tenant with all tables
	'''
	@light_tenant.setter
	def light_tenant(self,light_tenant):
		try :
			if not isinstance(light_tenant,long):
				raise TypeError("light_tenant must be set to long value")
			self._light_tenant = light_tenant
		except Exception as e :
			raise e


	'''
	get Tenant Company Information
	'''
	@property
	def company_info(self) :
		try:
			return self._company_info
		except Exception as e :
			raise e
	'''
	set Tenant Company Information
	'''
	@company_info.setter
	def company_info(self,company_info):
		try :
			if not isinstance(company_info,tenant_company_info):
				raise TypeError("company_info must be set to tenant_company_info value")
			self._company_info = company_info
		except Exception as e :
			raise e

	'''
	Entitlement string received from citrix cloud.
	'''
	@property
	def entitlement(self):
		try:
			return self._entitlement
		except Exception as e :
			raise e
	'''
	Entitlement string received from citrix cloud.
	'''
	@entitlement.setter
	def entitlement(self,entitlement):
		try :
			if not isinstance(entitlement,str):
				raise TypeError("entitlement must be set to str value")
			self._entitlement = entitlement
		except Exception as e :
			raise e

	'''
	Activity ID that is used by GUI to track the provisioning status.
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e
	'''
	Activity ID that is used by GUI to track the provisioning status.
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	Use this operation to add a tenant..
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
				tenant_obj= tenant()
				return cls.perform_operation_bulk_request(service,resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get tenants..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				tenant_obj=tenant()
				response = tenant_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete a tenant..
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
					tenant_obj=tenant()
					return cls.delete_bulk_request(client,resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify a tenant..
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
				tenant_obj=tenant()
				return cls.update_bulk_request(client,resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._filter=filter_
			return tenant_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._count=True
			response = tenant_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_responses, response, "tenant_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_response_array
				i=0
				error = [tenant() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_response_array
			i=0
			tenant_objs = [tenant() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant'):
					for props in obj._tenant:
						result = service.payload_formatter.string_to_bulk_resource(tenant_response,self.__class__.__name__,props)
						tenant_objs[i] = result.tenant
						i=i+1
			return tenant_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_response(base_response):
	def __init__(self,length=1) :
		self.tenant= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant= [ tenant() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_response_array = [ tenant() for _ in range(length)]
