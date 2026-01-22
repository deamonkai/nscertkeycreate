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
Configuration for Service Graph Nodes Report table for Level 3 resource
'''

class aa_service_graph_nodes_l3(base_resource):
	_ip_address= ""
	_servercertsize= ""
	_vserverls= ""
	_total_bytes= ""
	_svcrt_99= ""
	_ciphervalue= ""
	_svcname= ""
	_frontend_ssl_error_count= ""
	_svcresponsetime= ""
	_frontend_tcp_error_count= ""
	_cipherstrength= ""
	_backend_ssl_error_count= ""
	_rpt_sample_time= ""
	_backend_handshakemsg= ""
	_srvr_cert_hash= ""
	_frontend_handshakemsg= ""
	_cluster_name= ""
	_ctnsappname= ""
	_error_count= ""
	_node_namespace= ""
	_rec_type= ""
	_protocol= ""
	_hits= ""
	_svcrt_95= ""
	_backend_tcp_error_count= ""
	_labels= ""
	_node_type= ""
	_svcrt_999= ""
	_sslversion= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_service_graph_nodes_l3"
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
			return "aa_service_graph_nodes_l3s"
		except Exception as e :
			raise e



	'''
	get Netscaler IP
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Netscaler IP
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
	get SSL certficate size
	'''
	@property
	def servercertsize(self) :
		try:
			return self._servercertsize
		except Exception as e :
			raise e
	'''
	set SSL certficate size
	'''
	@servercertsize.setter
	def servercertsize(self,servercertsize):
		try :
			if not isinstance(servercertsize,int):
				raise TypeError("servercertsize must be set to int value")
			self._servercertsize = servercertsize
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
	get 99 th Percentile of Server response time in sampled timeframe.
	'''
	@property
	def svcrt_99(self) :
		try:
			return self._svcrt_99
		except Exception as e :
			raise e
	'''
	set 99 th Percentile of Server response time in sampled timeframe.
	'''
	@svcrt_99.setter
	def svcrt_99(self,svcrt_99):
		try :
			if not isinstance(svcrt_99,float):
				raise TypeError("svcrt_99 must be set to float value")
			self._svcrt_99 = svcrt_99
		except Exception as e :
			raise e


	'''
	get SSL cipher value
	'''
	@property
	def ciphervalue(self) :
		try:
			return self._ciphervalue
		except Exception as e :
			raise e
	'''
	set SSL cipher value
	'''
	@ciphervalue.setter
	def ciphervalue(self,ciphervalue):
		try :
			if not isinstance(ciphervalue,int):
				raise TypeError("ciphervalue must be set to int value")
			self._ciphervalue = ciphervalue
		except Exception as e :
			raise e


	'''
	get Service Name in Kubernetes
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set Service Name in Kubernetes
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
	get Frontend SSL based errors
	'''
	@property
	def frontend_ssl_error_count(self) :
		try:
			return self._frontend_ssl_error_count
		except Exception as e :
			raise e
	'''
	set Frontend SSL based errors
	'''
	@frontend_ssl_error_count.setter
	def frontend_ssl_error_count(self,frontend_ssl_error_count):
		try :
			if not isinstance(frontend_ssl_error_count,long):
				raise TypeError("frontend_ssl_error_count must be set to long value")
			self._frontend_ssl_error_count = frontend_ssl_error_count
		except Exception as e :
			raise e


	'''
	get svcresponsetime in sampled timeframe.
	'''
	@property
	def svcresponsetime(self) :
		try:
			return self._svcresponsetime
		except Exception as e :
			raise e
	'''
	set svcresponsetime in sampled timeframe.
	'''
	@svcresponsetime.setter
	def svcresponsetime(self,svcresponsetime):
		try :
			if not isinstance(svcresponsetime,long):
				raise TypeError("svcresponsetime must be set to long value")
			self._svcresponsetime = svcresponsetime
		except Exception as e :
			raise e


	'''
	get Number of frontend TCP errors
	'''
	@property
	def frontend_tcp_error_count(self) :
		try:
			return self._frontend_tcp_error_count
		except Exception as e :
			raise e
	'''
	set Number of frontend TCP errors
	'''
	@frontend_tcp_error_count.setter
	def frontend_tcp_error_count(self,frontend_tcp_error_count):
		try :
			if not isinstance(frontend_tcp_error_count,long):
				raise TypeError("frontend_tcp_error_count must be set to long value")
			self._frontend_tcp_error_count = frontend_tcp_error_count
		except Exception as e :
			raise e


	'''
	get SSL cipher strength
	'''
	@property
	def cipherstrength(self) :
		try:
			return self._cipherstrength
		except Exception as e :
			raise e
	'''
	set SSL cipher strength
	'''
	@cipherstrength.setter
	def cipherstrength(self,cipherstrength):
		try :
			if not isinstance(cipherstrength,int):
				raise TypeError("cipherstrength must be set to int value")
			self._cipherstrength = cipherstrength
		except Exception as e :
			raise e


	'''
	get Backend SSL based errors
	'''
	@property
	def backend_ssl_error_count(self) :
		try:
			return self._backend_ssl_error_count
		except Exception as e :
			raise e
	'''
	set Backend SSL based errors
	'''
	@backend_ssl_error_count.setter
	def backend_ssl_error_count(self,backend_ssl_error_count):
		try :
			if not isinstance(backend_ssl_error_count,long):
				raise TypeError("backend_ssl_error_count must be set to long value")
			self._backend_ssl_error_count = backend_ssl_error_count
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
	get Backend HandShake Message.
	'''
	@property
	def backend_handshakemsg(self) :
		try:
			return self._backend_handshakemsg
		except Exception as e :
			raise e
	'''
	set Backend HandShake Message.
	'''
	@backend_handshakemsg.setter
	def backend_handshakemsg(self,backend_handshakemsg):
		try :
			if not isinstance(backend_handshakemsg,int):
				raise TypeError("backend_handshakemsg must be set to int value")
			self._backend_handshakemsg = backend_handshakemsg
		except Exception as e :
			raise e


	'''
	get SSL cerificate hash
	'''
	@property
	def srvr_cert_hash(self) :
		try:
			return self._srvr_cert_hash
		except Exception as e :
			raise e
	'''
	set SSL cerificate hash
	'''
	@srvr_cert_hash.setter
	def srvr_cert_hash(self,srvr_cert_hash):
		try :
			if not isinstance(srvr_cert_hash,int):
				raise TypeError("srvr_cert_hash must be set to int value")
			self._srvr_cert_hash = srvr_cert_hash
		except Exception as e :
			raise e


	'''
	get Frontend HandShake Message.
	'''
	@property
	def frontend_handshakemsg(self) :
		try:
			return self._frontend_handshakemsg
		except Exception as e :
			raise e
	'''
	set Frontend HandShake Message.
	'''
	@frontend_handshakemsg.setter
	def frontend_handshakemsg(self,frontend_handshakemsg):
		try :
			if not isinstance(frontend_handshakemsg,int):
				raise TypeError("frontend_handshakemsg must be set to int value")
			self._frontend_handshakemsg = frontend_handshakemsg
		except Exception as e :
			raise e


	'''
	get Kubernetes cluster name
	'''
	@property
	def cluster_name(self) :
		try:
			return self._cluster_name
		except Exception as e :
			raise e
	'''
	set Kubernetes cluster name
	'''
	@cluster_name.setter
	def cluster_name(self,cluster_name):
		try :
			if not isinstance(cluster_name,str):
				raise TypeError("cluster_name must be set to str value")
			self._cluster_name = cluster_name
		except Exception as e :
			raise e


	'''
	get vserver name
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set vserver name
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
	get Error count based on http response status
	'''
	@property
	def error_count(self) :
		try:
			return self._error_count
		except Exception as e :
			raise e
	'''
	set Error count based on http response status
	'''
	@error_count.setter
	def error_count(self,error_count):
		try :
			if not isinstance(error_count,long):
				raise TypeError("error_count must be set to long value")
			self._error_count = error_count
		except Exception as e :
			raise e


	'''
	get Namespace of service in Kubernetes
	'''
	@property
	def node_namespace(self) :
		try:
			return self._node_namespace
		except Exception as e :
			raise e
	'''
	set Namespace of service in Kubernetes
	'''
	@node_namespace.setter
	def node_namespace(self,node_namespace):
		try :
			if not isinstance(node_namespace,str):
				raise TypeError("node_namespace must be set to str value")
			self._node_namespace = node_namespace
		except Exception as e :
			raise e


	'''
	get Record Type is used for classification of data
	'''
	@property
	def rec_type(self) :
		try:
			return self._rec_type
		except Exception as e :
			raise e
	'''
	set Record Type is used for classification of data
	'''
	@rec_type.setter
	def rec_type(self,rec_type):
		try :
			if not isinstance(rec_type,str):
				raise TypeError("rec_type must be set to str value")
			self._rec_type = rec_type
		except Exception as e :
			raise e


	'''
	get Service Type
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set Service Type
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,str):
				raise TypeError("protocol must be set to str value")
			self._protocol = protocol
		except Exception as e :
			raise e


	'''
	get Hits in sampled timeframe.
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	set Hits in sampled timeframe.
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,long):
				raise TypeError("hits must be set to long value")
			self._hits = hits
		except Exception as e :
			raise e


	'''
	get 95 th Percentile of Server response time in sampled timeframe.
	'''
	@property
	def svcrt_95(self) :
		try:
			return self._svcrt_95
		except Exception as e :
			raise e
	'''
	set 95 th Percentile of Server response time in sampled timeframe.
	'''
	@svcrt_95.setter
	def svcrt_95(self,svcrt_95):
		try :
			if not isinstance(svcrt_95,float):
				raise TypeError("svcrt_95 must be set to float value")
			self._svcrt_95 = svcrt_95
		except Exception as e :
			raise e


	'''
	get Number of backend TCP errors
	'''
	@property
	def backend_tcp_error_count(self) :
		try:
			return self._backend_tcp_error_count
		except Exception as e :
			raise e
	'''
	set Number of backend TCP errors
	'''
	@backend_tcp_error_count.setter
	def backend_tcp_error_count(self,backend_tcp_error_count):
		try :
			if not isinstance(backend_tcp_error_count,long):
				raise TypeError("backend_tcp_error_count must be set to long value")
			self._backend_tcp_error_count = backend_tcp_error_count
		except Exception as e :
			raise e


	'''
	get Labels defined for service
	'''
	@property
	def labels(self) :
		try:
			return self._labels
		except Exception as e :
			raise e
	'''
	set Labels defined for service
	'''
	@labels.setter
	def labels(self,labels):
		try :
			if not isinstance(labels,str):
				raise TypeError("labels must be set to str value")
			self._labels = labels
		except Exception as e :
			raise e


	'''
	get Node Type is used for classification of node
	'''
	@property
	def node_type(self) :
		try:
			return self._node_type
		except Exception as e :
			raise e
	'''
	set Node Type is used for classification of node
	'''
	@node_type.setter
	def node_type(self,node_type):
		try :
			if not isinstance(node_type,str):
				raise TypeError("node_type must be set to str value")
			self._node_type = node_type
		except Exception as e :
			raise e


	'''
	get 99.9 th Percentile of Server response time in sampled timeframe.
	'''
	@property
	def svcrt_999(self) :
		try:
			return self._svcrt_999
		except Exception as e :
			raise e
	'''
	set 99.9 th Percentile of Server response time in sampled timeframe.
	'''
	@svcrt_999.setter
	def svcrt_999(self,svcrt_999):
		try :
			if not isinstance(svcrt_999,float):
				raise TypeError("svcrt_999 must be set to float value")
			self._svcrt_999 = svcrt_999
		except Exception as e :
			raise e


	'''
	get SSL Version used
	'''
	@property
	def sslversion(self) :
		try:
			return self._sslversion
		except Exception as e :
			raise e
	'''
	set SSL Version used
	'''
	@sslversion.setter
	def sslversion(self,sslversion):
		try :
			if not isinstance(sslversion,int):
				raise TypeError("sslversion must be set to int value")
			self._sslversion = sslversion
		except Exception as e :
			raise e

	'''
	Af Report for Service Graph Nodes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_service_graph_nodes_l3_obj=aa_service_graph_nodes_l3()
				response = aa_service_graph_nodes_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_service_graph_nodes_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_service_graph_nodes_l3_obj = aa_service_graph_nodes_l3()
			option_ = options()
			option_._filter=filter_
			return aa_service_graph_nodes_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_service_graph_nodes_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_service_graph_nodes_l3_obj = aa_service_graph_nodes_l3()
			option_ = options()
			option_._count=True
			response = aa_service_graph_nodes_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_service_graph_nodes_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_service_graph_nodes_l3_obj = aa_service_graph_nodes_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_service_graph_nodes_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_service_graph_nodes_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_service_graph_nodes_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_service_graph_nodes_l3_responses, response, "aa_service_graph_nodes_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_service_graph_nodes_l3_response_array
				i=0
				error = [aa_service_graph_nodes_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_service_graph_nodes_l3_response_array
			i=0
			aa_service_graph_nodes_l3_objs = [aa_service_graph_nodes_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_service_graph_nodes_l3:
					result = service.payload_formatter.string_to_bulk_resource(aa_service_graph_nodes_l3_response,self.__class__.__name__,props)
					aa_service_graph_nodes_l3_objs[i] = result.aa_service_graph_nodes_l3
					i=i+1
			return aa_service_graph_nodes_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_service_graph_nodes_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_service_graph_nodes_l3_response(base_response):
	def __init__(self,length=1) :
		self.aa_service_graph_nodes_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_service_graph_nodes_l3= [ aa_service_graph_nodes_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_service_graph_nodes_l3_responses(base_response):
	def __init__(self,length=1) :
		self.aa_service_graph_nodes_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_service_graph_nodes_l3_response_array = [ aa_service_graph_nodes_l3() for _ in range(length)]
