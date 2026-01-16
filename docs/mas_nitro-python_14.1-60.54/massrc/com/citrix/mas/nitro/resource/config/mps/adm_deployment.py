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
Configuration for NetScaler Console Deployment Settings resource
'''

class adm_deployment(base_resource):
	_pooled_only= ""
	_NSlicensingType= ""
	_id= ""
	_msp_tenant_name= ""
	_ads_service_type= ""
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
			return "adm_deployment"
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
			return "adm_deployments"
		except Exception as e :
			raise e



	'''
	get Pooled Licensing only
	'''
	@property
	def pooled_only(self) :
		try:
			return self._pooled_only
		except Exception as e :
			raise e
	'''
	set Pooled Licensing only
	'''
	@pooled_only.setter
	def pooled_only(self,pooled_only):
		try :
			if not isinstance(pooled_only,bool):
				raise TypeError("pooled_only must be set to bool value")
			self._pooled_only = pooled_only
		except Exception as e :
			raise e


	'''
	get NS Licensing type, it could be pooled, flexed or npl
	'''
	@property
	def NSlicensingType(self) :
		try:
			return self._NSlicensingType
		except Exception as e :
			raise e
	'''
	set NS Licensing type, it could be pooled, flexed or npl
	'''
	@NSlicensingType.setter
	def NSlicensingType(self,NSlicensingType):
		try :
			if not isinstance(NSlicensingType,str):
				raise TypeError("NSlicensingType must be set to str value")
			self._NSlicensingType = NSlicensingType
		except Exception as e :
			raise e


	'''
	get Id is system generated for each setting
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated for each setting
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
	MSP Tenant Name
	'''
	@property
	def msp_tenant_name(self):
		try:
			return self._msp_tenant_name
		except Exception as e :
			raise e
	'''
	MSP Tenant Name
	'''
	@msp_tenant_name.setter
	def msp_tenant_name(self,msp_tenant_name):
		try :
			if not isinstance(msp_tenant_name,str):
				raise TypeError("msp_tenant_name must be set to str value")
			self._msp_tenant_name = msp_tenant_name
		except Exception as e :
			raise e

	'''
	ADS Service Type. Supported Types: NetScaler Console, AUTOMATION, INTENT
	'''
	@property
	def ads_service_type(self):
		try:
			return self._ads_service_type
		except Exception as e :
			raise e
	'''
	ADS Service Type. Supported Types: NetScaler Console, AUTOMATION, INTENT
	'''
	@ads_service_type.setter
	def ads_service_type(self,ads_service_type):
		try :
			if not isinstance(ads_service_type,str):
				raise TypeError("ads_service_type must be set to str value")
			self._ads_service_type = ads_service_type
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler Console Deployment.
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
				adm_deployment_obj=adm_deployment()
				return cls.update_bulk_request(client,resource,adm_deployment_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Console Deployment.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adm_deployment_obj=adm_deployment()
				response = adm_deployment_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adm_deployment resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adm_deployment_obj = adm_deployment()
			option_ = options()
			option_._filter=filter_
			return adm_deployment_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adm_deployment resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adm_deployment_obj = adm_deployment()
			option_ = options()
			option_._count=True
			response = adm_deployment_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adm_deployment resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adm_deployment_obj = adm_deployment()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adm_deployment_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adm_deployment_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adm_deployment
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_deployment_responses, response, "adm_deployment_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adm_deployment_response_array
				i=0
				error = [adm_deployment() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adm_deployment_response_array
			i=0
			adm_deployment_objs = [adm_deployment() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adm_deployment'):
					for props in obj._adm_deployment:
						result = service.payload_formatter.string_to_bulk_resource(adm_deployment_response,self.__class__.__name__,props)
						adm_deployment_objs[i] = result.adm_deployment
						i=i+1
			return adm_deployment_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adm_deployment,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adm_deployment_response(base_response):
	def __init__(self,length=1) :
		self.adm_deployment= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adm_deployment= [ adm_deployment() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adm_deployment_responses(base_response):
	def __init__(self,length=1) :
		self.adm_deployment_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adm_deployment_response_array = [ adm_deployment() for _ in range(length)]
