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
Configuration for Health Monitor for ADC resource
'''

class ns_health_monitor(base_resource):
	_monstatparam3= ""
	_monitor_state= ""
	_monitortotalfailedprobes= ""
	_partition_name= ""
	_monstatparam2= ""
	_poll_time= ""
	_monitor_name= ""
	_responsetime= ""
	_ns_ip_address= ""
	_monstatparam1= ""
	_monitortotalprobes= ""
	_monitorcurrentfailedprobes= ""
	_svc_grp_name= ""
	_svc_name= ""
	_monstatcode= ""
	_lastresponse= ""
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
			return "ns_health_monitor"
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
			return "ns_health_monitors"
		except Exception as e :
			raise e



	'''
	get Third parameter for use with message code
	'''
	@property
	def monstatparam3(self) :
		try:
			return self._monstatparam3
		except Exception as e :
			raise e
	'''
	set Third parameter for use with message code
	'''
	@monstatparam3.setter
	def monstatparam3(self,monstatparam3):
		try :
			if not isinstance(monstatparam3,int):
				raise TypeError("monstatparam3 must be set to int value")
			self._monstatparam3 = monstatparam3
		except Exception as e :
			raise e


	'''
	get State of monitor possible values UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED
	'''
	@property
	def monitor_state(self) :
		try:
			return self._monitor_state
		except Exception as e :
			raise e
	'''
	set State of monitor possible values UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED
	'''
	@monitor_state.setter
	def monitor_state(self,monitor_state):
		try :
			if not isinstance(monitor_state,str):
				raise TypeError("monitor_state must be set to str value")
			self._monitor_state = monitor_state
		except Exception as e :
			raise e


	'''
	get Total number of failed probes
	'''
	@property
	def monitortotalfailedprobes(self) :
		try:
			return self._monitortotalfailedprobes
		except Exception as e :
			raise e
	'''
	set Total number of failed probes
	'''
	@monitortotalfailedprobes.setter
	def monitortotalfailedprobes(self,monitortotalfailedprobes):
		try :
			if not isinstance(monitortotalfailedprobes,str):
				raise TypeError("monitortotalfailedprobes must be set to str value")
			self._monitortotalfailedprobes = monitortotalfailedprobes
		except Exception as e :
			raise e


	'''
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Second parameter for use with message code
	'''
	@property
	def monstatparam2(self) :
		try:
			return self._monstatparam2
		except Exception as e :
			raise e
	'''
	set Second parameter for use with message code
	'''
	@monstatparam2.setter
	def monstatparam2(self,monstatparam2):
		try :
			if not isinstance(monstatparam2,int):
				raise TypeError("monstatparam2 must be set to int value")
			self._monstatparam2 = monstatparam2
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get Name of the monitor
	'''
	@property
	def monitor_name(self) :
		try:
			return self._monitor_name
		except Exception as e :
			raise e
	'''
	set Name of the monitor
	'''
	@monitor_name.setter
	def monitor_name(self,monitor_name):
		try :
			if not isinstance(monitor_name,str):
				raise TypeError("monitor_name must be set to str value")
			self._monitor_name = monitor_name
		except Exception as e :
			raise e


	'''
	get Response time of this monitor
	'''
	@property
	def responsetime(self) :
		try:
			return self._responsetime
		except Exception as e :
			raise e
	'''
	set Response time of this monitor
	'''
	@responsetime.setter
	def responsetime(self,responsetime):
		try :
			if not isinstance(responsetime,str):
				raise TypeError("responsetime must be set to str value")
			self._responsetime = responsetime
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
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
	get First parameter for use with message code
	'''
	@property
	def monstatparam1(self) :
		try:
			return self._monstatparam1
		except Exception as e :
			raise e
	'''
	set First parameter for use with message code
	'''
	@monstatparam1.setter
	def monstatparam1(self,monstatparam1):
		try :
			if not isinstance(monstatparam1,int):
				raise TypeError("monstatparam1 must be set to int value")
			self._monstatparam1 = monstatparam1
		except Exception as e :
			raise e


	'''
	get Total number of probes sent to monitor this service.
	'''
	@property
	def monitortotalprobes(self) :
		try:
			return self._monitortotalprobes
		except Exception as e :
			raise e
	'''
	set Total number of probes sent to monitor this service.
	'''
	@monitortotalprobes.setter
	def monitortotalprobes(self,monitortotalprobes):
		try :
			if not isinstance(monitortotalprobes,str):
				raise TypeError("monitortotalprobes must be set to str value")
			self._monitortotalprobes = monitortotalprobes
		except Exception as e :
			raise e


	'''
	get  Total number of currently failed probes
	'''
	@property
	def monitorcurrentfailedprobes(self) :
		try:
			return self._monitorcurrentfailedprobes
		except Exception as e :
			raise e
	'''
	set  Total number of currently failed probes
	'''
	@monitorcurrentfailedprobes.setter
	def monitorcurrentfailedprobes(self,monitorcurrentfailedprobes):
		try :
			if not isinstance(monitorcurrentfailedprobes,str):
				raise TypeError("monitorcurrentfailedprobes must be set to str value")
			self._monitorcurrentfailedprobes = monitorcurrentfailedprobes
		except Exception as e :
			raise e


	'''
	get The NetScaler Console
	'''
	@property
	def svc_grp_name(self) :
		try:
			return self._svc_grp_name
		except Exception as e :
			raise e
	'''
	set The NetScaler Console
	'''
	@svc_grp_name.setter
	def svc_grp_name(self,svc_grp_name):
		try :
			if not isinstance(svc_grp_name,str):
				raise TypeError("svc_grp_name must be set to str value")
			self._svc_grp_name = svc_grp_name
		except Exception as e :
			raise e


	'''
	get service name monitor associated with
	'''
	@property
	def svc_name(self) :
		try:
			return self._svc_name
		except Exception as e :
			raise e
	'''
	set service name monitor associated with
	'''
	@svc_name.setter
	def svc_name(self,svc_name):
		try :
			if not isinstance(svc_name,str):
				raise TypeError("svc_name must be set to str value")
			self._svc_name = svc_name
		except Exception as e :
			raise e


	'''
	get The code indicating the monitor response
	'''
	@property
	def monstatcode(self) :
		try:
			return self._monstatcode
		except Exception as e :
			raise e
	'''
	set The code indicating the monitor response
	'''
	@monstatcode.setter
	def monstatcode(self,monstatcode):
		try :
			if not isinstance(monstatcode,int):
				raise TypeError("monstatcode must be set to int value")
			self._monstatcode = monstatcode
		except Exception as e :
			raise e


	'''
	get The string form of monstatcode
	'''
	@property
	def lastresponse(self) :
		try:
			return self._lastresponse
		except Exception as e :
			raise e
	'''
	set The string form of monstatcode
	'''
	@lastresponse.setter
	def lastresponse(self,lastresponse):
		try :
			if not isinstance(lastresponse,str):
				raise TypeError("lastresponse must be set to str value")
			self._lastresponse = lastresponse
		except Exception as e :
			raise e

	'''
	Use this operation to get Health Monitor details of NetScaler Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_health_monitor_obj=ns_health_monitor()
				response = ns_health_monitor_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_health_monitor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_health_monitor_obj = ns_health_monitor()
			option_ = options()
			option_._filter=filter_
			return ns_health_monitor_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_health_monitor resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_health_monitor_obj = ns_health_monitor()
			option_ = options()
			option_._count=True
			response = ns_health_monitor_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_health_monitor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_health_monitor_obj = ns_health_monitor()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_health_monitor_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_health_monitor_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_health_monitor
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_health_monitor_responses, response, "ns_health_monitor_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_health_monitor_response_array
				i=0
				error = [ns_health_monitor() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_health_monitor_response_array
			i=0
			ns_health_monitor_objs = [ns_health_monitor() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_health_monitor'):
					for props in obj._ns_health_monitor:
						result = service.payload_formatter.string_to_bulk_resource(ns_health_monitor_response,self.__class__.__name__,props)
						ns_health_monitor_objs[i] = result.ns_health_monitor
						i=i+1
			return ns_health_monitor_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_health_monitor,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_health_monitor_response(base_response):
	def __init__(self,length=1) :
		self.ns_health_monitor= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_health_monitor= [ ns_health_monitor() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_health_monitor_responses(base_response):
	def __init__(self,length=1) :
		self.ns_health_monitor_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_health_monitor_response_array = [ ns_health_monitor() for _ in range(length)]
