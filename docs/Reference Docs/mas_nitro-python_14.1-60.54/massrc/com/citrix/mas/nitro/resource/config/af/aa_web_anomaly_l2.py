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
Configuration for AA Web Anomaly table for Level 2 resource
'''

class aa_web_anomaly_l2(base_resource):
	_snl_time= ""
	_metric_id= ""
	_cnl_time= ""
	_ctnsappname= ""
	_app_resp_time= ""
	_spt_time= ""
	_client_ip_str= ""
	_ulim= ""
	_rpt_sample_time= ""
	_client_ip= ""
	_confidence= ""
	_server_ip_str= ""
	_anomolous_tot_reqs= ""
	_ip_address= ""
	_server_ip= ""
	_application_name= ""
	_llim= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_web_anomaly_l2"
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
			return "aa_web_anomaly_l2s"
		except Exception as e :
			raise e



	'''
	get Server Network Latency Time
	'''
	@property
	def snl_time(self) :
		try:
			return self._snl_time
		except Exception as e :
			raise e
	'''
	set Server Network Latency Time
	'''
	@snl_time.setter
	def snl_time(self,snl_time):
		try :
			if not isinstance(snl_time,long):
				raise TypeError("snl_time must be set to long value")
			self._snl_time = snl_time
		except Exception as e :
			raise e


	'''
	get Anomaly Metic id
	'''
	@property
	def metric_id(self) :
		try:
			return self._metric_id
		except Exception as e :
			raise e
	'''
	set Anomaly Metic id
	'''
	@metric_id.setter
	def metric_id(self,metric_id):
		try :
			if not isinstance(metric_id,int):
				raise TypeError("metric_id must be set to int value")
			self._metric_id = metric_id
		except Exception as e :
			raise e


	'''
	get Client Network Latency Time
	'''
	@property
	def cnl_time(self) :
		try:
			return self._cnl_time
		except Exception as e :
			raise e
	'''
	set Client Network Latency Time
	'''
	@cnl_time.setter
	def cnl_time(self,cnl_time):
		try :
			if not isinstance(cnl_time,long):
				raise TypeError("cnl_time must be set to long value")
			self._cnl_time = cnl_time
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
	get App Response time
	'''
	@property
	def app_resp_time(self) :
		try:
			return self._app_resp_time
		except Exception as e :
			raise e
	'''
	set App Response time
	'''
	@app_resp_time.setter
	def app_resp_time(self,app_resp_time):
		try :
			if not isinstance(app_resp_time,long):
				raise TypeError("app_resp_time must be set to long value")
			self._app_resp_time = app_resp_time
		except Exception as e :
			raise e


	'''
	get Server Processing Time
	'''
	@property
	def spt_time(self) :
		try:
			return self._spt_time
		except Exception as e :
			raise e
	'''
	set Server Processing Time
	'''
	@spt_time.setter
	def spt_time(self,spt_time):
		try :
			if not isinstance(spt_time,long):
				raise TypeError("spt_time must be set to long value")
			self._spt_time = spt_time
		except Exception as e :
			raise e


	'''
	get Client IP Address String
	'''
	@property
	def client_ip_str(self) :
		try:
			return self._client_ip_str
		except Exception as e :
			raise e
	'''
	set Client IP Address String
	'''
	@client_ip_str.setter
	def client_ip_str(self,client_ip_str):
		try :
			if not isinstance(client_ip_str,str):
				raise TypeError("client_ip_str must be set to str value")
			self._client_ip_str = client_ip_str
		except Exception as e :
			raise e


	'''
	get Upper Limit
	'''
	@property
	def ulim(self) :
		try:
			return self._ulim
		except Exception as e :
			raise e
	'''
	set Upper Limit
	'''
	@ulim.setter
	def ulim(self,ulim):
		try :
			if not isinstance(ulim,float):
				raise TypeError("ulim must be set to float value")
			self._ulim = ulim
		except Exception as e :
			raise e


	'''
	get Report Sample time
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time
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
	get Client IP address
	'''
	@property
	def client_ip(self) :
		try:
			return self._client_ip
		except Exception as e :
			raise e
	'''
	set Client IP address
	'''
	@client_ip.setter
	def client_ip(self,client_ip):
		try :
			if not isinstance(client_ip,long):
				raise TypeError("client_ip must be set to long value")
			self._client_ip = client_ip
		except Exception as e :
			raise e


	'''
	get Percentage Deviation
	'''
	@property
	def confidence(self) :
		try:
			return self._confidence
		except Exception as e :
			raise e
	'''
	set Percentage Deviation
	'''
	@confidence.setter
	def confidence(self,confidence):
		try :
			if not isinstance(confidence,float):
				raise TypeError("confidence must be set to float value")
			self._confidence = confidence
		except Exception as e :
			raise e


	'''
	get Server IP Address String
	'''
	@property
	def server_ip_str(self) :
		try:
			return self._server_ip_str
		except Exception as e :
			raise e
	'''
	set Server IP Address String
	'''
	@server_ip_str.setter
	def server_ip_str(self,server_ip_str):
		try :
			if not isinstance(server_ip_str,str):
				raise TypeError("server_ip_str must be set to str value")
			self._server_ip_str = server_ip_str
		except Exception as e :
			raise e


	'''
	get Total Anomolous Requests for this device in given sampled timeframe.
	'''
	@property
	def anomolous_tot_reqs(self) :
		try:
			return self._anomolous_tot_reqs
		except Exception as e :
			raise e
	'''
	set Total Anomolous Requests for this device in given sampled timeframe.
	'''
	@anomolous_tot_reqs.setter
	def anomolous_tot_reqs(self,anomolous_tot_reqs):
		try :
			if not isinstance(anomolous_tot_reqs,long):
				raise TypeError("anomolous_tot_reqs must be set to long value")
			self._anomolous_tot_reqs = anomolous_tot_reqs
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
	get Server IP address
	'''
	@property
	def server_ip(self) :
		try:
			return self._server_ip
		except Exception as e :
			raise e
	'''
	set Server IP address
	'''
	@server_ip.setter
	def server_ip(self,server_ip):
		try :
			if not isinstance(server_ip,long):
				raise TypeError("server_ip must be set to long value")
			self._server_ip = server_ip
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set Application Name
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
	get Lower Limit
	'''
	@property
	def llim(self) :
		try:
			return self._llim
		except Exception as e :
			raise e
	'''
	set Lower Limit
	'''
	@llim.setter
	def llim(self,llim):
		try :
			if not isinstance(llim,float):
				raise TypeError("llim must be set to float value")
			self._llim = llim
		except Exception as e :
			raise e

	'''
	Af Web Anomaly details for Web Insight Data.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_web_anomaly_l2_obj=aa_web_anomaly_l2()
				response = aa_web_anomaly_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_web_anomaly_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_web_anomaly_l2_obj = aa_web_anomaly_l2()
			option_ = options()
			option_._filter=filter_
			return aa_web_anomaly_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_web_anomaly_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_web_anomaly_l2_obj = aa_web_anomaly_l2()
			option_ = options()
			option_._count=True
			response = aa_web_anomaly_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_web_anomaly_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_web_anomaly_l2_obj = aa_web_anomaly_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_web_anomaly_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_web_anomaly_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_web_anomaly_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_web_anomaly_l2_responses, response, "aa_web_anomaly_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_web_anomaly_l2_response_array
				i=0
				error = [aa_web_anomaly_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_web_anomaly_l2_response_array
			i=0
			aa_web_anomaly_l2_objs = [aa_web_anomaly_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_web_anomaly_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_web_anomaly_l2_response,self.__class__.__name__,props)
					aa_web_anomaly_l2_objs[i] = result.aa_web_anomaly_l2
					i=i+1
			return aa_web_anomaly_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_web_anomaly_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_web_anomaly_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_web_anomaly_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_web_anomaly_l2= [ aa_web_anomaly_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_web_anomaly_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_web_anomaly_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_web_anomaly_l2_response_array = [ aa_web_anomaly_l2() for _ in range(length)]
