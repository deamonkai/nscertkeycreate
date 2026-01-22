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
Configuration for AF Policy Hits Counter Report for Level 2 resource
'''

class af_policy_hits_counter_l2(base_resource):
	_ns_ip_address= ""
	_schema_type= ""
	_rpt_sample_time= ""
	_network_function= ""
	_rule= ""
	_pcp_hits= ""
	_application_name= ""
	_policy_name= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_policy_hits_counter_l2"
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
			return "af_policy_hits_counter_l2s"
		except Exception as e :
			raise e



	'''
	get IP address of the NetScaler the policy is bound to.
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set IP address of the NetScaler the policy is bound to.
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get One of the supported schema types.
	'''
	@property
	def schema_type(self) :
		try:
			return self._schema_type
		except Exception as e :
			raise e
	'''
	set One of the supported schema types.
	'''
	@schema_type.setter
	def schema_type(self,schema_type):
		try :
			if not isinstance(schema_type,str):
				raise TypeError("schema_type must be set to str value")
			self._schema_type = schema_type
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
	get network_function name configured on ADC.
	'''
	@property
	def network_function(self) :
		try:
			return self._network_function
		except Exception as e :
			raise e
	'''
	set network_function name configured on ADC.
	'''
	@network_function.setter
	def network_function(self,network_function):
		try :
			if not isinstance(network_function,str):
				raise TypeError("network_function must be set to str value")
			self._network_function = network_function
		except Exception as e :
			raise e


	'''
	get Rule name configured on ADC.
	'''
	@property
	def rule(self) :
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	set Rule name configured on ADC.
	'''
	@rule.setter
	def rule(self,rule):
		try :
			if not isinstance(rule,str):
				raise TypeError("rule must be set to str value")
			self._rule = rule
		except Exception as e :
			raise e


	'''
	get PCP hits of the counter
	'''
	@property
	def pcp_hits(self) :
		try:
			return self._pcp_hits
		except Exception as e :
			raise e
	'''
	set PCP hits of the counter
	'''
	@pcp_hits.setter
	def pcp_hits(self,pcp_hits):
		try :
			if not isinstance(pcp_hits,int):
				raise TypeError("pcp_hits must be set to int value")
			self._pcp_hits = pcp_hits
		except Exception as e :
			raise e


	'''
	get application_name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set application_name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e


	'''
	get Policy name configured on ADC.
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set Policy name configured on ADC.
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
		except Exception as e :
			raise e

	'''
	Af Report for Policy hits counter..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_policy_hits_counter_l2_obj=af_policy_hits_counter_l2()
				response = af_policy_hits_counter_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_policy_hits_counter_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_policy_hits_counter_l2_obj = af_policy_hits_counter_l2()
			option_ = options()
			option_._filter=filter_
			return af_policy_hits_counter_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_policy_hits_counter_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_policy_hits_counter_l2_obj = af_policy_hits_counter_l2()
			option_ = options()
			option_._count=True
			response = af_policy_hits_counter_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_policy_hits_counter_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_policy_hits_counter_l2_obj = af_policy_hits_counter_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_policy_hits_counter_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_policy_hits_counter_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_policy_hits_counter_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_policy_hits_counter_l2_responses, response, "af_policy_hits_counter_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_policy_hits_counter_l2_response_array
				i=0
				error = [af_policy_hits_counter_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_policy_hits_counter_l2_response_array
			i=0
			af_policy_hits_counter_l2_objs = [af_policy_hits_counter_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_policy_hits_counter_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_policy_hits_counter_l2_response,self.__class__.__name__,props)
					af_policy_hits_counter_l2_objs[i] = result.af_policy_hits_counter_l2
					i=i+1
			return af_policy_hits_counter_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_policy_hits_counter_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_policy_hits_counter_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_policy_hits_counter_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_policy_hits_counter_l2= [ af_policy_hits_counter_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_policy_hits_counter_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_policy_hits_counter_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_policy_hits_counter_l2_response_array = [ af_policy_hits_counter_l2() for _ in range(length)]
