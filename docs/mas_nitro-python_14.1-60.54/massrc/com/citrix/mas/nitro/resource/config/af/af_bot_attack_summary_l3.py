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
Configuration for AF Bot Attack summary table for Level 3 resource
'''

class af_bot_attack_summary_l3(base_resource):
	_backend_appname= ""
	_bot_severity= ""
	_action_flags= ""
	_total_fingerprinted_bots= ""
	_total_tps_bots= ""
	_appname= ""
	_total_ratebased_bots= ""
	_total_honeytrap_bots= ""
	_ctnsappname= ""
	_backend_vserver= ""
	_total_human_browsers= ""
	_total_signatured_bots= ""
	_rpt_sample_time= ""
	_total_ipreputation_bots= ""
	_total_blacklist_bots= ""
	_total_whitelist_bots= ""
	_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_bot_attack_summary_l3"
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
			return "af_bot_attack_summary_l3s"
		except Exception as e :
			raise e



	'''
	get Backend AppName
	'''
	@property
	def backend_appname(self) :
		try:
			return self._backend_appname
		except Exception as e :
			raise e
	'''
	set Backend AppName
	'''
	@backend_appname.setter
	def backend_appname(self,backend_appname):
		try :
			if not isinstance(backend_appname,str):
				raise TypeError("backend_appname must be set to str value")
			self._backend_appname = backend_appname
		except Exception as e :
			raise e


	'''
	get Bot Severity.
	'''
	@property
	def bot_severity(self) :
		try:
			return self._bot_severity
		except Exception as e :
			raise e
	'''
	set Bot Severity.
	'''
	@bot_severity.setter
	def bot_severity(self,bot_severity):
		try :
			if not isinstance(bot_severity,int):
				raise TypeError("bot_severity must be set to int value")
			self._bot_severity = bot_severity
		except Exception as e :
			raise e


	'''
	get action_flags.
	'''
	@property
	def action_flags(self) :
		try:
			return self._action_flags
		except Exception as e :
			raise e
	'''
	set action_flags.
	'''
	@action_flags.setter
	def action_flags(self,action_flags):
		try :
			if not isinstance(action_flags,long):
				raise TypeError("action_flags must be set to long value")
			self._action_flags = action_flags
		except Exception as e :
			raise e


	'''
	get Total Fingerprinted Bots.
	'''
	@property
	def total_fingerprinted_bots(self) :
		try:
			return self._total_fingerprinted_bots
		except Exception as e :
			raise e
	'''
	set Total Fingerprinted Bots.
	'''
	@total_fingerprinted_bots.setter
	def total_fingerprinted_bots(self,total_fingerprinted_bots):
		try :
			if not isinstance(total_fingerprinted_bots,long):
				raise TypeError("total_fingerprinted_bots must be set to long value")
			self._total_fingerprinted_bots = total_fingerprinted_bots
		except Exception as e :
			raise e


	'''
	get Total TPS Bots.
	'''
	@property
	def total_tps_bots(self) :
		try:
			return self._total_tps_bots
		except Exception as e :
			raise e
	'''
	set Total TPS Bots.
	'''
	@total_tps_bots.setter
	def total_tps_bots(self,total_tps_bots):
		try :
			if not isinstance(total_tps_bots,long):
				raise TypeError("total_tps_bots must be set to long value")
			self._total_tps_bots = total_tps_bots
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
	get Total RateBased Bots.
	'''
	@property
	def total_ratebased_bots(self) :
		try:
			return self._total_ratebased_bots
		except Exception as e :
			raise e
	'''
	set Total RateBased Bots.
	'''
	@total_ratebased_bots.setter
	def total_ratebased_bots(self,total_ratebased_bots):
		try :
			if not isinstance(total_ratebased_bots,long):
				raise TypeError("total_ratebased_bots must be set to long value")
			self._total_ratebased_bots = total_ratebased_bots
		except Exception as e :
			raise e


	'''
	get Total HoneyTrap Bots.
	'''
	@property
	def total_honeytrap_bots(self) :
		try:
			return self._total_honeytrap_bots
		except Exception as e :
			raise e
	'''
	set Total HoneyTrap Bots.
	'''
	@total_honeytrap_bots.setter
	def total_honeytrap_bots(self,total_honeytrap_bots):
		try :
			if not isinstance(total_honeytrap_bots,long):
				raise TypeError("total_honeytrap_bots must be set to long value")
			self._total_honeytrap_bots = total_honeytrap_bots
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
	get Backend vserver name.
	'''
	@property
	def backend_vserver(self) :
		try:
			return self._backend_vserver
		except Exception as e :
			raise e
	'''
	set Backend vserver name.
	'''
	@backend_vserver.setter
	def backend_vserver(self,backend_vserver):
		try :
			if not isinstance(backend_vserver,str):
				raise TypeError("backend_vserver must be set to str value")
			self._backend_vserver = backend_vserver
		except Exception as e :
			raise e


	'''
	get Total Human Browsers.
	'''
	@property
	def total_human_browsers(self) :
		try:
			return self._total_human_browsers
		except Exception as e :
			raise e
	'''
	set Total Human Browsers.
	'''
	@total_human_browsers.setter
	def total_human_browsers(self,total_human_browsers):
		try :
			if not isinstance(total_human_browsers,long):
				raise TypeError("total_human_browsers must be set to long value")
			self._total_human_browsers = total_human_browsers
		except Exception as e :
			raise e


	'''
	get Total Signatured Bots.
	'''
	@property
	def total_signatured_bots(self) :
		try:
			return self._total_signatured_bots
		except Exception as e :
			raise e
	'''
	set Total Signatured Bots.
	'''
	@total_signatured_bots.setter
	def total_signatured_bots(self,total_signatured_bots):
		try :
			if not isinstance(total_signatured_bots,long):
				raise TypeError("total_signatured_bots must be set to long value")
			self._total_signatured_bots = total_signatured_bots
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
	get Total IP Reputation Bots.
	'''
	@property
	def total_ipreputation_bots(self) :
		try:
			return self._total_ipreputation_bots
		except Exception as e :
			raise e
	'''
	set Total IP Reputation Bots.
	'''
	@total_ipreputation_bots.setter
	def total_ipreputation_bots(self,total_ipreputation_bots):
		try :
			if not isinstance(total_ipreputation_bots,long):
				raise TypeError("total_ipreputation_bots must be set to long value")
			self._total_ipreputation_bots = total_ipreputation_bots
		except Exception as e :
			raise e


	'''
	get Total BlackList Bots.
	'''
	@property
	def total_blacklist_bots(self) :
		try:
			return self._total_blacklist_bots
		except Exception as e :
			raise e
	'''
	set Total BlackList Bots.
	'''
	@total_blacklist_bots.setter
	def total_blacklist_bots(self,total_blacklist_bots):
		try :
			if not isinstance(total_blacklist_bots,long):
				raise TypeError("total_blacklist_bots must be set to long value")
			self._total_blacklist_bots = total_blacklist_bots
		except Exception as e :
			raise e


	'''
	get Total WhiteList Bots.
	'''
	@property
	def total_whitelist_bots(self) :
		try:
			return self._total_whitelist_bots
		except Exception as e :
			raise e
	'''
	set Total WhiteList Bots.
	'''
	@total_whitelist_bots.setter
	def total_whitelist_bots(self,total_whitelist_bots):
		try :
			if not isinstance(total_whitelist_bots,long):
				raise TypeError("total_whitelist_bots must be set to long value")
			self._total_whitelist_bots = total_whitelist_bots
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
	Af Report for Bot Attack Summary..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_bot_attack_summary_l3_obj=af_bot_attack_summary_l3()
				response = af_bot_attack_summary_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_bot_attack_summary_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_bot_attack_summary_l3_obj = af_bot_attack_summary_l3()
			option_ = options()
			option_._filter=filter_
			return af_bot_attack_summary_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_bot_attack_summary_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_bot_attack_summary_l3_obj = af_bot_attack_summary_l3()
			option_ = options()
			option_._count=True
			response = af_bot_attack_summary_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_bot_attack_summary_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_bot_attack_summary_l3_obj = af_bot_attack_summary_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_bot_attack_summary_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_bot_attack_summary_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_bot_attack_summary_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_bot_attack_summary_l3_responses, response, "af_bot_attack_summary_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_bot_attack_summary_l3_response_array
				i=0
				error = [af_bot_attack_summary_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_bot_attack_summary_l3_response_array
			i=0
			af_bot_attack_summary_l3_objs = [af_bot_attack_summary_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_bot_attack_summary_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_bot_attack_summary_l3_response,self.__class__.__name__,props)
					af_bot_attack_summary_l3_objs[i] = result.af_bot_attack_summary_l3
					i=i+1
			return af_bot_attack_summary_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_bot_attack_summary_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_bot_attack_summary_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_bot_attack_summary_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_bot_attack_summary_l3= [ af_bot_attack_summary_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_bot_attack_summary_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_bot_attack_summary_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_bot_attack_summary_l3_response_array = [ af_bot_attack_summary_l3() for _ in range(length)]
