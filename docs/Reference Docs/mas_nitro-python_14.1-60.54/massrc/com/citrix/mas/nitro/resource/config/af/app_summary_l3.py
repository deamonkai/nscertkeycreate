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
Configuration for APP Report table for Level 3 resource
'''

class app_summary_l3(base_resource):
	_exporter_id= ""
	_response_bytes= ""
	_vsvr_ip_address= ""
	_app_threat_index= ""
	_total_bytes_cur= ""
	_appname= ""
	_pkt_recvd= ""
	_total_requests= ""
	_hostname= ""
	_total_bytes= ""
	_vservertype= ""
	_vservername= ""
	_ip_address= ""
	_health_score= ""
	_issues_detected= ""
	_app_safety_index= ""
	_curr_state= ""
	_clnt_connections= ""
	_pkt_sent_cur= ""
	_error_percentage= ""
	_srvr_connections= ""
	_response_time= ""
	_pkt_recvd_cur= ""
	_total_attacks= ""
	_throughput= ""
	_request_bytes= ""
	_total_requests_cur= ""
	_application_class= ""
	_pkt_sent= ""
	_app_ssl_rating= ""
	_appcategory= ""
	_state_code= ""
	_vslbhealth= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "app_summary_l3"
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
			return "app_summary_l3s"
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
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
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
			if not isinstance(response_bytes,long):
				raise TypeError("response_bytes must be set to long value")
			self._response_bytes = response_bytes
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
	get threat index.
	'''
	@property
	def app_threat_index(self) :
		try:
			return self._app_threat_index
		except Exception as e :
			raise e
	'''
	set threat index.
	'''
	@app_threat_index.setter
	def app_threat_index(self,app_threat_index):
		try :
			if not isinstance(app_threat_index,long):
				raise TypeError("app_threat_index must be set to long value")
			self._app_threat_index = app_threat_index
		except Exception as e :
			raise e


	'''
	get Session total bytes received in current duration
	'''
	@property
	def total_bytes_cur(self) :
		try:
			return self._total_bytes_cur
		except Exception as e :
			raise e
	'''
	set Session total bytes received in current duration
	'''
	@total_bytes_cur.setter
	def total_bytes_cur(self,total_bytes_cur):
		try :
			if not isinstance(total_bytes_cur,long):
				raise TypeError("total_bytes_cur must be set to long value")
			self._total_bytes_cur = total_bytes_cur
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
			if not isinstance(pkt_recvd,long):
				raise TypeError("pkt_recvd must be set to long value")
			self._pkt_recvd = pkt_recvd
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
			if not isinstance(total_requests,long):
				raise TypeError("total_requests must be set to long value")
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
			if not isinstance(total_bytes,long):
				raise TypeError("total_bytes must be set to long value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get vserver_type
	'''
	@property
	def vservertype(self) :
		try:
			return self._vservertype
		except Exception as e :
			raise e
	'''
	set vserver_type
	'''
	@vservertype.setter
	def vservertype(self,vservertype):
		try :
			if not isinstance(vservertype,str):
				raise TypeError("vservertype must be set to str value")
			self._vservertype = vservertype
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
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
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
			if not isinstance(health_score,long):
				raise TypeError("health_score must be set to long value")
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
	get safety index.
	'''
	@property
	def app_safety_index(self) :
		try:
			return self._app_safety_index
		except Exception as e :
			raise e
	'''
	set safety index.
	'''
	@app_safety_index.setter
	def app_safety_index(self,app_safety_index):
		try :
			if not isinstance(app_safety_index,long):
				raise TypeError("app_safety_index must be set to long value")
			self._app_safety_index = app_safety_index
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
			if not isinstance(clnt_connections,long):
				raise TypeError("clnt_connections must be set to long value")
			self._clnt_connections = clnt_connections
		except Exception as e :
			raise e


	'''
	get Total Pkts Sent in current duration
	'''
	@property
	def pkt_sent_cur(self) :
		try:
			return self._pkt_sent_cur
		except Exception as e :
			raise e
	'''
	set Total Pkts Sent in current duration
	'''
	@pkt_sent_cur.setter
	def pkt_sent_cur(self,pkt_sent_cur):
		try :
			if not isinstance(pkt_sent_cur,long):
				raise TypeError("pkt_sent_cur must be set to long value")
			self._pkt_sent_cur = pkt_sent_cur
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
			if not isinstance(srvr_connections,long):
				raise TypeError("srvr_connections must be set to long value")
			self._srvr_connections = srvr_connections
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
	get Total Pkts Received in current duration
	'''
	@property
	def pkt_recvd_cur(self) :
		try:
			return self._pkt_recvd_cur
		except Exception as e :
			raise e
	'''
	set Total Pkts Received in current duration
	'''
	@pkt_recvd_cur.setter
	def pkt_recvd_cur(self,pkt_recvd_cur):
		try :
			if not isinstance(pkt_recvd_cur,long):
				raise TypeError("pkt_recvd_cur must be set to long value")
			self._pkt_recvd_cur = pkt_recvd_cur
		except Exception as e :
			raise e


	'''
	get Atttacks .
	'''
	@property
	def total_attacks(self) :
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	set Atttacks .
	'''
	@total_attacks.setter
	def total_attacks(self,total_attacks):
		try :
			if not isinstance(total_attacks,long):
				raise TypeError("total_attacks must be set to long value")
			self._total_attacks = total_attacks
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
			if not isinstance(request_bytes,long):
				raise TypeError("request_bytes must be set to long value")
			self._request_bytes = request_bytes
		except Exception as e :
			raise e


	'''
	get Total Requests received in current duration
	'''
	@property
	def total_requests_cur(self) :
		try:
			return self._total_requests_cur
		except Exception as e :
			raise e
	'''
	set Total Requests received in current duration
	'''
	@total_requests_cur.setter
	def total_requests_cur(self,total_requests_cur):
		try :
			if not isinstance(total_requests_cur,long):
				raise TypeError("total_requests_cur must be set to long value")
			self._total_requests_cur = total_requests_cur
		except Exception as e :
			raise e


	'''
	get Application Class
	'''
	@property
	def application_class(self) :
		try:
			return self._application_class
		except Exception as e :
			raise e
	'''
	set Application Class
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
			if not isinstance(pkt_sent,long):
				raise TypeError("pkt_sent must be set to long value")
			self._pkt_sent = pkt_sent
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
	Af Report for App information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				app_summary_l3_obj=app_summary_l3()
				response = app_summary_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_summary_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_summary_l3_obj = app_summary_l3()
			option_ = options()
			option_._filter=filter_
			return app_summary_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_summary_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_summary_l3_obj = app_summary_l3()
			option_ = options()
			option_._count=True
			response = app_summary_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_summary_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_summary_l3_obj = app_summary_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_summary_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(app_summary_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_summary_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_summary_l3_responses, response, "app_summary_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_summary_l3_response_array
				i=0
				error = [app_summary_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_summary_l3_response_array
			i=0
			app_summary_l3_objs = [app_summary_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._app_summary_l3:
					result = service.payload_formatter.string_to_bulk_resource(app_summary_l3_response,self.__class__.__name__,props)
					app_summary_l3_objs[i] = result.app_summary_l3
					i=i+1
			return app_summary_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_summary_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_summary_l3_response(base_response):
	def __init__(self,length=1) :
		self.app_summary_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_summary_l3= [ app_summary_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_summary_l3_responses(base_response):
	def __init__(self,length=1) :
		self.app_summary_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_summary_l3_response_array = [ app_summary_l3() for _ in range(length)]
