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
Configuration for AA Anomaly Report table for Level 2 resource
'''

class aa_anomaly_l2(base_resource):
	_metric_value= ""
	_rpt_sample_time= ""
	_metric_name= ""
	_ip_address= ""
	_usecase= ""
	_reason= ""
	_svcname= ""
	_ctnsappname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_anomaly_l2"
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
			return "aa_anomaly_l2s"
		except Exception as e :
			raise e



	'''
	get metric_value in sampled timeframe.
	'''
	@property
	def metric_value(self) :
		try:
			return self._metric_value
		except Exception as e :
			raise e
	'''
	set metric_value in sampled timeframe.
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
	get metric_name in UnevenLB, serverDelay
	'''
	@property
	def metric_name(self) :
		try:
			return self._metric_name
		except Exception as e :
			raise e
	'''
	set metric_name in UnevenLB, serverDelay
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
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
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
	get usecase name
	'''
	@property
	def usecase(self) :
		try:
			return self._usecase
		except Exception as e :
			raise e
	'''
	set usecase name
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
	get Reason.
	'''
	@property
	def reason(self) :
		try:
			return self._reason
		except Exception as e :
			raise e
	'''
	set Reason.
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
	get Source IP Address
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set Source IP Address
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
	Af Report for Anomaly details for this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_anomaly_l2_obj=aa_anomaly_l2()
				response = aa_anomaly_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_anomaly_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_anomaly_l2_obj = aa_anomaly_l2()
			option_ = options()
			option_._filter=filter_
			return aa_anomaly_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_anomaly_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_anomaly_l2_obj = aa_anomaly_l2()
			option_ = options()
			option_._count=True
			response = aa_anomaly_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_anomaly_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_anomaly_l2_obj = aa_anomaly_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_anomaly_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_anomaly_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_anomaly_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_anomaly_l2_responses, response, "aa_anomaly_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_anomaly_l2_response_array
				i=0
				error = [aa_anomaly_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_anomaly_l2_response_array
			i=0
			aa_anomaly_l2_objs = [aa_anomaly_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_anomaly_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_anomaly_l2_response,self.__class__.__name__,props)
					aa_anomaly_l2_objs[i] = result.aa_anomaly_l2
					i=i+1
			return aa_anomaly_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_anomaly_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_anomaly_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_anomaly_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_anomaly_l2= [ aa_anomaly_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_anomaly_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_anomaly_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_anomaly_l2_response_array = [ aa_anomaly_l2() for _ in range(length)]
