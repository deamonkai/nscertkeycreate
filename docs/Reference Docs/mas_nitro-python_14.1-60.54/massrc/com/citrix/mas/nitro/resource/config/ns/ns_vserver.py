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
Configuration for NetScaler Lbvserver Information resource
'''

class ns_vserver(base_resource):
	_unified_appsec_profile_name= ""
	_hostname= ""
	_ns_ip_address= ""
	_transaction_log_effective= ""
	_device_type= ""
	_metrics_enabled= ""
	_configpack_id= ""
	_monitor_mode_toggle= ""
	_display_name= ""
	_throughput= ""
	_user_managed= ""
	_icalog= ""
	_es4nslog= ""
	_transport_mode= ""
	_appflow_policy_rule= ""
	_instance_id= ""
	_metrics_option_list= ""
	_agent_list= ""
	_appsec_profile_name= ""
	_license_type= ""
	_unified_appsec_protection_count= ""
	_cachetype= ""
	_state= ""
	_hits= ""
	_export_list= ""
	_httpxforwardedfor= ""
	_appflowlog_effective= ""
	_appflowlog= ""
	_id= ""
	_vsvr_ip_address= ""
	_client_header= ""
	_analytics_managed= ""
	_comment= ""
	_export_option= ""
	_targetlbvserver= ""
	_instance_license= ""
	_secure_vsvr_state= ""
	_name= ""
	_svc_name= ""
	_svc_grp_name= ""
	_is_bot_policy_bound= ""
	_svc_grp_id= ""
	_csvip_id= ""
	_save_config= ""
	_is_appfw_policy_bound= ""
	_csvip_name= ""
	_svc_id= ""
	_is_throughput_req= ""
	_app_security= ""
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
			return "ns_vserver"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "ns_vservers"
		except Exception as e :
			raise e



	'''
	get unified appsec profile bound to this vserver
	'''
	@property
	def unified_appsec_profile_name(self) :
		try:
			return self._unified_appsec_profile_name
		except Exception as e :
			raise e
	'''
	set unified appsec profile bound to this vserver
	'''
	@unified_appsec_profile_name.setter
	def unified_appsec_profile_name(self,unified_appsec_profile_name):
		try :
			if not isinstance(unified_appsec_profile_name,str):
				raise TypeError("unified_appsec_profile_name must be set to str value")
			self._unified_appsec_profile_name = unified_appsec_profile_name
		except Exception as e :
			raise e


	'''
	get Hostname of the managed device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of the managed device
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
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
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
	get Transaction Log enable/disable
	'''
	@property
	def transaction_log_effective(self) :
		try:
			return self._transaction_log_effective
		except Exception as e :
			raise e
	'''
	set Transaction Log enable/disable
	'''
	@transaction_log_effective.setter
	def transaction_log_effective(self,transaction_log_effective):
		try :
			if not isinstance(transaction_log_effective,str):
				raise TypeError("transaction_log_effective must be set to str value")
			self._transaction_log_effective = transaction_log_effective
		except Exception as e :
			raise e


	'''
	get Device Type : vpx, cpx, blx, cpx-sidecar
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e


	'''
	get Flag to indicate Metrics Enablement for the given vserver
	'''
	@property
	def metrics_enabled(self) :
		try:
			return self._metrics_enabled
		except Exception as e :
			raise e
	'''
	set Flag to indicate Metrics Enablement for the given vserver
	'''
	@metrics_enabled.setter
	def metrics_enabled(self,metrics_enabled):
		try :
			if not isinstance(metrics_enabled,bool):
				raise TypeError("metrics_enabled must be set to bool value")
			self._metrics_enabled = metrics_enabled
		except Exception as e :
			raise e


	'''
	get Stylebooks config pack ID
	'''
	@property
	def configpack_id(self) :
		try:
			return self._configpack_id
		except Exception as e :
			raise e
	'''
	set Stylebooks config pack ID
	'''
	@configpack_id.setter
	def configpack_id(self,configpack_id):
		try :
			if not isinstance(configpack_id,str):
				raise TypeError("configpack_id must be set to str value")
			self._configpack_id = configpack_id
		except Exception as e :
			raise e


	'''
	get Unified Appsec Monitor mode toggle
	'''
	@property
	def monitor_mode_toggle(self) :
		try:
			return self._monitor_mode_toggle
		except Exception as e :
			raise e
	'''
	set Unified Appsec Monitor mode toggle
	'''
	@monitor_mode_toggle.setter
	def monitor_mode_toggle(self,monitor_mode_toggle):
		try :
			if not isinstance(monitor_mode_toggle,bool):
				raise TypeError("monitor_mode_toggle must be set to bool value")
			self._monitor_mode_toggle = monitor_mode_toggle
		except Exception as e :
			raise e


	'''
	get Display Name of Vserver
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get throughput value
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set throughput value
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
	get User Managed Idenfication
	'''
	@property
	def user_managed(self) :
		try:
			return self._user_managed
		except Exception as e :
			raise e
	'''
	set User Managed Idenfication
	'''
	@user_managed.setter
	def user_managed(self,user_managed):
		try :
			if not isinstance(user_managed,bool):
				raise TypeError("user_managed must be set to bool value")
			self._user_managed = user_managed
		except Exception as e :
			raise e


	'''
	get ICA log
	'''
	@property
	def icalog(self) :
		try:
			return self._icalog
		except Exception as e :
			raise e
	'''
	set ICA log
	'''
	@icalog.setter
	def icalog(self,icalog):
		try :
			if not isinstance(icalog,str):
				raise TypeError("icalog must be set to str value")
			self._icalog = icalog
		except Exception as e :
			raise e


	'''
	get ESNS enable
	'''
	@property
	def es4nslog(self) :
		try:
			return self._es4nslog
		except Exception as e :
			raise e
	'''
	set ESNS enable
	'''
	@es4nslog.setter
	def es4nslog(self,es4nslog):
		try :
			if not isinstance(es4nslog,str):
				raise TypeError("es4nslog must be set to str value")
			self._es4nslog = es4nslog
		except Exception as e :
			raise e


	'''
	get Transport type - IPFix or LogStream
	'''
	@property
	def transport_mode(self) :
		try:
			return self._transport_mode
		except Exception as e :
			raise e
	'''
	set Transport type - IPFix or LogStream
	'''
	@transport_mode.setter
	def transport_mode(self,transport_mode):
		try :
			if not isinstance(transport_mode,str):
				raise TypeError("transport_mode must be set to str value")
			self._transport_mode = transport_mode
		except Exception as e :
			raise e


	'''
	get AppFlow policy rule present
	'''
	@property
	def appflow_policy_rule(self) :
		try:
			return self._appflow_policy_rule
		except Exception as e :
			raise e
	'''
	set AppFlow policy rule present
	'''
	@appflow_policy_rule.setter
	def appflow_policy_rule(self,appflow_policy_rule):
		try :
			if not isinstance(appflow_policy_rule,str):
				raise TypeError("appflow_policy_rule must be set to str value")
			self._appflow_policy_rule = appflow_policy_rule
		except Exception as e :
			raise e


	'''
	get Netscaler ID
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e
	'''
	set Netscaler ID
	'''
	@instance_id.setter
	def instance_id(self,instance_id):
		try :
			if not isinstance(instance_id,str):
				raise TypeError("instance_id must be set to str value")
			self._instance_id = instance_id
		except Exception as e :
			raise e


	'''
	get Metric usecases user wants to enable
	'''
	@property
	def metrics_option_list(self) :
		try:
			return self._metrics_option_list
		except Exception as e :
			raise e
	'''
	set Metric usecases user wants to enable
	'''
	@metrics_option_list.setter
	def metrics_option_list(self,metrics_option_list):
		try :
			if not isinstance(metrics_option_list,str):
				raise TypeError("metrics_option_list must be set to str value")
			self._metrics_option_list = metrics_option_list
		except Exception as e :
			raise e


	'''
	get Agent List, on which traffic will flow
	'''
	@property
	def agent_list(self) :
		try:
			return self._agent_list
		except Exception as e :
			raise e
	'''
	set Agent List, on which traffic will flow
	'''
	@agent_list.setter
	def agent_list(self,agent_list):
		try :
			if not isinstance(agent_list,str):
				raise TypeError("agent_list must be set to str value")
			self._agent_list = agent_list
		except Exception as e :
			raise e


	'''
	get appsec profile bound to this vserver
	'''
	@property
	def appsec_profile_name(self) :
		try:
			return self._appsec_profile_name
		except Exception as e :
			raise e
	'''
	set appsec profile bound to this vserver
	'''
	@appsec_profile_name.setter
	def appsec_profile_name(self,appsec_profile_name):
		try :
			if not isinstance(appsec_profile_name,str):
				raise TypeError("appsec_profile_name must be set to str value")
			self._appsec_profile_name = appsec_profile_name
		except Exception as e :
			raise e


	'''
	get License Type : 0 - not licensed, 1 - manual, 2 - vpx, 3 - cpx, 4 - auto, 5 - cpx-sidecar/free
	'''
	@property
	def license_type(self) :
		try:
			return self._license_type
		except Exception as e :
			raise e


	'''
	get unified appsec protection count to this vserver
	'''
	@property
	def unified_appsec_protection_count(self) :
		try:
			return self._unified_appsec_protection_count
		except Exception as e :
			raise e
	'''
	set unified appsec protection count to this vserver
	'''
	@unified_appsec_protection_count.setter
	def unified_appsec_protection_count(self,unified_appsec_protection_count):
		try :
			if not isinstance(unified_appsec_protection_count,int):
				raise TypeError("unified_appsec_protection_count must be set to int value")
			self._unified_appsec_protection_count = unified_appsec_protection_count
		except Exception as e :
			raise e


	'''
	get Cache Type
	'''
	@property
	def cachetype(self) :
		try:
			return self._cachetype
		except Exception as e :
			raise e


	'''
	get State of VServer
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e


	'''
	get Traffic Domain
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e


	'''
	get Export List present for the given LB VServer
	'''
	@property
	def export_list(self) :
		try:
			return self._export_list
		except Exception as e :
			raise e
	'''
	set Export List present for the given LB VServer
	'''
	@export_list.setter
	def export_list(self,export_list):
		try :
			if not isinstance(export_list,str):
				raise TypeError("export_list must be set to str value")
			self._export_list = export_list
		except Exception as e :
			raise e


	'''
	get X-Forwarded-For Header Export status
	'''
	@property
	def httpxforwardedfor(self) :
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	set X-Forwarded-For Header Export status
	'''
	@httpxforwardedfor.setter
	def httpxforwardedfor(self,httpxforwardedfor):
		try :
			if not isinstance(httpxforwardedfor,str):
				raise TypeError("httpxforwardedfor must be set to str value")
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e :
			raise e


	'''
	get Appflowlog effective (validating AppFlow config) enabled or disabled
	'''
	@property
	def appflowlog_effective(self) :
		try:
			return self._appflowlog_effective
		except Exception as e :
			raise e
	'''
	set Appflowlog effective (validating AppFlow config) enabled or disabled
	'''
	@appflowlog_effective.setter
	def appflowlog_effective(self,appflowlog_effective):
		try :
			if not isinstance(appflowlog_effective,str):
				raise TypeError("appflowlog_effective must be set to str value")
			self._appflowlog_effective = appflowlog_effective
		except Exception as e :
			raise e


	'''
	get Appflowlog enabled or disabled
	'''
	@property
	def appflowlog(self) :
		try:
			return self._appflowlog
		except Exception as e :
			raise e
	'''
	set Appflowlog enabled or disabled
	'''
	@appflowlog.setter
	def appflowlog(self,appflowlog):
		try :
			if not isinstance(appflowlog,str):
				raise TypeError("appflowlog must be set to str value")
			self._appflowlog = appflowlog
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
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
	get Custom Client Header to Export
	'''
	@property
	def client_header(self) :
		try:
			return self._client_header
		except Exception as e :
			raise e
	'''
	set Custom Client Header to Export
	'''
	@client_header.setter
	def client_header(self,client_header):
		try :
			if not isinstance(client_header,str):
				raise TypeError("client_header must be set to str value")
			self._client_header = client_header
		except Exception as e :
			raise e


	'''
	get whether the analytics is auto_enabled/manual_enabled/manual_disabled...
	'''
	@property
	def analytics_managed(self) :
		try:
			return self._analytics_managed
		except Exception as e :
			raise e
	'''
	set whether the analytics is auto_enabled/manual_enabled/manual_disabled...
	'''
	@analytics_managed.setter
	def analytics_managed(self,analytics_managed):
		try :
			if not isinstance(analytics_managed,str):
				raise TypeError("analytics_managed must be set to str value")
			self._analytics_managed = analytics_managed
		except Exception as e :
			raise e


	'''
	get Vserver comment
	'''
	@property
	def comment(self) :
		try:
			return self._comment
		except Exception as e :
			raise e


	'''
	get Export Options present for the given LB VServer
	'''
	@property
	def export_option(self) :
		try:
			return self._export_option
		except Exception as e :
			raise e
	'''
	set Export Options present for the given LB VServer
	'''
	@export_option.setter
	def export_option(self,export_option):
		try :
			if not isinstance(export_option,str):
				raise TypeError("export_option must be set to str value")
			self._export_option = export_option
		except Exception as e :
			raise e


	'''
	get Default Target LBVserver
	'''
	@property
	def targetlbvserver(self) :
		try:
			return self._targetlbvserver
		except Exception as e :
			raise e


	'''
	get Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@property
	def instance_license(self) :
		try:
			return self._instance_license
		except Exception as e :
			raise e
	'''
	set Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@instance_license.setter
	def instance_license(self,instance_license):
		try :
			if not isinstance(instance_license,str):
				raise TypeError("instance_license must be set to str value")
			self._instance_license = instance_license
		except Exception as e :
			raise e


	'''
	get VServer state wheather it is secured or not
	'''
	@property
	def secure_vsvr_state(self) :
		try:
			return self._secure_vsvr_state
		except Exception as e :
			raise e
	'''
	set VServer state wheather it is secured or not
	'''
	@secure_vsvr_state.setter
	def secure_vsvr_state(self,secure_vsvr_state):
		try :
			if not isinstance(secure_vsvr_state,int):
				raise TypeError("secure_vsvr_state must be set to int value")
			self._secure_vsvr_state = secure_vsvr_state
		except Exception as e :
			raise e


	'''
	get Vserver Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Vserver Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e

	'''
	Service Name
	'''
	@property
	def svc_name(self):
		try:
			return self._svc_name
		except Exception as e :
			raise e
	'''
	Service Name
	'''
	@svc_name.setter
	def svc_name(self,svc_name):
		try :
			if not isinstance(svc_name,str):
				raise TypeError("svc_name must be set to str value")
			self._svc_name = svc_name
		except Exception as e :
			raise e

	'''
	Service Group Name
	'''
	@property
	def svc_grp_name(self):
		try:
			return self._svc_grp_name
		except Exception as e :
			raise e
	'''
	Service Group Name
	'''
	@svc_grp_name.setter
	def svc_grp_name(self,svc_grp_name):
		try :
			if not isinstance(svc_grp_name,str):
				raise TypeError("svc_grp_name must be set to str value")
			self._svc_grp_name = svc_grp_name
		except Exception as e :
			raise e

	'''
	Is Bot Policy bound to vserver.
	'''
	@property
	def is_bot_policy_bound(self):
		try:
			return self._is_bot_policy_bound
		except Exception as e :
			raise e
	'''
	Is Bot Policy bound to vserver.
	'''
	@is_bot_policy_bound.setter
	def is_bot_policy_bound(self,is_bot_policy_bound):
		try :
			if not isinstance(is_bot_policy_bound,bool):
				raise TypeError("is_bot_policy_bound must be set to bool value")
			self._is_bot_policy_bound = is_bot_policy_bound
		except Exception as e :
			raise e

	'''
	Service Group ID
	'''
	@property
	def svc_grp_id(self):
		try:
			return self._svc_grp_id
		except Exception as e :
			raise e
	'''
	Service Group ID
	'''
	@svc_grp_id.setter
	def svc_grp_id(self,svc_grp_id):
		try :
			if not isinstance(svc_grp_id,str):
				raise TypeError("svc_grp_id must be set to str value")
			self._svc_grp_id = svc_grp_id
		except Exception as e :
			raise e

	'''
	CSVIP ID
	'''
	@property
	def csvip_id(self):
		try:
			return self._csvip_id
		except Exception as e :
			raise e
	'''
	CSVIP ID
	'''
	@csvip_id.setter
	def csvip_id(self,csvip_id):
		try :
			if not isinstance(csvip_id,str):
				raise TypeError("csvip_id must be set to str value")
			self._csvip_id = csvip_id
		except Exception as e :
			raise e

	'''
	Save configuration after enable/disable
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	Save configuration after enable/disable
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
	Is Appfw Policy bound to vserver.
	'''
	@property
	def is_appfw_policy_bound(self):
		try:
			return self._is_appfw_policy_bound
		except Exception as e :
			raise e
	'''
	Is Appfw Policy bound to vserver.
	'''
	@is_appfw_policy_bound.setter
	def is_appfw_policy_bound(self,is_appfw_policy_bound):
		try :
			if not isinstance(is_appfw_policy_bound,bool):
				raise TypeError("is_appfw_policy_bound must be set to bool value")
			self._is_appfw_policy_bound = is_appfw_policy_bound
		except Exception as e :
			raise e

	'''
	CSVIP Name
	'''
	@property
	def csvip_name(self):
		try:
			return self._csvip_name
		except Exception as e :
			raise e
	'''
	CSVIP Name
	'''
	@csvip_name.setter
	def csvip_name(self,csvip_name):
		try :
			if not isinstance(csvip_name,str):
				raise TypeError("csvip_name must be set to str value")
			self._csvip_name = csvip_name
		except Exception as e :
			raise e

	'''
	Service ID
	'''
	@property
	def svc_id(self):
		try:
			return self._svc_id
		except Exception as e :
			raise e
	'''
	Service ID
	'''
	@svc_id.setter
	def svc_id(self,svc_id):
		try :
			if not isinstance(svc_id,str):
				raise TypeError("svc_id must be set to str value")
			self._svc_id = svc_id
		except Exception as e :
			raise e

	'''
	Throghput required
	'''
	@property
	def is_throughput_req(self):
		try:
			return self._is_throughput_req
		except Exception as e :
			raise e
	'''
	Throghput required
	'''
	@is_throughput_req.setter
	def is_throughput_req(self,is_throughput_req):
		try :
			if not isinstance(is_throughput_req,bool):
				raise TypeError("is_throughput_req must be set to bool value")
			self._is_throughput_req = is_throughput_req
		except Exception as e :
			raise e

	'''
	App Security to know whether bot and appfw policies are bound.
	'''
	@property
	def app_security(self):
		try:
			return self._app_security
		except Exception as e :
			raise e
	'''
	App Security to know whether bot and appfw policies are bound.
	'''
	@app_security.setter
	def app_security(self,app_security):
		try :
			if not isinstance(app_security,str):
				raise TypeError("app_security must be set to str value")
			self._app_security = app_security
		except Exception as e :
			raise e

	'''
	Use this operation to enable the Vserver.
	'''
	@classmethod
	def enable(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"enable")
				return res
		except Exception as e :
			raise e

	'''
	Use this operation to poll the Vserver.
	'''
	@classmethod
	def poll(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"poll")
				return res
		except Exception as e :
			raise e

	'''
	Use this operation to disable the Vserver.
	'''
	@classmethod
	def disable(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"disable")
				return res
		except Exception as e :
			raise e

	'''
	Use this operation to get Vserver Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_vserver_obj=ns_vserver()
				response = ns_vserver_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_vserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_vserver_obj = ns_vserver()
			option_ = options()
			option_._filter=filter_
			return ns_vserver_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_vserver resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_vserver_obj = ns_vserver()
			option_ = options()
			option_._count=True
			response = ns_vserver_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_vserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_vserver_obj = ns_vserver()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_vserver_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_vserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_vserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_vserver_responses, response, "ns_vserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_vserver_response_array
				i=0
				error = [ns_vserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_vserver_response_array
			i=0
			ns_vserver_objs = [ns_vserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_vserver'):
					for props in obj._ns_vserver:
						result = service.payload_formatter.string_to_bulk_resource(ns_vserver_response,self.__class__.__name__,props)
						ns_vserver_objs[i] = result.ns_vserver
						i=i+1
			return ns_vserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_vserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_vserver_response(base_response):
	def __init__(self,length=1) :
		self.ns_vserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_vserver= [ ns_vserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_vserver_responses(base_response):
	def __init__(self,length=1) :
		self.ns_vserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_vserver_response_array = [ ns_vserver() for _ in range(length)]
