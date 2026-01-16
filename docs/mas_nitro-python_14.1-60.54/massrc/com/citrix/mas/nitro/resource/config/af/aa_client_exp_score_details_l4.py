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
Configuration for Client Experience score details table for Level 4 resource
'''

class aa_client_exp_score_details_l4(base_resource):
	_srvr_cert_hash_frontend= ""
	_ctnsappname= ""
	_operating_system= ""
	_ssl_failures_panelty= ""
	_client_score= ""
	_sslversion_frontend= ""
	_render_time_panelty= ""
	_load_time_panelty= ""
	_load_time= ""
	_ciphervalue_frontend= ""
	_issslfrontend= ""
	_client_failures= ""
	_country_name= ""
	_cipherstrength_frontend= ""
	_client_failures_panelty= ""
	_rpt_sample_time= ""
	_client_rtt= ""
	_clientip= ""
	_handshakemsg= ""
	_ssl_failures= ""
	_user_agent= ""
	_render_time= ""
	_servercertsize_frontend= ""
	_client_rtt_panelty= ""
	_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_client_exp_score_details_l4"
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
			return "aa_client_exp_score_details_l4s"
		except Exception as e :
			raise e



	'''
	get srvr_cert_hash_frontend value. SSL Certificate, SHA-1, SHA-2
	'''
	@property
	def srvr_cert_hash_frontend(self) :
		try:
			return self._srvr_cert_hash_frontend
		except Exception as e :
			raise e
	'''
	set srvr_cert_hash_frontend value. SSL Certificate, SHA-1, SHA-2
	'''
	@srvr_cert_hash_frontend.setter
	def srvr_cert_hash_frontend(self,srvr_cert_hash_frontend):
		try :
			if not isinstance(srvr_cert_hash_frontend,int):
				raise TypeError("srvr_cert_hash_frontend must be set to int value")
			self._srvr_cert_hash_frontend = srvr_cert_hash_frontend
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
	get operating_system in sampled timeframe.
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set operating_system in sampled timeframe.
	'''
	@operating_system.setter
	def operating_system(self,operating_system):
		try :
			if not isinstance(operating_system,str):
				raise TypeError("operating_system must be set to str value")
			self._operating_system = operating_system
		except Exception as e :
			raise e


	'''
	get ssl_failures_panelty in sampled timeframe.
	'''
	@property
	def ssl_failures_panelty(self) :
		try:
			return self._ssl_failures_panelty
		except Exception as e :
			raise e
	'''
	set ssl_failures_panelty in sampled timeframe.
	'''
	@ssl_failures_panelty.setter
	def ssl_failures_panelty(self,ssl_failures_panelty):
		try :
			if not isinstance(ssl_failures_panelty,int):
				raise TypeError("ssl_failures_panelty must be set to int value")
			self._ssl_failures_panelty = ssl_failures_panelty
		except Exception as e :
			raise e


	'''
	get ssl_failures in sampled timeframe.
	'''
	@property
	def client_score(self) :
		try:
			return self._client_score
		except Exception as e :
			raise e
	'''
	set ssl_failures in sampled timeframe.
	'''
	@client_score.setter
	def client_score(self,client_score):
		try :
			if not isinstance(client_score,int):
				raise TypeError("client_score must be set to int value")
			self._client_score = client_score
		except Exception as e :
			raise e


	'''
	get sslVersion_frontend value. SSL Protocol, TLS 1.1, TLS 1.2, SSLv3 
	'''
	@property
	def sslversion_frontend(self) :
		try:
			return self._sslversion_frontend
		except Exception as e :
			raise e
	'''
	set sslVersion_frontend value. SSL Protocol, TLS 1.1, TLS 1.2, SSLv3 
	'''
	@sslversion_frontend.setter
	def sslversion_frontend(self,sslversion_frontend):
		try :
			if not isinstance(sslversion_frontend,int):
				raise TypeError("sslversion_frontend must be set to int value")
			self._sslversion_frontend = sslversion_frontend
		except Exception as e :
			raise e


	'''
	get render_time_panelty in sampled timeframe.
	'''
	@property
	def render_time_panelty(self) :
		try:
			return self._render_time_panelty
		except Exception as e :
			raise e
	'''
	set render_time_panelty in sampled timeframe.
	'''
	@render_time_panelty.setter
	def render_time_panelty(self,render_time_panelty):
		try :
			if not isinstance(render_time_panelty,int):
				raise TypeError("render_time_panelty must be set to int value")
			self._render_time_panelty = render_time_panelty
		except Exception as e :
			raise e


	'''
	get load_time_panelty in sampled timeframe.
	'''
	@property
	def load_time_panelty(self) :
		try:
			return self._load_time_panelty
		except Exception as e :
			raise e
	'''
	set load_time_panelty in sampled timeframe.
	'''
	@load_time_panelty.setter
	def load_time_panelty(self,load_time_panelty):
		try :
			if not isinstance(load_time_panelty,int):
				raise TypeError("load_time_panelty must be set to int value")
			self._load_time_panelty = load_time_panelty
		except Exception as e :
			raise e


	'''
	get load_time in sampled timeframe.
	'''
	@property
	def load_time(self) :
		try:
			return self._load_time
		except Exception as e :
			raise e
	'''
	set load_time in sampled timeframe.
	'''
	@load_time.setter
	def load_time(self,load_time):
		try :
			if not isinstance(load_time,int):
				raise TypeError("load_time must be set to int value")
			self._load_time = load_time
		except Exception as e :
			raise e


	'''
	get cipherValue_frontend value. Cipher name.
	'''
	@property
	def ciphervalue_frontend(self) :
		try:
			return self._ciphervalue_frontend
		except Exception as e :
			raise e
	'''
	set cipherValue_frontend value. Cipher name.
	'''
	@ciphervalue_frontend.setter
	def ciphervalue_frontend(self,ciphervalue_frontend):
		try :
			if not isinstance(ciphervalue_frontend,int):
				raise TypeError("ciphervalue_frontend must be set to int value")
			self._ciphervalue_frontend = ciphervalue_frontend
		except Exception as e :
			raise e


	'''
	get SSL Error isFrontEnd. 0 - Back end, 1 - Front end
	'''
	@property
	def issslfrontend(self) :
		try:
			return self._issslfrontend
		except Exception as e :
			raise e
	'''
	set SSL Error isFrontEnd. 0 - Back end, 1 - Front end
	'''
	@issslfrontend.setter
	def issslfrontend(self,issslfrontend):
		try :
			if not isinstance(issslfrontend,int):
				raise TypeError("issslfrontend must be set to int value")
			self._issslfrontend = issslfrontend
		except Exception as e :
			raise e


	'''
	get client_failures in sampled timeframe.
	'''
	@property
	def client_failures(self) :
		try:
			return self._client_failures
		except Exception as e :
			raise e
	'''
	set client_failures in sampled timeframe.
	'''
	@client_failures.setter
	def client_failures(self,client_failures):
		try :
			if not isinstance(client_failures,int):
				raise TypeError("client_failures must be set to int value")
			self._client_failures = client_failures
		except Exception as e :
			raise e


	'''
	get Country Name
	'''
	@property
	def country_name(self) :
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	set Country Name
	'''
	@country_name.setter
	def country_name(self,country_name):
		try :
			if not isinstance(country_name,str):
				raise TypeError("country_name must be set to str value")
			self._country_name = country_name
		except Exception as e :
			raise e


	'''
	get cipherstrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@property
	def cipherstrength_frontend(self) :
		try:
			return self._cipherstrength_frontend
		except Exception as e :
			raise e
	'''
	set cipherstrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@cipherstrength_frontend.setter
	def cipherstrength_frontend(self,cipherstrength_frontend):
		try :
			if not isinstance(cipherstrength_frontend,int):
				raise TypeError("cipherstrength_frontend must be set to int value")
			self._cipherstrength_frontend = cipherstrength_frontend
		except Exception as e :
			raise e


	'''
	get client_failures_panelty in sampled timeframe.
	'''
	@property
	def client_failures_panelty(self) :
		try:
			return self._client_failures_panelty
		except Exception as e :
			raise e
	'''
	set client_failures_panelty in sampled timeframe.
	'''
	@client_failures_panelty.setter
	def client_failures_panelty(self,client_failures_panelty):
		try :
			if not isinstance(client_failures_panelty,int):
				raise TypeError("client_failures_panelty must be set to int value")
			self._client_failures_panelty = client_failures_panelty
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
	get client_rtt in sampled timeframe.
	'''
	@property
	def client_rtt(self) :
		try:
			return self._client_rtt
		except Exception as e :
			raise e
	'''
	set client_rtt in sampled timeframe.
	'''
	@client_rtt.setter
	def client_rtt(self,client_rtt):
		try :
			if not isinstance(client_rtt,int):
				raise TypeError("client_rtt must be set to int value")
			self._client_rtt = client_rtt
		except Exception as e :
			raise e


	'''
	get Client IP Address
	'''
	@property
	def clientip(self) :
		try:
			return self._clientip
		except Exception as e :
			raise e
	'''
	set Client IP Address
	'''
	@clientip.setter
	def clientip(self,clientip):
		try :
			if not isinstance(clientip,long):
				raise TypeError("clientip must be set to long value")
			self._clientip = clientip
		except Exception as e :
			raise e


	'''
	get HandShake Message.
	'''
	@property
	def handshakemsg(self) :
		try:
			return self._handshakemsg
		except Exception as e :
			raise e
	'''
	set HandShake Message.
	'''
	@handshakemsg.setter
	def handshakemsg(self,handshakemsg):
		try :
			if not isinstance(handshakemsg,long):
				raise TypeError("handshakemsg must be set to long value")
			self._handshakemsg = handshakemsg
		except Exception as e :
			raise e


	'''
	get ssl_failures in sampled timeframe.
	'''
	@property
	def ssl_failures(self) :
		try:
			return self._ssl_failures
		except Exception as e :
			raise e
	'''
	set ssl_failures in sampled timeframe.
	'''
	@ssl_failures.setter
	def ssl_failures(self,ssl_failures):
		try :
			if not isinstance(ssl_failures,int):
				raise TypeError("ssl_failures must be set to int value")
			self._ssl_failures = ssl_failures
		except Exception as e :
			raise e


	'''
	get user_agent in sampled timeframe.
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set user_agent in sampled timeframe.
	'''
	@user_agent.setter
	def user_agent(self,user_agent):
		try :
			if not isinstance(user_agent,str):
				raise TypeError("user_agent must be set to str value")
			self._user_agent = user_agent
		except Exception as e :
			raise e


	'''
	get render_time in sampled timeframe.
	'''
	@property
	def render_time(self) :
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	set render_time in sampled timeframe.
	'''
	@render_time.setter
	def render_time(self,render_time):
		try :
			if not isinstance(render_time,int):
				raise TypeError("render_time must be set to int value")
			self._render_time = render_time
		except Exception as e :
			raise e


	'''
	get serverCertSize_frontend value. Key Strenght, 2048, 1024, 4096.
	'''
	@property
	def servercertsize_frontend(self) :
		try:
			return self._servercertsize_frontend
		except Exception as e :
			raise e
	'''
	set serverCertSize_frontend value. Key Strenght, 2048, 1024, 4096.
	'''
	@servercertsize_frontend.setter
	def servercertsize_frontend(self,servercertsize_frontend):
		try :
			if not isinstance(servercertsize_frontend,int):
				raise TypeError("servercertsize_frontend must be set to int value")
			self._servercertsize_frontend = servercertsize_frontend
		except Exception as e :
			raise e


	'''
	get client_rtt_panelty in sampled timeframe.
	'''
	@property
	def client_rtt_panelty(self) :
		try:
			return self._client_rtt_panelty
		except Exception as e :
			raise e
	'''
	set client_rtt_panelty in sampled timeframe.
	'''
	@client_rtt_panelty.setter
	def client_rtt_panelty(self,client_rtt_panelty):
		try :
			if not isinstance(client_rtt_panelty,int):
				raise TypeError("client_rtt_panelty must be set to int value")
			self._client_rtt_panelty = client_rtt_panelty
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
	Af Report for Anomaly details for this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_client_exp_score_details_l4_obj=aa_client_exp_score_details_l4()
				response = aa_client_exp_score_details_l4_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_client_exp_score_details_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_client_exp_score_details_l4_obj = aa_client_exp_score_details_l4()
			option_ = options()
			option_._filter=filter_
			return aa_client_exp_score_details_l4_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_client_exp_score_details_l4 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_client_exp_score_details_l4_obj = aa_client_exp_score_details_l4()
			option_ = options()
			option_._count=True
			response = aa_client_exp_score_details_l4_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_client_exp_score_details_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_client_exp_score_details_l4_obj = aa_client_exp_score_details_l4()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_client_exp_score_details_l4_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_client_exp_score_details_l4_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_client_exp_score_details_l4
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_client_exp_score_details_l4_responses, response, "aa_client_exp_score_details_l4_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_client_exp_score_details_l4_response_array
				i=0
				error = [aa_client_exp_score_details_l4() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_client_exp_score_details_l4_response_array
			i=0
			aa_client_exp_score_details_l4_objs = [aa_client_exp_score_details_l4() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_client_exp_score_details_l4:
					result = service.payload_formatter.string_to_bulk_resource(aa_client_exp_score_details_l4_response,self.__class__.__name__,props)
					aa_client_exp_score_details_l4_objs[i] = result.aa_client_exp_score_details_l4
					i=i+1
			return aa_client_exp_score_details_l4_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_client_exp_score_details_l4,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_client_exp_score_details_l4_response(base_response):
	def __init__(self,length=1) :
		self.aa_client_exp_score_details_l4= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_client_exp_score_details_l4= [ aa_client_exp_score_details_l4() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_client_exp_score_details_l4_responses(base_response):
	def __init__(self,length=1) :
		self.aa_client_exp_score_details_l4_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_client_exp_score_details_l4_response_array = [ aa_client_exp_score_details_l4() for _ in range(length)]
