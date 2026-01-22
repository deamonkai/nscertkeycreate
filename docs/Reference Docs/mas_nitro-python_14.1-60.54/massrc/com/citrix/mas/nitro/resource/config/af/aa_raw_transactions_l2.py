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
Configuration for AA Transaction Report table for Level 2 resource
'''

class aa_raw_transactions_l2(base_resource):
	_country_name= ""
	_issslfrontend= ""
	_server_rsp_time= ""
	_rpt_sample_time= ""
	_span_id= ""
	_httpreqxforwardedfor= ""
	_sslcerttype_frontend= ""
	_transaction_start_time= ""
	_total_bytes= ""
	_http_req_method= ""
	_servercertsize_frontend= ""
	_srvr_cert_hash_backend= ""
	_ciphervalue_backend= ""
	_appresponsetime= ""
	_content_type= ""
	_url= ""
	_transaction_end_time= ""
	_parent_span_id= ""
	_datatransfertime= ""
	_httpreferer= ""
	_state= ""
	_sslversion_backend= ""
	_cipherstrength_backend= ""
	_cipherstrength_frontend= ""
	_source_svcname= ""
	_server_ip_str= ""
	_location= ""
	_country_code= ""
	_operating_system= ""
	_device_type= ""
	_ctnsappname= ""
	_srvr_cert_hash_frontend= ""
	_servercertsize_backend= ""
	_ciphervalue_frontend= ""
	_serverip= ""
	_server_rtt= ""
	_sslversion_frontend= ""
	_host_name= ""
	_dest_svcname= ""
	_ns_processing_time= ""
	_ip_address= ""
	_vserverls= ""
	_client_ip_str= ""
	_sslcerttype_backend= ""
	_transactionid= ""
	_handshakemsg= ""
	_client_rtt= ""
	_clientip= ""
	_domain_name= ""
	_svcname= ""
	_trace_id= ""
	_city= ""
	_http_rsp_status= ""
	_appname= ""
	_user_agent= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_raw_transactions_l2"
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
			return "aa_raw_transactions_l2s"
		except Exception as e :
			raise e



	'''
	get country_name
	'''
	@property
	def country_name(self) :
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	set country_name
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
	get server_rsp_time
	'''
	@property
	def server_rsp_time(self) :
		try:
			return self._server_rsp_time
		except Exception as e :
			raise e
	'''
	set server_rsp_time
	'''
	@server_rsp_time.setter
	def server_rsp_time(self,server_rsp_time):
		try :
			if not isinstance(server_rsp_time,long):
				raise TypeError("server_rsp_time must be set to long value")
			self._server_rsp_time = server_rsp_time
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
	get span_id
	'''
	@property
	def span_id(self) :
		try:
			return self._span_id
		except Exception as e :
			raise e
	'''
	set span_id
	'''
	@span_id.setter
	def span_id(self,span_id):
		try :
			if not isinstance(span_id,str):
				raise TypeError("span_id must be set to str value")
			self._span_id = span_id
		except Exception as e :
			raise e


	'''
	get httpreqxforwardedfor in sampled timeframe.
	'''
	@property
	def httpreqxforwardedfor(self) :
		try:
			return self._httpreqxforwardedfor
		except Exception as e :
			raise e
	'''
	set httpreqxforwardedfor in sampled timeframe.
	'''
	@httpreqxforwardedfor.setter
	def httpreqxforwardedfor(self,httpreqxforwardedfor):
		try :
			if not isinstance(httpreqxforwardedfor,str):
				raise TypeError("httpreqxforwardedfor must be set to str value")
			self._httpreqxforwardedfor = httpreqxforwardedfor
		except Exception as e :
			raise e


	'''
	get sslcerttype_frontend value. SSL Certificate Type, RSA, DSA, ECDSA, DH 
	'''
	@property
	def sslcerttype_frontend(self) :
		try:
			return self._sslcerttype_frontend
		except Exception as e :
			raise e
	'''
	set sslcerttype_frontend value. SSL Certificate Type, RSA, DSA, ECDSA, DH 
	'''
	@sslcerttype_frontend.setter
	def sslcerttype_frontend(self,sslcerttype_frontend):
		try :
			if not isinstance(sslcerttype_frontend,int):
				raise TypeError("sslcerttype_frontend must be set to int value")
			self._sslcerttype_frontend = sslcerttype_frontend
		except Exception as e :
			raise e


	'''
	get transaction_start_time in sampled timeframe.
	'''
	@property
	def transaction_start_time(self) :
		try:
			return self._transaction_start_time
		except Exception as e :
			raise e
	'''
	set transaction_start_time in sampled timeframe.
	'''
	@transaction_start_time.setter
	def transaction_start_time(self,transaction_start_time):
		try :
			if not isinstance(transaction_start_time,long):
				raise TypeError("transaction_start_time must be set to long value")
			self._transaction_start_time = transaction_start_time
		except Exception as e :
			raise e


	'''
	get total_bytes in sampled timeframe.
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set total_bytes in sampled timeframe.
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
	get http_req_method in sampled timeframe.
	'''
	@property
	def http_req_method(self) :
		try:
			return self._http_req_method
		except Exception as e :
			raise e
	'''
	set http_req_method in sampled timeframe.
	'''
	@http_req_method.setter
	def http_req_method(self,http_req_method):
		try :
			if not isinstance(http_req_method,str):
				raise TypeError("http_req_method must be set to str value")
			self._http_req_method = http_req_method
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
	get srvr_cert_hash_backend value.SSL Certificate, SHA-1, SHA-2
	'''
	@property
	def srvr_cert_hash_backend(self) :
		try:
			return self._srvr_cert_hash_backend
		except Exception as e :
			raise e
	'''
	set srvr_cert_hash_backend value.SSL Certificate, SHA-1, SHA-2
	'''
	@srvr_cert_hash_backend.setter
	def srvr_cert_hash_backend(self,srvr_cert_hash_backend):
		try :
			if not isinstance(srvr_cert_hash_backend,int):
				raise TypeError("srvr_cert_hash_backend must be set to int value")
			self._srvr_cert_hash_backend = srvr_cert_hash_backend
		except Exception as e :
			raise e


	'''
	get cipherValue_backend value. Cipher name.
	'''
	@property
	def ciphervalue_backend(self) :
		try:
			return self._ciphervalue_backend
		except Exception as e :
			raise e
	'''
	set cipherValue_backend value. Cipher name.
	'''
	@ciphervalue_backend.setter
	def ciphervalue_backend(self,ciphervalue_backend):
		try :
			if not isinstance(ciphervalue_backend,int):
				raise TypeError("ciphervalue_backend must be set to int value")
			self._ciphervalue_backend = ciphervalue_backend
		except Exception as e :
			raise e


	'''
	get appresponsetime in sampled timeframe.
	'''
	@property
	def appresponsetime(self) :
		try:
			return self._appresponsetime
		except Exception as e :
			raise e
	'''
	set appresponsetime in sampled timeframe.
	'''
	@appresponsetime.setter
	def appresponsetime(self,appresponsetime):
		try :
			if not isinstance(appresponsetime,long):
				raise TypeError("appresponsetime must be set to long value")
			self._appresponsetime = appresponsetime
		except Exception as e :
			raise e


	'''
	get content_type in sampled timeframe.
	'''
	@property
	def content_type(self) :
		try:
			return self._content_type
		except Exception as e :
			raise e
	'''
	set content_type in sampled timeframe.
	'''
	@content_type.setter
	def content_type(self,content_type):
		try :
			if not isinstance(content_type,str):
				raise TypeError("content_type must be set to str value")
			self._content_type = content_type
		except Exception as e :
			raise e


	'''
	get url in sampled timeframe.
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set url in sampled timeframe.
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e


	'''
	get transaction_end_time in sampled timeframe.
	'''
	@property
	def transaction_end_time(self) :
		try:
			return self._transaction_end_time
		except Exception as e :
			raise e
	'''
	set transaction_end_time in sampled timeframe.
	'''
	@transaction_end_time.setter
	def transaction_end_time(self,transaction_end_time):
		try :
			if not isinstance(transaction_end_time,long):
				raise TypeError("transaction_end_time must be set to long value")
			self._transaction_end_time = transaction_end_time
		except Exception as e :
			raise e


	'''
	get parent_span_id
	'''
	@property
	def parent_span_id(self) :
		try:
			return self._parent_span_id
		except Exception as e :
			raise e
	'''
	set parent_span_id
	'''
	@parent_span_id.setter
	def parent_span_id(self,parent_span_id):
		try :
			if not isinstance(parent_span_id,str):
				raise TypeError("parent_span_id must be set to str value")
			self._parent_span_id = parent_span_id
		except Exception as e :
			raise e


	'''
	get datatransfertime
	'''
	@property
	def datatransfertime(self) :
		try:
			return self._datatransfertime
		except Exception as e :
			raise e
	'''
	set datatransfertime
	'''
	@datatransfertime.setter
	def datatransfertime(self,datatransfertime):
		try :
			if not isinstance(datatransfertime,int):
				raise TypeError("datatransfertime must be set to int value")
			self._datatransfertime = datatransfertime
		except Exception as e :
			raise e


	'''
	get httpReferer.
	'''
	@property
	def httpreferer(self) :
		try:
			return self._httpreferer
		except Exception as e :
			raise e
	'''
	set httpReferer.
	'''
	@httpreferer.setter
	def httpreferer(self,httpreferer):
		try :
			if not isinstance(httpreferer,str):
				raise TypeError("httpreferer must be set to str value")
			self._httpreferer = httpreferer
		except Exception as e :
			raise e


	'''
	get state
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set state
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
	get sslVersion_backend value.  SSL Protocol, TLS 1.1, TLS 1.2, SSLv3 
	'''
	@property
	def sslversion_backend(self) :
		try:
			return self._sslversion_backend
		except Exception as e :
			raise e
	'''
	set sslVersion_backend value.  SSL Protocol, TLS 1.1, TLS 1.2, SSLv3 
	'''
	@sslversion_backend.setter
	def sslversion_backend(self,sslversion_backend):
		try :
			if not isinstance(sslversion_backend,int):
				raise TypeError("sslversion_backend must be set to int value")
			self._sslversion_backend = sslversion_backend
		except Exception as e :
			raise e


	'''
	get cipherStrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@property
	def cipherstrength_backend(self) :
		try:
			return self._cipherstrength_backend
		except Exception as e :
			raise e
	'''
	set cipherStrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@cipherstrength_backend.setter
	def cipherstrength_backend(self,cipherstrength_backend):
		try :
			if not isinstance(cipherstrength_backend,int):
				raise TypeError("cipherstrength_backend must be set to int value")
			self._cipherstrength_backend = cipherstrength_backend
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
	get Source service
	'''
	@property
	def source_svcname(self) :
		try:
			return self._source_svcname
		except Exception as e :
			raise e
	'''
	set Source service
	'''
	@source_svcname.setter
	def source_svcname(self,source_svcname):
		try :
			if not isinstance(source_svcname,str):
				raise TypeError("source_svcname must be set to str value")
			self._source_svcname = source_svcname
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
	get location Country, City
	'''
	@property
	def location(self) :
		try:
			return self._location
		except Exception as e :
			raise e
	'''
	set location Country, City
	'''
	@location.setter
	def location(self,location):
		try :
			if not isinstance(location,str):
				raise TypeError("location must be set to str value")
			self._location = location
		except Exception as e :
			raise e


	'''
	get country_code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set country_code
	'''
	@country_code.setter
	def country_code(self,country_code):
		try :
			if not isinstance(country_code,str):
				raise TypeError("country_code must be set to str value")
			self._country_code = country_code
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
	get device_type in sampled timeframe.
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set device_type in sampled timeframe.
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
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
	get serverCertSize_backend value. Key Strenght, 2048, 1024, 4096.
	'''
	@property
	def servercertsize_backend(self) :
		try:
			return self._servercertsize_backend
		except Exception as e :
			raise e
	'''
	set serverCertSize_backend value. Key Strenght, 2048, 1024, 4096.
	'''
	@servercertsize_backend.setter
	def servercertsize_backend(self,servercertsize_backend):
		try :
			if not isinstance(servercertsize_backend,int):
				raise TypeError("servercertsize_backend must be set to int value")
			self._servercertsize_backend = servercertsize_backend
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
	get serv_hits_rate in sampled timeframe.
	'''
	@property
	def serverip(self) :
		try:
			return self._serverip
		except Exception as e :
			raise e
	'''
	set serv_hits_rate in sampled timeframe.
	'''
	@serverip.setter
	def serverip(self,serverip):
		try :
			if not isinstance(serverip,long):
				raise TypeError("serverip must be set to long value")
			self._serverip = serverip
		except Exception as e :
			raise e


	'''
	get serv_tot_persistencehits in sampled timeframe.
	'''
	@property
	def server_rtt(self) :
		try:
			return self._server_rtt
		except Exception as e :
			raise e
	'''
	set serv_tot_persistencehits in sampled timeframe.
	'''
	@server_rtt.setter
	def server_rtt(self,server_rtt):
		try :
			if not isinstance(server_rtt,int):
				raise TypeError("server_rtt must be set to int value")
			self._server_rtt = server_rtt
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
	get host_name in sampled timeframe.
	'''
	@property
	def host_name(self) :
		try:
			return self._host_name
		except Exception as e :
			raise e
	'''
	set host_name in sampled timeframe.
	'''
	@host_name.setter
	def host_name(self,host_name):
		try :
			if not isinstance(host_name,str):
				raise TypeError("host_name must be set to str value")
			self._host_name = host_name
		except Exception as e :
			raise e


	'''
	get Destincation Service
	'''
	@property
	def dest_svcname(self) :
		try:
			return self._dest_svcname
		except Exception as e :
			raise e
	'''
	set Destincation Service
	'''
	@dest_svcname.setter
	def dest_svcname(self,dest_svcname):
		try :
			if not isinstance(dest_svcname,str):
				raise TypeError("dest_svcname must be set to str value")
			self._dest_svcname = dest_svcname
		except Exception as e :
			raise e


	'''
	get ns_processing_time in sampled timeframe.
	'''
	@property
	def ns_processing_time(self) :
		try:
			return self._ns_processing_time
		except Exception as e :
			raise e
	'''
	set ns_processing_time in sampled timeframe.
	'''
	@ns_processing_time.setter
	def ns_processing_time(self,ns_processing_time):
		try :
			if not isinstance(ns_processing_time,long):
				raise TypeError("ns_processing_time must be set to long value")
			self._ns_processing_time = ns_processing_time
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
	get LB Behind CS
	'''
	@property
	def vserverls(self) :
		try:
			return self._vserverls
		except Exception as e :
			raise e
	'''
	set LB Behind CS
	'''
	@vserverls.setter
	def vserverls(self,vserverls):
		try :
			if not isinstance(vserverls,str):
				raise TypeError("vserverls must be set to str value")
			self._vserverls = vserverls
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
	get sslcerttype_backend value. SSL Certificate Type, RSA, DSA, ECDSA, DH 
	'''
	@property
	def sslcerttype_backend(self) :
		try:
			return self._sslcerttype_backend
		except Exception as e :
			raise e
	'''
	set sslcerttype_backend value. SSL Certificate Type, RSA, DSA, ECDSA, DH 
	'''
	@sslcerttype_backend.setter
	def sslcerttype_backend(self,sslcerttype_backend):
		try :
			if not isinstance(sslcerttype_backend,int):
				raise TypeError("sslcerttype_backend must be set to int value")
			self._sslcerttype_backend = sslcerttype_backend
		except Exception as e :
			raise e


	'''
	get transactionid in sampled timeframe.
	'''
	@property
	def transactionid(self) :
		try:
			return self._transactionid
		except Exception as e :
			raise e
	'''
	set transactionid in sampled timeframe.
	'''
	@transactionid.setter
	def transactionid(self,transactionid):
		try :
			if not isinstance(transactionid,long):
				raise TypeError("transactionid must be set to long value")
			self._transactionid = transactionid
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
	get serv_tot_hits in sampled timeframe.
	'''
	@property
	def client_rtt(self) :
		try:
			return self._client_rtt
		except Exception as e :
			raise e
	'''
	set serv_tot_hits in sampled timeframe.
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
	get serv_persistencehits_rate in sampled timeframe.
	'''
	@property
	def clientip(self) :
		try:
			return self._clientip
		except Exception as e :
			raise e
	'''
	set serv_persistencehits_rate in sampled timeframe.
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
	get domain_name in sampled timeframe.
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set domain_name in sampled timeframe.
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
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
	get trace_id
	'''
	@property
	def trace_id(self) :
		try:
			return self._trace_id
		except Exception as e :
			raise e
	'''
	set trace_id
	'''
	@trace_id.setter
	def trace_id(self,trace_id):
		try :
			if not isinstance(trace_id,str):
				raise TypeError("trace_id must be set to str value")
			self._trace_id = trace_id
		except Exception as e :
			raise e


	'''
	get city
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set city
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e


	'''
	get http_rsp_status in sampled timeframe.
	'''
	@property
	def http_rsp_status(self) :
		try:
			return self._http_rsp_status
		except Exception as e :
			raise e
	'''
	set http_rsp_status in sampled timeframe.
	'''
	@http_rsp_status.setter
	def http_rsp_status(self,http_rsp_status):
		try :
			if not isinstance(http_rsp_status,int):
				raise TypeError("http_rsp_status must be set to int value")
			self._http_rsp_status = http_rsp_status
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
	Af Report for Transaction details for this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_raw_transactions_l2_obj=aa_raw_transactions_l2()
				response = aa_raw_transactions_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_raw_transactions_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_raw_transactions_l2_obj = aa_raw_transactions_l2()
			option_ = options()
			option_._filter=filter_
			return aa_raw_transactions_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_raw_transactions_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_raw_transactions_l2_obj = aa_raw_transactions_l2()
			option_ = options()
			option_._count=True
			response = aa_raw_transactions_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_raw_transactions_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_raw_transactions_l2_obj = aa_raw_transactions_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_raw_transactions_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_raw_transactions_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_raw_transactions_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_raw_transactions_l2_responses, response, "aa_raw_transactions_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_raw_transactions_l2_response_array
				i=0
				error = [aa_raw_transactions_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_raw_transactions_l2_response_array
			i=0
			aa_raw_transactions_l2_objs = [aa_raw_transactions_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_raw_transactions_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_raw_transactions_l2_response,self.__class__.__name__,props)
					aa_raw_transactions_l2_objs[i] = result.aa_raw_transactions_l2
					i=i+1
			return aa_raw_transactions_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_raw_transactions_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_raw_transactions_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_raw_transactions_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_raw_transactions_l2= [ aa_raw_transactions_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_raw_transactions_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_raw_transactions_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_raw_transactions_l2_response_array = [ aa_raw_transactions_l2() for _ in range(length)]
