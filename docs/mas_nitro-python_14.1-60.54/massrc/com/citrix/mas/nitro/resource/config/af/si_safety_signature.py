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

from massrc.com.citrix.mas.nitro.resource.config.mps.af_generic_api import af_generic_api

'''
Configuration for AF Safety Data Report table resource
'''

class si_safety_signature(af_generic_api):
	_configuration= ""
	_sig_rule_id= ""
	_si_app_unit_name= ""
	_sig_log_count= ""
	_sig_sig_name= ""
	_sig_stat_count= ""
	_profile_safety_index= ""
	_sig_rule_category= ""
	_sig_rule_logstring= ""
	_id= ""
	_sig_block= ""
	_sig_log= ""
	_sig_safety_index= ""
	_name= ""
	_profile_not_block_count= ""
	_si_device_ip_address= ""
	_profile_sig_disable_count= ""
	_sig_block_count= ""
	_sig_none= ""
	_sig_learn= ""
	_sig_stat= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_safety_signature"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_safety_signature,self).get_object_id()
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
			return "si_safety_signatures"
		except Exception as e :
			raise e


	'''
	Profile Security configuration
	'''
	@property
	def configuration(self):
		try:
			return self._configuration
		except Exception as e :
			raise e
	'''
	Profile Security configuration
	'''
	@configuration.setter
	def configuration(self,configuration):
		try :
			if not isinstance(configuration,str):
				raise TypeError("configuration must be set to str value")
			self._configuration = configuration
		except Exception as e :
			raise e

	'''
	Signature Rule Id
	'''
	@property
	def sig_rule_id(self):
		try:
			return self._sig_rule_id
		except Exception as e :
			raise e
	'''
	Signature Rule Id
	'''
	@sig_rule_id.setter
	def sig_rule_id(self,sig_rule_id):
		try :
			if not isinstance(sig_rule_id,float):
				raise TypeError("sig_rule_id must be set to float value")
			self._sig_rule_id = sig_rule_id
		except Exception as e :
			raise e

	'''
	AppName
	'''
	@property
	def si_app_unit_name(self):
		try:
			return self._si_app_unit_name
		except Exception as e :
			raise e
	'''
	AppName
	'''
	@si_app_unit_name.setter
	def si_app_unit_name(self,si_app_unit_name):
		try :
			if not isinstance(si_app_unit_name,str):
				raise TypeError("si_app_unit_name must be set to str value")
			self._si_app_unit_name = si_app_unit_name
		except Exception as e :
			raise e

	'''
	Count of Signature Logs
	'''
	@property
	def sig_log_count(self):
		try:
			return self._sig_log_count
		except Exception as e :
			raise e
	'''
	Count of Signature Logs
	'''
	@sig_log_count.setter
	def sig_log_count(self,sig_log_count):
		try :
			if not isinstance(sig_log_count,float):
				raise TypeError("sig_log_count must be set to float value")
			self._sig_log_count = sig_log_count
		except Exception as e :
			raise e

	'''
	Profile signature name
	'''
	@property
	def sig_sig_name(self):
		try:
			return self._sig_sig_name
		except Exception as e :
			raise e
	'''
	Profile signature name
	'''
	@sig_sig_name.setter
	def sig_sig_name(self,sig_sig_name):
		try :
			if not isinstance(sig_sig_name,str):
				raise TypeError("sig_sig_name must be set to str value")
			self._sig_sig_name = sig_sig_name
		except Exception as e :
			raise e

	'''
	Count of Signature Stats.
	'''
	@property
	def sig_stat_count(self):
		try:
			return self._sig_stat_count
		except Exception as e :
			raise e
	'''
	Count of Signature Stats.
	'''
	@sig_stat_count.setter
	def sig_stat_count(self,sig_stat_count):
		try :
			if not isinstance(sig_stat_count,float):
				raise TypeError("sig_stat_count must be set to float value")
			self._sig_stat_count = sig_stat_count
		except Exception as e :
			raise e

	'''
	Profile Safety Index.
	'''
	@property
	def profile_safety_index(self):
		try:
			return self._profile_safety_index
		except Exception as e :
			raise e
	'''
	Profile Safety Index.
	'''
	@profile_safety_index.setter
	def profile_safety_index(self,profile_safety_index):
		try :
			if not isinstance(profile_safety_index,float):
				raise TypeError("profile_safety_index must be set to float value")
			self._profile_safety_index = profile_safety_index
		except Exception as e :
			raise e

	'''
	Profile sig_rule_category
	'''
	@property
	def sig_rule_category(self):
		try:
			return self._sig_rule_category
		except Exception as e :
			raise e
	'''
	Profile sig_rule_category
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
	Profile sig_rule_logstring
	'''
	@property
	def sig_rule_logstring(self):
		try:
			return self._sig_rule_logstring
		except Exception as e :
			raise e
	'''
	Profile sig_rule_logstring
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
	Id is safety profile
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is safety profile
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
	Signature Block Flags.
	'''
	@property
	def sig_block(self):
		try:
			return self._sig_block
		except Exception as e :
			raise e
	'''
	Signature Block Flags.
	'''
	@sig_block.setter
	def sig_block(self,sig_block):
		try :
			if not isinstance(sig_block,float):
				raise TypeError("sig_block must be set to float value")
			self._sig_block = sig_block
		except Exception as e :
			raise e

	'''
	Signature Log Flag.
	'''
	@property
	def sig_log(self):
		try:
			return self._sig_log
		except Exception as e :
			raise e
	'''
	Signature Log Flag.
	'''
	@sig_log.setter
	def sig_log(self,sig_log):
		try :
			if not isinstance(sig_log,float):
				raise TypeError("sig_log must be set to float value")
			self._sig_log = sig_log
		except Exception as e :
			raise e

	'''
	Signature Safety Index.
	'''
	@property
	def sig_safety_index(self):
		try:
			return self._sig_safety_index
		except Exception as e :
			raise e
	'''
	Signature Safety Index.
	'''
	@sig_safety_index.setter
	def sig_safety_index(self,sig_safety_index):
		try :
			if not isinstance(sig_safety_index,float):
				raise TypeError("sig_safety_index must be set to float value")
			self._sig_safety_index = sig_safety_index
		except Exception as e :
			raise e

	'''
	Profile Name
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Profile Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e

	'''
	Count of Blocked Profile.
	'''
	@property
	def profile_not_block_count(self):
		try:
			return self._profile_not_block_count
		except Exception as e :
			raise e
	'''
	Count of Blocked Profile.
	'''
	@profile_not_block_count.setter
	def profile_not_block_count(self,profile_not_block_count):
		try :
			if not isinstance(profile_not_block_count,float):
				raise TypeError("profile_not_block_count must be set to float value")
			self._profile_not_block_count = profile_not_block_count
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def si_device_ip_address(self):
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
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
	Count of Disabled Profile Signatures.
	'''
	@property
	def profile_sig_disable_count(self):
		try:
			return self._profile_sig_disable_count
		except Exception as e :
			raise e
	'''
	Count of Disabled Profile Signatures.
	'''
	@profile_sig_disable_count.setter
	def profile_sig_disable_count(self,profile_sig_disable_count):
		try :
			if not isinstance(profile_sig_disable_count,float):
				raise TypeError("profile_sig_disable_count must be set to float value")
			self._profile_sig_disable_count = profile_sig_disable_count
		except Exception as e :
			raise e

	'''
	Count of Blocked Signatures
	'''
	@property
	def sig_block_count(self):
		try:
			return self._sig_block_count
		except Exception as e :
			raise e
	'''
	Count of Blocked Signatures
	'''
	@sig_block_count.setter
	def sig_block_count(self,sig_block_count):
		try :
			if not isinstance(sig_block_count,float):
				raise TypeError("sig_block_count must be set to float value")
			self._sig_block_count = sig_block_count
		except Exception as e :
			raise e

	'''
	Signature None Flags.
	'''
	@property
	def sig_none(self):
		try:
			return self._sig_none
		except Exception as e :
			raise e
	'''
	Signature None Flags.
	'''
	@sig_none.setter
	def sig_none(self,sig_none):
		try :
			if not isinstance(sig_none,float):
				raise TypeError("sig_none must be set to float value")
			self._sig_none = sig_none
		except Exception as e :
			raise e

	'''
	Signature Learn Flag.
	'''
	@property
	def sig_learn(self):
		try:
			return self._sig_learn
		except Exception as e :
			raise e
	'''
	Signature Learn Flag.
	'''
	@sig_learn.setter
	def sig_learn(self,sig_learn):
		try :
			if not isinstance(sig_learn,float):
				raise TypeError("sig_learn must be set to float value")
			self._sig_learn = sig_learn
		except Exception as e :
			raise e

	'''
	Signature Stats.
	'''
	@property
	def sig_stat(self):
		try:
			return self._sig_stat
		except Exception as e :
			raise e
	'''
	Signature Stats.
	'''
	@sig_stat.setter
	def sig_stat(self,sig_stat):
		try :
			if not isinstance(sig_stat,float):
				raise TypeError("sig_stat must be set to float value")
			self._sig_stat = sig_stat
		except Exception as e :
			raise e

	'''
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	Af Report for Security Insight Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_safety_signature_obj=si_safety_signature()
				response = si_safety_signature_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_safety_signature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_safety_signature_obj = si_safety_signature()
			option_ = options()
			option_._filter=filter_
			return si_safety_signature_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_safety_signature resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_safety_signature_obj = si_safety_signature()
			option_ = options()
			option_._count=True
			response = si_safety_signature_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_safety_signature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_safety_signature_obj = si_safety_signature()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_safety_signature_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_signature_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_safety_signature
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_safety_signature_responses, response, "si_safety_signature_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_safety_signature_response_array
				i=0
				error = [si_safety_signature() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_safety_signature_response_array
			i=0
			si_safety_signature_objs = [si_safety_signature() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_safety_signature:
					result = service.payload_formatter.string_to_bulk_resource(si_safety_signature_response,self.__class__.__name__,props)
					si_safety_signature_objs[i] = result.si_safety_signature
					i=i+1
			return si_safety_signature_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_safety_signature,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_safety_signature_response(base_response):
	def __init__(self,length=1) :
		self.si_safety_signature= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_safety_signature= [ si_safety_signature() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_safety_signature_responses(base_response):
	def __init__(self,length=1) :
		self.si_safety_signature_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_safety_signature_response_array = [ si_safety_signature() for _ in range(length)]
