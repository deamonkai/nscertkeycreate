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
Configuration for AF Transaction Report table resource
'''

class anomaly_events(base_resource):
	_event_type= ""
	_svcname= ""
	_ctnsappname= ""
	_ip_address= ""
	_event_value= ""
	_rpt_sample_time= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "anomaly_events"
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
			return "anomaly_eventss"
		except Exception as e :
			raise e


	'''
	Event Type.
	'''
	@property
	def event_type(self):
		try:
			return self._event_type
		except Exception as e :
			raise e
	'''
	Event Type.
	'''
	@event_type.setter
	def event_type(self,event_type):
		try :
			if not isinstance(event_type,str):
				raise TypeError("event_type must be set to str value")
			self._event_type = event_type
		except Exception as e :
			raise e

	'''
	svcname
	'''
	@property
	def svcname(self):
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	svcname
	'''
	@svcname.setter
	def svcname(self,svcname):
		try :
			if not isinstance(svcname,str):
				raise TypeError("svcname must be set to str value")
			self._svcname = svcname
		except Exception as e :
			raise e

	'''
	AppName
	'''
	@property
	def ctnsappname(self):
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	AppName
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
	IP Address
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	IP Address
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
	Event Value
	'''
	@property
	def event_value(self):
		try:
			return self._event_value
		except Exception as e :
			raise e
	'''
	Event Value
	'''
	@event_value.setter
	def event_value(self,event_value):
		try :
			if not isinstance(event_value,str):
				raise TypeError("event_value must be set to str value")
			self._event_value = event_value
		except Exception as e :
			raise e

	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
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
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				anomaly_events_obj=anomaly_events()
				response = anomaly_events_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of anomaly_events resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			anomaly_events_obj = anomaly_events()
			option_ = options()
			option_._filter=filter_
			return anomaly_events_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the anomaly_events resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			anomaly_events_obj = anomaly_events()
			option_ = options()
			option_._count=True
			response = anomaly_events_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of anomaly_events resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			anomaly_events_obj = anomaly_events()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = anomaly_events_obj.getfiltered(service, option_)
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
	Set Query Parameter - ns_vsvrs
	'''
	@classmethod
	def set_queryparam_ns_vsvrs(cls, option, value):
		option.add_queryparam("ns_vsvrs",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(anomaly_events_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.anomaly_events
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(anomaly_events_responses, response, "anomaly_events_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.anomaly_events_response_array
				i=0
				error = [anomaly_events() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.anomaly_events_response_array
			i=0
			anomaly_events_objs = [anomaly_events() for _ in range(len(response))]
			for obj in response :
				for props in obj._anomaly_events:
					result = service.payload_formatter.string_to_bulk_resource(anomaly_events_response,self.__class__.__name__,props)
					anomaly_events_objs[i] = result.anomaly_events
					i=i+1
			return anomaly_events_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(anomaly_events,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class anomaly_events_response(base_response):
	def __init__(self,length=1) :
		self.anomaly_events= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.anomaly_events= [ anomaly_events() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class anomaly_events_responses(base_response):
	def __init__(self,length=1) :
		self.anomaly_events_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.anomaly_events_response_array = [ anomaly_events() for _ in range(length)]
