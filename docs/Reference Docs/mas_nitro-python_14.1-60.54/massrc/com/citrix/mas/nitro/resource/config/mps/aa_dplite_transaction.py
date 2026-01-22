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
Configuration for NetScaler Txn Information resource
'''

class aa_dplite_transaction(base_resource):
	_sslServerCertSizeBE= ""
	_dest_cluster_name= ""
	_sslSigHashAlgFE= ""
	_httpReqCookie= ""
	_ato_config= ""
	_tracingTraceId= ""
	_recType= ""
	_server_rsp_time= ""
	_sslFLagsFE= ""
	_srvrTcpJitter= ""
	_httpResRcvFB= ""
	_transactionId= ""
	_clntTcpZeroWindowCount= ""
	_tracingReqSpanId= ""
	_httpReqHost= ""
	_httpReqRcvFB= ""
	_srvrFastRetxCount= ""
	_tracingReqParentSpanId= ""
	_sslCipherValueFE= ""
	_aaaUserEmailId= ""
	_clntTcpPacketsRetransmited= ""
	_login_attempt= ""
	_appresponsetime= ""
	_sslFLagsBE= ""
	_clntTcpRtoCount= ""
	_source_svcname= ""
	_VPNsessionID= ""
	_source_cluster_name= ""
	_srvrTcpPacketsRetransmited= ""
	_httpDomainName= ""
	_transCltIpv4Address= ""
	_httpContentType= ""
	_transCltDstIpv4Address= ""
	_backendSvrIpv4Address= ""
	_ns_processing_time= ""
	_httpReqUrl= ""
	_svrTcpFlagsTx= ""
	_dest_svcname= ""
	_httpReqMethod= ""
	_appNameVserverLs= ""
	_source_namespace= ""
	_api_auth_attempt= ""
	_session_track_method= ""
	_recSubType= ""
	_dest_namespace= ""
	_dest_labels= ""
	_httpReqReferer= ""
	_login_result= ""
	_srvrTcpZeroWindowCount= ""
	_sslSigHashAlgBE= ""
	_sslCipherValueBE= ""
	_httpResForwFB= ""
	_httpReqRcvLB= ""
	_transaction_start_time= ""
	_httpTransEndTime= ""
	_clntTcpJitter= ""
	_transCltTotRxOctCnt= ""
	_api_auth_result= ""
	_cltTcpFlagsTx= ""
	_transSvrRTT= ""
	_appName= ""
	_sslHandshakeErrorMsg= ""
	_transCltRTT= ""
	_httpReqForwLB= ""
	_transCltTotTxOctCnt= ""
	_httpRspStatus= ""
	_cltTcpFlagsRx= ""
	_httpReqUserAgent= ""
	_httpResRcvLB= ""
	_aaaUsername= ""
	_clntFastRetxCount= ""
	_sslErrFlag= ""
	_httpReqForwFB= ""
	_sslServerCertSizeFE= ""
	_application_name= ""
	_svrTcpFlagsRx= ""
	_httpReqXForwardedFor= ""
	_srvrTcpRtoCount= ""
	_session_attribute= ""
	_source_labels= ""
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
			return "aa_dplite_transaction"
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
			return "aa_dplite_transactions"
		except Exception as e :
			raise e



	'''
	get sslServerCertSizeBE
	'''
	@property
	def sslServerCertSizeBE(self) :
		try:
			return self._sslServerCertSizeBE
		except Exception as e :
			raise e
	'''
	set sslServerCertSizeBE
	'''
	@sslServerCertSizeBE.setter
	def sslServerCertSizeBE(self,sslServerCertSizeBE):
		try :
			if not isinstance(sslServerCertSizeBE,long):
				raise TypeError("sslServerCertSizeBE must be set to long value")
			self._sslServerCertSizeBE = sslServerCertSizeBE
		except Exception as e :
			raise e


	'''
	get dest_cluster_name
	'''
	@property
	def dest_cluster_name(self) :
		try:
			return self._dest_cluster_name
		except Exception as e :
			raise e
	'''
	set dest_cluster_name
	'''
	@dest_cluster_name.setter
	def dest_cluster_name(self,dest_cluster_name):
		try :
			if not isinstance(dest_cluster_name,str):
				raise TypeError("dest_cluster_name must be set to str value")
			self._dest_cluster_name = dest_cluster_name
		except Exception as e :
			raise e


	'''
	get sslSigHashAlgFE
	'''
	@property
	def sslSigHashAlgFE(self) :
		try:
			return self._sslSigHashAlgFE
		except Exception as e :
			raise e
	'''
	set sslSigHashAlgFE
	'''
	@sslSigHashAlgFE.setter
	def sslSigHashAlgFE(self,sslSigHashAlgFE):
		try :
			if not isinstance(sslSigHashAlgFE,long):
				raise TypeError("sslSigHashAlgFE must be set to long value")
			self._sslSigHashAlgFE = sslSigHashAlgFE
		except Exception as e :
			raise e


	'''
	get httpReqCookie
	'''
	@property
	def httpReqCookie(self) :
		try:
			return self._httpReqCookie
		except Exception as e :
			raise e
	'''
	set httpReqCookie
	'''
	@httpReqCookie.setter
	def httpReqCookie(self,httpReqCookie):
		try :
			if not isinstance(httpReqCookie,str):
				raise TypeError("httpReqCookie must be set to str value")
			self._httpReqCookie = httpReqCookie
		except Exception as e :
			raise e


	'''
	get ato_config
	'''
	@property
	def ato_config(self) :
		try:
			return self._ato_config
		except Exception as e :
			raise e
	'''
	set ato_config
	'''
	@ato_config.setter
	def ato_config(self,ato_config):
		try :
			if not isinstance(ato_config,long):
				raise TypeError("ato_config must be set to long value")
			self._ato_config = ato_config
		except Exception as e :
			raise e


	'''
	get tracingTraceId
	'''
	@property
	def tracingTraceId(self) :
		try:
			return self._tracingTraceId
		except Exception as e :
			raise e
	'''
	set tracingTraceId
	'''
	@tracingTraceId.setter
	def tracingTraceId(self,tracingTraceId):
		try :
			if not isinstance(tracingTraceId,str):
				raise TypeError("tracingTraceId must be set to str value")
			self._tracingTraceId = tracingTraceId
		except Exception as e :
			raise e


	'''
	get recType
	'''
	@property
	def recType(self) :
		try:
			return self._recType
		except Exception as e :
			raise e
	'''
	set recType
	'''
	@recType.setter
	def recType(self,recType):
		try :
			if not isinstance(recType,str):
				raise TypeError("recType must be set to str value")
			self._recType = recType
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
			if not isinstance(server_rsp_time,int):
				raise TypeError("server_rsp_time must be set to int value")
			self._server_rsp_time = server_rsp_time
		except Exception as e :
			raise e


	'''
	get sslFLagsFE
	'''
	@property
	def sslFLagsFE(self) :
		try:
			return self._sslFLagsFE
		except Exception as e :
			raise e
	'''
	set sslFLagsFE
	'''
	@sslFLagsFE.setter
	def sslFLagsFE(self,sslFLagsFE):
		try :
			if not isinstance(sslFLagsFE,long):
				raise TypeError("sslFLagsFE must be set to long value")
			self._sslFLagsFE = sslFLagsFE
		except Exception as e :
			raise e


	'''
	get srvrTcpJitter
	'''
	@property
	def srvrTcpJitter(self) :
		try:
			return self._srvrTcpJitter
		except Exception as e :
			raise e
	'''
	set srvrTcpJitter
	'''
	@srvrTcpJitter.setter
	def srvrTcpJitter(self,srvrTcpJitter):
		try :
			if not isinstance(srvrTcpJitter,long):
				raise TypeError("srvrTcpJitter must be set to long value")
			self._srvrTcpJitter = srvrTcpJitter
		except Exception as e :
			raise e


	'''
	get httpResRcvFB
	'''
	@property
	def httpResRcvFB(self) :
		try:
			return self._httpResRcvFB
		except Exception as e :
			raise e
	'''
	set httpResRcvFB
	'''
	@httpResRcvFB.setter
	def httpResRcvFB(self,httpResRcvFB):
		try :
			if not isinstance(httpResRcvFB,long):
				raise TypeError("httpResRcvFB must be set to long value")
			self._httpResRcvFB = httpResRcvFB
		except Exception as e :
			raise e


	'''
	get transactionId
	'''
	@property
	def transactionId(self) :
		try:
			return self._transactionId
		except Exception as e :
			raise e
	'''
	set transactionId
	'''
	@transactionId.setter
	def transactionId(self,transactionId):
		try :
			if not isinstance(transactionId,long):
				raise TypeError("transactionId must be set to long value")
			self._transactionId = transactionId
		except Exception as e :
			raise e


	'''
	get clntTcpZeroWindowCount
	'''
	@property
	def clntTcpZeroWindowCount(self) :
		try:
			return self._clntTcpZeroWindowCount
		except Exception as e :
			raise e
	'''
	set clntTcpZeroWindowCount
	'''
	@clntTcpZeroWindowCount.setter
	def clntTcpZeroWindowCount(self,clntTcpZeroWindowCount):
		try :
			if not isinstance(clntTcpZeroWindowCount,long):
				raise TypeError("clntTcpZeroWindowCount must be set to long value")
			self._clntTcpZeroWindowCount = clntTcpZeroWindowCount
		except Exception as e :
			raise e


	'''
	get tracingReqSpanId
	'''
	@property
	def tracingReqSpanId(self) :
		try:
			return self._tracingReqSpanId
		except Exception as e :
			raise e
	'''
	set tracingReqSpanId
	'''
	@tracingReqSpanId.setter
	def tracingReqSpanId(self,tracingReqSpanId):
		try :
			if not isinstance(tracingReqSpanId,str):
				raise TypeError("tracingReqSpanId must be set to str value")
			self._tracingReqSpanId = tracingReqSpanId
		except Exception as e :
			raise e


	'''
	get httpReqHost
	'''
	@property
	def httpReqHost(self) :
		try:
			return self._httpReqHost
		except Exception as e :
			raise e
	'''
	set httpReqHost
	'''
	@httpReqHost.setter
	def httpReqHost(self,httpReqHost):
		try :
			if not isinstance(httpReqHost,str):
				raise TypeError("httpReqHost must be set to str value")
			self._httpReqHost = httpReqHost
		except Exception as e :
			raise e


	'''
	get httpReqRcvFB
	'''
	@property
	def httpReqRcvFB(self) :
		try:
			return self._httpReqRcvFB
		except Exception as e :
			raise e
	'''
	set httpReqRcvFB
	'''
	@httpReqRcvFB.setter
	def httpReqRcvFB(self,httpReqRcvFB):
		try :
			if not isinstance(httpReqRcvFB,long):
				raise TypeError("httpReqRcvFB must be set to long value")
			self._httpReqRcvFB = httpReqRcvFB
		except Exception as e :
			raise e


	'''
	get srvrFastRetxCount
	'''
	@property
	def srvrFastRetxCount(self) :
		try:
			return self._srvrFastRetxCount
		except Exception as e :
			raise e
	'''
	set srvrFastRetxCount
	'''
	@srvrFastRetxCount.setter
	def srvrFastRetxCount(self,srvrFastRetxCount):
		try :
			if not isinstance(srvrFastRetxCount,long):
				raise TypeError("srvrFastRetxCount must be set to long value")
			self._srvrFastRetxCount = srvrFastRetxCount
		except Exception as e :
			raise e


	'''
	get tracingReqParentSpanId
	'''
	@property
	def tracingReqParentSpanId(self) :
		try:
			return self._tracingReqParentSpanId
		except Exception as e :
			raise e
	'''
	set tracingReqParentSpanId
	'''
	@tracingReqParentSpanId.setter
	def tracingReqParentSpanId(self,tracingReqParentSpanId):
		try :
			if not isinstance(tracingReqParentSpanId,str):
				raise TypeError("tracingReqParentSpanId must be set to str value")
			self._tracingReqParentSpanId = tracingReqParentSpanId
		except Exception as e :
			raise e


	'''
	get sslCipherValueFE
	'''
	@property
	def sslCipherValueFE(self) :
		try:
			return self._sslCipherValueFE
		except Exception as e :
			raise e
	'''
	set sslCipherValueFE
	'''
	@sslCipherValueFE.setter
	def sslCipherValueFE(self,sslCipherValueFE):
		try :
			if not isinstance(sslCipherValueFE,long):
				raise TypeError("sslCipherValueFE must be set to long value")
			self._sslCipherValueFE = sslCipherValueFE
		except Exception as e :
			raise e


	'''
	get aaaUserEmailId
	'''
	@property
	def aaaUserEmailId(self) :
		try:
			return self._aaaUserEmailId
		except Exception as e :
			raise e
	'''
	set aaaUserEmailId
	'''
	@aaaUserEmailId.setter
	def aaaUserEmailId(self,aaaUserEmailId):
		try :
			if not isinstance(aaaUserEmailId,str):
				raise TypeError("aaaUserEmailId must be set to str value")
			self._aaaUserEmailId = aaaUserEmailId
		except Exception as e :
			raise e


	'''
	get clntTcpPacketsRetransmited
	'''
	@property
	def clntTcpPacketsRetransmited(self) :
		try:
			return self._clntTcpPacketsRetransmited
		except Exception as e :
			raise e
	'''
	set clntTcpPacketsRetransmited
	'''
	@clntTcpPacketsRetransmited.setter
	def clntTcpPacketsRetransmited(self,clntTcpPacketsRetransmited):
		try :
			if not isinstance(clntTcpPacketsRetransmited,long):
				raise TypeError("clntTcpPacketsRetransmited must be set to long value")
			self._clntTcpPacketsRetransmited = clntTcpPacketsRetransmited
		except Exception as e :
			raise e


	'''
	get login_attempt
	'''
	@property
	def login_attempt(self) :
		try:
			return self._login_attempt
		except Exception as e :
			raise e
	'''
	set login_attempt
	'''
	@login_attempt.setter
	def login_attempt(self,login_attempt):
		try :
			if not isinstance(login_attempt,long):
				raise TypeError("login_attempt must be set to long value")
			self._login_attempt = login_attempt
		except Exception as e :
			raise e


	'''
	get appresponsetime
	'''
	@property
	def appresponsetime(self) :
		try:
			return self._appresponsetime
		except Exception as e :
			raise e
	'''
	set appresponsetime
	'''
	@appresponsetime.setter
	def appresponsetime(self,appresponsetime):
		try :
			if not isinstance(appresponsetime,int):
				raise TypeError("appresponsetime must be set to int value")
			self._appresponsetime = appresponsetime
		except Exception as e :
			raise e


	'''
	get sslFLagsBE
	'''
	@property
	def sslFLagsBE(self) :
		try:
			return self._sslFLagsBE
		except Exception as e :
			raise e
	'''
	set sslFLagsBE
	'''
	@sslFLagsBE.setter
	def sslFLagsBE(self,sslFLagsBE):
		try :
			if not isinstance(sslFLagsBE,long):
				raise TypeError("sslFLagsBE must be set to long value")
			self._sslFLagsBE = sslFLagsBE
		except Exception as e :
			raise e


	'''
	get clntTcpRtoCount
	'''
	@property
	def clntTcpRtoCount(self) :
		try:
			return self._clntTcpRtoCount
		except Exception as e :
			raise e
	'''
	set clntTcpRtoCount
	'''
	@clntTcpRtoCount.setter
	def clntTcpRtoCount(self,clntTcpRtoCount):
		try :
			if not isinstance(clntTcpRtoCount,long):
				raise TypeError("clntTcpRtoCount must be set to long value")
			self._clntTcpRtoCount = clntTcpRtoCount
		except Exception as e :
			raise e


	'''
	get source_svcname
	'''
	@property
	def source_svcname(self) :
		try:
			return self._source_svcname
		except Exception as e :
			raise e
	'''
	set source_svcname
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
	get VPNsessionID
	'''
	@property
	def VPNsessionID(self) :
		try:
			return self._VPNsessionID
		except Exception as e :
			raise e
	'''
	set VPNsessionID
	'''
	@VPNsessionID.setter
	def VPNsessionID(self,VPNsessionID):
		try :
			if not isinstance(VPNsessionID,str):
				raise TypeError("VPNsessionID must be set to str value")
			self._VPNsessionID = VPNsessionID
		except Exception as e :
			raise e


	'''
	get source_cluster_name
	'''
	@property
	def source_cluster_name(self) :
		try:
			return self._source_cluster_name
		except Exception as e :
			raise e
	'''
	set source_cluster_name
	'''
	@source_cluster_name.setter
	def source_cluster_name(self,source_cluster_name):
		try :
			if not isinstance(source_cluster_name,str):
				raise TypeError("source_cluster_name must be set to str value")
			self._source_cluster_name = source_cluster_name
		except Exception as e :
			raise e


	'''
	get srvrTcpPacketsRetransmited
	'''
	@property
	def srvrTcpPacketsRetransmited(self) :
		try:
			return self._srvrTcpPacketsRetransmited
		except Exception as e :
			raise e
	'''
	set srvrTcpPacketsRetransmited
	'''
	@srvrTcpPacketsRetransmited.setter
	def srvrTcpPacketsRetransmited(self,srvrTcpPacketsRetransmited):
		try :
			if not isinstance(srvrTcpPacketsRetransmited,long):
				raise TypeError("srvrTcpPacketsRetransmited must be set to long value")
			self._srvrTcpPacketsRetransmited = srvrTcpPacketsRetransmited
		except Exception as e :
			raise e


	'''
	get httpDomainName
	'''
	@property
	def httpDomainName(self) :
		try:
			return self._httpDomainName
		except Exception as e :
			raise e
	'''
	set httpDomainName
	'''
	@httpDomainName.setter
	def httpDomainName(self,httpDomainName):
		try :
			if not isinstance(httpDomainName,str):
				raise TypeError("httpDomainName must be set to str value")
			self._httpDomainName = httpDomainName
		except Exception as e :
			raise e


	'''
	get transCltIpv4Address
	'''
	@property
	def transCltIpv4Address(self) :
		try:
			return self._transCltIpv4Address
		except Exception as e :
			raise e
	'''
	set transCltIpv4Address
	'''
	@transCltIpv4Address.setter
	def transCltIpv4Address(self,transCltIpv4Address):
		try :
			if not isinstance(transCltIpv4Address,long):
				raise TypeError("transCltIpv4Address must be set to long value")
			self._transCltIpv4Address = transCltIpv4Address
		except Exception as e :
			raise e


	'''
	get httpContentType
	'''
	@property
	def httpContentType(self) :
		try:
			return self._httpContentType
		except Exception as e :
			raise e
	'''
	set httpContentType
	'''
	@httpContentType.setter
	def httpContentType(self,httpContentType):
		try :
			if not isinstance(httpContentType,str):
				raise TypeError("httpContentType must be set to str value")
			self._httpContentType = httpContentType
		except Exception as e :
			raise e


	'''
	get transCltDstIpv4Address
	'''
	@property
	def transCltDstIpv4Address(self) :
		try:
			return self._transCltDstIpv4Address
		except Exception as e :
			raise e
	'''
	set transCltDstIpv4Address
	'''
	@transCltDstIpv4Address.setter
	def transCltDstIpv4Address(self,transCltDstIpv4Address):
		try :
			if not isinstance(transCltDstIpv4Address,long):
				raise TypeError("transCltDstIpv4Address must be set to long value")
			self._transCltDstIpv4Address = transCltDstIpv4Address
		except Exception as e :
			raise e


	'''
	get App backendSvrIpv4Address
	'''
	@property
	def backendSvrIpv4Address(self) :
		try:
			return self._backendSvrIpv4Address
		except Exception as e :
			raise e
	'''
	set App backendSvrIpv4Address
	'''
	@backendSvrIpv4Address.setter
	def backendSvrIpv4Address(self,backendSvrIpv4Address):
		try :
			if not isinstance(backendSvrIpv4Address,long):
				raise TypeError("backendSvrIpv4Address must be set to long value")
			self._backendSvrIpv4Address = backendSvrIpv4Address
		except Exception as e :
			raise e


	'''
	get ns_processing_time
	'''
	@property
	def ns_processing_time(self) :
		try:
			return self._ns_processing_time
		except Exception as e :
			raise e
	'''
	set ns_processing_time
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
	get httpReqUrl
	'''
	@property
	def httpReqUrl(self) :
		try:
			return self._httpReqUrl
		except Exception as e :
			raise e
	'''
	set httpReqUrl
	'''
	@httpReqUrl.setter
	def httpReqUrl(self,httpReqUrl):
		try :
			if not isinstance(httpReqUrl,str):
				raise TypeError("httpReqUrl must be set to str value")
			self._httpReqUrl = httpReqUrl
		except Exception as e :
			raise e


	'''
	get svrTcpFlagsTx
	'''
	@property
	def svrTcpFlagsTx(self) :
		try:
			return self._svrTcpFlagsTx
		except Exception as e :
			raise e
	'''
	set svrTcpFlagsTx
	'''
	@svrTcpFlagsTx.setter
	def svrTcpFlagsTx(self,svrTcpFlagsTx):
		try :
			if not isinstance(svrTcpFlagsTx,long):
				raise TypeError("svrTcpFlagsTx must be set to long value")
			self._svrTcpFlagsTx = svrTcpFlagsTx
		except Exception as e :
			raise e


	'''
	get dest_svcname
	'''
	@property
	def dest_svcname(self) :
		try:
			return self._dest_svcname
		except Exception as e :
			raise e
	'''
	set dest_svcname
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
	get httpReqMethod
	'''
	@property
	def httpReqMethod(self) :
		try:
			return self._httpReqMethod
		except Exception as e :
			raise e
	'''
	set httpReqMethod
	'''
	@httpReqMethod.setter
	def httpReqMethod(self,httpReqMethod):
		try :
			if not isinstance(httpReqMethod,str):
				raise TypeError("httpReqMethod must be set to str value")
			self._httpReqMethod = httpReqMethod
		except Exception as e :
			raise e


	'''
	get App Name Vsver ls
	'''
	@property
	def appNameVserverLs(self) :
		try:
			return self._appNameVserverLs
		except Exception as e :
			raise e
	'''
	set App Name Vsver ls
	'''
	@appNameVserverLs.setter
	def appNameVserverLs(self,appNameVserverLs):
		try :
			if not isinstance(appNameVserverLs,str):
				raise TypeError("appNameVserverLs must be set to str value")
			self._appNameVserverLs = appNameVserverLs
		except Exception as e :
			raise e


	'''
	get source_namespace
	'''
	@property
	def source_namespace(self) :
		try:
			return self._source_namespace
		except Exception as e :
			raise e
	'''
	set source_namespace
	'''
	@source_namespace.setter
	def source_namespace(self,source_namespace):
		try :
			if not isinstance(source_namespace,str):
				raise TypeError("source_namespace must be set to str value")
			self._source_namespace = source_namespace
		except Exception as e :
			raise e


	'''
	get api_auth_attempt
	'''
	@property
	def api_auth_attempt(self) :
		try:
			return self._api_auth_attempt
		except Exception as e :
			raise e
	'''
	set api_auth_attempt
	'''
	@api_auth_attempt.setter
	def api_auth_attempt(self,api_auth_attempt):
		try :
			if not isinstance(api_auth_attempt,long):
				raise TypeError("api_auth_attempt must be set to long value")
			self._api_auth_attempt = api_auth_attempt
		except Exception as e :
			raise e


	'''
	get session_track_method
	'''
	@property
	def session_track_method(self) :
		try:
			return self._session_track_method
		except Exception as e :
			raise e
	'''
	set session_track_method
	'''
	@session_track_method.setter
	def session_track_method(self,session_track_method):
		try :
			if not isinstance(session_track_method,int):
				raise TypeError("session_track_method must be set to int value")
			self._session_track_method = session_track_method
		except Exception as e :
			raise e


	'''
	get recSubType
	'''
	@property
	def recSubType(self) :
		try:
			return self._recSubType
		except Exception as e :
			raise e
	'''
	set recSubType
	'''
	@recSubType.setter
	def recSubType(self,recSubType):
		try :
			if not isinstance(recSubType,int):
				raise TypeError("recSubType must be set to int value")
			self._recSubType = recSubType
		except Exception as e :
			raise e


	'''
	get dest_namespace
	'''
	@property
	def dest_namespace(self) :
		try:
			return self._dest_namespace
		except Exception as e :
			raise e
	'''
	set dest_namespace
	'''
	@dest_namespace.setter
	def dest_namespace(self,dest_namespace):
		try :
			if not isinstance(dest_namespace,str):
				raise TypeError("dest_namespace must be set to str value")
			self._dest_namespace = dest_namespace
		except Exception as e :
			raise e


	'''
	get dest_labels
	'''
	@property
	def dest_labels(self) :
		try:
			return self._dest_labels
		except Exception as e :
			raise e
	'''
	set dest_labels
	'''
	@dest_labels.setter
	def dest_labels(self,dest_labels):
		try :
			if not isinstance(dest_labels,str):
				raise TypeError("dest_labels must be set to str value")
			self._dest_labels = dest_labels
		except Exception as e :
			raise e


	'''
	get httpReqReferer
	'''
	@property
	def httpReqReferer(self) :
		try:
			return self._httpReqReferer
		except Exception as e :
			raise e
	'''
	set httpReqReferer
	'''
	@httpReqReferer.setter
	def httpReqReferer(self,httpReqReferer):
		try :
			if not isinstance(httpReqReferer,str):
				raise TypeError("httpReqReferer must be set to str value")
			self._httpReqReferer = httpReqReferer
		except Exception as e :
			raise e


	'''
	get login_result
	'''
	@property
	def login_result(self) :
		try:
			return self._login_result
		except Exception as e :
			raise e
	'''
	set login_result
	'''
	@login_result.setter
	def login_result(self,login_result):
		try :
			if not isinstance(login_result,long):
				raise TypeError("login_result must be set to long value")
			self._login_result = login_result
		except Exception as e :
			raise e


	'''
	get srvrTcpZeroWindowCount
	'''
	@property
	def srvrTcpZeroWindowCount(self) :
		try:
			return self._srvrTcpZeroWindowCount
		except Exception as e :
			raise e
	'''
	set srvrTcpZeroWindowCount
	'''
	@srvrTcpZeroWindowCount.setter
	def srvrTcpZeroWindowCount(self,srvrTcpZeroWindowCount):
		try :
			if not isinstance(srvrTcpZeroWindowCount,long):
				raise TypeError("srvrTcpZeroWindowCount must be set to long value")
			self._srvrTcpZeroWindowCount = srvrTcpZeroWindowCount
		except Exception as e :
			raise e


	'''
	get sslSigHashAlgBE
	'''
	@property
	def sslSigHashAlgBE(self) :
		try:
			return self._sslSigHashAlgBE
		except Exception as e :
			raise e
	'''
	set sslSigHashAlgBE
	'''
	@sslSigHashAlgBE.setter
	def sslSigHashAlgBE(self,sslSigHashAlgBE):
		try :
			if not isinstance(sslSigHashAlgBE,long):
				raise TypeError("sslSigHashAlgBE must be set to long value")
			self._sslSigHashAlgBE = sslSigHashAlgBE
		except Exception as e :
			raise e


	'''
	get sslCipherValueBE
	'''
	@property
	def sslCipherValueBE(self) :
		try:
			return self._sslCipherValueBE
		except Exception as e :
			raise e
	'''
	set sslCipherValueBE
	'''
	@sslCipherValueBE.setter
	def sslCipherValueBE(self,sslCipherValueBE):
		try :
			if not isinstance(sslCipherValueBE,long):
				raise TypeError("sslCipherValueBE must be set to long value")
			self._sslCipherValueBE = sslCipherValueBE
		except Exception as e :
			raise e


	'''
	get httpResForwFB
	'''
	@property
	def httpResForwFB(self) :
		try:
			return self._httpResForwFB
		except Exception as e :
			raise e
	'''
	set httpResForwFB
	'''
	@httpResForwFB.setter
	def httpResForwFB(self,httpResForwFB):
		try :
			if not isinstance(httpResForwFB,long):
				raise TypeError("httpResForwFB must be set to long value")
			self._httpResForwFB = httpResForwFB
		except Exception as e :
			raise e


	'''
	get httpReqRcvLB
	'''
	@property
	def httpReqRcvLB(self) :
		try:
			return self._httpReqRcvLB
		except Exception as e :
			raise e
	'''
	set httpReqRcvLB
	'''
	@httpReqRcvLB.setter
	def httpReqRcvLB(self,httpReqRcvLB):
		try :
			if not isinstance(httpReqRcvLB,long):
				raise TypeError("httpReqRcvLB must be set to long value")
			self._httpReqRcvLB = httpReqRcvLB
		except Exception as e :
			raise e


	'''
	get transaction_start_time
	'''
	@property
	def transaction_start_time(self) :
		try:
			return self._transaction_start_time
		except Exception as e :
			raise e
	'''
	set transaction_start_time
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
	get httpTransEndTime
	'''
	@property
	def httpTransEndTime(self) :
		try:
			return self._httpTransEndTime
		except Exception as e :
			raise e
	'''
	set httpTransEndTime
	'''
	@httpTransEndTime.setter
	def httpTransEndTime(self,httpTransEndTime):
		try :
			if not isinstance(httpTransEndTime,long):
				raise TypeError("httpTransEndTime must be set to long value")
			self._httpTransEndTime = httpTransEndTime
		except Exception as e :
			raise e


	'''
	get clntTcpJitter
	'''
	@property
	def clntTcpJitter(self) :
		try:
			return self._clntTcpJitter
		except Exception as e :
			raise e
	'''
	set clntTcpJitter
	'''
	@clntTcpJitter.setter
	def clntTcpJitter(self,clntTcpJitter):
		try :
			if not isinstance(clntTcpJitter,long):
				raise TypeError("clntTcpJitter must be set to long value")
			self._clntTcpJitter = clntTcpJitter
		except Exception as e :
			raise e


	'''
	get transCltTotRxOctCnt
	'''
	@property
	def transCltTotRxOctCnt(self) :
		try:
			return self._transCltTotRxOctCnt
		except Exception as e :
			raise e
	'''
	set transCltTotRxOctCnt
	'''
	@transCltTotRxOctCnt.setter
	def transCltTotRxOctCnt(self,transCltTotRxOctCnt):
		try :
			if not isinstance(transCltTotRxOctCnt,long):
				raise TypeError("transCltTotRxOctCnt must be set to long value")
			self._transCltTotRxOctCnt = transCltTotRxOctCnt
		except Exception as e :
			raise e


	'''
	get api_auth_result
	'''
	@property
	def api_auth_result(self) :
		try:
			return self._api_auth_result
		except Exception as e :
			raise e
	'''
	set api_auth_result
	'''
	@api_auth_result.setter
	def api_auth_result(self,api_auth_result):
		try :
			if not isinstance(api_auth_result,long):
				raise TypeError("api_auth_result must be set to long value")
			self._api_auth_result = api_auth_result
		except Exception as e :
			raise e


	'''
	get App cltTcpFlagsTx
	'''
	@property
	def cltTcpFlagsTx(self) :
		try:
			return self._cltTcpFlagsTx
		except Exception as e :
			raise e
	'''
	set App cltTcpFlagsTx
	'''
	@cltTcpFlagsTx.setter
	def cltTcpFlagsTx(self,cltTcpFlagsTx):
		try :
			if not isinstance(cltTcpFlagsTx,long):
				raise TypeError("cltTcpFlagsTx must be set to long value")
			self._cltTcpFlagsTx = cltTcpFlagsTx
		except Exception as e :
			raise e


	'''
	get transSvrRTT
	'''
	@property
	def transSvrRTT(self) :
		try:
			return self._transSvrRTT
		except Exception as e :
			raise e
	'''
	set transSvrRTT
	'''
	@transSvrRTT.setter
	def transSvrRTT(self,transSvrRTT):
		try :
			if not isinstance(transSvrRTT,long):
				raise TypeError("transSvrRTT must be set to long value")
			self._transSvrRTT = transSvrRTT
		except Exception as e :
			raise e


	'''
	get App Name
	'''
	@property
	def appName(self) :
		try:
			return self._appName
		except Exception as e :
			raise e
	'''
	set App Name
	'''
	@appName.setter
	def appName(self,appName):
		try :
			if not isinstance(appName,str):
				raise TypeError("appName must be set to str value")
			self._appName = appName
		except Exception as e :
			raise e


	'''
	get sslHandshakeErrorMsg
	'''
	@property
	def sslHandshakeErrorMsg(self) :
		try:
			return self._sslHandshakeErrorMsg
		except Exception as e :
			raise e
	'''
	set sslHandshakeErrorMsg
	'''
	@sslHandshakeErrorMsg.setter
	def sslHandshakeErrorMsg(self,sslHandshakeErrorMsg):
		try :
			if not isinstance(sslHandshakeErrorMsg,long):
				raise TypeError("sslHandshakeErrorMsg must be set to long value")
			self._sslHandshakeErrorMsg = sslHandshakeErrorMsg
		except Exception as e :
			raise e


	'''
	get transCltRTT
	'''
	@property
	def transCltRTT(self) :
		try:
			return self._transCltRTT
		except Exception as e :
			raise e
	'''
	set transCltRTT
	'''
	@transCltRTT.setter
	def transCltRTT(self,transCltRTT):
		try :
			if not isinstance(transCltRTT,long):
				raise TypeError("transCltRTT must be set to long value")
			self._transCltRTT = transCltRTT
		except Exception as e :
			raise e


	'''
	get httpReqForwLB
	'''
	@property
	def httpReqForwLB(self) :
		try:
			return self._httpReqForwLB
		except Exception as e :
			raise e
	'''
	set httpReqForwLB
	'''
	@httpReqForwLB.setter
	def httpReqForwLB(self,httpReqForwLB):
		try :
			if not isinstance(httpReqForwLB,long):
				raise TypeError("httpReqForwLB must be set to long value")
			self._httpReqForwLB = httpReqForwLB
		except Exception as e :
			raise e


	'''
	get transCltTotTxOctCnt
	'''
	@property
	def transCltTotTxOctCnt(self) :
		try:
			return self._transCltTotTxOctCnt
		except Exception as e :
			raise e
	'''
	set transCltTotTxOctCnt
	'''
	@transCltTotTxOctCnt.setter
	def transCltTotTxOctCnt(self,transCltTotTxOctCnt):
		try :
			if not isinstance(transCltTotTxOctCnt,long):
				raise TypeError("transCltTotTxOctCnt must be set to long value")
			self._transCltTotTxOctCnt = transCltTotTxOctCnt
		except Exception as e :
			raise e


	'''
	get httpRspStatus
	'''
	@property
	def httpRspStatus(self) :
		try:
			return self._httpRspStatus
		except Exception as e :
			raise e
	'''
	set httpRspStatus
	'''
	@httpRspStatus.setter
	def httpRspStatus(self,httpRspStatus):
		try :
			if not isinstance(httpRspStatus,long):
				raise TypeError("httpRspStatus must be set to long value")
			self._httpRspStatus = httpRspStatus
		except Exception as e :
			raise e


	'''
	get App cltTcpFlagsRx
	'''
	@property
	def cltTcpFlagsRx(self) :
		try:
			return self._cltTcpFlagsRx
		except Exception as e :
			raise e
	'''
	set App cltTcpFlagsRx
	'''
	@cltTcpFlagsRx.setter
	def cltTcpFlagsRx(self,cltTcpFlagsRx):
		try :
			if not isinstance(cltTcpFlagsRx,long):
				raise TypeError("cltTcpFlagsRx must be set to long value")
			self._cltTcpFlagsRx = cltTcpFlagsRx
		except Exception as e :
			raise e


	'''
	get httpReqUserAgent
	'''
	@property
	def httpReqUserAgent(self) :
		try:
			return self._httpReqUserAgent
		except Exception as e :
			raise e
	'''
	set httpReqUserAgent
	'''
	@httpReqUserAgent.setter
	def httpReqUserAgent(self,httpReqUserAgent):
		try :
			if not isinstance(httpReqUserAgent,str):
				raise TypeError("httpReqUserAgent must be set to str value")
			self._httpReqUserAgent = httpReqUserAgent
		except Exception as e :
			raise e


	'''
	get httpResRcvLB
	'''
	@property
	def httpResRcvLB(self) :
		try:
			return self._httpResRcvLB
		except Exception as e :
			raise e
	'''
	set httpResRcvLB
	'''
	@httpResRcvLB.setter
	def httpResRcvLB(self,httpResRcvLB):
		try :
			if not isinstance(httpResRcvLB,long):
				raise TypeError("httpResRcvLB must be set to long value")
			self._httpResRcvLB = httpResRcvLB
		except Exception as e :
			raise e


	'''
	get aaaUsername
	'''
	@property
	def aaaUsername(self) :
		try:
			return self._aaaUsername
		except Exception as e :
			raise e
	'''
	set aaaUsername
	'''
	@aaaUsername.setter
	def aaaUsername(self,aaaUsername):
		try :
			if not isinstance(aaaUsername,str):
				raise TypeError("aaaUsername must be set to str value")
			self._aaaUsername = aaaUsername
		except Exception as e :
			raise e


	'''
	get clntFastRetxCount
	'''
	@property
	def clntFastRetxCount(self) :
		try:
			return self._clntFastRetxCount
		except Exception as e :
			raise e
	'''
	set clntFastRetxCount
	'''
	@clntFastRetxCount.setter
	def clntFastRetxCount(self,clntFastRetxCount):
		try :
			if not isinstance(clntFastRetxCount,long):
				raise TypeError("clntFastRetxCount must be set to long value")
			self._clntFastRetxCount = clntFastRetxCount
		except Exception as e :
			raise e


	'''
	get sslErrFlag
	'''
	@property
	def sslErrFlag(self) :
		try:
			return self._sslErrFlag
		except Exception as e :
			raise e
	'''
	set sslErrFlag
	'''
	@sslErrFlag.setter
	def sslErrFlag(self,sslErrFlag):
		try :
			if not isinstance(sslErrFlag,long):
				raise TypeError("sslErrFlag must be set to long value")
			self._sslErrFlag = sslErrFlag
		except Exception as e :
			raise e


	'''
	get httpReqForwFB
	'''
	@property
	def httpReqForwFB(self) :
		try:
			return self._httpReqForwFB
		except Exception as e :
			raise e
	'''
	set httpReqForwFB
	'''
	@httpReqForwFB.setter
	def httpReqForwFB(self,httpReqForwFB):
		try :
			if not isinstance(httpReqForwFB,long):
				raise TypeError("httpReqForwFB must be set to long value")
			self._httpReqForwFB = httpReqForwFB
		except Exception as e :
			raise e


	'''
	get sslServerCertSizeFE
	'''
	@property
	def sslServerCertSizeFE(self) :
		try:
			return self._sslServerCertSizeFE
		except Exception as e :
			raise e
	'''
	set sslServerCertSizeFE
	'''
	@sslServerCertSizeFE.setter
	def sslServerCertSizeFE(self,sslServerCertSizeFE):
		try :
			if not isinstance(sslServerCertSizeFE,long):
				raise TypeError("sslServerCertSizeFE must be set to long value")
			self._sslServerCertSizeFE = sslServerCertSizeFE
		except Exception as e :
			raise e


	'''
	get application_name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set application_name
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
	get svrTcpFlagsRx
	'''
	@property
	def svrTcpFlagsRx(self) :
		try:
			return self._svrTcpFlagsRx
		except Exception as e :
			raise e
	'''
	set svrTcpFlagsRx
	'''
	@svrTcpFlagsRx.setter
	def svrTcpFlagsRx(self,svrTcpFlagsRx):
		try :
			if not isinstance(svrTcpFlagsRx,long):
				raise TypeError("svrTcpFlagsRx must be set to long value")
			self._svrTcpFlagsRx = svrTcpFlagsRx
		except Exception as e :
			raise e


	'''
	get httpReqXForwardedFor
	'''
	@property
	def httpReqXForwardedFor(self) :
		try:
			return self._httpReqXForwardedFor
		except Exception as e :
			raise e
	'''
	set httpReqXForwardedFor
	'''
	@httpReqXForwardedFor.setter
	def httpReqXForwardedFor(self,httpReqXForwardedFor):
		try :
			if not isinstance(httpReqXForwardedFor,str):
				raise TypeError("httpReqXForwardedFor must be set to str value")
			self._httpReqXForwardedFor = httpReqXForwardedFor
		except Exception as e :
			raise e


	'''
	get srvrTcpRtoCount
	'''
	@property
	def srvrTcpRtoCount(self) :
		try:
			return self._srvrTcpRtoCount
		except Exception as e :
			raise e
	'''
	set srvrTcpRtoCount
	'''
	@srvrTcpRtoCount.setter
	def srvrTcpRtoCount(self,srvrTcpRtoCount):
		try :
			if not isinstance(srvrTcpRtoCount,long):
				raise TypeError("srvrTcpRtoCount must be set to long value")
			self._srvrTcpRtoCount = srvrTcpRtoCount
		except Exception as e :
			raise e


	'''
	get session_attribute
	'''
	@property
	def session_attribute(self) :
		try:
			return self._session_attribute
		except Exception as e :
			raise e
	'''
	set session_attribute
	'''
	@session_attribute.setter
	def session_attribute(self,session_attribute):
		try :
			if not isinstance(session_attribute,str):
				raise TypeError("session_attribute must be set to str value")
			self._session_attribute = session_attribute
		except Exception as e :
			raise e


	'''
	get source_labels
	'''
	@property
	def source_labels(self) :
		try:
			return self._source_labels
		except Exception as e :
			raise e
	'''
	set source_labels
	'''
	@source_labels.setter
	def source_labels(self,source_labels):
		try :
			if not isinstance(source_labels,str):
				raise TypeError("source_labels must be set to str value")
			self._source_labels = source_labels
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_dplite_transaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_dplite_transaction
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_dplite_transaction_responses, response, "aa_dplite_transaction_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_dplite_transaction_response_array
				i=0
				error = [aa_dplite_transaction() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_dplite_transaction_response_array
			i=0
			aa_dplite_transaction_objs = [aa_dplite_transaction() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_aa_dplite_transaction'):
					for props in obj._aa_dplite_transaction:
						result = service.payload_formatter.string_to_bulk_resource(aa_dplite_transaction_response,self.__class__.__name__,props)
						aa_dplite_transaction_objs[i] = result.aa_dplite_transaction
						i=i+1
			return aa_dplite_transaction_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_dplite_transaction,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_dplite_transaction_response(base_response):
	def __init__(self,length=1) :
		self.aa_dplite_transaction= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_dplite_transaction= [ aa_dplite_transaction() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_dplite_transaction_responses(base_response):
	def __init__(self,length=1) :
		self.aa_dplite_transaction_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_dplite_transaction_response_array = [ aa_dplite_transaction() for _ in range(length)]
