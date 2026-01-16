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
Configuration for swg_ssl_details resource
'''

class swg_ssl_details(base_resource):
	_total_not_intercepted= ""
	_rpt_sample_time= ""
	_user_name= ""
	_total_not_attempted= ""
	_ssli_policy_action= ""
	_ssli_executed_action= ""
	_ssli_reason_for_action= ""
	_total_not_attempted_prev= ""
	___count= ""
	_exporter_id= ""
	_domain_name= ""
	_total_not_intercepted_prev= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "swg_ssl_details"
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
			return "swg_ssl_detailss"
		except Exception as e :
			raise e



	'''
	get total_not_intercepted
	'''
	@property
	def total_not_intercepted(self) :
		try:
			return self._total_not_intercepted
		except Exception as e :
			raise e
	'''
	set total_not_intercepted
	'''
	@total_not_intercepted.setter
	def total_not_intercepted(self,total_not_intercepted):
		try :
			if not isinstance(total_not_intercepted,float):
				raise TypeError("total_not_intercepted must be set to float value")
			self._total_not_intercepted = total_not_intercepted
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
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get User Name
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set User Name
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
	get total_not_attempted
	'''
	@property
	def total_not_attempted(self) :
		try:
			return self._total_not_attempted
		except Exception as e :
			raise e
	'''
	set total_not_attempted
	'''
	@total_not_attempted.setter
	def total_not_attempted(self,total_not_attempted):
		try :
			if not isinstance(total_not_attempted,float):
				raise TypeError("total_not_attempted must be set to float value")
			self._total_not_attempted = total_not_attempted
		except Exception as e :
			raise e


	'''
	get ssli_policy_action
	'''
	@property
	def ssli_policy_action(self) :
		try:
			return self._ssli_policy_action
		except Exception as e :
			raise e
	'''
	set ssli_policy_action
	'''
	@ssli_policy_action.setter
	def ssli_policy_action(self,ssli_policy_action):
		try :
			if not isinstance(ssli_policy_action,float):
				raise TypeError("ssli_policy_action must be set to float value")
			self._ssli_policy_action = ssli_policy_action
		except Exception as e :
			raise e


	'''
	get SSL Executed Action.
	'''
	@property
	def ssli_executed_action(self) :
		try:
			return self._ssli_executed_action
		except Exception as e :
			raise e
	'''
	set SSL Executed Action.
	'''
	@ssli_executed_action.setter
	def ssli_executed_action(self,ssli_executed_action):
		try :
			if not isinstance(ssli_executed_action,str):
				raise TypeError("ssli_executed_action must be set to str value")
			self._ssli_executed_action = ssli_executed_action
		except Exception as e :
			raise e


	'''
	get SSL REASON Codes.
	'''
	@property
	def ssli_reason_for_action(self) :
		try:
			return self._ssli_reason_for_action
		except Exception as e :
			raise e
	'''
	set SSL REASON Codes.
	'''
	@ssli_reason_for_action.setter
	def ssli_reason_for_action(self,ssli_reason_for_action):
		try :
			if not isinstance(ssli_reason_for_action,str):
				raise TypeError("ssli_reason_for_action must be set to str value")
			self._ssli_reason_for_action = ssli_reason_for_action
		except Exception as e :
			raise e


	'''
	get total_not_attempted_prev
	'''
	@property
	def total_not_attempted_prev(self) :
		try:
			return self._total_not_attempted_prev
		except Exception as e :
			raise e
	'''
	set total_not_attempted_prev
	'''
	@total_not_attempted_prev.setter
	def total_not_attempted_prev(self,total_not_attempted_prev):
		try :
			if not isinstance(total_not_attempted_prev,float):
				raise TypeError("total_not_attempted_prev must be set to float value")
			self._total_not_attempted_prev = total_not_attempted_prev
		except Exception as e :
			raise e


	'''
	get count.
	'''
	@property
	def __count(self) :
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	set count.
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
			if not isinstance(exporter_id,float):
				raise TypeError("exporter_id must be set to float value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get HTTP Request URL.
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set HTTP Request URL.
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
		except Exception as e :
			raise e


	'''
	get total_not_intercepted_prev
	'''
	@property
	def total_not_intercepted_prev(self) :
		try:
			return self._total_not_intercepted_prev
		except Exception as e :
			raise e
	'''
	set total_not_intercepted_prev
	'''
	@total_not_intercepted_prev.setter
	def total_not_intercepted_prev(self,total_not_intercepted_prev):
		try :
			if not isinstance(total_not_intercepted_prev,float):
				raise TypeError("total_not_intercepted_prev must be set to float value")
			self._total_not_intercepted_prev = total_not_intercepted_prev
		except Exception as e :
			raise e

	'''
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				swg_ssl_details_obj=swg_ssl_details()
				response = swg_ssl_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of swg_ssl_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			swg_ssl_details_obj = swg_ssl_details()
			option_ = options()
			option_._filter=filter_
			return swg_ssl_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the swg_ssl_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			swg_ssl_details_obj = swg_ssl_details()
			option_ = options()
			option_._count=True
			response = swg_ssl_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of swg_ssl_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			swg_ssl_details_obj = swg_ssl_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = swg_ssl_details_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - group_by
	'''
	@classmethod
	def set_queryparam_group_by(cls, option, value):
		option.add_queryparam("group_by",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(swg_ssl_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.swg_ssl_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(swg_ssl_details_responses, response, "swg_ssl_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.swg_ssl_details_response_array
				i=0
				error = [swg_ssl_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.swg_ssl_details_response_array
			i=0
			swg_ssl_details_objs = [swg_ssl_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._swg_ssl_details:
					result = service.payload_formatter.string_to_bulk_resource(swg_ssl_details_response,self.__class__.__name__,props)
					swg_ssl_details_objs[i] = result.swg_ssl_details
					i=i+1
			return swg_ssl_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(swg_ssl_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class swg_ssl_details_response(base_response):
	def __init__(self,length=1) :
		self.swg_ssl_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.swg_ssl_details= [ swg_ssl_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class swg_ssl_details_responses(base_response):
	def __init__(self,length=1) :
		self.swg_ssl_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.swg_ssl_details_response_array = [ swg_ssl_details() for _ in range(length)]
