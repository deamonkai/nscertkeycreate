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
Configuration for AA vsvr and service mapping Report table for Level 2 resource
'''

class aa_svc_counters_l2(base_resource):
	_ctnsappname= ""
	_svcname= ""
	_serv_tot_hits= ""
	_tot_respbytes= ""
	_curr_state= ""
	_appname= ""
	_tot_pkt_rcvd= ""
	_tot_pkt_sent= ""
	_tot_reqbytes= ""
	_tot_requests= ""
	_ip_address= ""
	_serv_reqbytes_rate= ""
	_serv_rspbytes_rate= ""
	_pkt_rcvd_rate= ""
	_rpt_sample_time= ""
	_serv_req_rate= ""
	_tot_svr_ttfb= ""
	_serv_rsp_rate= ""
	_adc_time= ""
	_tot_svr_ttfb_transactions= ""
	_pkt_sent_rate= ""
	_tot_svr_busy_err= ""
	_tot_responses= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_svc_counters_l2"
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
			return "aa_svc_counters_l2s"
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
	get Service Tot Hits
	'''
	@property
	def serv_tot_hits(self) :
		try:
			return self._serv_tot_hits
		except Exception as e :
			raise e
	'''
	set Service Tot Hits
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
	get Service Resp Rate
	'''
	@property
	def tot_respbytes(self) :
		try:
			return self._tot_respbytes
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_respbytes.setter
	def tot_respbytes(self,tot_respbytes):
		try :
			if not isinstance(tot_respbytes,long):
				raise TypeError("tot_respbytes must be set to long value")
			self._tot_respbytes = tot_respbytes
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def curr_state(self) :
		try:
			return self._curr_state
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@curr_state.setter
	def curr_state(self,curr_state):
		try :
			if not isinstance(curr_state,str):
				raise TypeError("curr_state must be set to str value")
			self._curr_state = curr_state
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
	get Service Resp Rate
	'''
	@property
	def tot_pkt_rcvd(self) :
		try:
			return self._tot_pkt_rcvd
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_pkt_rcvd.setter
	def tot_pkt_rcvd(self,tot_pkt_rcvd):
		try :
			if not isinstance(tot_pkt_rcvd,long):
				raise TypeError("tot_pkt_rcvd must be set to long value")
			self._tot_pkt_rcvd = tot_pkt_rcvd
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_pkt_sent(self) :
		try:
			return self._tot_pkt_sent
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_pkt_sent.setter
	def tot_pkt_sent(self,tot_pkt_sent):
		try :
			if not isinstance(tot_pkt_sent,long):
				raise TypeError("tot_pkt_sent must be set to long value")
			self._tot_pkt_sent = tot_pkt_sent
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_reqbytes(self) :
		try:
			return self._tot_reqbytes
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_reqbytes.setter
	def tot_reqbytes(self,tot_reqbytes):
		try :
			if not isinstance(tot_reqbytes,long):
				raise TypeError("tot_reqbytes must be set to long value")
			self._tot_reqbytes = tot_reqbytes
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_requests(self) :
		try:
			return self._tot_requests
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_requests.setter
	def tot_requests(self,tot_requests):
		try :
			if not isinstance(tot_requests,long):
				raise TypeError("tot_requests must be set to long value")
			self._tot_requests = tot_requests
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
	get Service Bytes Rate
	'''
	@property
	def serv_reqbytes_rate(self) :
		try:
			return self._serv_reqbytes_rate
		except Exception as e :
			raise e
	'''
	set Service Bytes Rate
	'''
	@serv_reqbytes_rate.setter
	def serv_reqbytes_rate(self,serv_reqbytes_rate):
		try :
			if not isinstance(serv_reqbytes_rate,long):
				raise TypeError("serv_reqbytes_rate must be set to long value")
			self._serv_reqbytes_rate = serv_reqbytes_rate
		except Exception as e :
			raise e


	'''
	get Service Resp Bytes Rate
	'''
	@property
	def serv_rspbytes_rate(self) :
		try:
			return self._serv_rspbytes_rate
		except Exception as e :
			raise e
	'''
	set Service Resp Bytes Rate
	'''
	@serv_rspbytes_rate.setter
	def serv_rspbytes_rate(self,serv_rspbytes_rate):
		try :
			if not isinstance(serv_rspbytes_rate,long):
				raise TypeError("serv_rspbytes_rate must be set to long value")
			self._serv_rspbytes_rate = serv_rspbytes_rate
		except Exception as e :
			raise e


	'''
	get Pkt received  Rate
	'''
	@property
	def pkt_rcvd_rate(self) :
		try:
			return self._pkt_rcvd_rate
		except Exception as e :
			raise e
	'''
	set Pkt received  Rate
	'''
	@pkt_rcvd_rate.setter
	def pkt_rcvd_rate(self,pkt_rcvd_rate):
		try :
			if not isinstance(pkt_rcvd_rate,long):
				raise TypeError("pkt_rcvd_rate must be set to long value")
			self._pkt_rcvd_rate = pkt_rcvd_rate
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
	get Service Req Rate
	'''
	@property
	def serv_req_rate(self) :
		try:
			return self._serv_req_rate
		except Exception as e :
			raise e
	'''
	set Service Req Rate
	'''
	@serv_req_rate.setter
	def serv_req_rate(self,serv_req_rate):
		try :
			if not isinstance(serv_req_rate,long):
				raise TypeError("serv_req_rate must be set to long value")
			self._serv_req_rate = serv_req_rate
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_svr_ttfb(self) :
		try:
			return self._tot_svr_ttfb
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_svr_ttfb.setter
	def tot_svr_ttfb(self,tot_svr_ttfb):
		try :
			if not isinstance(tot_svr_ttfb,long):
				raise TypeError("tot_svr_ttfb must be set to long value")
			self._tot_svr_ttfb = tot_svr_ttfb
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def serv_rsp_rate(self) :
		try:
			return self._serv_rsp_rate
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@serv_rsp_rate.setter
	def serv_rsp_rate(self,serv_rsp_rate):
		try :
			if not isinstance(serv_rsp_rate,long):
				raise TypeError("serv_rsp_rate must be set to long value")
			self._serv_rsp_rate = serv_rsp_rate
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
	get Service Resp Rate
	'''
	@property
	def tot_svr_ttfb_transactions(self) :
		try:
			return self._tot_svr_ttfb_transactions
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_svr_ttfb_transactions.setter
	def tot_svr_ttfb_transactions(self,tot_svr_ttfb_transactions):
		try :
			if not isinstance(tot_svr_ttfb_transactions,long):
				raise TypeError("tot_svr_ttfb_transactions must be set to long value")
			self._tot_svr_ttfb_transactions = tot_svr_ttfb_transactions
		except Exception as e :
			raise e


	'''
	get Pkt Sent Rate
	'''
	@property
	def pkt_sent_rate(self) :
		try:
			return self._pkt_sent_rate
		except Exception as e :
			raise e
	'''
	set Pkt Sent Rate
	'''
	@pkt_sent_rate.setter
	def pkt_sent_rate(self,pkt_sent_rate):
		try :
			if not isinstance(pkt_sent_rate,long):
				raise TypeError("pkt_sent_rate must be set to long value")
			self._pkt_sent_rate = pkt_sent_rate
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_svr_busy_err(self) :
		try:
			return self._tot_svr_busy_err
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_svr_busy_err.setter
	def tot_svr_busy_err(self,tot_svr_busy_err):
		try :
			if not isinstance(tot_svr_busy_err,long):
				raise TypeError("tot_svr_busy_err must be set to long value")
			self._tot_svr_busy_err = tot_svr_busy_err
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_responses(self) :
		try:
			return self._tot_responses
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_responses.setter
	def tot_responses(self,tot_responses):
		try :
			if not isinstance(tot_responses,long):
				raise TypeError("tot_responses must be set to long value")
			self._tot_responses = tot_responses
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
				aa_svc_counters_l2_obj=aa_svc_counters_l2()
				response = aa_svc_counters_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_svc_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_svc_counters_l2_obj = aa_svc_counters_l2()
			option_ = options()
			option_._filter=filter_
			return aa_svc_counters_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_svc_counters_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_svc_counters_l2_obj = aa_svc_counters_l2()
			option_ = options()
			option_._count=True
			response = aa_svc_counters_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_svc_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_svc_counters_l2_obj = aa_svc_counters_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_svc_counters_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_svc_counters_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_svc_counters_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_svc_counters_l2_responses, response, "aa_svc_counters_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_svc_counters_l2_response_array
				i=0
				error = [aa_svc_counters_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_svc_counters_l2_response_array
			i=0
			aa_svc_counters_l2_objs = [aa_svc_counters_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_svc_counters_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_svc_counters_l2_response,self.__class__.__name__,props)
					aa_svc_counters_l2_objs[i] = result.aa_svc_counters_l2
					i=i+1
			return aa_svc_counters_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_svc_counters_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_svc_counters_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_svc_counters_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_svc_counters_l2= [ aa_svc_counters_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_svc_counters_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_svc_counters_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_svc_counters_l2_response_array = [ aa_svc_counters_l2() for _ in range(length)]
