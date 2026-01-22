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
Configuration for PagerDuty profile details. resource
'''

class pagerduty_profile(base_resource):
	_service_key= ""
	_profile_name= ""
	_id= ""
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
			return "pagerduty_profile"
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
			return "pagerduty_profiles"
		except Exception as e :
			raise e



	'''
	get Service key
	'''
	@property
	def service_key(self) :
		try:
			return self._service_key
		except Exception as e :
			raise e
	'''
	set Service key
	'''
	@service_key.setter
	def service_key(self,service_key):
		try :
			if not isinstance(service_key,str):
				raise TypeError("service_key must be set to str value")
			self._service_key = service_key
		except Exception as e :
			raise e


	'''
	get Profile name through which pagerduty alert will be sent.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name through which pagerduty alert will be sent.
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
	get Id is system generated key for all the sent pagerduty alerts.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sent pagerduty alerts.
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
	Use this operation to add pagerduty profile..
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
				pagerduty_profile_obj= pagerduty_profile()
				return cls.perform_operation_bulk_request(service,resource,pagerduty_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get pagerduty details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				pagerduty_profile_obj=pagerduty_profile()
				response = pagerduty_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete pagerduty details..
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
					pagerduty_profile_obj=pagerduty_profile()
					return cls.delete_bulk_request(client,resource,pagerduty_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify pagerduty details..
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
				pagerduty_profile_obj=pagerduty_profile()
				return cls.update_bulk_request(client,resource,pagerduty_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of pagerduty_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			pagerduty_profile_obj = pagerduty_profile()
			option_ = options()
			option_._filter=filter_
			return pagerduty_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the pagerduty_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			pagerduty_profile_obj = pagerduty_profile()
			option_ = options()
			option_._count=True
			response = pagerduty_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of pagerduty_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			pagerduty_profile_obj = pagerduty_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = pagerduty_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(pagerduty_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pagerduty_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(pagerduty_profile_responses, response, "pagerduty_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.pagerduty_profile_response_array
				i=0
				error = [pagerduty_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.pagerduty_profile_response_array
			i=0
			pagerduty_profile_objs = [pagerduty_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_pagerduty_profile'):
					for props in obj._pagerduty_profile:
						result = service.payload_formatter.string_to_bulk_resource(pagerduty_profile_response,self.__class__.__name__,props)
						pagerduty_profile_objs[i] = result.pagerduty_profile
						i=i+1
			return pagerduty_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(pagerduty_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class pagerduty_profile_response(base_response):
	def __init__(self,length=1) :
		self.pagerduty_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.pagerduty_profile= [ pagerduty_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class pagerduty_profile_responses(base_response):
	def __init__(self,length=1) :
		self.pagerduty_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.pagerduty_profile_response_array = [ pagerduty_profile() for _ in range(length)]
