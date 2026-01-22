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
Configuration for application summarized information resource
'''

class adc_application_summary(base_resource):
	_total_bytes= ""
	_issues_detected= ""
	_vslbhealth= ""
	_ip_address= ""
	_application_class= ""
	_health_score= ""
	_pkt_recvd_cur= ""
	_vservertype= ""
	_appcategory= ""
	_vservername= ""
	_pkt_sent_cur= ""
	_clnt_connections= ""
	_srvr_connections= ""
	_ssl_rating= ""
	_total_requests= ""
	_throughput= ""
	_error_percentage= ""
	_response_time= ""
	_tags= ""
	_curr_state= ""
	_appname= ""
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
			return "adc_application_summary"
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
			return "adc_application_summarys"
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
	get Application class
	'''
	@property
	def application_class(self) :
		try:
			return self._application_class
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
	get Total Pkts Received
	'''
	@property
	def pkt_recvd_cur(self) :
		try:
			return self._pkt_recvd_cur
		except Exception as e :
			raise e
	'''
	set Total Pkts Received
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
	get Vserver Tyoe
	'''
	@property
	def vservertype(self) :
		try:
			return self._vservertype
		except Exception as e :
			raise e
	'''
	set Vserver Tyoe
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
	get Total Pkts Sent
	'''
	@property
	def pkt_sent_cur(self) :
		try:
			return self._pkt_sent_cur
		except Exception as e :
			raise e
	'''
	set Total Pkts Sent
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
	get A+ / non-A+ / NA
	'''
	@property
	def ssl_rating(self) :
		try:
			return self._ssl_rating
		except Exception as e :
			raise e
	'''
	set A+ / non-A+ / NA
	'''
	@ssl_rating.setter
	def ssl_rating(self,ssl_rating):
		try :
			if not isinstance(ssl_rating,str):
				raise TypeError("ssl_rating must be set to str value")
			self._ssl_rating = ssl_rating
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
	get Tags associated with apps
	'''
	@property
	def tags(self) :
		try:
			return self._tags
		except Exception as e :
			raise e
	'''
	set Tags associated with apps
	'''
	@tags.setter
	def tags(self,tags):
		try :
			if not isinstance(tags,str):
				raise TypeError("tags must be set to str value")
			self._tags = tags
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
	Af Report for App information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_application_summary_obj=adc_application_summary()
				response = adc_application_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_application_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_application_summary_obj = adc_application_summary()
			option_ = options()
			option_._filter=filter_
			return adc_application_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_application_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_application_summary_obj = adc_application_summary()
			option_ = options()
			option_._count=True
			response = adc_application_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_application_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_application_summary_obj = adc_application_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_application_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_application_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_application_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_application_summary_responses, response, "adc_application_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_application_summary_response_array
				i=0
				error = [adc_application_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_application_summary_response_array
			i=0
			adc_application_summary_objs = [adc_application_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_application_summary'):
					for props in obj._adc_application_summary:
						result = service.payload_formatter.string_to_bulk_resource(adc_application_summary_response,self.__class__.__name__,props)
						adc_application_summary_objs[i] = result.adc_application_summary
						i=i+1
			return adc_application_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_application_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_application_summary_response(base_response):
	def __init__(self,length=1) :
		self.adc_application_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_application_summary= [ adc_application_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_application_summary_responses(base_response):
	def __init__(self,length=1) :
		self.adc_application_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_application_summary_response_array = [ adc_application_summary() for _ in range(length)]
