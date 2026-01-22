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
Configuration for AF Profile Security data table for Level 3 resource
'''

class af_profile_safety_config_l3(base_resource):
	_none_flag= ""
	_exporter_id= ""
	_profile_sig_name= ""
	_sig_rule_logstring= ""
	_security_type= ""
	_ctnsappname= ""
	_block_flag= ""
	_appname= ""
	_log_flag= ""
	_learn_flag= ""
	_sig_rule_id= ""
	_ip_address= ""
	_stat_flag= ""
	_sig_rule_category= ""
	_rpt_sample_time= ""
	_profile_name= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_profile_safety_config_l3"
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
			return "af_profile_safety_config_l3s"
		except Exception as e :
			raise e



	'''
	get none_flag
	'''
	@property
	def none_flag(self) :
		try:
			return self._none_flag
		except Exception as e :
			raise e
	'''
	set none_flag
	'''
	@none_flag.setter
	def none_flag(self,none_flag):
		try :
			if not isinstance(none_flag,long):
				raise TypeError("none_flag must be set to long value")
			self._none_flag = none_flag
		except Exception as e :
			raise e


	'''
	get Exporter ID
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter ID
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get profile_sig_name
	'''
	@property
	def profile_sig_name(self) :
		try:
			return self._profile_sig_name
		except Exception as e :
			raise e
	'''
	set profile_sig_name
	'''
	@profile_sig_name.setter
	def profile_sig_name(self,profile_sig_name):
		try :
			if not isinstance(profile_sig_name,str):
				raise TypeError("profile_sig_name must be set to str value")
			self._profile_sig_name = profile_sig_name
		except Exception as e :
			raise e


	'''
	get signature rule logstring
	'''
	@property
	def sig_rule_logstring(self) :
		try:
			return self._sig_rule_logstring
		except Exception as e :
			raise e
	'''
	set signature rule logstring
	'''
	@sig_rule_logstring.setter
	def sig_rule_logstring(self,sig_rule_logstring):
		try :
			if not isinstance(sig_rule_logstring,str):
				raise TypeError("sig_rule_logstring must be set to str value")
			self._sig_rule_logstring = sig_rule_logstring
		except Exception as e :
			raise e


	'''
	get severity.
	'''
	@property
	def security_type(self) :
		try:
			return self._security_type
		except Exception as e :
			raise e
	'''
	set severity.
	'''
	@security_type.setter
	def security_type(self,security_type):
		try :
			if not isinstance(security_type,long):
				raise TypeError("security_type must be set to long value")
			self._security_type = security_type
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
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
	get block_flag.
	'''
	@property
	def block_flag(self) :
		try:
			return self._block_flag
		except Exception as e :
			raise e
	'''
	set block_flag.
	'''
	@block_flag.setter
	def block_flag(self,block_flag):
		try :
			if not isinstance(block_flag,long):
				raise TypeError("block_flag must be set to long value")
			self._block_flag = block_flag
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get log_flag.
	'''
	@property
	def log_flag(self) :
		try:
			return self._log_flag
		except Exception as e :
			raise e
	'''
	set log_flag.
	'''
	@log_flag.setter
	def log_flag(self,log_flag):
		try :
			if not isinstance(log_flag,long):
				raise TypeError("log_flag must be set to long value")
			self._log_flag = log_flag
		except Exception as e :
			raise e


	'''
	get learn_flag.
	'''
	@property
	def learn_flag(self) :
		try:
			return self._learn_flag
		except Exception as e :
			raise e
	'''
	set learn_flag.
	'''
	@learn_flag.setter
	def learn_flag(self,learn_flag):
		try :
			if not isinstance(learn_flag,long):
				raise TypeError("learn_flag must be set to long value")
			self._learn_flag = learn_flag
		except Exception as e :
			raise e


	'''
	get Signature Rule ID
	'''
	@property
	def sig_rule_id(self) :
		try:
			return self._sig_rule_id
		except Exception as e :
			raise e
	'''
	set Signature Rule ID
	'''
	@sig_rule_id.setter
	def sig_rule_id(self,sig_rule_id):
		try :
			if not isinstance(sig_rule_id,long):
				raise TypeError("sig_rule_id must be set to long value")
			self._sig_rule_id = sig_rule_id
		except Exception as e :
			raise e


	'''
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
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
	get stat_flag
	'''
	@property
	def stat_flag(self) :
		try:
			return self._stat_flag
		except Exception as e :
			raise e
	'''
	set stat_flag
	'''
	@stat_flag.setter
	def stat_flag(self,stat_flag):
		try :
			if not isinstance(stat_flag,long):
				raise TypeError("stat_flag must be set to long value")
			self._stat_flag = stat_flag
		except Exception as e :
			raise e


	'''
	get signature rule category
	'''
	@property
	def sig_rule_category(self) :
		try:
			return self._sig_rule_category
		except Exception as e :
			raise e
	'''
	set signature rule category
	'''
	@sig_rule_category.setter
	def sig_rule_category(self,sig_rule_category):
		try :
			if not isinstance(sig_rule_category,str):
				raise TypeError("sig_rule_category must be set to str value")
			self._sig_rule_category = sig_rule_category
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
	Af Report for Saftey Index Data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_profile_safety_config_l3_obj=af_profile_safety_config_l3()
				response = af_profile_safety_config_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_profile_safety_config_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_profile_safety_config_l3_obj = af_profile_safety_config_l3()
			option_ = options()
			option_._filter=filter_
			return af_profile_safety_config_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_profile_safety_config_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_profile_safety_config_l3_obj = af_profile_safety_config_l3()
			option_ = options()
			option_._count=True
			response = af_profile_safety_config_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_profile_safety_config_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_profile_safety_config_l3_obj = af_profile_safety_config_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_profile_safety_config_l3_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_profile_safety_config_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_profile_safety_config_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_profile_safety_config_l3_responses, response, "af_profile_safety_config_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_profile_safety_config_l3_response_array
				i=0
				error = [af_profile_safety_config_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_profile_safety_config_l3_response_array
			i=0
			af_profile_safety_config_l3_objs = [af_profile_safety_config_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_profile_safety_config_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_profile_safety_config_l3_response,self.__class__.__name__,props)
					af_profile_safety_config_l3_objs[i] = result.af_profile_safety_config_l3
					i=i+1
			return af_profile_safety_config_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_profile_safety_config_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_profile_safety_config_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_profile_safety_config_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_profile_safety_config_l3= [ af_profile_safety_config_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_profile_safety_config_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_profile_safety_config_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_profile_safety_config_l3_response_array = [ af_profile_safety_config_l3() for _ in range(length)]
