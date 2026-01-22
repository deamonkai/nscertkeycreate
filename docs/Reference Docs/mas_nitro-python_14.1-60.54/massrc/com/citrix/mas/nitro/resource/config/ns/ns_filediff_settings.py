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
Configuration for Mail settings for Config File Diff feature resource
'''

class ns_filediff_settings(base_resource):
	_slack_profile= ""
	_mail_profile= ""
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
			return "ns_filediff_settings"
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
			return "ns_filediff_settingss"
		except Exception as e :
			raise e


	'''
	slack profile 
	'''
	@property
	def slack_profile(self):
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	slack profile 
	'''
	@slack_profile.setter
	def slack_profile(self,slack_profile):
		try :
			if not isinstance(slack_profile,str):
				raise TypeError("slack_profile must be set to str value")
			self._slack_profile = slack_profile
		except Exception as e :
			raise e

	'''
	mail profile 
	'''
	@property
	def mail_profile(self):
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	mail profile 
	'''
	@mail_profile.setter
	def mail_profile(self,mail_profile):
		try :
			if not isinstance(mail_profile,str):
				raise TypeError("mail_profile must be set to str value")
			self._mail_profile = mail_profile
		except Exception as e :
			raise e

	'''
	Use this operation to get mail profile and slack profile for notification of Config File Diff .
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_filediff_settings_obj=ns_filediff_settings()
				response = ns_filediff_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update mail profile and slack profile for notification of Config File Diff .
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
				ns_filediff_settings_obj=ns_filediff_settings()
				return cls.update_bulk_request(client,resource,ns_filediff_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_filediff_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_filediff_settings_obj = ns_filediff_settings()
			option_ = options()
			option_._filter=filter_
			return ns_filediff_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_filediff_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_filediff_settings_obj = ns_filediff_settings()
			option_ = options()
			option_._count=True
			response = ns_filediff_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_filediff_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_filediff_settings_obj = ns_filediff_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_filediff_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_filediff_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_filediff_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_filediff_settings_responses, response, "ns_filediff_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_filediff_settings_response_array
				i=0
				error = [ns_filediff_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_filediff_settings_response_array
			i=0
			ns_filediff_settings_objs = [ns_filediff_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_filediff_settings'):
					for props in obj._ns_filediff_settings:
						result = service.payload_formatter.string_to_bulk_resource(ns_filediff_settings_response,self.__class__.__name__,props)
						ns_filediff_settings_objs[i] = result.ns_filediff_settings
						i=i+1
			return ns_filediff_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_filediff_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_filediff_settings_response(base_response):
	def __init__(self,length=1) :
		self.ns_filediff_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_filediff_settings= [ ns_filediff_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_filediff_settings_responses(base_response):
	def __init__(self,length=1) :
		self.ns_filediff_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_filediff_settings_response_array = [ ns_filediff_settings() for _ in range(length)]
