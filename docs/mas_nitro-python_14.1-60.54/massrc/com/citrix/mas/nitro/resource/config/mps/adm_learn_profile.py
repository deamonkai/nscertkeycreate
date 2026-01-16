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
from massrc.com.citrix.mas.nitro.resource.config.mps.waf_profile_devices import waf_profile_devices
from massrc.com.citrix.mas.nitro.resource.config.mps.waf_security_settings import waf_security_settings


'''
Configuration for NetScaler Console WAF Profile to manage learning groups resource
'''

class adm_learn_profile(base_resource):
	_id= ""
	_enabled= ""
	_learning_mode= ""
	_adm_learn_profile_name= ""
	_mail_profile= ""
	_slack_profile= ""
	_waf_profile_devices_info=[]
	_servicenow_profile= ""
	_sms_profile= ""
	_no_of_deployed_rules= ""
	_no_of_learned_rules= ""
	_waf_security_settings_info=[]
	_no_of_waf= ""
	_no_of_adc= ""
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
			return "adm_learn_profile"
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
			return "adm_learn_profiles"
		except Exception as e :
			raise e



	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get enable learning on this profile
	'''
	@property
	def enabled(self) :
		try:
			return self._enabled
		except Exception as e :
			raise e
	'''
	set enable learning on this profile
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
	get WAF Learning modes can be WAF Profile name based (0), Application name based (1), Rule removal (2), Hybrid (3) 
	'''
	@property
	def learning_mode(self) :
		try:
			return self._learning_mode
		except Exception as e :
			raise e
	'''
	set WAF Learning modes can be WAF Profile name based (0), Application name based (1), Rule removal (2), Hybrid (3) 
	'''
	@learning_mode.setter
	def learning_mode(self,learning_mode):
		try :
			if not isinstance(learning_mode,int):
				raise TypeError("learning_mode must be set to int value")
			self._learning_mode = learning_mode
		except Exception as e :
			raise e


	'''
	get Profile Name used for naming a learning group
	'''
	@property
	def adm_learn_profile_name(self) :
		try:
			return self._adm_learn_profile_name
		except Exception as e :
			raise e
	'''
	set Profile Name used for naming a learning group
	'''
	@adm_learn_profile_name.setter
	def adm_learn_profile_name(self,adm_learn_profile_name):
		try :
			if not isinstance(adm_learn_profile_name,str):
				raise TypeError("adm_learn_profile_name must be set to str value")
			self._adm_learn_profile_name = adm_learn_profile_name
		except Exception as e :
			raise e


	'''
	get Mail Profile
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail Profile
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
	get Slack Profile
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack Profile
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
	get Mapping NetScaler IPs to WAF Profiles
	'''
	@property
	def waf_profile_devices_info(self) :
		try:
			return self._waf_profile_devices_info
		except Exception as e :
			raise e
	'''
	set Mapping NetScaler IPs to WAF Profiles
	'''
	@waf_profile_devices_info.setter
	def waf_profile_devices_info(self,waf_profile_devices_info) :
		try :
			if not isinstance(waf_profile_devices_info,list):
				raise TypeError("waf_profile_devices_info must be set to array of waf_profile_devices value")
			for item in waf_profile_devices_info :
				if not isinstance(item,waf_profile_devices):
					raise TypeError("item must be set to waf_profile_devices value")
			self._waf_profile_devices_info = waf_profile_devices_info
		except Exception as e :
			raise e


	'''
	get ServiceNow Profile Name
	'''
	@property
	def servicenow_profile(self) :
		try:
			return self._servicenow_profile
		except Exception as e :
			raise e
	'''
	set ServiceNow Profile Name
	'''
	@servicenow_profile.setter
	def servicenow_profile(self,servicenow_profile):
		try :
			if not isinstance(servicenow_profile,str):
				raise TypeError("servicenow_profile must be set to str value")
			self._servicenow_profile = servicenow_profile
		except Exception as e :
			raise e


	'''
	get SMS Profile
	'''
	@property
	def sms_profile(self) :
		try:
			return self._sms_profile
		except Exception as e :
			raise e
	'''
	set SMS Profile
	'''
	@sms_profile.setter
	def sms_profile(self,sms_profile):
		try :
			if not isinstance(sms_profile,str):
				raise TypeError("sms_profile must be set to str value")
			self._sms_profile = sms_profile
		except Exception as e :
			raise e


	'''
	get Number of WAF Profile names configured
	'''
	@property
	def no_of_deployed_rules(self) :
		try:
			return self._no_of_deployed_rules
		except Exception as e :
			raise e
	'''
	set Number of WAF Profile names configured
	'''
	@no_of_deployed_rules.setter
	def no_of_deployed_rules(self,no_of_deployed_rules):
		try :
			if not isinstance(no_of_deployed_rules,int):
				raise TypeError("no_of_deployed_rules must be set to int value")
			self._no_of_deployed_rules = no_of_deployed_rules
		except Exception as e :
			raise e


	'''
	get Number of WAF Profile names configured
	'''
	@property
	def no_of_learned_rules(self) :
		try:
			return self._no_of_learned_rules
		except Exception as e :
			raise e
	'''
	set Number of WAF Profile names configured
	'''
	@no_of_learned_rules.setter
	def no_of_learned_rules(self,no_of_learned_rules):
		try :
			if not isinstance(no_of_learned_rules,int):
				raise TypeError("no_of_learned_rules must be set to int value")
			self._no_of_learned_rules = no_of_learned_rules
		except Exception as e :
			raise e


	'''
	get WAF Security Checks Settings info
	'''
	@property
	def waf_security_settings_info(self) :
		try:
			return self._waf_security_settings_info
		except Exception as e :
			raise e
	'''
	set WAF Security Checks Settings info
	'''
	@waf_security_settings_info.setter
	def waf_security_settings_info(self,waf_security_settings_info) :
		try :
			if not isinstance(waf_security_settings_info,list):
				raise TypeError("waf_security_settings_info must be set to array of waf_security_settings value")
			for item in waf_security_settings_info :
				if not isinstance(item,waf_security_settings):
					raise TypeError("item must be set to waf_security_settings value")
			self._waf_security_settings_info = waf_security_settings_info
		except Exception as e :
			raise e

	'''
	Number of WAF Profile names configured
	'''
	@property
	def no_of_waf(self):
		try:
			return self._no_of_waf
		except Exception as e :
			raise e
	'''
	Number of WAF Profile names configured
	'''
	@no_of_waf.setter
	def no_of_waf(self,no_of_waf):
		try :
			if not isinstance(no_of_waf,int):
				raise TypeError("no_of_waf must be set to int value")
			self._no_of_waf = no_of_waf
		except Exception as e :
			raise e

	'''
	Number of ADCs
	'''
	@property
	def no_of_adc(self):
		try:
			return self._no_of_adc
		except Exception as e :
			raise e
	'''
	Number of ADCs
	'''
	@no_of_adc.setter
	def no_of_adc(self,no_of_adc):
		try :
			if not isinstance(no_of_adc,int):
				raise TypeError("no_of_adc must be set to int value")
			self._no_of_adc = no_of_adc
		except Exception as e :
			raise e

	'''
	Use this operation to delete NetScaler Console Learn Profile.
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
					adm_learn_profile_obj=adm_learn_profile()
					return cls.delete_bulk_request(client,resource,adm_learn_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler Console Learn profile.
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
				adm_learn_profile_obj=adm_learn_profile()
				return cls.update_bulk_request(client,resource,adm_learn_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add NetScaler Console Learn profile.
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
				adm_learn_profile_obj= adm_learn_profile()
				return cls.perform_operation_bulk_request(service,resource,adm_learn_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Console Learn Profile.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adm_learn_profile_obj=adm_learn_profile()
				response = adm_learn_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adm_learn_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adm_learn_profile_obj = adm_learn_profile()
			option_ = options()
			option_._filter=filter_
			return adm_learn_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adm_learn_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adm_learn_profile_obj = adm_learn_profile()
			option_ = options()
			option_._count=True
			response = adm_learn_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adm_learn_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adm_learn_profile_obj = adm_learn_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adm_learn_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adm_learn_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adm_learn_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_learn_profile_responses, response, "adm_learn_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adm_learn_profile_response_array
				i=0
				error = [adm_learn_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adm_learn_profile_response_array
			i=0
			adm_learn_profile_objs = [adm_learn_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adm_learn_profile'):
					for props in obj._adm_learn_profile:
						result = service.payload_formatter.string_to_bulk_resource(adm_learn_profile_response,self.__class__.__name__,props)
						adm_learn_profile_objs[i] = result.adm_learn_profile
						i=i+1
			return adm_learn_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adm_learn_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adm_learn_profile_response(base_response):
	def __init__(self,length=1) :
		self.adm_learn_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adm_learn_profile= [ adm_learn_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adm_learn_profile_responses(base_response):
	def __init__(self,length=1) :
		self.adm_learn_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adm_learn_profile_response_array = [ adm_learn_profile() for _ in range(length)]
