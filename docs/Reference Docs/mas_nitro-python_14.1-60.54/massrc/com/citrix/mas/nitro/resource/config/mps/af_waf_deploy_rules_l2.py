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

class af_waf_deploy_rules_l2(base_resource):
	_field_type= ""
	_id= ""
	_failure_reason= ""
	_ctnsappname= ""
	_http_req_url= ""
	_violation_id= ""
	_profile_name= ""
	_field_name= ""
	_learning_mode= ""
	_value_type= ""
	_is_deployed= ""
	_count_value= ""
	_rpt_sample_time= ""
	_user_name= ""
	_violation_location= ""
	_adm_learn_profile_name= ""
	_max_value= ""
	_hits= ""
	_mode= ""
	_is_system= ""
	_value_expr= ""
	_lastpolltime= ""
	_min_value= ""
	_resourceid= ""
	_si_device_ip_address= ""
	_lasthittime= ""
	_status= ""
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
			return "af_waf_deploy_rules_l2"
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
			return "af_waf_deploy_rules_l2s"
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
	get Field used to help the user figure out point of failure for a rule
	'''
	@property
	def failure_reason(self) :
		try:
			return self._failure_reason
		except Exception as e :
			raise e
	'''
	set Field used to help the user figure out point of failure for a rule
	'''
	@failure_reason.setter
	def failure_reason(self,failure_reason):
		try :
			if not isinstance(failure_reason,str):
				raise TypeError("failure_reason must be set to str value")
			self._failure_reason = failure_reason
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
	get Number of hits for the relaxation rule in this appfw profile.
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	set Number of hits for the relaxation rule in this appfw profile.
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,int):
				raise TypeError("hits must be set to int value")
			self._hits = hits
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
	get Last Time polling was done to fetch hits
	'''
	@property
	def lastpolltime(self) :
		try:
			return self._lastpolltime
		except Exception as e :
			raise e
	'''
	set Last Time polling was done to fetch hits
	'''
	@lastpolltime.setter
	def lastpolltime(self,lastpolltime):
		try :
			if not isinstance(lastpolltime,long):
				raise TypeError("lastpolltime must be set to long value")
			self._lastpolltime = lastpolltime
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
	get Resourceid generated for each relaxation rule.
	'''
	@property
	def resourceid(self) :
		try:
			return self._resourceid
		except Exception as e :
			raise e
	'''
	set Resourceid generated for each relaxation rule.
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
	get Last hit for the relaxation rule in this appfw profile.
	'''
	@property
	def lasthittime(self) :
		try:
			return self._lasthittime
		except Exception as e :
			raise e
	'''
	set Last hit for the relaxation rule in this appfw profile.
	'''
	@lasthittime.setter
	def lasthittime(self,lasthittime):
		try :
			if not isinstance(lasthittime,long):
				raise TypeError("lasthittime must be set to long value")
			self._lasthittime = lasthittime
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
	WAF Learning engine Deployed rules.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				af_waf_deploy_rules_l2_obj=af_waf_deploy_rules_l2()
				response = af_waf_deploy_rules_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_waf_deploy_rules_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_waf_deploy_rules_l2_obj = af_waf_deploy_rules_l2()
			option_ = options()
			option_._filter=filter_
			return af_waf_deploy_rules_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_waf_deploy_rules_l2 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_waf_deploy_rules_l2_obj = af_waf_deploy_rules_l2()
			option_ = options()
			option_._count=True
			response = af_waf_deploy_rules_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_waf_deploy_rules_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_waf_deploy_rules_l2_obj = af_waf_deploy_rules_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_waf_deploy_rules_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_waf_deploy_rules_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_waf_deploy_rules_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_waf_deploy_rules_l2_responses, response, "af_waf_deploy_rules_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_waf_deploy_rules_l2_response_array
				i=0
				error = [af_waf_deploy_rules_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_waf_deploy_rules_l2_response_array
			i=0
			af_waf_deploy_rules_l2_objs = [af_waf_deploy_rules_l2() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_af_waf_deploy_rules_l2'):
					for props in obj._af_waf_deploy_rules_l2:
						result = service.payload_formatter.string_to_bulk_resource(af_waf_deploy_rules_l2_response,self.__class__.__name__,props)
						af_waf_deploy_rules_l2_objs[i] = result.af_waf_deploy_rules_l2
						i=i+1
			return af_waf_deploy_rules_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_waf_deploy_rules_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_waf_deploy_rules_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_waf_deploy_rules_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_waf_deploy_rules_l2= [ af_waf_deploy_rules_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_waf_deploy_rules_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_waf_deploy_rules_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_waf_deploy_rules_l2_response_array = [ af_waf_deploy_rules_l2() for _ in range(length)]
