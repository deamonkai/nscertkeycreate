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
Configuration for AF Bot profile counters table for Level 2 resource
'''

class af_bot_profile_counters_l2(base_resource):
	_bot_tot_log_profile= ""
	_prev_bot_tot_drop_profile= ""
	_bot_tot_drop_profile= ""
	_ctnsappname= ""
	_prev_bot_Requests_profile= ""
	_bot_tot_reset_profile= ""
	_bot_Requests_profile= ""
	_prev_bot_tot_redirect_profile= ""
	_prev_bot_tot_log_profile= ""
	_adc_time= ""
	_prev_bot_tot_reset_profile= ""
	_rpt_sample_time= ""
	_ip_address= ""
	_bot_tot_redirect_profile= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_bot_profile_counters_l2"
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
			return "af_bot_profile_counters_l2s"
		except Exception as e :
			raise e



	'''
	get Total number of bot profile logged.
	'''
	@property
	def bot_tot_log_profile(self) :
		try:
			return self._bot_tot_log_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile logged.
	'''
	@bot_tot_log_profile.setter
	def bot_tot_log_profile(self,bot_tot_log_profile):
		try :
			if not isinstance(bot_tot_log_profile,long):
				raise TypeError("bot_tot_log_profile must be set to long value")
			self._bot_tot_log_profile = bot_tot_log_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile dropped..
	'''
	@property
	def prev_bot_tot_drop_profile(self) :
		try:
			return self._prev_bot_tot_drop_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile dropped..
	'''
	@prev_bot_tot_drop_profile.setter
	def prev_bot_tot_drop_profile(self,prev_bot_tot_drop_profile):
		try :
			if not isinstance(prev_bot_tot_drop_profile,long):
				raise TypeError("prev_bot_tot_drop_profile must be set to long value")
			self._prev_bot_tot_drop_profile = prev_bot_tot_drop_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile dropped..
	'''
	@property
	def bot_tot_drop_profile(self) :
		try:
			return self._bot_tot_drop_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile dropped..
	'''
	@bot_tot_drop_profile.setter
	def bot_tot_drop_profile(self,bot_tot_drop_profile):
		try :
			if not isinstance(bot_tot_drop_profile,long):
				raise TypeError("bot_tot_drop_profile must be set to long value")
			self._bot_tot_drop_profile = bot_tot_drop_profile
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
	get Total number of bot profile requested.
	'''
	@property
	def prev_bot_Requests_profile(self) :
		try:
			return self._prev_bot_Requests_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile requested.
	'''
	@prev_bot_Requests_profile.setter
	def prev_bot_Requests_profile(self,prev_bot_Requests_profile):
		try :
			if not isinstance(prev_bot_Requests_profile,long):
				raise TypeError("prev_bot_Requests_profile must be set to long value")
			self._prev_bot_Requests_profile = prev_bot_Requests_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile reseted.
	'''
	@property
	def bot_tot_reset_profile(self) :
		try:
			return self._bot_tot_reset_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile reseted.
	'''
	@bot_tot_reset_profile.setter
	def bot_tot_reset_profile(self,bot_tot_reset_profile):
		try :
			if not isinstance(bot_tot_reset_profile,long):
				raise TypeError("bot_tot_reset_profile must be set to long value")
			self._bot_tot_reset_profile = bot_tot_reset_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile requested.
	'''
	@property
	def bot_Requests_profile(self) :
		try:
			return self._bot_Requests_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile requested.
	'''
	@bot_Requests_profile.setter
	def bot_Requests_profile(self,bot_Requests_profile):
		try :
			if not isinstance(bot_Requests_profile,long):
				raise TypeError("bot_Requests_profile must be set to long value")
			self._bot_Requests_profile = bot_Requests_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile redirected.
	'''
	@property
	def prev_bot_tot_redirect_profile(self) :
		try:
			return self._prev_bot_tot_redirect_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile redirected.
	'''
	@prev_bot_tot_redirect_profile.setter
	def prev_bot_tot_redirect_profile(self,prev_bot_tot_redirect_profile):
		try :
			if not isinstance(prev_bot_tot_redirect_profile,long):
				raise TypeError("prev_bot_tot_redirect_profile must be set to long value")
			self._prev_bot_tot_redirect_profile = prev_bot_tot_redirect_profile
		except Exception as e :
			raise e


	'''
	get Total number of bot profile logged.
	'''
	@property
	def prev_bot_tot_log_profile(self) :
		try:
			return self._prev_bot_tot_log_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile logged.
	'''
	@prev_bot_tot_log_profile.setter
	def prev_bot_tot_log_profile(self,prev_bot_tot_log_profile):
		try :
			if not isinstance(prev_bot_tot_log_profile,long):
				raise TypeError("prev_bot_tot_log_profile must be set to long value")
			self._prev_bot_tot_log_profile = prev_bot_tot_log_profile
		except Exception as e :
			raise e


	'''
	get NetScaler time.
	'''
	@property
	def adc_time(self) :
		try:
			return self._adc_time
		except Exception as e :
			raise e
	'''
	set NetScaler time.
	'''
	@adc_time.setter
	def adc_time(self,adc_time):
		try :
			if not isinstance(adc_time,long):
				raise TypeError("adc_time must be set to long value")
			self._adc_time = adc_time
		except Exception as e :
			raise e


	'''
	get Total number of bot profile reseted.
	'''
	@property
	def prev_bot_tot_reset_profile(self) :
		try:
			return self._prev_bot_tot_reset_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile reseted.
	'''
	@prev_bot_tot_reset_profile.setter
	def prev_bot_tot_reset_profile(self,prev_bot_tot_reset_profile):
		try :
			if not isinstance(prev_bot_tot_reset_profile,long):
				raise TypeError("prev_bot_tot_reset_profile must be set to long value")
			self._prev_bot_tot_reset_profile = prev_bot_tot_reset_profile
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
	get Total number of bot profile redirected.
	'''
	@property
	def bot_tot_redirect_profile(self) :
		try:
			return self._bot_tot_redirect_profile
		except Exception as e :
			raise e
	'''
	set Total number of bot profile redirected.
	'''
	@bot_tot_redirect_profile.setter
	def bot_tot_redirect_profile(self,bot_tot_redirect_profile):
		try :
			if not isinstance(bot_tot_redirect_profile,long):
				raise TypeError("bot_tot_redirect_profile must be set to long value")
			self._bot_tot_redirect_profile = bot_tot_redirect_profile
		except Exception as e :
			raise e

	'''
	Get all bot profile counters..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_bot_profile_counters_l2_obj=af_bot_profile_counters_l2()
				response = af_bot_profile_counters_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_bot_profile_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_bot_profile_counters_l2_obj = af_bot_profile_counters_l2()
			option_ = options()
			option_._filter=filter_
			return af_bot_profile_counters_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_bot_profile_counters_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_bot_profile_counters_l2_obj = af_bot_profile_counters_l2()
			option_ = options()
			option_._count=True
			response = af_bot_profile_counters_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_bot_profile_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_bot_profile_counters_l2_obj = af_bot_profile_counters_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_bot_profile_counters_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_bot_profile_counters_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_bot_profile_counters_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_bot_profile_counters_l2_responses, response, "af_bot_profile_counters_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_bot_profile_counters_l2_response_array
				i=0
				error = [af_bot_profile_counters_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_bot_profile_counters_l2_response_array
			i=0
			af_bot_profile_counters_l2_objs = [af_bot_profile_counters_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_bot_profile_counters_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_bot_profile_counters_l2_response,self.__class__.__name__,props)
					af_bot_profile_counters_l2_objs[i] = result.af_bot_profile_counters_l2
					i=i+1
			return af_bot_profile_counters_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_bot_profile_counters_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_bot_profile_counters_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_bot_profile_counters_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_bot_profile_counters_l2= [ af_bot_profile_counters_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_bot_profile_counters_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_bot_profile_counters_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_bot_profile_counters_l2_response_array = [ af_bot_profile_counters_l2() for _ in range(length)]
