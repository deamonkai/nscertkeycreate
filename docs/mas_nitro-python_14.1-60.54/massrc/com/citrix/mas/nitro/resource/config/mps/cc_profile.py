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
Configuration for Cloud Profile resource
'''

class cc_profile(base_resource):
	_skip_setting= ""
	_tenant_id= ""
	_cc_id= ""
	_is_set= ""
	_svc_end_point= ""
	_customer_id= ""
	_enable_mastlmy= ""
	_customer_name= ""
	_pop_name= ""
	_enable_service_now= ""
	_id= ""
	_new_with_cloudconnect= ""
	_svc_name= ""
	_instance_id= ""
	_act_id= ""
	_verify_url= ""
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
			return "cc_profile"
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
			return "cc_profiles"
		except Exception as e :
			raise e



	'''
	get True, if this setting is skipped by user
	'''
	@property
	def skip_setting(self) :
		try:
			return self._skip_setting
		except Exception as e :
			raise e


	'''
	get Tenant Id of cloud profile
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of cloud profile
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
	get Cloud Connect ID stored at server side
	'''
	@property
	def cc_id(self) :
		try:
			return self._cc_id
		except Exception as e :
			raise e
	'''
	set Cloud Connect ID stored at server side
	'''
	@cc_id.setter
	def cc_id(self,cc_id):
		try :
			if not isinstance(cc_id,str):
				raise TypeError("cc_id must be set to str value")
			self._cc_id = cc_id
		except Exception as e :
			raise e


	'''
	get True, if this profile is updated by user
	'''
	@property
	def is_set(self) :
		try:
			return self._is_set
		except Exception as e :
			raise e


	'''
	get Service end point of the service
	'''
	@property
	def svc_end_point(self) :
		try:
			return self._svc_end_point
		except Exception as e :
			raise e


	'''
	get Customer ID of the cloud profile holder
	'''
	@property
	def customer_id(self) :
		try:
			return self._customer_id
		except Exception as e :
			raise e


	'''
	get Enable NetScaler Console telemetry feature
	'''
	@property
	def enable_mastlmy(self) :
		try:
			return self._enable_mastlmy
		except Exception as e :
			raise e


	'''
	get Customer Name
	'''
	@property
	def customer_name(self) :
		try:
			return self._customer_name
		except Exception as e :
			raise e


	'''
	get Cloud service POP Name
	'''
	@property
	def pop_name(self) :
		try:
			return self._pop_name
		except Exception as e :
			raise e


	'''
	get Enable Service  Now feature
	'''
	@property
	def enable_service_now(self) :
		try:
			return self._enable_service_now
		except Exception as e :
			raise e
	'''
	set Enable Service  Now feature
	'''
	@enable_service_now.setter
	def enable_service_now(self,enable_service_now):
		try :
			if not isinstance(enable_service_now,bool):
				raise TypeError("enable_service_now must be set to bool value")
			self._enable_service_now = enable_service_now
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the cloud profiles
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the cloud profiles
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
	get True, if this profile is updated by user with cloudconnect
	'''
	@property
	def new_with_cloudconnect(self) :
		try:
			return self._new_with_cloudconnect
		except Exception as e :
			raise e


	'''
	get Cloud service Name
	'''
	@property
	def svc_name(self) :
		try:
			return self._svc_name
		except Exception as e :
			raise e


	'''
	get Instance ID of the system
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	Verify URL
	'''
	@property
	def verify_url(self):
		try:
			return self._verify_url
		except Exception as e :
			raise e

	'''
	Use this operation to modify cloud profile settings..
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
				cc_profile_obj=cc_profile()
				return cls.update_bulk_request(client,resource,cc_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to authenticate cloud profile settings..
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
				cc_profile_obj= cc_profile()
				return cls.perform_operation_bulk_request(service,resource,cc_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get cloud profile details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				cc_profile_obj=cc_profile()
				response = cc_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cc_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cc_profile_obj = cc_profile()
			option_ = options()
			option_._filter=filter_
			return cc_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cc_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cc_profile_obj = cc_profile()
			option_ = options()
			option_._count=True
			response = cc_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cc_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cc_profile_obj = cc_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cc_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cc_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cc_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cc_profile_responses, response, "cc_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cc_profile_response_array
				i=0
				error = [cc_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cc_profile_response_array
			i=0
			cc_profile_objs = [cc_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cc_profile'):
					for props in obj._cc_profile:
						result = service.payload_formatter.string_to_bulk_resource(cc_profile_response,self.__class__.__name__,props)
						cc_profile_objs[i] = result.cc_profile
						i=i+1
			return cc_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cc_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cc_profile_response(base_response):
	def __init__(self,length=1) :
		self.cc_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cc_profile= [ cc_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cc_profile_responses(base_response):
	def __init__(self,length=1) :
		self.cc_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cc_profile_response_array = [ cc_profile() for _ in range(length)]
