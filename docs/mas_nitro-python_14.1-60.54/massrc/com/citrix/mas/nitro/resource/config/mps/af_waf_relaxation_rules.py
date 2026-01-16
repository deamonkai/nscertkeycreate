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
Configuration for WAF relaxation rules resource
'''

class af_waf_relaxation_rules(base_resource):
	_value_type= ""
	_learning_mode= ""
	_field_name= ""
	_grace_period= ""
	_is_deployed= ""
	_count_value= ""
	_is_auto_deploy= ""
	_user_name= ""
	_rpt_sample_time= ""
	_violation_location= ""
	_adm_learn_profile_name= ""
	_max_value= ""
	_is_system= ""
	_mode= ""
	_regex= ""
	_value_expr= ""
	_min_value= ""
	_resourceid= ""
	_sms_profile= ""
	_status= ""
	_si_device_ip_address= ""
	_field_type= ""
	_id= ""
	_mail_profile= ""
	_ctnsappname= ""
	_violation_id= ""
	_http_req_url= ""
	_slack_profile= ""
	_profile_name= ""
	_servicenow_profile= ""
	_grace_period_expiry= ""
	_comment= ""
	_no_of_violations= ""
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
			return "af_waf_relaxation_rules"
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
			return "af_waf_relaxation_ruless"
		except Exception as e :
			raise e



	'''
	get Value type to be relaxed
	'''
	@property
	def value_type(self) :
		try:
			return self._value_type
		except Exception as e :
			raise e
	'''
	set Value type to be relaxed
	'''
	@value_type.setter
	def value_type(self,value_type):
		try :
			if not isinstance(value_type,str):
				raise TypeError("value_type must be set to str value")
			self._value_type = value_type
		except Exception as e :
			raise e


	'''
	get Learning mode to differentate between a rule to be pruned (2) or deployed (0 or 1)
	'''
	@property
	def learning_mode(self) :
		try:
			return self._learning_mode
		except Exception as e :
			raise e
	'''
	set Learning mode to differentate between a rule to be pruned (2) or deployed (0 or 1)
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
	get Field name to be relaxed
	'''
	@property
	def field_name(self) :
		try:
			return self._field_name
		except Exception as e :
			raise e
	'''
	set Field name to be relaxed
	'''
	@field_name.setter
	def field_name(self,field_name):
		try :
			if not isinstance(field_name,str):
				raise TypeError("field_name must be set to str value")
			self._field_name = field_name
		except Exception as e :
			raise e


	'''
	get time before a rule is auto deployed
	'''
	@property
	def grace_period(self) :
		try:
			return self._grace_period
		except Exception as e :
			raise e
	'''
	set time before a rule is auto deployed
	'''
	@grace_period.setter
	def grace_period(self,grace_period):
		try :
			if not isinstance(grace_period,long):
				raise TypeError("grace_period must be set to long value")
			self._grace_period = grace_period
		except Exception as e :
			raise e


	'''
	get Field refelecting status of rule i.e 0-ready to deploy,1-deployed,2-skipped,4-failed
	'''
	@property
	def is_deployed(self) :
		try:
			return self._is_deployed
		except Exception as e :
			raise e
	'''
	set Field refelecting status of rule i.e 0-ready to deploy,1-deployed,2-skipped,4-failed
	'''
	@is_deployed.setter
	def is_deployed(self,is_deployed):
		try :
			if not isinstance(is_deployed,int):
				raise TypeError("is_deployed must be set to int value")
			self._is_deployed = is_deployed
		except Exception as e :
			raise e


	'''
	get count for the number of times this rule has caused violation
	'''
	@property
	def count_value(self) :
		try:
			return self._count_value
		except Exception as e :
			raise e
	'''
	set count for the number of times this rule has caused violation
	'''
	@count_value.setter
	def count_value(self,count_value):
		try :
			if not isinstance(count_value,int):
				raise TypeError("count_value must be set to int value")
			self._count_value = count_value
		except Exception as e :
			raise e


	'''
	get Field to check if auto deploying is ENABLED/DISABLED
	'''
	@property
	def is_auto_deploy(self) :
		try:
			return self._is_auto_deploy
		except Exception as e :
			raise e
	'''
	set Field to check if auto deploying is ENABLED/DISABLED
	'''
	@is_auto_deploy.setter
	def is_auto_deploy(self,is_auto_deploy):
		try :
			if not isinstance(is_auto_deploy,bool):
				raise TypeError("is_auto_deploy must be set to bool value")
			self._is_auto_deploy = is_auto_deploy
		except Exception as e :
			raise e


	'''
	get Field used to maintain the name of User who take an action that lead to this transaction record
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set Field used to maintain the name of User who take an action that lead to this transaction record
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
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Violation Location
	'''
	@property
	def violation_location(self) :
		try:
			return self._violation_location
		except Exception as e :
			raise e
	'''
	set Violation Location
	'''
	@violation_location.setter
	def violation_location(self,violation_location):
		try :
			if not isinstance(violation_location,int):
				raise TypeError("violation_location must be set to int value")
			self._violation_location = violation_location
		except Exception as e :
			raise e


	'''
	get adm_learn_profile_name
	'''
	@property
	def adm_learn_profile_name(self) :
		try:
			return self._adm_learn_profile_name
		except Exception as e :
			raise e
	'''
	set adm_learn_profile_name
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
	get Maximum length of the filed to be relaxed
	'''
	@property
	def max_value(self) :
		try:
			return self._max_value
		except Exception as e :
			raise e
	'''
	set Maximum length of the filed to be relaxed
	'''
	@max_value.setter
	def max_value(self,max_value):
		try :
			if not isinstance(max_value,int):
				raise TypeError("max_value must be set to int value")
			self._max_value = max_value
		except Exception as e :
			raise e


	'''
	get Set to true when system generated and false for user configured rule
	'''
	@property
	def is_system(self) :
		try:
			return self._is_system
		except Exception as e :
			raise e
	'''
	set Set to true when system generated and false for user configured rule
	'''
	@is_system.setter
	def is_system(self,is_system):
		try :
			if not isinstance(is_system,bool):
				raise TypeError("is_system must be set to bool value")
			self._is_system = is_system
		except Exception as e :
			raise e


	'''
	get Deployment mode would be OPEN(0) / CLOSE(1)
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set Deployment mode would be OPEN(0) / CLOSE(1)
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,int):
				raise TypeError("mode must be set to int value")
			self._mode = mode
		except Exception as e :
			raise e


	'''
	get Regex number 1 is REGEX and 2 is NOTREGEX in  bind appfw profile per security check
	'''
	@property
	def regex(self) :
		try:
			return self._regex
		except Exception as e :
			raise e
	'''
	set Regex number 1 is REGEX and 2 is NOTREGEX in  bind appfw profile per security check
	'''
	@regex.setter
	def regex(self,regex):
		try :
			if not isinstance(regex,int):
				raise TypeError("regex must be set to int value")
			self._regex = regex
		except Exception as e :
			raise e


	'''
	get Value expression to be relaxed
	'''
	@property
	def value_expr(self) :
		try:
			return self._value_expr
		except Exception as e :
			raise e
	'''
	set Value expression to be relaxed
	'''
	@value_expr.setter
	def value_expr(self,value_expr):
		try :
			if not isinstance(value_expr,str):
				raise TypeError("value_expr must be set to str value")
			self._value_expr = value_expr
		except Exception as e :
			raise e


	'''
	get minimum length of the field to be relaxed
	'''
	@property
	def min_value(self) :
		try:
			return self._min_value
		except Exception as e :
			raise e
	'''
	set minimum length of the field to be relaxed
	'''
	@min_value.setter
	def min_value(self,min_value):
		try :
			if not isinstance(min_value,int):
				raise TypeError("min_value must be set to int value")
			self._min_value = min_value
		except Exception as e :
			raise e


	'''
	get Resource Id generated for each relaxation rule which is bound to appfw profile.
	'''
	@property
	def resourceid(self) :
		try:
			return self._resourceid
		except Exception as e :
			raise e
	'''
	set Resource Id generated for each relaxation rule which is bound to appfw profile.
	'''
	@resourceid.setter
	def resourceid(self,resourceid):
		try :
			if not isinstance(resourceid,str):
				raise TypeError("resourceid must be set to str value")
			self._resourceid = resourceid
		except Exception as e :
			raise e


	'''
	get SMS Profile name
	'''
	@property
	def sms_profile(self) :
		try:
			return self._sms_profile
		except Exception as e :
			raise e
	'''
	set SMS Profile name
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
	get Status is true when the rule is enabled and false when the rule is disabled
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status is true when the rule is enabled and false when the rule is disabled
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,bool):
				raise TypeError("status must be set to bool value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address.
	'''
	@property
	def si_device_ip_address(self) :
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address.
	'''
	@si_device_ip_address.setter
	def si_device_ip_address(self,si_device_ip_address):
		try :
			if not isinstance(si_device_ip_address,str):
				raise TypeError("si_device_ip_address must be set to str value")
			self._si_device_ip_address = si_device_ip_address
		except Exception as e :
			raise e


	'''
	get Field type to be relaxed
	'''
	@property
	def field_type(self) :
		try:
			return self._field_type
		except Exception as e :
			raise e
	'''
	set Field type to be relaxed
	'''
	@field_type.setter
	def field_type(self,field_type):
		try :
			if not isinstance(field_type,str):
				raise TypeError("field_type must be set to str value")
			self._field_type = field_type
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
	get Mail Profile name
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail Profile name
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
	get ctnsappname
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set ctnsappname
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Violation Category
	'''
	@property
	def violation_id(self) :
		try:
			return self._violation_id
		except Exception as e :
			raise e
	'''
	set Violation Category
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
	get HTTP Request URL to be relaxed
	'''
	@property
	def http_req_url(self) :
		try:
			return self._http_req_url
		except Exception as e :
			raise e
	'''
	set HTTP Request URL to be relaxed
	'''
	@http_req_url.setter
	def http_req_url(self,http_req_url):
		try :
			if not isinstance(http_req_url,str):
				raise TypeError("http_req_url must be set to str value")
			self._http_req_url = http_req_url
		except Exception as e :
			raise e


	'''
	get Slack Profile name
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack Profile name
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
	get profile_name
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set profile_name
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
	get servicenow Profile name
	'''
	@property
	def servicenow_profile(self) :
		try:
			return self._servicenow_profile
		except Exception as e :
			raise e
	'''
	set servicenow Profile name
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
	Number of seconds left to trigger autodeploy for relaxation of URL
	'''
	@property
	def grace_period_expiry(self):
		try:
			return self._grace_period_expiry
		except Exception as e :
			raise e
	'''
	Number of seconds left to trigger autodeploy for relaxation of URL
	'''
	@grace_period_expiry.setter
	def grace_period_expiry(self,grace_period_expiry):
		try :
			if not isinstance(grace_period_expiry,long):
				raise TypeError("grace_period_expiry must be set to long value")
			self._grace_period_expiry = grace_period_expiry
		except Exception as e :
			raise e

	'''
	Comment to be added to a relaxation rule while deploying it
	'''
	@property
	def comment(self):
		try:
			return self._comment
		except Exception as e :
			raise e
	'''
	Comment to be added to a relaxation rule while deploying it
	'''
	@comment.setter
	def comment(self,comment):
		try :
			if not isinstance(comment,str):
				raise TypeError("comment must be set to str value")
			self._comment = comment
		except Exception as e :
			raise e

	'''
	Number of violations
	'''
	@property
	def no_of_violations(self):
		try:
			return self._no_of_violations
		except Exception as e :
			raise e
	'''
	Number of violations
	'''
	@no_of_violations.setter
	def no_of_violations(self,no_of_violations):
		try :
			if not isinstance(no_of_violations,long):
				raise TypeError("no_of_violations must be set to long value")
			self._no_of_violations = no_of_violations
		except Exception as e :
			raise e

	'''
	WAF Learning engine learnt rules.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				af_waf_relaxation_rules_obj=af_waf_relaxation_rules()
				response = af_waf_relaxation_rules_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
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
				af_waf_relaxation_rules_obj= af_waf_relaxation_rules()
				return cls.perform_operation_bulk_request(service,resource,af_waf_relaxation_rules_obj)
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
					af_waf_relaxation_rules_obj=af_waf_relaxation_rules()
					return cls.delete_bulk_request(client,resource,af_waf_relaxation_rules_obj)
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
				af_waf_relaxation_rules_obj=af_waf_relaxation_rules()
				return cls.update_bulk_request(client,resource,af_waf_relaxation_rules_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_waf_relaxation_rules resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_waf_relaxation_rules_obj = af_waf_relaxation_rules()
			option_ = options()
			option_._filter=filter_
			return af_waf_relaxation_rules_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_waf_relaxation_rules resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_waf_relaxation_rules_obj = af_waf_relaxation_rules()
			option_ = options()
			option_._count=True
			response = af_waf_relaxation_rules_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_waf_relaxation_rules resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_waf_relaxation_rules_obj = af_waf_relaxation_rules()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_waf_relaxation_rules_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_waf_relaxation_rules_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_waf_relaxation_rules
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_waf_relaxation_rules_responses, response, "af_waf_relaxation_rules_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_waf_relaxation_rules_response_array
				i=0
				error = [af_waf_relaxation_rules() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_waf_relaxation_rules_response_array
			i=0
			af_waf_relaxation_rules_objs = [af_waf_relaxation_rules() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_af_waf_relaxation_rules'):
					for props in obj._af_waf_relaxation_rules:
						result = service.payload_formatter.string_to_bulk_resource(af_waf_relaxation_rules_response,self.__class__.__name__,props)
						af_waf_relaxation_rules_objs[i] = result.af_waf_relaxation_rules
						i=i+1
			return af_waf_relaxation_rules_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_waf_relaxation_rules,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_waf_relaxation_rules_response(base_response):
	def __init__(self,length=1) :
		self.af_waf_relaxation_rules= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_waf_relaxation_rules= [ af_waf_relaxation_rules() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_waf_relaxation_rules_responses(base_response):
	def __init__(self,length=1) :
		self.af_waf_relaxation_rules_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_waf_relaxation_rules_response_array = [ af_waf_relaxation_rules() for _ in range(length)]
