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

class anomaly_details(base_resource):
	_max_hits= ""
	_avg_ttfb= ""
	_reason= ""
	_ctnsappname= ""
	_svcname= ""
	_serv_tot_hits= ""
	_hits_rate= ""
	___count= ""
	_hits_total= ""
	_state= ""
	_ip_address= ""
	_max_avg_ttfb= ""
	_metric_key= ""
	_server_ip_address= ""
	_usecase= ""
	_metric_name= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "anomaly_details"
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
			return "anomaly_detailss"
		except Exception as e :
			raise e


	'''
	Count of this URL in given sampled timeframe.
	'''
	@property
	def max_hits(self):
		try:
			return self._max_hits
		except Exception as e :
			raise e
	'''
	Count of this URL in given sampled timeframe.
	'''
	@max_hits.setter
	def max_hits(self,max_hits):
		try :
			if not isinstance(max_hits,long):
				raise TypeError("max_hits must be set to long value")
			self._max_hits = max_hits
		except Exception as e :
			raise e

	'''
	Render time.
	'''
	@property
	def avg_ttfb(self):
		try:
			return self._avg_ttfb
		except Exception as e :
			raise e
	'''
	Render time.
	'''
	@avg_ttfb.setter
	def avg_ttfb(self,avg_ttfb):
		try :
			if not isinstance(avg_ttfb,float):
				raise TypeError("avg_ttfb must be set to float value")
			self._avg_ttfb = avg_ttfb
		except Exception as e :
			raise e

	'''
	HTTP Request URL.
	'''
	@property
	def reason(self):
		try:
			return self._reason
		except Exception as e :
			raise e
	'''
	HTTP Request URL.
	'''
	@reason.setter
	def reason(self,reason):
		try :
			if not isinstance(reason,str):
				raise TypeError("reason must be set to str value")
			self._reason = reason
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
	AppName
	'''
	@property
	def svcname(self):
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	AppName
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
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@property
	def serv_tot_hits(self):
		try:
			return self._serv_tot_hits
		except Exception as e :
			raise e
	'''
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@serv_tot_hits.setter
	def serv_tot_hits(self,serv_tot_hits):
		try :
			if not isinstance(serv_tot_hits,long):
				raise TypeError("serv_tot_hits must be set to long value")
			self._serv_tot_hits = serv_tot_hits
		except Exception as e :
			raise e

	'''
	Hits Rate
	'''
	@property
	def hits_rate(self):
		try:
			return self._hits_rate
		except Exception as e :
			raise e
	'''
	Hits Rate
	'''
	@hits_rate.setter
	def hits_rate(self,hits_rate):
		try :
			if not isinstance(hits_rate,float):
				raise TypeError("hits_rate must be set to float value")
			self._hits_rate = hits_rate
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
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
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def hits_total(self):
		try:
			return self._hits_total
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@hits_total.setter
	def hits_total(self,hits_total):
		try :
			if not isinstance(hits_total,long):
				raise TypeError("hits_total must be set to long value")
			self._hits_total = hits_total
		except Exception as e :
			raise e

	'''
	State up/down
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	State up/down
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
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
	 max_avg_ttfb time.
	'''
	@property
	def max_avg_ttfb(self):
		try:
			return self._max_avg_ttfb
		except Exception as e :
			raise e
	'''
	 max_avg_ttfb time.
	'''
	@max_avg_ttfb.setter
	def max_avg_ttfb(self,max_avg_ttfb):
		try :
			if not isinstance(max_avg_ttfb,float):
				raise TypeError("max_avg_ttfb must be set to float value")
			self._max_avg_ttfb = max_avg_ttfb
		except Exception as e :
			raise e

	'''
	metric_key.
	'''
	@property
	def metric_key(self):
		try:
			return self._metric_key
		except Exception as e :
			raise e
	'''
	metric_key.
	'''
	@metric_key.setter
	def metric_key(self,metric_key):
		try :
			if not isinstance(metric_key,str):
				raise TypeError("metric_key must be set to str value")
			self._metric_key = metric_key
		except Exception as e :
			raise e

	'''
	Server Source IP Address
	'''
	@property
	def server_ip_address(self):
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	Server Source IP Address
	'''
	@server_ip_address.setter
	def server_ip_address(self,server_ip_address):
		try :
			if not isinstance(server_ip_address,str):
				raise TypeError("server_ip_address must be set to str value")
			self._server_ip_address = server_ip_address
		except Exception as e :
			raise e

	'''
	Use Case.
	'''
	@property
	def usecase(self):
		try:
			return self._usecase
		except Exception as e :
			raise e
	'''
	Use Case.
	'''
	@usecase.setter
	def usecase(self,usecase):
		try :
			if not isinstance(usecase,str):
				raise TypeError("usecase must be set to str value")
			self._usecase = usecase
		except Exception as e :
			raise e

	'''
	HTTP Request Method.
	'''
	@property
	def metric_name(self):
		try:
			return self._metric_name
		except Exception as e :
			raise e
	'''
	HTTP Request Method.
	'''
	@metric_name.setter
	def metric_name(self,metric_name):
		try :
			if not isinstance(metric_name,str):
				raise TypeError("metric_name must be set to str value")
			self._metric_name = metric_name
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
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
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
				anomaly_details_obj=anomaly_details()
				response = anomaly_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of anomaly_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			anomaly_details_obj = anomaly_details()
			option_ = options()
			option_._filter=filter_
			return anomaly_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the anomaly_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			anomaly_details_obj = anomaly_details()
			option_ = options()
			option_._count=True
			response = anomaly_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of anomaly_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			anomaly_details_obj = anomaly_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = anomaly_details_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(anomaly_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.anomaly_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(anomaly_details_responses, response, "anomaly_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.anomaly_details_response_array
				i=0
				error = [anomaly_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.anomaly_details_response_array
			i=0
			anomaly_details_objs = [anomaly_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._anomaly_details:
					result = service.payload_formatter.string_to_bulk_resource(anomaly_details_response,self.__class__.__name__,props)
					anomaly_details_objs[i] = result.anomaly_details
					i=i+1
			return anomaly_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(anomaly_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class anomaly_details_response(base_response):
	def __init__(self,length=1) :
		self.anomaly_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.anomaly_details= [ anomaly_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class anomaly_details_responses(base_response):
	def __init__(self,length=1) :
		self.anomaly_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.anomaly_details_response_array = [ anomaly_details() for _ in range(length)]
