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

from massrc.com.citrix.mas.nitro.resource.config.mps.vm_device import vm_device

'''
Configuration for NetScaler resource
'''

class ns(vm_device):
	_disksize= ""
	_disk1_used= ""
	_instance_id= ""
	_disk1_free= ""
	_system_hardwareversion= ""
	_diskused= ""
	_ns_mgmt_cpu_usage= ""
	_disk0_total= ""
	_is_clip= ""
	_state= ""
	_disk1_total= ""
	_node_state= ""
	_disk0_used= ""
	_diskavail= ""
	_waf_signature_version= ""
	_disk0_free= ""
	_clusterid= ""
	_ns_cpu_usage= ""
	_is_ns_in_use= ""
	_lastconfigsavetime= ""
	_nodeid= ""
	_health= ""
	_license= ""
	_ns_total_tx= ""
	_number_of_ssl_cores_up= ""
	_ns_memory_usage= ""
	_ns_tx= ""
	_ns_rx= ""
	_http_req= ""
	_clip= ""
	_backplane= ""
	_nic_discards_in= ""
	_ns_ip_address= ""
	_last_nonzero_throughput_time= ""
	_diskperusage= ""
	_iscco= ""
	_lastconfigchangedtime= ""
	_number_of_ssl_cards= ""
	_cmd_policy= ""
	_netprofile_metrics_collector= ""
	_ns_observationdomainName= ""
	_ns_observationdomainid= ""
	_ns_total_rx= ""
	_metrics_collection= ""
	_num_pes= ""
	_bot_signature_version= ""
	_pre_auth_key= ""
	_netprofile= ""
	_nic_discards_out= ""
	_customid= ""
	_save_config= ""
	_LS_IP= ""
	_diff_exists= ""
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
			return "ns"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ns,self).get_object_id()
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
			return "nss"
		except Exception as e :
			raise e



	'''
	get NetScaler Disk Size(MB)
	'''
	@property
	def disksize(self) :
		try:
			return self._disksize
		except Exception as e :
			raise e


	'''
	get Disk1 used space in percentage
	'''
	@property
	def disk1_used(self) :
		try:
			return self._disk1_used
		except Exception as e :
			raise e


	'''
	get Id of CPX instance
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e


	'''
	get Disk1 free space in MB
	'''
	@property
	def disk1_free(self) :
		try:
			return self._disk1_free
		except Exception as e :
			raise e


	'''
	get System Hardware Version
	'''
	@property
	def system_hardwareversion(self) :
		try:
			return self._system_hardwareversion
		except Exception as e :
			raise e


	'''
	get NetScaler Disk Used(MB)
	'''
	@property
	def diskused(self) :
		try:
			return self._diskused
		except Exception as e :
			raise e


	'''
	get Management CPU Usage (%)
	'''
	@property
	def ns_mgmt_cpu_usage(self) :
		try:
			return self._ns_mgmt_cpu_usage
		except Exception as e :
			raise e


	'''
	get Disk0 total space in MB
	'''
	@property
	def disk0_total(self) :
		try:
			return self._disk0_total
		except Exception as e :
			raise e


	'''
	get Is Clip
	'''
	@property
	def is_clip(self) :
		try:
			return self._is_clip
		except Exception as e :
			raise e
	'''
	set Is Clip
	'''
	@is_clip.setter
	def is_clip(self,is_clip):
		try :
			if not isinstance(is_clip,bool):
				raise TypeError("is_clip must be set to bool value")
			self._is_clip = is_clip
		except Exception as e :
			raise e


	'''
	get Node State
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Node State
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
	get Disk1 total space in MB
	'''
	@property
	def disk1_total(self) :
		try:
			return self._disk1_total
		except Exception as e :
			raise e


	'''
	get Node State of NetScaler Instance
	'''
	@property
	def node_state(self) :
		try:
			return self._node_state
		except Exception as e :
			raise e


	'''
	get Disk0 used space in percentage
	'''
	@property
	def disk0_used(self) :
		try:
			return self._disk0_used
		except Exception as e :
			raise e


	'''
	get NetScaler Disk Available(MB)
	'''
	@property
	def diskavail(self) :
		try:
			return self._diskavail
		except Exception as e :
			raise e


	'''
	get NetScaler WAF Default signature version
	'''
	@property
	def waf_signature_version(self) :
		try:
			return self._waf_signature_version
		except Exception as e :
			raise e
	'''
	set NetScaler WAF Default signature version
	'''
	@waf_signature_version.setter
	def waf_signature_version(self,waf_signature_version):
		try :
			if not isinstance(waf_signature_version,str):
				raise TypeError("waf_signature_version must be set to str value")
			self._waf_signature_version = waf_signature_version
		except Exception as e :
			raise e


	'''
	get Disk0 Free space in MB
	'''
	@property
	def disk0_free(self) :
		try:
			return self._disk0_free
		except Exception as e :
			raise e


	'''
	get Cluster Id
	'''
	@property
	def clusterid(self) :
		try:
			return self._clusterid
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of NetScaler Instance
	'''
	@property
	def ns_cpu_usage(self) :
		try:
			return self._ns_cpu_usage
		except Exception as e :
			raise e


	'''
	get is_ns_in_use
	'''
	@property
	def is_ns_in_use(self) :
		try:
			return self._is_ns_in_use
		except Exception as e :
			raise e
	'''
	set is_ns_in_use
	'''
	@is_ns_in_use.setter
	def is_ns_in_use(self,is_ns_in_use):
		try :
			if not isinstance(is_ns_in_use,bool):
				raise TypeError("is_ns_in_use must be set to bool value")
			self._is_ns_in_use = is_ns_in_use
		except Exception as e :
			raise e


	'''
	get Last Config Save Time
	'''
	@property
	def lastconfigsavetime(self) :
		try:
			return self._lastconfigsavetime
		except Exception as e :
			raise e
	'''
	set Last Config Save Time
	'''
	@lastconfigsavetime.setter
	def lastconfigsavetime(self,lastconfigsavetime):
		try :
			if not isinstance(lastconfigsavetime,long):
				raise TypeError("lastconfigsavetime must be set to long value")
			self._lastconfigsavetime = lastconfigsavetime
		except Exception as e :
			raise e


	'''
	get Node Id
	'''
	@property
	def nodeid(self) :
		try:
			return self._nodeid
		except Exception as e :
			raise e


	'''
	get Node Health
	'''
	@property
	def health(self) :
		try:
			return self._health
		except Exception as e :
			raise e


	'''
	get Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@property
	def license(self) :
		try:
			return self._license
		except Exception as e :
			raise e
	'''
	set Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@license.setter
	def license(self,license):
		try :
			if not isinstance(license,str):
				raise TypeError("license must be set to str value")
			self._license = license
		except Exception as e :
			raise e


	'''
	get Total Tx of NetScaler Instance in Mbits
	'''
	@property
	def ns_total_tx(self) :
		try:
			return self._ns_total_tx
		except Exception as e :
			raise e


	'''
	get Number of SSL Cores Up
	'''
	@property
	def number_of_ssl_cores_up(self) :
		try:
			return self._number_of_ssl_cores_up
		except Exception as e :
			raise e
	'''
	set Number of SSL Cores Up
	'''
	@number_of_ssl_cores_up.setter
	def number_of_ssl_cores_up(self,number_of_ssl_cores_up):
		try :
			if not isinstance(number_of_ssl_cores_up,int):
				raise TypeError("number_of_ssl_cores_up must be set to int value")
			self._number_of_ssl_cores_up = number_of_ssl_cores_up
		except Exception as e :
			raise e


	'''
	get Memory Usage (%)
	'''
	@property
	def ns_memory_usage(self) :
		try:
			return self._ns_memory_usage
		except Exception as e :
			raise e


	'''
	get Out Throughput of NetScaler Instance in Mbps
	'''
	@property
	def ns_tx(self) :
		try:
			return self._ns_tx
		except Exception as e :
			raise e


	'''
	get In Throughput of NetScaler Instance in Mbps
	'''
	@property
	def ns_rx(self) :
		try:
			return self._ns_rx
		except Exception as e :
			raise e


	'''
	get HTTP Requests/second
	'''
	@property
	def http_req(self) :
		try:
			return self._http_req
		except Exception as e :
			raise e


	'''
	get Cluster IP Address
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e


	'''
	get Backplane Interface
	'''
	@property
	def backplane(self) :
		try:
			return self._backplane
		except Exception as e :
			raise e
	'''
	set Backplane Interface
	'''
	@backplane.setter
	def backplane(self,backplane):
		try :
			if not isinstance(backplane,str):
				raise TypeError("backplane must be set to str value")
			self._backplane = backplane
		except Exception as e :
			raise e


	'''
	get nic discards on incoming packets
	'''
	@property
	def nic_discards_in(self) :
		try:
			return self._nic_discards_in
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address for this managed device
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address for this managed device
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get Last NonZero Throughput Time in seconds
	'''
	@property
	def last_nonzero_throughput_time(self) :
		try:
			return self._last_nonzero_throughput_time
		except Exception as e :
			raise e
	'''
	set Last NonZero Throughput Time in seconds
	'''
	@last_nonzero_throughput_time.setter
	def last_nonzero_throughput_time(self,last_nonzero_throughput_time):
		try :
			if not isinstance(last_nonzero_throughput_time,long):
				raise TypeError("last_nonzero_throughput_time must be set to long value")
			self._last_nonzero_throughput_time = last_nonzero_throughput_time
		except Exception as e :
			raise e


	'''
	get NetScaler Disk Utilization (%)
	'''
	@property
	def diskperusage(self) :
		try:
			return self._diskperusage
		except Exception as e :
			raise e


	'''
	get Is CCO
	'''
	@property
	def iscco(self) :
		try:
			return self._iscco
		except Exception as e :
			raise e
	'''
	set Is CCO
	'''
	@iscco.setter
	def iscco(self,iscco):
		try :
			if not isinstance(iscco,bool):
				raise TypeError("iscco must be set to bool value")
			self._iscco = iscco
		except Exception as e :
			raise e


	'''
	get Last Config Changed Time
	'''
	@property
	def lastconfigchangedtime(self) :
		try:
			return self._lastconfigchangedtime
		except Exception as e :
			raise e
	'''
	set Last Config Changed Time
	'''
	@lastconfigchangedtime.setter
	def lastconfigchangedtime(self,lastconfigchangedtime):
		try :
			if not isinstance(lastconfigchangedtime,long):
				raise TypeError("lastconfigchangedtime must be set to long value")
			self._lastconfigchangedtime = lastconfigchangedtime
		except Exception as e :
			raise e


	'''
	get Number of SSL Cards
	'''
	@property
	def number_of_ssl_cards(self) :
		try:
			return self._number_of_ssl_cards
		except Exception as e :
			raise e
	'''
	set Number of SSL Cards
	'''
	@number_of_ssl_cards.setter
	def number_of_ssl_cards(self,number_of_ssl_cards):
		try :
			if not isinstance(number_of_ssl_cards,int):
				raise TypeError("number_of_ssl_cards must be set to int value")
			self._number_of_ssl_cards = number_of_ssl_cards
		except Exception as e :
			raise e


	'''
	get true if you want to allow shell/sftp/scp access to NetScaler Instance administrator
	'''
	@property
	def cmd_policy(self) :
		try:
			return self._cmd_policy
		except Exception as e :
			raise e
	'''
	set true if you want to allow shell/sftp/scp access to NetScaler Instance administrator
	'''
	@cmd_policy.setter
	def cmd_policy(self,cmd_policy):
		try :
			if not isinstance(cmd_policy,str):
				raise TypeError("cmd_policy must be set to str value")
			self._cmd_policy = cmd_policy
		except Exception as e :
			raise e


	'''
	get Net Profile for Metrics Collector
	'''
	@property
	def netprofile_metrics_collector(self) :
		try:
			return self._netprofile_metrics_collector
		except Exception as e :
			raise e
	'''
	set Net Profile for Metrics Collector
	'''
	@netprofile_metrics_collector.setter
	def netprofile_metrics_collector(self,netprofile_metrics_collector):
		try :
			if not isinstance(netprofile_metrics_collector,str):
				raise TypeError("netprofile_metrics_collector must be set to str value")
			self._netprofile_metrics_collector = netprofile_metrics_collector
		except Exception as e :
			raise e


	'''
	get ns_observationdomainName
	'''
	@property
	def ns_observationdomainName(self) :
		try:
			return self._ns_observationdomainName
		except Exception as e :
			raise e
	'''
	set ns_observationdomainName
	'''
	@ns_observationdomainName.setter
	def ns_observationdomainName(self,ns_observationdomainName):
		try :
			if not isinstance(ns_observationdomainName,str):
				raise TypeError("ns_observationdomainName must be set to str value")
			self._ns_observationdomainName = ns_observationdomainName
		except Exception as e :
			raise e


	'''
	get ns_observationdomainid
	'''
	@property
	def ns_observationdomainid(self) :
		try:
			return self._ns_observationdomainid
		except Exception as e :
			raise e
	'''
	set ns_observationdomainid
	'''
	@ns_observationdomainid.setter
	def ns_observationdomainid(self,ns_observationdomainid):
		try :
			if not isinstance(ns_observationdomainid,str):
				raise TypeError("ns_observationdomainid must be set to str value")
			self._ns_observationdomainid = ns_observationdomainid
		except Exception as e :
			raise e


	'''
	get Total Rx of NetScaler Instance in Mbits
	'''
	@property
	def ns_total_rx(self) :
		try:
			return self._ns_total_rx
		except Exception as e :
			raise e


	'''
	get Flag to check if metrics collection is enabled or disabled.
	'''
	@property
	def metrics_collection(self) :
		try:
			return self._metrics_collection
		except Exception as e :
			raise e
	'''
	set Flag to check if metrics collection is enabled or disabled.
	'''
	@metrics_collection.setter
	def metrics_collection(self,metrics_collection):
		try :
			if not isinstance(metrics_collection,bool):
				raise TypeError("metrics_collection must be set to bool value")
			self._metrics_collection = metrics_collection
		except Exception as e :
			raise e


	'''
	get Total number of PEs
	'''
	@property
	def num_pes(self) :
		try:
			return self._num_pes
		except Exception as e :
			raise e
	'''
	set Total number of PEs
	'''
	@num_pes.setter
	def num_pes(self,num_pes):
		try :
			if not isinstance(num_pes,int):
				raise TypeError("num_pes must be set to int value")
			self._num_pes = num_pes
		except Exception as e :
			raise e


	'''
	get NetScaler Bot Default signature version
	'''
	@property
	def bot_signature_version(self) :
		try:
			return self._bot_signature_version
		except Exception as e :
			raise e
	'''
	set NetScaler Bot Default signature version
	'''
	@bot_signature_version.setter
	def bot_signature_version(self,bot_signature_version):
		try :
			if not isinstance(bot_signature_version,str):
				raise TypeError("bot_signature_version must be set to str value")
			self._bot_signature_version = bot_signature_version
		except Exception as e :
			raise e


	'''
	get Shared secret that used for orchestration deployment
	'''
	@property
	def pre_auth_key(self) :
		try:
			return self._pre_auth_key
		except Exception as e :
			raise e
	'''
	set Shared secret that used for orchestration deployment
	'''
	@pre_auth_key.setter
	def pre_auth_key(self,pre_auth_key):
		try :
			if not isinstance(pre_auth_key,str):
				raise TypeError("pre_auth_key must be set to str value")
			self._pre_auth_key = pre_auth_key
		except Exception as e :
			raise e


	'''
	get Net Profile
	'''
	@property
	def netprofile(self) :
		try:
			return self._netprofile
		except Exception as e :
			raise e
	'''
	set Net Profile
	'''
	@netprofile.setter
	def netprofile(self,netprofile):
		try :
			if not isinstance(netprofile,str):
				raise TypeError("netprofile must be set to str value")
			self._netprofile = netprofile
		except Exception as e :
			raise e


	'''
	get nic discards on outgoing packets
	'''
	@property
	def nic_discards_out(self) :
		try:
			return self._nic_discards_out
		except Exception as e :
			raise e


	'''
	get Custom ID
	'''
	@property
	def customid(self) :
		try:
			return self._customid
		except Exception as e :
			raise e
	'''
	set Custom ID
	'''
	@customid.setter
	def customid(self,customid):
		try :
			if not isinstance(customid,str):
				raise TypeError("customid must be set to str value")
			self._customid = customid
		except Exception as e :
			raise e

	'''
	Should config be saved first in case instance is rebooted while modify
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	Should config be saved first in case instance is rebooted while modify
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e

	'''
	License server IP address
	'''
	@property
	def LS_IP(self):
		try:
			return self._LS_IP
		except Exception as e :
			raise e
	'''
	License server IP address
	'''
	@LS_IP.setter
	def LS_IP(self,LS_IP):
		try :
			if not isinstance(LS_IP,str):
				raise TypeError("LS_IP must be set to str value")
			self._LS_IP = LS_IP
		except Exception as e :
			raise e

	'''
	Indicates whether config diff exists for this instances or not
	'''
	@property
	def diff_exists(self):
		try:
			return self._diff_exists
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_obj=ns()
				response = ns_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to unmanage NetScaler Instance.
	'''

	'''
	Use this operation to unmanage NetScaler Instance.
	'''
	@classmethod
	def unmanage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"unmanage")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"unmanage", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to manage NetScaler Instance.
	'''

	'''
	Use this operation to manage NetScaler Instance.
	'''
	@classmethod
	def manage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"manage")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"manage", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to reboot NetScaler Instance.
	'''

	'''
	Use this operation to reboot NetScaler Instance.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"reboot")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"reboot", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_obj = ns()
			option_ = options()
			option_._filter=filter_
			return ns_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_obj = ns()
			option_ = options()
			option_._count=True
			response = ns_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_obj = ns()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_responses, response, "ns_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_response_array
				i=0
				error = [ns() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_response_array
			i=0
			ns_objs = [ns() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns'):
					for props in obj._ns:
						result = service.payload_formatter.string_to_bulk_resource(ns_response,self.__class__.__name__,props)
						ns_objs[i] = result.ns
						i=i+1
			return ns_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_response(base_response):
	def __init__(self,length=1) :
		self.ns= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns= [ ns() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_responses(base_response):
	def __init__(self,length=1) :
		self.ns_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_response_array = [ ns() for _ in range(length)]
