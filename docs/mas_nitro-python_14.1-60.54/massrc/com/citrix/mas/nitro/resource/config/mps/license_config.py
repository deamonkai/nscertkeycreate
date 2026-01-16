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
Configuration for License Configuration resource
'''

class license_config(base_resource):
	_ip_address= ""
	_id= ""
	_max_limit= ""
	_policyName= ""
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
			return "license_config"
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
			return "license_configs"
		except Exception as e :
			raise e



	'''
	get IP Addresse list
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Addresse list
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get System generated value
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set System generated value
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
	get Max limit
	'''
	@property
	def max_limit(self) :
		try:
			return self._max_limit
		except Exception as e :
			raise e
	'''
	set Max limit
	'''
	@max_limit.setter
	def max_limit(self,max_limit):
		try :
			if not isinstance(max_limit,int):
				raise TypeError("max_limit must be set to int value")
			self._max_limit = max_limit
		except Exception as e :
			raise e


	'''
	get policyName
	'''
	@property
	def policyName(self) :
		try:
			return self._policyName
		except Exception as e :
			raise e
	'''
	set policyName
	'''
	@policyName.setter
	def policyName(self,policyName):
		try :
			if not isinstance(policyName,str):
				raise TypeError("policyName must be set to str value")
			self._policyName = policyName
		except Exception as e :
			raise e

	'''
	Use this operation to apply new licenses files.
	'''

	'''
	Use this operation to apply new licenses files.
	'''
	@classmethod
	def apply(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"apply")
		except Exception as e :
			raise e

	'''
	Use this operation to get license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_config_obj=license_config()
				response = license_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_config_obj = license_config()
			option_ = options()
			option_._filter=filter_
			return license_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_config_obj = license_config()
			option_ = options()
			option_._count=True
			response = license_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_config_obj = license_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_config_responses, response, "license_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_config_response_array
				i=0
				error = [license_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_config_response_array
			i=0
			license_config_objs = [license_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_config'):
					for props in obj._license_config:
						result = service.payload_formatter.string_to_bulk_resource(license_config_response,self.__class__.__name__,props)
						license_config_objs[i] = result.license_config
						i=i+1
			return license_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_config_response(base_response):
	def __init__(self,length=1) :
		self.license_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_config= [ license_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_config_responses(base_response):
	def __init__(self,length=1) :
		self.license_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_config_response_array = [ license_config() for _ in range(length)]
