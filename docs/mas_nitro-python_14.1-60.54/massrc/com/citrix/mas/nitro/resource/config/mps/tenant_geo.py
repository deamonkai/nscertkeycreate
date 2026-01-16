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
Configuration for Refresh Tenant geo mapping resource
'''

class tenant_geo(base_resource):
	_cc_region= ""
	_name= ""
	_admin_tenant= ""
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
			return "tenant_geo"
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
			return "tenant_geos"
		except Exception as e :
			raise e



	'''
	get Citrix Cloud Region of the tenant
	'''
	@property
	def cc_region(self) :
		try:
			return self._cc_region
		except Exception as e :
			raise e
	'''
	set Citrix Cloud Region of the tenant
	'''
	@cc_region.setter
	def cc_region(self,cc_region):
		try :
			if not isinstance(cc_region,str):
				raise TypeError("cc_region must be set to str value")
			self._cc_region = cc_region
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Tenant Name
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
	get Admin Tenant
	'''
	@property
	def admin_tenant(self) :
		try:
			return self._admin_tenant
		except Exception as e :
			raise e
	'''
	set Admin Tenant
	'''
	@admin_tenant.setter
	def admin_tenant(self,admin_tenant):
		try :
			if not isinstance(admin_tenant,str):
				raise TypeError("admin_tenant must be set to str value")
			self._admin_tenant = admin_tenant
		except Exception as e :
			raise e

	'''
	Use this operation to get the tenant geo mapping for NGS Admin tenants.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				tenant_geo_obj=tenant_geo()
				response = tenant_geo_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant_geo resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_geo_obj = tenant_geo()
			option_ = options()
			option_._filter=filter_
			return tenant_geo_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant_geo resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_geo_obj = tenant_geo()
			option_ = options()
			option_._count=True
			response = tenant_geo_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant_geo resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_geo_obj = tenant_geo()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_geo_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_geo_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_geo
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_geo_responses, response, "tenant_geo_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_geo_response_array
				i=0
				error = [tenant_geo() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_geo_response_array
			i=0
			tenant_geo_objs = [tenant_geo() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_geo'):
					for props in obj._tenant_geo:
						result = service.payload_formatter.string_to_bulk_resource(tenant_geo_response,self.__class__.__name__,props)
						tenant_geo_objs[i] = result.tenant_geo
						i=i+1
			return tenant_geo_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_geo,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_geo_response(base_response):
	def __init__(self,length=1) :
		self.tenant_geo= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_geo= [ tenant_geo() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_geo_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_geo_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_geo_response_array = [ tenant_geo() for _ in range(length)]
