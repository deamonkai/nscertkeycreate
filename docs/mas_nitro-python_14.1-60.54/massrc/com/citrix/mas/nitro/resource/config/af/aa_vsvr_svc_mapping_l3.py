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
Configuration for AA vsvr and service mapping Report table for Level 3 resource
'''

class aa_vsvr_svc_mapping_l3(base_resource):
	_adc_time= ""
	_appname= ""
	_rpt_sample_time= ""
	_ip_address= ""
	_serv_tot_persistencehits= ""
	_ctnsappname= ""
	_svcname= ""
	_serv_tot_hits= ""
	_serv_hits_rate= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_vsvr_svc_mapping_l3"
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
			return "aa_vsvr_svc_mapping_l3s"
		except Exception as e :
			raise e



	'''
	get Time on NetScaler when metrics data send
	'''
	@property
	def adc_time(self) :
		try:
			return self._adc_time
		except Exception as e :
			raise e
	'''
	set Time on NetScaler when metrics data send
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
	get ApplicationName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set ApplicationName
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
	get serv_tot_persistencehits in sampled timeframe.
	'''
	@property
	def serv_tot_persistencehits(self) :
		try:
			return self._serv_tot_persistencehits
		except Exception as e :
			raise e
	'''
	set serv_tot_persistencehits in sampled timeframe.
	'''
	@serv_tot_persistencehits.setter
	def serv_tot_persistencehits(self,serv_tot_persistencehits):
		try :
			if not isinstance(serv_tot_persistencehits,long):
				raise TypeError("serv_tot_persistencehits must be set to long value")
			self._serv_tot_persistencehits = serv_tot_persistencehits
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
	get serv_tot_hits in sampled timeframe.
	'''
	@property
	def serv_tot_hits(self) :
		try:
			return self._serv_tot_hits
		except Exception as e :
			raise e
	'''
	set serv_tot_hits in sampled timeframe.
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
	get serv_hits_rate in sampled timeframe.
	'''
	@property
	def serv_hits_rate(self) :
		try:
			return self._serv_hits_rate
		except Exception as e :
			raise e
	'''
	set serv_hits_rate in sampled timeframe.
	'''
	@serv_hits_rate.setter
	def serv_hits_rate(self,serv_hits_rate):
		try :
			if not isinstance(serv_hits_rate,long):
				raise TypeError("serv_hits_rate must be set to long value")
			self._serv_hits_rate = serv_hits_rate
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
				aa_vsvr_svc_mapping_l3_obj=aa_vsvr_svc_mapping_l3()
				response = aa_vsvr_svc_mapping_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_vsvr_svc_mapping_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_vsvr_svc_mapping_l3_obj = aa_vsvr_svc_mapping_l3()
			option_ = options()
			option_._filter=filter_
			return aa_vsvr_svc_mapping_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_vsvr_svc_mapping_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_vsvr_svc_mapping_l3_obj = aa_vsvr_svc_mapping_l3()
			option_ = options()
			option_._count=True
			response = aa_vsvr_svc_mapping_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_vsvr_svc_mapping_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_vsvr_svc_mapping_l3_obj = aa_vsvr_svc_mapping_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_vsvr_svc_mapping_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_vsvr_svc_mapping_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_vsvr_svc_mapping_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_vsvr_svc_mapping_l3_responses, response, "aa_vsvr_svc_mapping_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_vsvr_svc_mapping_l3_response_array
				i=0
				error = [aa_vsvr_svc_mapping_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_vsvr_svc_mapping_l3_response_array
			i=0
			aa_vsvr_svc_mapping_l3_objs = [aa_vsvr_svc_mapping_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_vsvr_svc_mapping_l3:
					result = service.payload_formatter.string_to_bulk_resource(aa_vsvr_svc_mapping_l3_response,self.__class__.__name__,props)
					aa_vsvr_svc_mapping_l3_objs[i] = result.aa_vsvr_svc_mapping_l3
					i=i+1
			return aa_vsvr_svc_mapping_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_vsvr_svc_mapping_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_vsvr_svc_mapping_l3_response(base_response):
	def __init__(self,length=1) :
		self.aa_vsvr_svc_mapping_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_vsvr_svc_mapping_l3= [ aa_vsvr_svc_mapping_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_vsvr_svc_mapping_l3_responses(base_response):
	def __init__(self,length=1) :
		self.aa_vsvr_svc_mapping_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_vsvr_svc_mapping_l3_response_array = [ aa_vsvr_svc_mapping_l3() for _ in range(length)]
