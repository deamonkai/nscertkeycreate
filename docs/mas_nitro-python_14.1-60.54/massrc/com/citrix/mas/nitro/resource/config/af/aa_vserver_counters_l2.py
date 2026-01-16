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

class aa_vserver_counters_l2(base_resource):
	_tot_reqbytes= ""
	_vsvr_tot_unused_persistencesession_freed= ""
	_throughput= ""
	_tot_clt_ttlb_transactions= ""
	_curr_clients= ""
	_total_requests_cur= ""
	_response_time= ""
	_error_percentage= ""
	_tot_clt_ttlb= ""
	_tot_respbytes= ""
	_sslctxencbytesrate= ""
	_ctnsappname= ""
	_vsvr_tot_hits= ""
	_ssl_ctx_cur_sessions= ""
	_tot_pkt_rcvd= ""
	_vsvr_reqbytes_rate= ""
	_total_bytes_cur= ""
	_appname= ""
	_vsvr_rsp_rate= ""
	_svcname= ""
	_ssl_ctx_handshakes_rate= ""
	_vsvr_tot_persistencesession_freed= ""
	_curr_surgecnt= ""
	_curr_connestablised= ""
	_adc_time= ""
	_vsvr_pkt_sent_rate= ""
	_vservertype= ""
	_ip_address= ""
	_tot_pkt_sent= ""
	_vsvr_total_hits_rate= ""
	_tot_ttlb_tolerating_transactions= ""
	_sslctxsessionnewrate= ""
	_curr_state= ""
	_sslctxdecbytesrate= ""
	_vsvr_pkt_rcvd_rate= ""
	_vsvr_cpu_usage= ""
	_rpt_sample_time= ""
	_sslctxsessionhitsrate= ""
	_curr_svcsurgecnt= ""
	_tot_requests= ""
	_vsvr_rspbytes_rate= ""
	_curr_vsvrsurgecnt= ""
	_vsvr_req_rate= ""
	_ssl_ctx_tot_handshakes= ""
	_curr_svrs= ""
	_tot_responses= ""
	_tot_ttlb_frustrating_transactions= ""
	_vserver_protocol= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_vserver_counters_l2"
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
			return "aa_vserver_counters_l2s"
		except Exception as e :
			raise e



	'''
	get Total Request Bytes
	'''
	@property
	def tot_reqbytes(self) :
		try:
			return self._tot_reqbytes
		except Exception as e :
			raise e
	'''
	set Total Request Bytes
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
	get Vserver total unused persistence Session freed
	'''
	@property
	def vsvr_tot_unused_persistencesession_freed(self) :
		try:
			return self._vsvr_tot_unused_persistencesession_freed
		except Exception as e :
			raise e
	'''
	set Vserver total unused persistence Session freed
	'''
	@vsvr_tot_unused_persistencesession_freed.setter
	def vsvr_tot_unused_persistencesession_freed(self,vsvr_tot_unused_persistencesession_freed):
		try :
			if not isinstance(vsvr_tot_unused_persistencesession_freed,long):
				raise TypeError("vsvr_tot_unused_persistencesession_freed must be set to long value")
			self._vsvr_tot_unused_persistencesession_freed = vsvr_tot_unused_persistencesession_freed
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
	get Total Client TTLB Transaction
	'''
	@property
	def tot_clt_ttlb_transactions(self) :
		try:
			return self._tot_clt_ttlb_transactions
		except Exception as e :
			raise e
	'''
	set Total Client TTLB Transaction
	'''
	@tot_clt_ttlb_transactions.setter
	def tot_clt_ttlb_transactions(self,tot_clt_ttlb_transactions):
		try :
			if not isinstance(tot_clt_ttlb_transactions,long):
				raise TypeError("tot_clt_ttlb_transactions must be set to long value")
			self._tot_clt_ttlb_transactions = tot_clt_ttlb_transactions
		except Exception as e :
			raise e


	'''
	get Current Clients
	'''
	@property
	def curr_clients(self) :
		try:
			return self._curr_clients
		except Exception as e :
			raise e
	'''
	set Current Clients
	'''
	@curr_clients.setter
	def curr_clients(self,curr_clients):
		try :
			if not isinstance(curr_clients,long):
				raise TypeError("curr_clients must be set to long value")
			self._curr_clients = curr_clients
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
	get Total client ttlb
	'''
	@property
	def tot_clt_ttlb(self) :
		try:
			return self._tot_clt_ttlb
		except Exception as e :
			raise e
	'''
	set Total client ttlb
	'''
	@tot_clt_ttlb.setter
	def tot_clt_ttlb(self,tot_clt_ttlb):
		try :
			if not isinstance(tot_clt_ttlb,long):
				raise TypeError("tot_clt_ttlb must be set to long value")
			self._tot_clt_ttlb = tot_clt_ttlb
		except Exception as e :
			raise e


	'''
	get Total response bytes
	'''
	@property
	def tot_respbytes(self) :
		try:
			return self._tot_respbytes
		except Exception as e :
			raise e
	'''
	set Total response bytes
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
	get SSL transaction encrypted bytes rate
	'''
	@property
	def sslctxencbytesrate(self) :
		try:
			return self._sslctxencbytesrate
		except Exception as e :
			raise e
	'''
	set SSL transaction encrypted bytes rate
	'''
	@sslctxencbytesrate.setter
	def sslctxencbytesrate(self,sslctxencbytesrate):
		try :
			if not isinstance(sslctxencbytesrate,long):
				raise TypeError("sslctxencbytesrate must be set to long value")
			self._sslctxencbytesrate = sslctxencbytesrate
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
	get Vserver Total Hits
	'''
	@property
	def vsvr_tot_hits(self) :
		try:
			return self._vsvr_tot_hits
		except Exception as e :
			raise e
	'''
	set Vserver Total Hits
	'''
	@vsvr_tot_hits.setter
	def vsvr_tot_hits(self,vsvr_tot_hits):
		try :
			if not isinstance(vsvr_tot_hits,long):
				raise TypeError("vsvr_tot_hits must be set to long value")
			self._vsvr_tot_hits = vsvr_tot_hits
		except Exception as e :
			raise e


	'''
	get SSL Context Current Sessions
	'''
	@property
	def ssl_ctx_cur_sessions(self) :
		try:
			return self._ssl_ctx_cur_sessions
		except Exception as e :
			raise e
	'''
	set SSL Context Current Sessions
	'''
	@ssl_ctx_cur_sessions.setter
	def ssl_ctx_cur_sessions(self,ssl_ctx_cur_sessions):
		try :
			if not isinstance(ssl_ctx_cur_sessions,long):
				raise TypeError("ssl_ctx_cur_sessions must be set to long value")
			self._ssl_ctx_cur_sessions = ssl_ctx_cur_sessions
		except Exception as e :
			raise e


	'''
	get Total packets received
	'''
	@property
	def tot_pkt_rcvd(self) :
		try:
			return self._tot_pkt_rcvd
		except Exception as e :
			raise e
	'''
	set Total packets received
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
	get Vserver Request Bytes Rate
	'''
	@property
	def vsvr_reqbytes_rate(self) :
		try:
			return self._vsvr_reqbytes_rate
		except Exception as e :
			raise e
	'''
	set Vserver Request Bytes Rate
	'''
	@vsvr_reqbytes_rate.setter
	def vsvr_reqbytes_rate(self,vsvr_reqbytes_rate):
		try :
			if not isinstance(vsvr_reqbytes_rate,long):
				raise TypeError("vsvr_reqbytes_rate must be set to long value")
			self._vsvr_reqbytes_rate = vsvr_reqbytes_rate
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
	get Vserver Response Rate
	'''
	@property
	def vsvr_rsp_rate(self) :
		try:
			return self._vsvr_rsp_rate
		except Exception as e :
			raise e
	'''
	set Vserver Response Rate
	'''
	@vsvr_rsp_rate.setter
	def vsvr_rsp_rate(self,vsvr_rsp_rate):
		try :
			if not isinstance(vsvr_rsp_rate,long):
				raise TypeError("vsvr_rsp_rate must be set to long value")
			self._vsvr_rsp_rate = vsvr_rsp_rate
		except Exception as e :
			raise e


	'''
	get Svc IP Address
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set Svc IP Address
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
	get SSL Context Handshakes Rate
	'''
	@property
	def ssl_ctx_handshakes_rate(self) :
		try:
			return self._ssl_ctx_handshakes_rate
		except Exception as e :
			raise e
	'''
	set SSL Context Handshakes Rate
	'''
	@ssl_ctx_handshakes_rate.setter
	def ssl_ctx_handshakes_rate(self,ssl_ctx_handshakes_rate):
		try :
			if not isinstance(ssl_ctx_handshakes_rate,long):
				raise TypeError("ssl_ctx_handshakes_rate must be set to long value")
			self._ssl_ctx_handshakes_rate = ssl_ctx_handshakes_rate
		except Exception as e :
			raise e


	'''
	get Vserver total persistence Session freed
	'''
	@property
	def vsvr_tot_persistencesession_freed(self) :
		try:
			return self._vsvr_tot_persistencesession_freed
		except Exception as e :
			raise e
	'''
	set Vserver total persistence Session freed
	'''
	@vsvr_tot_persistencesession_freed.setter
	def vsvr_tot_persistencesession_freed(self,vsvr_tot_persistencesession_freed):
		try :
			if not isinstance(vsvr_tot_persistencesession_freed,long):
				raise TypeError("vsvr_tot_persistencesession_freed must be set to long value")
			self._vsvr_tot_persistencesession_freed = vsvr_tot_persistencesession_freed
		except Exception as e :
			raise e


	'''
	get Surge count Rate
	'''
	@property
	def curr_surgecnt(self) :
		try:
			return self._curr_surgecnt
		except Exception as e :
			raise e
	'''
	set Surge count Rate
	'''
	@curr_surgecnt.setter
	def curr_surgecnt(self,curr_surgecnt):
		try :
			if not isinstance(curr_surgecnt,long):
				raise TypeError("curr_surgecnt must be set to long value")
			self._curr_surgecnt = curr_surgecnt
		except Exception as e :
			raise e


	'''
	get Current connection established
	'''
	@property
	def curr_connestablised(self) :
		try:
			return self._curr_connestablised
		except Exception as e :
			raise e
	'''
	set Current connection established
	'''
	@curr_connestablised.setter
	def curr_connestablised(self,curr_connestablised):
		try :
			if not isinstance(curr_connestablised,long):
				raise TypeError("curr_connestablised must be set to long value")
			self._curr_connestablised = curr_connestablised
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
	get Pkt Sent  Rate
	'''
	@property
	def vsvr_pkt_sent_rate(self) :
		try:
			return self._vsvr_pkt_sent_rate
		except Exception as e :
			raise e
	'''
	set Pkt Sent  Rate
	'''
	@vsvr_pkt_sent_rate.setter
	def vsvr_pkt_sent_rate(self,vsvr_pkt_sent_rate):
		try :
			if not isinstance(vsvr_pkt_sent_rate,long):
				raise TypeError("vsvr_pkt_sent_rate must be set to long value")
			self._vsvr_pkt_sent_rate = vsvr_pkt_sent_rate
		except Exception as e :
			raise e


	'''
	get Vserver Name
	'''
	@property
	def vservertype(self) :
		try:
			return self._vservertype
		except Exception as e :
			raise e
	'''
	set Vserver Name
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
	get Total packets sent
	'''
	@property
	def tot_pkt_sent(self) :
		try:
			return self._tot_pkt_sent
		except Exception as e :
			raise e
	'''
	set Total packets sent
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
	get Total hits Rate
	'''
	@property
	def vsvr_total_hits_rate(self) :
		try:
			return self._vsvr_total_hits_rate
		except Exception as e :
			raise e
	'''
	set Total hits Rate
	'''
	@vsvr_total_hits_rate.setter
	def vsvr_total_hits_rate(self,vsvr_total_hits_rate):
		try :
			if not isinstance(vsvr_total_hits_rate,long):
				raise TypeError("vsvr_total_hits_rate must be set to long value")
			self._vsvr_total_hits_rate = vsvr_total_hits_rate
		except Exception as e :
			raise e


	'''
	get Tolerating transactions
	'''
	@property
	def tot_ttlb_tolerating_transactions(self) :
		try:
			return self._tot_ttlb_tolerating_transactions
		except Exception as e :
			raise e
	'''
	set Tolerating transactions
	'''
	@tot_ttlb_tolerating_transactions.setter
	def tot_ttlb_tolerating_transactions(self,tot_ttlb_tolerating_transactions):
		try :
			if not isinstance(tot_ttlb_tolerating_transactions,long):
				raise TypeError("tot_ttlb_tolerating_transactions must be set to long value")
			self._tot_ttlb_tolerating_transactions = tot_ttlb_tolerating_transactions
		except Exception as e :
			raise e


	'''
	get SSL Encrypted Bytes
	'''
	@property
	def sslctxsessionnewrate(self) :
		try:
			return self._sslctxsessionnewrate
		except Exception as e :
			raise e
	'''
	set SSL Encrypted Bytes
	'''
	@sslctxsessionnewrate.setter
	def sslctxsessionnewrate(self,sslctxsessionnewrate):
		try :
			if not isinstance(sslctxsessionnewrate,long):
				raise TypeError("sslctxsessionnewrate must be set to long value")
			self._sslctxsessionnewrate = sslctxsessionnewrate
		except Exception as e :
			raise e


	'''
	get  State
	'''
	@property
	def curr_state(self) :
		try:
			return self._curr_state
		except Exception as e :
			raise e
	'''
	set  State
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
	get SSL transaction decrypted bytes rate
	'''
	@property
	def sslctxdecbytesrate(self) :
		try:
			return self._sslctxdecbytesrate
		except Exception as e :
			raise e
	'''
	set SSL transaction decrypted bytes rate
	'''
	@sslctxdecbytesrate.setter
	def sslctxdecbytesrate(self,sslctxdecbytesrate):
		try :
			if not isinstance(sslctxdecbytesrate,long):
				raise TypeError("sslctxdecbytesrate must be set to long value")
			self._sslctxdecbytesrate = sslctxdecbytesrate
		except Exception as e :
			raise e


	'''
	get Packet Received Rate
	'''
	@property
	def vsvr_pkt_rcvd_rate(self) :
		try:
			return self._vsvr_pkt_rcvd_rate
		except Exception as e :
			raise e
	'''
	set Packet Received Rate
	'''
	@vsvr_pkt_rcvd_rate.setter
	def vsvr_pkt_rcvd_rate(self,vsvr_pkt_rcvd_rate):
		try :
			if not isinstance(vsvr_pkt_rcvd_rate,long):
				raise TypeError("vsvr_pkt_rcvd_rate must be set to long value")
			self._vsvr_pkt_rcvd_rate = vsvr_pkt_rcvd_rate
		except Exception as e :
			raise e


	'''
	get VServer CPU Usuage
	'''
	@property
	def vsvr_cpu_usage(self) :
		try:
			return self._vsvr_cpu_usage
		except Exception as e :
			raise e
	'''
	set VServer CPU Usuage
	'''
	@vsvr_cpu_usage.setter
	def vsvr_cpu_usage(self,vsvr_cpu_usage):
		try :
			if not isinstance(vsvr_cpu_usage,long):
				raise TypeError("vsvr_cpu_usage must be set to long value")
			self._vsvr_cpu_usage = vsvr_cpu_usage
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
	get SSL session hits rate
	'''
	@property
	def sslctxsessionhitsrate(self) :
		try:
			return self._sslctxsessionhitsrate
		except Exception as e :
			raise e
	'''
	set SSL session hits rate
	'''
	@sslctxsessionhitsrate.setter
	def sslctxsessionhitsrate(self,sslctxsessionhitsrate):
		try :
			if not isinstance(sslctxsessionhitsrate,long):
				raise TypeError("sslctxsessionhitsrate must be set to long value")
			self._sslctxsessionhitsrate = sslctxsessionhitsrate
		except Exception as e :
			raise e


	'''
	get Service Surge count Rate
	'''
	@property
	def curr_svcsurgecnt(self) :
		try:
			return self._curr_svcsurgecnt
		except Exception as e :
			raise e
	'''
	set Service Surge count Rate
	'''
	@curr_svcsurgecnt.setter
	def curr_svcsurgecnt(self,curr_svcsurgecnt):
		try :
			if not isinstance(curr_svcsurgecnt,long):
				raise TypeError("curr_svcsurgecnt must be set to long value")
			self._curr_svcsurgecnt = curr_svcsurgecnt
		except Exception as e :
			raise e


	'''
	get Total requests
	'''
	@property
	def tot_requests(self) :
		try:
			return self._tot_requests
		except Exception as e :
			raise e
	'''
	set Total requests
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
	get Response Bytes Rate
	'''
	@property
	def vsvr_rspbytes_rate(self) :
		try:
			return self._vsvr_rspbytes_rate
		except Exception as e :
			raise e
	'''
	set Response Bytes Rate
	'''
	@vsvr_rspbytes_rate.setter
	def vsvr_rspbytes_rate(self,vsvr_rspbytes_rate):
		try :
			if not isinstance(vsvr_rspbytes_rate,long):
				raise TypeError("vsvr_rspbytes_rate must be set to long value")
			self._vsvr_rspbytes_rate = vsvr_rspbytes_rate
		except Exception as e :
			raise e


	'''
	get VServer Surge count Rate
	'''
	@property
	def curr_vsvrsurgecnt(self) :
		try:
			return self._curr_vsvrsurgecnt
		except Exception as e :
			raise e
	'''
	set VServer Surge count Rate
	'''
	@curr_vsvrsurgecnt.setter
	def curr_vsvrsurgecnt(self,curr_vsvrsurgecnt):
		try :
			if not isinstance(curr_vsvrsurgecnt,long):
				raise TypeError("curr_vsvrsurgecnt must be set to long value")
			self._curr_vsvrsurgecnt = curr_vsvrsurgecnt
		except Exception as e :
			raise e


	'''
	get Vserver Request Rate
	'''
	@property
	def vsvr_req_rate(self) :
		try:
			return self._vsvr_req_rate
		except Exception as e :
			raise e
	'''
	set Vserver Request Rate
	'''
	@vsvr_req_rate.setter
	def vsvr_req_rate(self,vsvr_req_rate):
		try :
			if not isinstance(vsvr_req_rate,long):
				raise TypeError("vsvr_req_rate must be set to long value")
			self._vsvr_req_rate = vsvr_req_rate
		except Exception as e :
			raise e


	'''
	get SSL Context Total Handshakes
	'''
	@property
	def ssl_ctx_tot_handshakes(self) :
		try:
			return self._ssl_ctx_tot_handshakes
		except Exception as e :
			raise e
	'''
	set SSL Context Total Handshakes
	'''
	@ssl_ctx_tot_handshakes.setter
	def ssl_ctx_tot_handshakes(self,ssl_ctx_tot_handshakes):
		try :
			if not isinstance(ssl_ctx_tot_handshakes,long):
				raise TypeError("ssl_ctx_tot_handshakes must be set to long value")
			self._ssl_ctx_tot_handshakes = ssl_ctx_tot_handshakes
		except Exception as e :
			raise e


	'''
	get current servers
	'''
	@property
	def curr_svrs(self) :
		try:
			return self._curr_svrs
		except Exception as e :
			raise e
	'''
	set current servers
	'''
	@curr_svrs.setter
	def curr_svrs(self,curr_svrs):
		try :
			if not isinstance(curr_svrs,long):
				raise TypeError("curr_svrs must be set to long value")
			self._curr_svrs = curr_svrs
		except Exception as e :
			raise e


	'''
	get Total Responses
	'''
	@property
	def tot_responses(self) :
		try:
			return self._tot_responses
		except Exception as e :
			raise e
	'''
	set Total Responses
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
	get Frustrating transactions
	'''
	@property
	def tot_ttlb_frustrating_transactions(self) :
		try:
			return self._tot_ttlb_frustrating_transactions
		except Exception as e :
			raise e
	'''
	set Frustrating transactions
	'''
	@tot_ttlb_frustrating_transactions.setter
	def tot_ttlb_frustrating_transactions(self,tot_ttlb_frustrating_transactions):
		try :
			if not isinstance(tot_ttlb_frustrating_transactions,long):
				raise TypeError("tot_ttlb_frustrating_transactions must be set to long value")
			self._tot_ttlb_frustrating_transactions = tot_ttlb_frustrating_transactions
		except Exception as e :
			raise e


	'''
	get Vserver Protocol
	'''
	@property
	def vserver_protocol(self) :
		try:
			return self._vserver_protocol
		except Exception as e :
			raise e
	'''
	set Vserver Protocol
	'''
	@vserver_protocol.setter
	def vserver_protocol(self,vserver_protocol):
		try :
			if not isinstance(vserver_protocol,str):
				raise TypeError("vserver_protocol must be set to str value")
			self._vserver_protocol = vserver_protocol
		except Exception as e :
			raise e

	'''
	Af Report for vserver counters details for this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_vserver_counters_l2_obj=aa_vserver_counters_l2()
				response = aa_vserver_counters_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_vserver_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_vserver_counters_l2_obj = aa_vserver_counters_l2()
			option_ = options()
			option_._filter=filter_
			return aa_vserver_counters_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_vserver_counters_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_vserver_counters_l2_obj = aa_vserver_counters_l2()
			option_ = options()
			option_._count=True
			response = aa_vserver_counters_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_vserver_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_vserver_counters_l2_obj = aa_vserver_counters_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_vserver_counters_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_vserver_counters_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_vserver_counters_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_vserver_counters_l2_responses, response, "aa_vserver_counters_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_vserver_counters_l2_response_array
				i=0
				error = [aa_vserver_counters_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_vserver_counters_l2_response_array
			i=0
			aa_vserver_counters_l2_objs = [aa_vserver_counters_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_vserver_counters_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_vserver_counters_l2_response,self.__class__.__name__,props)
					aa_vserver_counters_l2_objs[i] = result.aa_vserver_counters_l2
					i=i+1
			return aa_vserver_counters_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_vserver_counters_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_vserver_counters_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_vserver_counters_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_vserver_counters_l2= [ aa_vserver_counters_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_vserver_counters_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_vserver_counters_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_vserver_counters_l2_response_array = [ aa_vserver_counters_l2() for _ in range(length)]
