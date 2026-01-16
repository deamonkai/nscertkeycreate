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
Configuration for DNS Details resource
'''

class dns_details(base_resource):
	_dns_tot_neg_nxdmn_entries= ""
	_metric_value= ""
	_dns_tot_queries= ""
	_rpt_sample_time= ""
	___count= ""
	_metric_name= ""
	_ip_address= ""
	_cpuusagepcnt= ""
	_mem_usage_bytes= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "dns_details"
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
			return "dns_detailss"
		except Exception as e :
			raise e


	'''
	DNS Total Negative nxdmn entries
	'''
	@property
	def dns_tot_neg_nxdmn_entries(self):
		try:
			return self._dns_tot_neg_nxdmn_entries
		except Exception as e :
			raise e
	'''
	DNS Total Negative nxdmn entries
	'''
	@dns_tot_neg_nxdmn_entries.setter
	def dns_tot_neg_nxdmn_entries(self,dns_tot_neg_nxdmn_entries):
		try :
			if not isinstance(dns_tot_neg_nxdmn_entries,long):
				raise TypeError("dns_tot_neg_nxdmn_entries must be set to long value")
			self._dns_tot_neg_nxdmn_entries = dns_tot_neg_nxdmn_entries
		except Exception as e :
			raise e

	'''
	Metric Value
	'''
	@property
	def metric_value(self):
		try:
			return self._metric_value
		except Exception as e :
			raise e
	'''
	Metric Value
	'''
	@metric_value.setter
	def metric_value(self,metric_value):
		try :
			if not isinstance(metric_value,long):
				raise TypeError("metric_value must be set to long value")
			self._metric_value = metric_value
		except Exception as e :
			raise e

	'''
	DNS TOT Queries
	'''
	@property
	def dns_tot_queries(self):
		try:
			return self._dns_tot_queries
		except Exception as e :
			raise e
	'''
	DNS TOT Queries
	'''
	@dns_tot_queries.setter
	def dns_tot_queries(self,dns_tot_queries):
		try :
			if not isinstance(dns_tot_queries,long):
				raise TypeError("dns_tot_queries must be set to long value")
			self._dns_tot_queries = dns_tot_queries
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
	Metric Name
	'''
	@property
	def metric_name(self):
		try:
			return self._metric_name
		except Exception as e :
			raise e
	'''
	Metric Name
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
	CPU Usage Count
	'''
	@property
	def cpuusagepcnt(self):
		try:
			return self._cpuusagepcnt
		except Exception as e :
			raise e
	'''
	CPU Usage Count
	'''
	@cpuusagepcnt.setter
	def cpuusagepcnt(self,cpuusagepcnt):
		try :
			if not isinstance(cpuusagepcnt,long):
				raise TypeError("cpuusagepcnt must be set to long value")
			self._cpuusagepcnt = cpuusagepcnt
		except Exception as e :
			raise e

	'''
	Mem Usage Bytes
	'''
	@property
	def mem_usage_bytes(self):
		try:
			return self._mem_usage_bytes
		except Exception as e :
			raise e
	'''
	Mem Usage Bytes
	'''
	@mem_usage_bytes.setter
	def mem_usage_bytes(self,mem_usage_bytes):
		try :
			if not isinstance(mem_usage_bytes,long):
				raise TypeError("mem_usage_bytes must be set to long value")
			self._mem_usage_bytes = mem_usage_bytes
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
				dns_details_obj=dns_details()
				response = dns_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of dns_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			dns_details_obj = dns_details()
			option_ = options()
			option_._filter=filter_
			return dns_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the dns_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			dns_details_obj = dns_details()
			option_ = options()
			option_._count=True
			response = dns_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of dns_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			dns_details_obj = dns_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = dns_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(dns_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dns_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dns_details_responses, response, "dns_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dns_details_response_array
				i=0
				error = [dns_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dns_details_response_array
			i=0
			dns_details_objs = [dns_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._dns_details:
					result = service.payload_formatter.string_to_bulk_resource(dns_details_response,self.__class__.__name__,props)
					dns_details_objs[i] = result.dns_details
					i=i+1
			return dns_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dns_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dns_details_response(base_response):
	def __init__(self,length=1) :
		self.dns_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dns_details= [ dns_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dns_details_responses(base_response):
	def __init__(self,length=1) :
		self.dns_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dns_details_response_array = [ dns_details() for _ in range(length)]
