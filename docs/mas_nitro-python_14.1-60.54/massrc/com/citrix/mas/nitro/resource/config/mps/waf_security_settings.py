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
Configuration for Mapping Learning group with Learning settings resource
'''

class waf_security_settings(base_resource):
	_parent_id= ""
	_configured_grace_period= ""
	_is_autodeploy= ""
	_violation_id= ""
	_check_type= ""
	_parent_name= ""
	_configured_time_window= ""
	_configured_threshold= ""
	_id= ""
	_enabled= ""
	_violation_name= ""
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
			return "waf_security_settings"
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
			return "waf_security_settingss"
		except Exception as e :
			raise e



	'''
	get Id of the parent resource
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id of the parent resource
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
	get time before a rule is auto deployed
	'''
	@property
	def configured_grace_period(self) :
		try:
			return self._configured_grace_period
		except Exception as e :
			raise e
	'''
	set time before a rule is auto deployed
	'''
	@configured_grace_period.setter
	def configured_grace_period(self,configured_grace_period):
		try :
			if not isinstance(configured_grace_period,long):
				raise TypeError("configured_grace_period must be set to long value")
			self._configured_grace_period = configured_grace_period
		except Exception as e :
			raise e


	'''
	get when TRUE NetScaler Console will deploy if user does not respond to alerts
	'''
	@property
	def is_autodeploy(self) :
		try:
			return self._is_autodeploy
		except Exception as e :
			raise e
	'''
	set when TRUE NetScaler Console will deploy if user does not respond to alerts
	'''
	@is_autodeploy.setter
	def is_autodeploy(self,is_autodeploy):
		try :
			if not isinstance(is_autodeploy,bool):
				raise TypeError("is_autodeploy must be set to bool value")
			self._is_autodeploy = is_autodeploy
		except Exception as e :
			raise e


	'''
	get NetScaler WAF Security checks have unique ID i.e violation_id
	'''
	@property
	def violation_id(self) :
		try:
			return self._violation_id
		except Exception as e :
			raise e
	'''
	set NetScaler WAF Security checks have unique ID i.e violation_id
	'''
	@violation_id.setter
	def violation_id(self,violation_id):
		try :
			if not isinstance(violation_id,int):
				raise TypeError("violation_id must be set to int value")
			self._violation_id = violation_id
		except Exception as e :
			raise e


	'''
	get Check type can be WAF Profile name based (0), Application name based (1), Rule removal (2) 
	'''
	@property
	def check_type(self) :
		try:
			return self._check_type
		except Exception as e :
			raise e
	'''
	set Check type can be WAF Profile name based (0), Application name based (1), Rule removal (2) 
	'''
	@check_type.setter
	def check_type(self,check_type):
		try :
			if not isinstance(check_type,int):
				raise TypeError("check_type must be set to int value")
			self._check_type = check_type
		except Exception as e :
			raise e


	'''
	get Resource name of parent resource
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Resource name of parent resource
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get time duration in seconds for which a rule's hit are accounted for in rule removal
	'''
	@property
	def configured_time_window(self) :
		try:
			return self._configured_time_window
		except Exception as e :
			raise e
	'''
	set time duration in seconds for which a rule's hit are accounted for in rule removal
	'''
	@configured_time_window.setter
	def configured_time_window(self,configured_time_window):
		try :
			if not isinstance(configured_time_window,long):
				raise TypeError("configured_time_window must be set to long value")
			self._configured_time_window = configured_time_window
		except Exception as e :
			raise e


	'''
	get the number of times a violation needs to occur for it to be ready to be deployed
	'''
	@property
	def configured_threshold(self) :
		try:
			return self._configured_threshold
		except Exception as e :
			raise e
	'''
	set the number of times a violation needs to occur for it to be ready to be deployed
	'''
	@configured_threshold.setter
	def configured_threshold(self,configured_threshold):
		try :
			if not isinstance(configured_threshold,long):
				raise TypeError("configured_threshold must be set to long value")
			self._configured_threshold = configured_threshold
		except Exception as e :
			raise e


	'''
	get Id is system generated key for WAF Profile - NetScaler map
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for WAF Profile - NetScaler map
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
	get TRUE when this Security check is enabled for Learning
	'''
	@property
	def enabled(self) :
		try:
			return self._enabled
		except Exception as e :
			raise e
	'''
	set TRUE when this Security check is enabled for Learning
	'''
	@enabled.setter
	def enabled(self,enabled):
		try :
			if not isinstance(enabled,bool):
				raise TypeError("enabled must be set to bool value")
			self._enabled = enabled
		except Exception as e :
			raise e


	'''
	get violation name used for each violation id
	'''
	@property
	def violation_name(self) :
		try:
			return self._violation_name
		except Exception as e :
			raise e
	'''
	set violation name used for each violation id
	'''
	@violation_name.setter
	def violation_name(self,violation_name):
		try :
			if not isinstance(violation_name,str):
				raise TypeError("violation_name must be set to str value")
			self._violation_name = violation_name
		except Exception as e :
			raise e

	'''
	Use this operation to display NetScaler IP - WAF Profile names.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				waf_security_settings_obj=waf_security_settings()
				response = waf_security_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler IP - WAF Profile names.
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
				waf_security_settings_obj=waf_security_settings()
				return cls.update_bulk_request(client,resource,waf_security_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of waf_security_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			waf_security_settings_obj = waf_security_settings()
			option_ = options()
			option_._filter=filter_
			return waf_security_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the waf_security_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			waf_security_settings_obj = waf_security_settings()
			option_ = options()
			option_._count=True
			response = waf_security_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of waf_security_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			waf_security_settings_obj = waf_security_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = waf_security_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(waf_security_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.waf_security_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(waf_security_settings_responses, response, "waf_security_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.waf_security_settings_response_array
				i=0
				error = [waf_security_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.waf_security_settings_response_array
			i=0
			waf_security_settings_objs = [waf_security_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_waf_security_settings'):
					for props in obj._waf_security_settings:
						result = service.payload_formatter.string_to_bulk_resource(waf_security_settings_response,self.__class__.__name__,props)
						waf_security_settings_objs[i] = result.waf_security_settings
						i=i+1
			return waf_security_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(waf_security_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class waf_security_settings_response(base_response):
	def __init__(self,length=1) :
		self.waf_security_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.waf_security_settings= [ waf_security_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class waf_security_settings_responses(base_response):
	def __init__(self,length=1) :
		self.waf_security_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.waf_security_settings_response_array = [ waf_security_settings() for _ in range(length)]
