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
Configuration for APP Report table resource
'''

class app_summary(base_resource):
	_vservername= ""
	_total_requests= ""
	_hostname= ""
	_total_bytes= ""
	_total_bytes_prev= ""
	_throughput_prev= ""
	_health_score= ""
	_issues_detected= ""
	_vsvr_ip_address= ""
	_response_bytes= ""
	_exporter_id= ""
	_pkt_recvd= ""
	_appname= ""
	_app_ssl_rating= ""
	_appcategory= ""
	_health_score_prev= ""
	_pkt_sent= ""
	_total_requests_prev= ""
	_rpt_sample_time= ""
	_vslbhealth= ""
	_state_code= ""
	_error_percentage= ""
	_response_time= ""
	_srvr_connections= ""
	_curr_state= ""
	_clnt_connections= ""
	_srvr_connections_prev= ""
	_application_class= ""
	_request_bytes= ""
	_clnt_connections_prev= ""
	___count= ""
	_throughput= ""
	_app_family= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "app_summary"
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
			return "app_summarys"
		except Exception as e :
			raise e



	'''
	get Vserver Name
	'''
	@property
	def vservername(self) :
		try:
			return self._vservername
		except Exception as e :
			raise e
	'''
	set Vserver Name
	'''
	@vservername.setter
	def vservername(self,vservername):
		try :
			if not isinstance(vservername,str):
				raise TypeError("vservername must be set to str value")
			self._vservername = vservername
		except Exception as e :
			raise e


	'''
	get Total Requests
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total Requests
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,float):
				raise TypeError("total_requests must be set to float value")
			self._total_requests = total_requests
		except Exception as e :
			raise e


	'''
	get NetScaler Hostname
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set NetScaler Hostname
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e


	'''
	get Session total bytes
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Session total bytes
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,float):
				raise TypeError("total_bytes must be set to float value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get Session total bytes
	'''
	@property
	def total_bytes_prev(self) :
		try:
			return self._total_bytes_prev
		except Exception as e :
			raise e
	'''
	set Session total bytes
	'''
	@total_bytes_prev.setter
	def total_bytes_prev(self,total_bytes_prev):
		try :
			if not isinstance(total_bytes_prev,float):
				raise TypeError("total_bytes_prev must be set to float value")
			self._total_bytes_prev = total_bytes_prev
		except Exception as e :
			raise e


	'''
	get Throughput .
	'''
	@property
	def throughput_prev(self) :
		try:
			return self._throughput_prev
		except Exception as e :
			raise e
	'''
	set Throughput .
	'''
	@throughput_prev.setter
	def throughput_prev(self,throughput_prev):
		try :
			if not isinstance(throughput_prev,float):
				raise TypeError("throughput_prev must be set to float value")
			self._throughput_prev = throughput_prev
		except Exception as e :
			raise e


	'''
	get App Health Score
	'''
	@property
	def health_score(self) :
		try:
			return self._health_score
		except Exception as e :
			raise e
	'''
	set App Health Score
	'''
	@health_score.setter
	def health_score(self,health_score):
		try :
			if not isinstance(health_score,float):
				raise TypeError("health_score must be set to float value")
			self._health_score = health_score
		except Exception as e :
			raise e


	'''
	get Array of all app issues affecting health score. Each array element tells issueId, penalty and time when it occured
	'''
	@property
	def issues_detected(self) :
		try:
			return self._issues_detected
		except Exception as e :
			raise e
	'''
	set Array of all app issues affecting health score. Each array element tells issueId, penalty and time when it occured
	'''
	@issues_detected.setter
	def issues_detected(self,issues_detected):
		try :
			if not isinstance(issues_detected,str):
				raise TypeError("issues_detected must be set to str value")
			self._issues_detected = issues_detected
		except Exception as e :
			raise e


	'''
	get Vserver IP Address
	'''
	@property
	def vsvr_ip_address(self) :
		try:
			return self._vsvr_ip_address
		except Exception as e :
			raise e
	'''
	set Vserver IP Address
	'''
	@vsvr_ip_address.setter
	def vsvr_ip_address(self,vsvr_ip_address):
		try :
			if not isinstance(vsvr_ip_address,str):
				raise TypeError("vsvr_ip_address must be set to str value")
			self._vsvr_ip_address = vsvr_ip_address
		except Exception as e :
			raise e


	'''
	get Session response bytes
	'''
	@property
	def response_bytes(self) :
		try:
			return self._response_bytes
		except Exception as e :
			raise e
	'''
	set Session response bytes
	'''
	@response_bytes.setter
	def response_bytes(self,response_bytes):
		try :
			if not isinstance(response_bytes,float):
				raise TypeError("response_bytes must be set to float value")
			self._response_bytes = response_bytes
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
			if not isinstance(exporter_id,str):
				raise TypeError("exporter_id must be set to str value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get Total Pkts Received
	'''
	@property
	def pkt_recvd(self) :
		try:
			return self._pkt_recvd
		except Exception as e :
			raise e
	'''
	set Total Pkts Received
	'''
	@pkt_recvd.setter
	def pkt_recvd(self,pkt_recvd):
		try :
			if not isinstance(pkt_recvd,float):
				raise TypeError("pkt_recvd must be set to float value")
			self._pkt_recvd = pkt_recvd
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set AppName
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
	get SSL Rating
	'''
	@property
	def app_ssl_rating(self) :
		try:
			return self._app_ssl_rating
		except Exception as e :
			raise e
	'''
	set SSL Rating
	'''
	@app_ssl_rating.setter
	def app_ssl_rating(self,app_ssl_rating):
		try :
			if not isinstance(app_ssl_rating,str):
				raise TypeError("app_ssl_rating must be set to str value")
			self._app_ssl_rating = app_ssl_rating
		except Exception as e :
			raise e


	'''
	get App Category
	'''
	@property
	def appcategory(self) :
		try:
			return self._appcategory
		except Exception as e :
			raise e
	'''
	set App Category
	'''
	@appcategory.setter
	def appcategory(self,appcategory):
		try :
			if not isinstance(appcategory,str):
				raise TypeError("appcategory must be set to str value")
			self._appcategory = appcategory
		except Exception as e :
			raise e


	'''
	get App Health Score
	'''
	@property
	def health_score_prev(self) :
		try:
			return self._health_score_prev
		except Exception as e :
			raise e
	'''
	set App Health Score
	'''
	@health_score_prev.setter
	def health_score_prev(self,health_score_prev):
		try :
			if not isinstance(health_score_prev,float):
				raise TypeError("health_score_prev must be set to float value")
			self._health_score_prev = health_score_prev
		except Exception as e :
			raise e


	'''
	get Total Pkts Sent
	'''
	@property
	def pkt_sent(self) :
		try:
			return self._pkt_sent
		except Exception as e :
			raise e
	'''
	set Total Pkts Sent
	'''
	@pkt_sent.setter
	def pkt_sent(self,pkt_sent):
		try :
			if not isinstance(pkt_sent,float):
				raise TypeError("pkt_sent must be set to float value")
			self._pkt_sent = pkt_sent
		except Exception as e :
			raise e


	'''
	get Total Requests
	'''
	@property
	def total_requests_prev(self) :
		try:
			return self._total_requests_prev
		except Exception as e :
			raise e
	'''
	set Total Requests
	'''
	@total_requests_prev.setter
	def total_requests_prev(self,total_requests_prev):
		try :
			if not isinstance(total_requests_prev,float):
				raise TypeError("total_requests_prev must be set to float value")
			self._total_requests_prev = total_requests_prev
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
	get Vserver Health
	'''
	@property
	def vslbhealth(self) :
		try:
			return self._vslbhealth
		except Exception as e :
			raise e
	'''
	set Vserver Health
	'''
	@vslbhealth.setter
	def vslbhealth(self,vslbhealth):
		try :
			if not isinstance(vslbhealth,int):
				raise TypeError("vslbhealth must be set to int value")
			self._vslbhealth = vslbhealth
		except Exception as e :
			raise e


	'''
	get Up:1, Down:2, OutOfService:3
	'''
	@property
	def state_code(self) :
		try:
			return self._state_code
		except Exception as e :
			raise e
	'''
	set Up:1, Down:2, OutOfService:3
	'''
	@state_code.setter
	def state_code(self,state_code):
		try :
			if not isinstance(state_code,long):
				raise TypeError("state_code must be set to long value")
			self._state_code = state_code
		except Exception as e :
			raise e


	'''
	get Number of 5xx response received wrt total requests
	'''
	@property
	def error_percentage(self) :
		try:
			return self._error_percentage
		except Exception as e :
			raise e
	'''
	set Number of 5xx response received wrt total requests
	'''
	@error_percentage.setter
	def error_percentage(self,error_percentage):
		try :
			if not isinstance(error_percentage,float):
				raise TypeError("error_percentage must be set to float value")
			self._error_percentage = error_percentage
		except Exception as e :
			raise e


	'''
	get total time taken by the app to send response to client
	'''
	@property
	def response_time(self) :
		try:
			return self._response_time
		except Exception as e :
			raise e
	'''
	set total time taken by the app to send response to client
	'''
	@response_time.setter
	def response_time(self,response_time):
		try :
			if not isinstance(response_time,float):
				raise TypeError("response_time must be set to float value")
			self._response_time = response_time
		except Exception as e :
			raise e


	'''
	get Current Server Connections
	'''
	@property
	def srvr_connections(self) :
		try:
			return self._srvr_connections
		except Exception as e :
			raise e
	'''
	set Current Server Connections
	'''
	@srvr_connections.setter
	def srvr_connections(self,srvr_connections):
		try :
			if not isinstance(srvr_connections,float):
				raise TypeError("srvr_connections must be set to float value")
			self._srvr_connections = srvr_connections
		except Exception as e :
			raise e


	'''
	get Current State
	'''
	@property
	def curr_state(self) :
		try:
			return self._curr_state
		except Exception as e :
			raise e
	'''
	set Current State
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
	get Current Client Connections
	'''
	@property
	def clnt_connections(self) :
		try:
			return self._clnt_connections
		except Exception as e :
			raise e
	'''
	set Current Client Connections
	'''
	@clnt_connections.setter
	def clnt_connections(self,clnt_connections):
		try :
			if not isinstance(clnt_connections,float):
				raise TypeError("clnt_connections must be set to float value")
			self._clnt_connections = clnt_connections
		except Exception as e :
			raise e


	'''
	get Current Server Connections
	'''
	@property
	def srvr_connections_prev(self) :
		try:
			return self._srvr_connections_prev
		except Exception as e :
			raise e
	'''
	set Current Server Connections
	'''
	@srvr_connections_prev.setter
	def srvr_connections_prev(self,srvr_connections_prev):
		try :
			if not isinstance(srvr_connections_prev,float):
				raise TypeError("srvr_connections_prev must be set to float value")
			self._srvr_connections_prev = srvr_connections_prev
		except Exception as e :
			raise e


	'''
	get Application class
	'''
	@property
	def application_class(self) :
		try:
			return self._application_class
		except Exception as e :
			raise e
	'''
	set Application class
	'''
	@application_class.setter
	def application_class(self,application_class):
		try :
			if not isinstance(application_class,str):
				raise TypeError("application_class must be set to str value")
			self._application_class = application_class
		except Exception as e :
			raise e


	'''
	get Session request bytes
	'''
	@property
	def request_bytes(self) :
		try:
			return self._request_bytes
		except Exception as e :
			raise e
	'''
	set Session request bytes
	'''
	@request_bytes.setter
	def request_bytes(self,request_bytes):
		try :
			if not isinstance(request_bytes,float):
				raise TypeError("request_bytes must be set to float value")
			self._request_bytes = request_bytes
		except Exception as e :
			raise e


	'''
	get Current Client Connections
	'''
	@property
	def clnt_connections_prev(self) :
		try:
			return self._clnt_connections_prev
		except Exception as e :
			raise e
	'''
	set Current Client Connections
	'''
	@clnt_connections_prev.setter
	def clnt_connections_prev(self,clnt_connections_prev):
		try :
			if not isinstance(clnt_connections_prev,float):
				raise TypeError("clnt_connections_prev must be set to float value")
			self._clnt_connections_prev = clnt_connections_prev
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
	get Throughput .
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set Throughput .
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,float):
				raise TypeError("throughput must be set to float value")
			self._throughput = throughput
		except Exception as e :
			raise e

	'''
	Application Family
	'''
	@property
	def app_family(self):
		try:
			return self._app_family
		except Exception as e :
			raise e
	'''
	Application Family
	'''
	@app_family.setter
	def app_family(self,app_family):
		try :
			if not isinstance(app_family,str):
				raise TypeError("app_family must be set to str value")
			self._app_family = app_family
		except Exception as e :
			raise e

	'''
	Af Report for App information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				app_summary_obj=app_summary()
				response = app_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_summary_obj = app_summary()
			option_ = options()
			option_._filter=filter_
			return app_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_summary resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_summary_obj = app_summary()
			option_ = options()
			option_._count=True
			response = app_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_summary_obj = app_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(app_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_summary_responses, response, "app_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_summary_response_array
				i=0
				error = [app_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_summary_response_array
			i=0
			app_summary_objs = [app_summary() for _ in range(len(response))]
			for obj in response :
				for props in obj._app_summary:
					result = service.payload_formatter.string_to_bulk_resource(app_summary_response,self.__class__.__name__,props)
					app_summary_objs[i] = result.app_summary
					i=i+1
			return app_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_summary_response(base_response):
	def __init__(self,length=1) :
		self.app_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_summary= [ app_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_summary_responses(base_response):
	def __init__(self,length=1) :
		self.app_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_summary_response_array = [ app_summary() for _ in range(length)]
