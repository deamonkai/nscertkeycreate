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
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map


'''
Configuration for Instance Score resource
'''

class instance_score(base_resource):
	_num_critical_events= ""
	_ind_disk_used= ""
	_display_name= ""
	_data_critical_events= ""
	_ind_memory_used= ""
	_tcpclient_connection= ""
	_vm_memory_total= ""
	_data_memory_used= ""
	_num_configdrift_template= ""
	_data_disk1_total= ""
	_num_rl_ssl_throughput= ""
	_ind_rl_rate= ""
	_ind_power_error= ""
	_ind_rl_cpu= ""
	_rx_throughput= ""
	_hostname= ""
	_ind_rule_security= ""
	_data_aggregate_bw_events= ""
	_uptime= ""
	_num_vservers_total= ""
	_ind_pooled_license_events= ""
	_num_capacity_cpu= ""
	_ind_rl_pps= ""
	_data_cpu_used_mgmt= ""
	_num_sslcert_notrecommended_keystrengh= ""
	_num_total_errors= ""
	_ind_nic_discards= ""
	_ind_cpu_used= ""
	_current_instance_state= ""
	_instance_state= ""
	_model= ""
	_num_rl_pps= ""
	_data_capacity_cpu= ""
	_data_cpu_used_packet= ""
	_ind_capacity_cpu= ""
	_num_vservers_active= ""
	_httprequest_rate= ""
	_httpresponse_rate= ""
	_data_rule_security= ""
	_ssl_transaction_rate= ""
	_data_rule_capacity= ""
	_data_platform_pps_events= ""
	_num_rule_security= ""
	_ind_configdrift_default= ""
	_data_rl_rate= ""
	_num_rl_cpu= ""
	_data_disk1_used= ""
	_system_poll_time= ""
	_data_rl_ssl_throughput= ""
	_num_rl_rate= ""
	_ind_configdrift_template= ""
	_datacenter_id= ""
	_ind_rl_ssl_throughput= ""
	_poll_time= ""
	_num_sslcert_notrecommended_algorithm= ""
	_data_disk1_free= ""
	_scale= ""
	_num_sslcert_notrecommended_issuer= ""
	_num_ssl_errors= ""
	_num_config_deviation_errors= ""
	_data_nic_discards_out= ""
	_max_contribution= ""
	_data_rule_config= ""
	_id= ""
	_data_rl_ssl_tps= ""
	_num_rule_networking= ""
	_ind_platform_pps_events= ""
	_ind_aggregate_bw_events= ""
	_num_rule_config= ""
	_num_sslcert_expiry_due= ""
	_num_applications_total= ""
	_num_rl_ssl_tps= ""
	_type= ""
	_data_disk0_total= ""
	_data_pooled_license_events= ""
	_num_sslcert_expired= ""
	_data_nic_discards_in= ""
	_num_applications_managed= ""
	_num_capacity_errors= ""
	_num_pooled_license_events= ""
	_num_systemresource_errors= ""
	_tcpserver_connection= ""
	_data_capacity_mem= ""
	_data_rule_networking= ""
	_ind_sslcert_notrecommended_algorithm= ""
	_num_rule_capacity= ""
	_ind_capacity_mem= ""
	_ind_rule_system_resource= ""
	_data_rl_cpu= ""
	_data_rule_system_resource= ""
	_cluster_node_ip_list= ""
	_num_rule_system_resource= ""
	_num_capacity_mem= ""
	_data_disk0_used= ""
	_num_ssl_cards= ""
	_ind_rule_capacity= ""
	_tenant_id= ""
	_site_name= ""
	_score= ""
	_ind_sslcert_notrecommended_keystrengh= ""
	_ind_sslcert_notrecommended_issuer= ""
	_managed_device_id= ""
	_tx_throughput= ""
	_data_memory_free= ""
	_ind_sslcert_expired= ""
	_ip_address= ""
	_is_clip= ""
	_ind_rl_ssl_tps= ""
	_ind_ssl_card_error= ""
	_version= ""
	_ind_rule_config= ""
	_ind_sslcert_expiry_due= ""
	_ind_flash_error= ""
	_num_platform_pps_events= ""
	_num_aggregate_bw_events= ""
	_data_rl_pps= ""
	_ind_harddiskdrive_error= ""
	_data_disk0_free= ""
	_ind_rule_networking= ""
	_th_memory_used_low= ""
	_th_rl_ssl_throughput_high= ""
	_th_cpu_used_high= ""
	_th_rl_cpu_high= ""
	_th_disk_used_low= ""
	_entity_tag=[]
	_th_rl_pps_high= ""
	_th_disk_used_high= ""
	_th_rl_ssl_tps_high= ""
	_th_nic_discards_high= ""
	_th_memory_used_high= ""
	_th_rl_rate_high= ""
	_th_cpu_used_low= ""
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
			return "instance_score"
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
			return "instance_scores"
		except Exception as e :
			raise e



	'''
	get Number of total critical events
	'''
	@property
	def num_critical_events(self) :
		try:
			return self._num_critical_events
		except Exception as e :
			raise e
	'''
	set Number of total critical events
	'''
	@num_critical_events.setter
	def num_critical_events(self,num_critical_events):
		try :
			if not isinstance(num_critical_events,int):
				raise TypeError("num_critical_events must be set to int value")
			self._num_critical_events = num_critical_events
		except Exception as e :
			raise e


	'''
	get Disk Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_disk_used(self) :
		try:
			return self._ind_disk_used
		except Exception as e :
			raise e
	'''
	set Disk Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_disk_used.setter
	def ind_disk_used(self,ind_disk_used):
		try :
			if not isinstance(ind_disk_used,int):
				raise TypeError("ind_disk_used must be set to int value")
			self._ind_disk_used = ind_disk_used
		except Exception as e :
			raise e


	'''
	get Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get List of categories from active_event table representing the current outstanding critical events
	'''
	@property
	def data_critical_events(self) :
		try:
			return self._data_critical_events
		except Exception as e :
			raise e
	'''
	set List of categories from active_event table representing the current outstanding critical events
	'''
	@data_critical_events.setter
	def data_critical_events(self,data_critical_events):
		try :
			if not isinstance(data_critical_events,str):
				raise TypeError("data_critical_events must be set to str value")
			self._data_critical_events = data_critical_events
		except Exception as e :
			raise e


	'''
	get Memory Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_memory_used(self) :
		try:
			return self._ind_memory_used
		except Exception as e :
			raise e
	'''
	set Memory Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_memory_used.setter
	def ind_memory_used(self,ind_memory_used):
		try :
			if not isinstance(ind_memory_used,int):
				raise TypeError("ind_memory_used must be set to int value")
			self._ind_memory_used = ind_memory_used
		except Exception as e :
			raise e


	'''
	get tcpcurclientconnestablished   Value
	'''
	@property
	def tcpclient_connection(self) :
		try:
			return self._tcpclient_connection
		except Exception as e :
			raise e
	'''
	set tcpcurclientconnestablished   Value
	'''
	@tcpclient_connection.setter
	def tcpclient_connection(self,tcpclient_connection):
		try :
			if not isinstance(tcpclient_connection,float):
				raise TypeError("tcpclient_connection must be set to float value")
			self._tcpclient_connection = tcpclient_connection
		except Exception as e :
			raise e


	'''
	get Total Memory of VM Instance in MB. 2048MB, 5120MB
	'''
	@property
	def vm_memory_total(self) :
		try:
			return self._vm_memory_total
		except Exception as e :
			raise e
	'''
	set Total Memory of VM Instance in MB. 2048MB, 5120MB
	'''
	@vm_memory_total.setter
	def vm_memory_total(self,vm_memory_total):
		try :
			if not isinstance(vm_memory_total,float):
				raise TypeError("vm_memory_total must be set to float value")
			self._vm_memory_total = vm_memory_total
		except Exception as e :
			raise e


	'''
	get Data Memory used in percentage
	'''
	@property
	def data_memory_used(self) :
		try:
			return self._data_memory_used
		except Exception as e :
			raise e
	'''
	set Data Memory used in percentage
	'''
	@data_memory_used.setter
	def data_memory_used(self,data_memory_used):
		try :
			if not isinstance(data_memory_used,float):
				raise TypeError("data_memory_used must be set to float value")
			self._data_memory_used = data_memory_used
		except Exception as e :
			raise e


	'''
	get Number of RunningVsTemplate Diffs
	'''
	@property
	def num_configdrift_template(self) :
		try:
			return self._num_configdrift_template
		except Exception as e :
			raise e
	'''
	set Number of RunningVsTemplate Diffs
	'''
	@num_configdrift_template.setter
	def num_configdrift_template(self,num_configdrift_template):
		try :
			if not isinstance(num_configdrift_template,int):
				raise TypeError("num_configdrift_template must be set to int value")
			self._num_configdrift_template = num_configdrift_template
		except Exception as e :
			raise e


	'''
	get Disk1 total space in MB
	'''
	@property
	def data_disk1_total(self) :
		try:
			return self._data_disk1_total
		except Exception as e :
			raise e
	'''
	set Disk1 total space in MB
	'''
	@data_disk1_total.setter
	def data_disk1_total(self,data_disk1_total):
		try :
			if not isinstance(data_disk1_total,float):
				raise TypeError("data_disk1_total must be set to float value")
			self._data_disk1_total = data_disk1_total
		except Exception as e :
			raise e


	'''
	get Number of times the SSL Throughput rate limit was reached from the last poll cycle
	'''
	@property
	def num_rl_ssl_throughput(self) :
		try:
			return self._num_rl_ssl_throughput
		except Exception as e :
			raise e
	'''
	set Number of times the SSL Throughput rate limit was reached from the last poll cycle
	'''
	@num_rl_ssl_throughput.setter
	def num_rl_ssl_throughput(self,num_rl_ssl_throughput):
		try :
			if not isinstance(num_rl_ssl_throughput,int):
				raise TypeError("num_rl_ssl_throughput must be set to int value")
			self._num_rl_ssl_throughput = num_rl_ssl_throughput
		except Exception as e :
			raise e


	'''
	get Indicates if the throughput rate limit was reached
	'''
	@property
	def ind_rl_rate(self) :
		try:
			return self._ind_rl_rate
		except Exception as e :
			raise e
	'''
	set Indicates if the throughput rate limit was reached
	'''
	@ind_rl_rate.setter
	def ind_rl_rate(self,ind_rl_rate):
		try :
			if not isinstance(ind_rl_rate,int):
				raise TypeError("ind_rl_rate must be set to int value")
			self._ind_rl_rate = ind_rl_rate
		except Exception as e :
			raise e


	'''
	get Power Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_power_error(self) :
		try:
			return self._ind_power_error
		except Exception as e :
			raise e
	'''
	set Power Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_power_error.setter
	def ind_power_error(self,ind_power_error):
		try :
			if not isinstance(ind_power_error,int):
				raise TypeError("ind_power_error must be set to int value")
			self._ind_power_error = ind_power_error
		except Exception as e :
			raise e


	'''
	get Indicates if the CPU rate limit was reached
	'''
	@property
	def ind_rl_cpu(self) :
		try:
			return self._ind_rl_cpu
		except Exception as e :
			raise e
	'''
	set Indicates if the CPU rate limit was reached
	'''
	@ind_rl_cpu.setter
	def ind_rl_cpu(self,ind_rl_cpu):
		try :
			if not isinstance(ind_rl_cpu,int):
				raise TypeError("ind_rl_cpu must be set to int value")
			self._ind_rl_cpu = ind_rl_cpu
		except Exception as e :
			raise e


	'''
	get rxmbitsrate Value
	'''
	@property
	def rx_throughput(self) :
		try:
			return self._rx_throughput
		except Exception as e :
			raise e
	'''
	set rxmbitsrate Value
	'''
	@rx_throughput.setter
	def rx_throughput(self,rx_throughput):
		try :
			if not isinstance(rx_throughput,float):
				raise TypeError("rx_throughput must be set to float value")
			self._rx_throughput = rx_throughput
		except Exception as e :
			raise e


	'''
	get Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Assign hostname to managed device, if this is not provided, name will be set as host name 
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
	get Indicates if errors related to Security rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@property
	def ind_rule_security(self) :
		try:
			return self._ind_rule_security
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to Security rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@ind_rule_security.setter
	def ind_rule_security(self,ind_rule_security):
		try :
			if not isinstance(ind_rule_security,int):
				raise TypeError("ind_rule_security must be set to int value")
			self._ind_rule_security = ind_rule_security
		except Exception as e :
			raise e


	'''
	get List of categories from active_event table representing the current outstanding aggregate bandwidth events
	'''
	@property
	def data_aggregate_bw_events(self) :
		try:
			return self._data_aggregate_bw_events
		except Exception as e :
			raise e
	'''
	set List of categories from active_event table representing the current outstanding aggregate bandwidth events
	'''
	@data_aggregate_bw_events.setter
	def data_aggregate_bw_events(self,data_aggregate_bw_events):
		try :
			if not isinstance(data_aggregate_bw_events,str):
				raise TypeError("data_aggregate_bw_events must be set to str value")
			self._data_aggregate_bw_events = data_aggregate_bw_events
		except Exception as e :
			raise e


	'''
	get Up time
	'''
	@property
	def uptime(self) :
		try:
			return self._uptime
		except Exception as e :
			raise e
	'''
	set Up time
	'''
	@uptime.setter
	def uptime(self,uptime):
		try :
			if not isinstance(uptime,str):
				raise TypeError("uptime must be set to str value")
			self._uptime = uptime
		except Exception as e :
			raise e


	'''
	get Number of total vservers
	'''
	@property
	def num_vservers_total(self) :
		try:
			return self._num_vservers_total
		except Exception as e :
			raise e
	'''
	set Number of total vservers
	'''
	@num_vservers_total.setter
	def num_vservers_total(self,num_vservers_total):
		try :
			if not isinstance(num_vservers_total,int):
				raise TypeError("num_vservers_total must be set to int value")
			self._num_vservers_total = num_vservers_total
		except Exception as e :
			raise e


	'''
	get Indicates if  erros related to pooled license has occured or not
	'''
	@property
	def ind_pooled_license_events(self) :
		try:
			return self._ind_pooled_license_events
		except Exception as e :
			raise e
	'''
	set Indicates if  erros related to pooled license has occured or not
	'''
	@ind_pooled_license_events.setter
	def ind_pooled_license_events(self,ind_pooled_license_events):
		try :
			if not isinstance(ind_pooled_license_events,int):
				raise TypeError("ind_pooled_license_events must be set to int value")
			self._ind_pooled_license_events = ind_pooled_license_events
		except Exception as e :
			raise e


	'''
	get Number of occuring in the poll cycle
	'''
	@property
	def num_capacity_cpu(self) :
		try:
			return self._num_capacity_cpu
		except Exception as e :
			raise e
	'''
	set Number of occuring in the poll cycle
	'''
	@num_capacity_cpu.setter
	def num_capacity_cpu(self,num_capacity_cpu):
		try :
			if not isinstance(num_capacity_cpu,int):
				raise TypeError("num_capacity_cpu must be set to int value")
			self._num_capacity_cpu = num_capacity_cpu
		except Exception as e :
			raise e


	'''
	get Indicates if the packet/s(PPS) rate limit was reached
	'''
	@property
	def ind_rl_pps(self) :
		try:
			return self._ind_rl_pps
		except Exception as e :
			raise e
	'''
	set Indicates if the packet/s(PPS) rate limit was reached
	'''
	@ind_rl_pps.setter
	def ind_rl_pps(self,ind_rl_pps):
		try :
			if not isinstance(ind_rl_pps,int):
				raise TypeError("ind_rl_pps must be set to int value")
			self._ind_rl_pps = ind_rl_pps
		except Exception as e :
			raise e


	'''
	get Management Cpu usage percentage
	'''
	@property
	def data_cpu_used_mgmt(self) :
		try:
			return self._data_cpu_used_mgmt
		except Exception as e :
			raise e
	'''
	set Management Cpu usage percentage
	'''
	@data_cpu_used_mgmt.setter
	def data_cpu_used_mgmt(self,data_cpu_used_mgmt):
		try :
			if not isinstance(data_cpu_used_mgmt,float):
				raise TypeError("data_cpu_used_mgmt must be set to float value")
			self._data_cpu_used_mgmt = data_cpu_used_mgmt
		except Exception as e :
			raise e


	'''
	get Number of not recommended key strength certificates
	'''
	@property
	def num_sslcert_notrecommended_keystrengh(self) :
		try:
			return self._num_sslcert_notrecommended_keystrengh
		except Exception as e :
			raise e
	'''
	set Number of not recommended key strength certificates
	'''
	@num_sslcert_notrecommended_keystrengh.setter
	def num_sslcert_notrecommended_keystrengh(self,num_sslcert_notrecommended_keystrengh):
		try :
			if not isinstance(num_sslcert_notrecommended_keystrengh,int):
				raise TypeError("num_sslcert_notrecommended_keystrengh must be set to int value")
			self._num_sslcert_notrecommended_keystrengh = num_sslcert_notrecommended_keystrengh
		except Exception as e :
			raise e


	'''
	get Number of total failures
	'''
	@property
	def num_total_errors(self) :
		try:
			return self._num_total_errors
		except Exception as e :
			raise e
	'''
	set Number of total failures
	'''
	@num_total_errors.setter
	def num_total_errors(self,num_total_errors):
		try :
			if not isinstance(num_total_errors,int):
				raise TypeError("num_total_errors must be set to int value")
			self._num_total_errors = num_total_errors
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to nic discards on incoming/outgoing packets has occured or not
	'''
	@property
	def ind_nic_discards(self) :
		try:
			return self._ind_nic_discards
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to nic discards on incoming/outgoing packets has occured or not
	'''
	@ind_nic_discards.setter
	def ind_nic_discards(self,ind_nic_discards):
		try :
			if not isinstance(ind_nic_discards,int):
				raise TypeError("ind_nic_discards must be set to int value")
			self._ind_nic_discards = ind_nic_discards
		except Exception as e :
			raise e


	'''
	get CPU Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_cpu_used(self) :
		try:
			return self._ind_cpu_used
		except Exception as e :
			raise e
	'''
	set CPU Usage Indicator. 0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_cpu_used.setter
	def ind_cpu_used(self,ind_cpu_used):
		try :
			if not isinstance(ind_cpu_used,int):
				raise TypeError("ind_cpu_used must be set to int value")
			self._ind_cpu_used = ind_cpu_used
		except Exception as e :
			raise e


	'''
	get Current State of device, UP only if device accessible
	'''
	@property
	def current_instance_state(self) :
		try:
			return self._current_instance_state
		except Exception as e :
			raise e
	'''
	set Current State of device, UP only if device accessible
	'''
	@current_instance_state.setter
	def current_instance_state(self,current_instance_state):
		try :
			if not isinstance(current_instance_state,str):
				raise TypeError("current_instance_state must be set to str value")
			self._current_instance_state = current_instance_state
		except Exception as e :
			raise e


	'''
	get State of device, UP only if device accessible
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
		except Exception as e :
			raise e
	'''
	set State of device, UP only if device accessible
	'''
	@instance_state.setter
	def instance_state(self,instance_state):
		try :
			if not isinstance(instance_state,str):
				raise TypeError("instance_state must be set to str value")
			self._instance_state = instance_state
		except Exception as e :
			raise e


	'''
	get model
	'''
	@property
	def model(self) :
		try:
			return self._model
		except Exception as e :
			raise e
	'''
	set model
	'''
	@model.setter
	def model(self,model):
		try :
			if not isinstance(model,str):
				raise TypeError("model must be set to str value")
			self._model = model
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the packet/s(PPS) rate limit was reached from the last polll cycle
	'''
	@property
	def num_rl_pps(self) :
		try:
			return self._num_rl_pps
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the packet/s(PPS) rate limit was reached from the last polll cycle
	'''
	@num_rl_pps.setter
	def num_rl_pps(self,num_rl_pps):
		try :
			if not isinstance(num_rl_pps,int):
				raise TypeError("num_rl_pps must be set to int value")
			self._num_rl_pps = num_rl_pps
		except Exception as e :
			raise e


	'''
	get CPU predicted values. Stores comma separated list of data
	'''
	@property
	def data_capacity_cpu(self) :
		try:
			return self._data_capacity_cpu
		except Exception as e :
			raise e
	'''
	set CPU predicted values. Stores comma separated list of data
	'''
	@data_capacity_cpu.setter
	def data_capacity_cpu(self,data_capacity_cpu):
		try :
			if not isinstance(data_capacity_cpu,str):
				raise TypeError("data_capacity_cpu must be set to str value")
			self._data_capacity_cpu = data_capacity_cpu
		except Exception as e :
			raise e


	'''
	get Packet Cpu usage percentage
	'''
	@property
	def data_cpu_used_packet(self) :
		try:
			return self._data_cpu_used_packet
		except Exception as e :
			raise e
	'''
	set Packet Cpu usage percentage
	'''
	@data_cpu_used_packet.setter
	def data_cpu_used_packet(self,data_cpu_used_packet):
		try :
			if not isinstance(data_cpu_used_packet,float):
				raise TypeError("data_cpu_used_packet must be set to float value")
			self._data_cpu_used_packet = data_cpu_used_packet
		except Exception as e :
			raise e


	'''
	get Indicates event occurs.0 indicates no ,1 indicates event occurs,-1 indicates not evaluated
	'''
	@property
	def ind_capacity_cpu(self) :
		try:
			return self._ind_capacity_cpu
		except Exception as e :
			raise e
	'''
	set Indicates event occurs.0 indicates no ,1 indicates event occurs,-1 indicates not evaluated
	'''
	@ind_capacity_cpu.setter
	def ind_capacity_cpu(self,ind_capacity_cpu):
		try :
			if not isinstance(ind_capacity_cpu,int):
				raise TypeError("ind_capacity_cpu must be set to int value")
			self._ind_capacity_cpu = ind_capacity_cpu
		except Exception as e :
			raise e


	'''
	get Number of active vservers
	'''
	@property
	def num_vservers_active(self) :
		try:
			return self._num_vservers_active
		except Exception as e :
			raise e
	'''
	set Number of active vservers
	'''
	@num_vservers_active.setter
	def num_vservers_active(self,num_vservers_active):
		try :
			if not isinstance(num_vservers_active,int):
				raise TypeError("num_vservers_active must be set to int value")
			self._num_vservers_active = num_vservers_active
		except Exception as e :
			raise e


	'''
	get httprxrequestbytesrate Value
	'''
	@property
	def httprequest_rate(self) :
		try:
			return self._httprequest_rate
		except Exception as e :
			raise e
	'''
	set httprxrequestbytesrate Value
	'''
	@httprequest_rate.setter
	def httprequest_rate(self,httprequest_rate):
		try :
			if not isinstance(httprequest_rate,float):
				raise TypeError("httprequest_rate must be set to float value")
			self._httprequest_rate = httprequest_rate
		except Exception as e :
			raise e


	'''
	get httprxresponsebytesrate Value
	'''
	@property
	def httpresponse_rate(self) :
		try:
			return self._httpresponse_rate
		except Exception as e :
			raise e
	'''
	set httprxresponsebytesrate Value
	'''
	@httpresponse_rate.setter
	def httpresponse_rate(self,httpresponse_rate):
		try :
			if not isinstance(httpresponse_rate,float):
				raise TypeError("httpresponse_rate must be set to float value")
			self._httpresponse_rate = httpresponse_rate
		except Exception as e :
			raise e


	'''
	get Rules triggered for Security errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@property
	def data_rule_security(self) :
		try:
			return self._data_rule_security
		except Exception as e :
			raise e
	'''
	set Rules triggered for Security errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@data_rule_security.setter
	def data_rule_security(self,data_rule_security):
		try :
			if not isinstance(data_rule_security,str):
				raise TypeError("data_rule_security must be set to str value")
			self._data_rule_security = data_rule_security
		except Exception as e :
			raise e


	'''
	get ssltransactionsrate Value
	'''
	@property
	def ssl_transaction_rate(self) :
		try:
			return self._ssl_transaction_rate
		except Exception as e :
			raise e
	'''
	set ssltransactionsrate Value
	'''
	@ssl_transaction_rate.setter
	def ssl_transaction_rate(self,ssl_transaction_rate):
		try :
			if not isinstance(ssl_transaction_rate,float):
				raise TypeError("ssl_transaction_rate must be set to float value")
			self._ssl_transaction_rate = ssl_transaction_rate
		except Exception as e :
			raise e


	'''
	get Rules triggered for Capacity errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@property
	def data_rule_capacity(self) :
		try:
			return self._data_rule_capacity
		except Exception as e :
			raise e
	'''
	set Rules triggered for Capacity errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@data_rule_capacity.setter
	def data_rule_capacity(self,data_rule_capacity):
		try :
			if not isinstance(data_rule_capacity,str):
				raise TypeError("data_rule_capacity must be set to str value")
			self._data_rule_capacity = data_rule_capacity
		except Exception as e :
			raise e


	'''
	get List of categories from active_event table representing the current outstanding platform PPS events
	'''
	@property
	def data_platform_pps_events(self) :
		try:
			return self._data_platform_pps_events
		except Exception as e :
			raise e
	'''
	set List of categories from active_event table representing the current outstanding platform PPS events
	'''
	@data_platform_pps_events.setter
	def data_platform_pps_events(self,data_platform_pps_events):
		try :
			if not isinstance(data_platform_pps_events,str):
				raise TypeError("data_platform_pps_events must be set to str value")
			self._data_platform_pps_events = data_platform_pps_events
		except Exception as e :
			raise e


	'''
	get Number of rules occuring in the poll cycle for Security category
	'''
	@property
	def num_rule_security(self) :
		try:
			return self._num_rule_security
		except Exception as e :
			raise e
	'''
	set Number of rules occuring in the poll cycle for Security category
	'''
	@num_rule_security.setter
	def num_rule_security(self,num_rule_security):
		try :
			if not isinstance(num_rule_security,int):
				raise TypeError("num_rule_security must be set to int value")
			self._num_rule_security = num_rule_security
		except Exception as e :
			raise e


	'''
	get SavedVsRunning diff state.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_configdrift_default(self) :
		try:
			return self._ind_configdrift_default
		except Exception as e :
			raise e
	'''
	set SavedVsRunning diff state.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_configdrift_default.setter
	def ind_configdrift_default(self,ind_configdrift_default):
		try :
			if not isinstance(ind_configdrift_default,int):
				raise TypeError("ind_configdrift_default must be set to int value")
			self._ind_configdrift_default = ind_configdrift_default
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the throughput rate limit was reached
	'''
	@property
	def data_rl_rate(self) :
		try:
			return self._data_rl_rate
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the throughput rate limit was reached
	'''
	@data_rl_rate.setter
	def data_rl_rate(self,data_rl_rate):
		try :
			if not isinstance(data_rl_rate,float):
				raise TypeError("data_rl_rate must be set to float value")
			self._data_rl_rate = data_rl_rate
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the CPU rate limit was reached from the last poll cycle
	'''
	@property
	def num_rl_cpu(self) :
		try:
			return self._num_rl_cpu
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the CPU rate limit was reached from the last poll cycle
	'''
	@num_rl_cpu.setter
	def num_rl_cpu(self,num_rl_cpu):
		try :
			if not isinstance(num_rl_cpu,int):
				raise TypeError("num_rl_cpu must be set to int value")
			self._num_rl_cpu = num_rl_cpu
		except Exception as e :
			raise e


	'''
	get Disk1 used space in percentage
	'''
	@property
	def data_disk1_used(self) :
		try:
			return self._data_disk1_used
		except Exception as e :
			raise e
	'''
	set Disk1 used space in percentage
	'''
	@data_disk1_used.setter
	def data_disk1_used(self,data_disk1_used):
		try :
			if not isinstance(data_disk1_used,float):
				raise TypeError("data_disk1_used must be set to float value")
			self._data_disk1_used = data_disk1_used
		except Exception as e :
			raise e


	'''
	get Time when the device score poll was initiated for this tenant in seconds
	'''
	@property
	def system_poll_time(self) :
		try:
			return self._system_poll_time
		except Exception as e :
			raise e
	'''
	set Time when the device score poll was initiated for this tenant in seconds
	'''
	@system_poll_time.setter
	def system_poll_time(self,system_poll_time):
		try :
			if not isinstance(system_poll_time,long):
				raise TypeError("system_poll_time must be set to long value")
			self._system_poll_time = system_poll_time
		except Exception as e :
			raise e


	'''
	get Number of times the SSL Throughput rate limit was reached
	'''
	@property
	def data_rl_ssl_throughput(self) :
		try:
			return self._data_rl_ssl_throughput
		except Exception as e :
			raise e
	'''
	set Number of times the SSL Throughput rate limit was reached
	'''
	@data_rl_ssl_throughput.setter
	def data_rl_ssl_throughput(self,data_rl_ssl_throughput):
		try :
			if not isinstance(data_rl_ssl_throughput,float):
				raise TypeError("data_rl_ssl_throughput must be set to float value")
			self._data_rl_ssl_throughput = data_rl_ssl_throughput
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the throughput rate limit was reached from the last poll cycle
	'''
	@property
	def num_rl_rate(self) :
		try:
			return self._num_rl_rate
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the throughput rate limit was reached from the last poll cycle
	'''
	@num_rl_rate.setter
	def num_rl_rate(self,num_rl_rate):
		try :
			if not isinstance(num_rl_rate,int):
				raise TypeError("num_rl_rate must be set to int value")
			self._num_rl_rate = num_rl_rate
		except Exception as e :
			raise e


	'''
	get RunningVsTemplate diff state
	'''
	@property
	def ind_configdrift_template(self) :
		try:
			return self._ind_configdrift_template
		except Exception as e :
			raise e
	'''
	set RunningVsTemplate diff state
	'''
	@ind_configdrift_template.setter
	def ind_configdrift_template(self,ind_configdrift_template):
		try :
			if not isinstance(ind_configdrift_template,int):
				raise TypeError("ind_configdrift_template must be set to int value")
			self._ind_configdrift_template = ind_configdrift_template
		except Exception as e :
			raise e


	'''
	get Datacenter Id
	'''
	@property
	def datacenter_id(self) :
		try:
			return self._datacenter_id
		except Exception as e :
			raise e
	'''
	set Datacenter Id
	'''
	@datacenter_id.setter
	def datacenter_id(self,datacenter_id):
		try :
			if not isinstance(datacenter_id,str):
				raise TypeError("datacenter_id must be set to str value")
			self._datacenter_id = datacenter_id
		except Exception as e :
			raise e


	'''
	get Indicates if the SSL Throughput rate limit was reached
	'''
	@property
	def ind_rl_ssl_throughput(self) :
		try:
			return self._ind_rl_ssl_throughput
		except Exception as e :
			raise e
	'''
	set Indicates if the SSL Throughput rate limit was reached
	'''
	@ind_rl_ssl_throughput.setter
	def ind_rl_ssl_throughput(self,ind_rl_ssl_throughput):
		try :
			if not isinstance(ind_rl_ssl_throughput,int):
				raise TypeError("ind_rl_ssl_throughput must be set to int value")
			self._ind_rl_ssl_throughput = ind_rl_ssl_throughput
		except Exception as e :
			raise e


	'''
	get Poll time in seconds
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e
	'''
	set Poll time in seconds
	'''
	@poll_time.setter
	def poll_time(self,poll_time):
		try :
			if not isinstance(poll_time,long):
				raise TypeError("poll_time must be set to long value")
			self._poll_time = poll_time
		except Exception as e :
			raise e


	'''
	get Number of sslcert with non recommended algorithm
	'''
	@property
	def num_sslcert_notrecommended_algorithm(self) :
		try:
			return self._num_sslcert_notrecommended_algorithm
		except Exception as e :
			raise e
	'''
	set Number of sslcert with non recommended algorithm
	'''
	@num_sslcert_notrecommended_algorithm.setter
	def num_sslcert_notrecommended_algorithm(self,num_sslcert_notrecommended_algorithm):
		try :
			if not isinstance(num_sslcert_notrecommended_algorithm,int):
				raise TypeError("num_sslcert_notrecommended_algorithm must be set to int value")
			self._num_sslcert_notrecommended_algorithm = num_sslcert_notrecommended_algorithm
		except Exception as e :
			raise e


	'''
	get Disk1 free space in MB
	'''
	@property
	def data_disk1_free(self) :
		try:
			return self._data_disk1_free
		except Exception as e :
			raise e
	'''
	set Disk1 free space in MB
	'''
	@data_disk1_free.setter
	def data_disk1_free(self,data_disk1_free):
		try :
			if not isinstance(data_disk1_free,float):
				raise TypeError("data_disk1_free must be set to float value")
			self._data_disk1_free = data_disk1_free
		except Exception as e :
			raise e


	'''
	get Scale
	'''
	@property
	def scale(self) :
		try:
			return self._scale
		except Exception as e :
			raise e
	'''
	set Scale
	'''
	@scale.setter
	def scale(self,scale):
		try :
			if not isinstance(scale,str):
				raise TypeError("scale must be set to str value")
			self._scale = scale
		except Exception as e :
			raise e


	'''
	get Number of not recommended issuer certificates
	'''
	@property
	def num_sslcert_notrecommended_issuer(self) :
		try:
			return self._num_sslcert_notrecommended_issuer
		except Exception as e :
			raise e
	'''
	set Number of not recommended issuer certificates
	'''
	@num_sslcert_notrecommended_issuer.setter
	def num_sslcert_notrecommended_issuer(self,num_sslcert_notrecommended_issuer):
		try :
			if not isinstance(num_sslcert_notrecommended_issuer,int):
				raise TypeError("num_sslcert_notrecommended_issuer must be set to int value")
			self._num_sslcert_notrecommended_issuer = num_sslcert_notrecommended_issuer
		except Exception as e :
			raise e


	'''
	get Number of total errors related to SSL Certificates
	'''
	@property
	def num_ssl_errors(self) :
		try:
			return self._num_ssl_errors
		except Exception as e :
			raise e
	'''
	set Number of total errors related to SSL Certificates
	'''
	@num_ssl_errors.setter
	def num_ssl_errors(self,num_ssl_errors):
		try :
			if not isinstance(num_ssl_errors,int):
				raise TypeError("num_ssl_errors must be set to int value")
			self._num_ssl_errors = num_ssl_errors
		except Exception as e :
			raise e


	'''
	get Number of total config drifts
	'''
	@property
	def num_config_deviation_errors(self) :
		try:
			return self._num_config_deviation_errors
		except Exception as e :
			raise e
	'''
	set Number of total config drifts
	'''
	@num_config_deviation_errors.setter
	def num_config_deviation_errors(self,num_config_deviation_errors):
		try :
			if not isinstance(num_config_deviation_errors,int):
				raise TypeError("num_config_deviation_errors must be set to int value")
			self._num_config_deviation_errors = num_config_deviation_errors
		except Exception as e :
			raise e


	'''
	get nic discards on outgoing packets indicating device name and the number of nic discards
	'''
	@property
	def data_nic_discards_out(self) :
		try:
			return self._data_nic_discards_out
		except Exception as e :
			raise e
	'''
	set nic discards on outgoing packets indicating device name and the number of nic discards
	'''
	@data_nic_discards_out.setter
	def data_nic_discards_out(self,data_nic_discards_out):
		try :
			if not isinstance(data_nic_discards_out,float):
				raise TypeError("data_nic_discards_out must be set to float value")
			self._data_nic_discards_out = data_nic_discards_out
		except Exception as e :
			raise e


	'''
	get Instance score category contributing to the maximum errors
	'''
	@property
	def max_contribution(self) :
		try:
			return self._max_contribution
		except Exception as e :
			raise e
	'''
	set Instance score category contributing to the maximum errors
	'''
	@max_contribution.setter
	def max_contribution(self,max_contribution):
		try :
			if not isinstance(max_contribution,str):
				raise TypeError("max_contribution must be set to str value")
			self._max_contribution = max_contribution
		except Exception as e :
			raise e


	'''
	get Rules triggered for Config errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@property
	def data_rule_config(self) :
		try:
			return self._data_rule_config
		except Exception as e :
			raise e
	'''
	set Rules triggered for Config errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@data_rule_config.setter
	def data_rule_config(self,data_rule_config):
		try :
			if not isinstance(data_rule_config,str):
				raise TypeError("data_rule_config must be set to str value")
			self._data_rule_config = data_rule_config
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
	get Number of times the SSL transactions/s(TPS) rate limit was reached
	'''
	@property
	def data_rl_ssl_tps(self) :
		try:
			return self._data_rl_ssl_tps
		except Exception as e :
			raise e
	'''
	set Number of times the SSL transactions/s(TPS) rate limit was reached
	'''
	@data_rl_ssl_tps.setter
	def data_rl_ssl_tps(self,data_rl_ssl_tps):
		try :
			if not isinstance(data_rl_ssl_tps,float):
				raise TypeError("data_rl_ssl_tps must be set to float value")
			self._data_rl_ssl_tps = data_rl_ssl_tps
		except Exception as e :
			raise e


	'''
	get Number of rules occuring in the poll cycle for networking category
	'''
	@property
	def num_rule_networking(self) :
		try:
			return self._num_rule_networking
		except Exception as e :
			raise e
	'''
	set Number of rules occuring in the poll cycle for networking category
	'''
	@num_rule_networking.setter
	def num_rule_networking(self,num_rule_networking):
		try :
			if not isinstance(num_rule_networking,int):
				raise TypeError("num_rule_networking must be set to int value")
			self._num_rule_networking = num_rule_networking
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to Platform PPS has occured or not
	'''
	@property
	def ind_platform_pps_events(self) :
		try:
			return self._ind_platform_pps_events
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to Platform PPS has occured or not
	'''
	@ind_platform_pps_events.setter
	def ind_platform_pps_events(self,ind_platform_pps_events):
		try :
			if not isinstance(ind_platform_pps_events,int):
				raise TypeError("ind_platform_pps_events must be set to int value")
			self._ind_platform_pps_events = ind_platform_pps_events
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to Aggregate Bandwidth has occurred or not
	'''
	@property
	def ind_aggregate_bw_events(self) :
		try:
			return self._ind_aggregate_bw_events
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to Aggregate Bandwidth has occurred or not
	'''
	@ind_aggregate_bw_events.setter
	def ind_aggregate_bw_events(self,ind_aggregate_bw_events):
		try :
			if not isinstance(ind_aggregate_bw_events,int):
				raise TypeError("ind_aggregate_bw_events must be set to int value")
			self._ind_aggregate_bw_events = ind_aggregate_bw_events
		except Exception as e :
			raise e


	'''
	get Number of rules occuring in the poll cycle for config category
	'''
	@property
	def num_rule_config(self) :
		try:
			return self._num_rule_config
		except Exception as e :
			raise e
	'''
	set Number of rules occuring in the poll cycle for config category
	'''
	@num_rule_config.setter
	def num_rule_config(self,num_rule_config):
		try :
			if not isinstance(num_rule_config,int):
				raise TypeError("num_rule_config must be set to int value")
			self._num_rule_config = num_rule_config
		except Exception as e :
			raise e


	'''
	get Number of ssl certs to expire within the next 7 days
	'''
	@property
	def num_sslcert_expiry_due(self) :
		try:
			return self._num_sslcert_expiry_due
		except Exception as e :
			raise e
	'''
	set Number of ssl certs to expire within the next 7 days
	'''
	@num_sslcert_expiry_due.setter
	def num_sslcert_expiry_due(self,num_sslcert_expiry_due):
		try :
			if not isinstance(num_sslcert_expiry_due,int):
				raise TypeError("num_sslcert_expiry_due must be set to int value")
			self._num_sslcert_expiry_due = num_sslcert_expiry_due
		except Exception as e :
			raise e


	'''
	get Number of total applications
	'''
	@property
	def num_applications_total(self) :
		try:
			return self._num_applications_total
		except Exception as e :
			raise e
	'''
	set Number of total applications
	'''
	@num_applications_total.setter
	def num_applications_total(self,num_applications_total):
		try :
			if not isinstance(num_applications_total,int):
				raise TypeError("num_applications_total must be set to int value")
			self._num_applications_total = num_applications_total
		except Exception as e :
			raise e


	'''
	get Number of times the SSL transactions/s(TPS) rate limit was reached from last poll cycle
	'''
	@property
	def num_rl_ssl_tps(self) :
		try:
			return self._num_rl_ssl_tps
		except Exception as e :
			raise e
	'''
	set Number of times the SSL transactions/s(TPS) rate limit was reached from last poll cycle
	'''
	@num_rl_ssl_tps.setter
	def num_rl_ssl_tps(self,num_rl_ssl_tps):
		try :
			if not isinstance(num_rl_ssl_tps,int):
				raise TypeError("num_rl_ssl_tps must be set to int value")
			self._num_rl_ssl_tps = num_rl_ssl_tps
		except Exception as e :
			raise e


	'''
	get Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Disk0 total space in MB
	'''
	@property
	def data_disk0_total(self) :
		try:
			return self._data_disk0_total
		except Exception as e :
			raise e
	'''
	set Disk0 total space in MB
	'''
	@data_disk0_total.setter
	def data_disk0_total(self,data_disk0_total):
		try :
			if not isinstance(data_disk0_total,float):
				raise TypeError("data_disk0_total must be set to float value")
			self._data_disk0_total = data_disk0_total
		except Exception as e :
			raise e


	'''
	get List of categories from active_event table representing the current outstanding pooled license events
	'''
	@property
	def data_pooled_license_events(self) :
		try:
			return self._data_pooled_license_events
		except Exception as e :
			raise e
	'''
	set List of categories from active_event table representing the current outstanding pooled license events
	'''
	@data_pooled_license_events.setter
	def data_pooled_license_events(self,data_pooled_license_events):
		try :
			if not isinstance(data_pooled_license_events,str):
				raise TypeError("data_pooled_license_events must be set to str value")
			self._data_pooled_license_events = data_pooled_license_events
		except Exception as e :
			raise e


	'''
	get Number of ssl certs expired
	'''
	@property
	def num_sslcert_expired(self) :
		try:
			return self._num_sslcert_expired
		except Exception as e :
			raise e
	'''
	set Number of ssl certs expired
	'''
	@num_sslcert_expired.setter
	def num_sslcert_expired(self,num_sslcert_expired):
		try :
			if not isinstance(num_sslcert_expired,int):
				raise TypeError("num_sslcert_expired must be set to int value")
			self._num_sslcert_expired = num_sslcert_expired
		except Exception as e :
			raise e


	'''
	get nic discards on incoming packets indicating device name and the number of nic discards
	'''
	@property
	def data_nic_discards_in(self) :
		try:
			return self._data_nic_discards_in
		except Exception as e :
			raise e
	'''
	set nic discards on incoming packets indicating device name and the number of nic discards
	'''
	@data_nic_discards_in.setter
	def data_nic_discards_in(self,data_nic_discards_in):
		try :
			if not isinstance(data_nic_discards_in,float):
				raise TypeError("data_nic_discards_in must be set to float value")
			self._data_nic_discards_in = data_nic_discards_in
		except Exception as e :
			raise e


	'''
	get Number of managed applications
	'''
	@property
	def num_applications_managed(self) :
		try:
			return self._num_applications_managed
		except Exception as e :
			raise e
	'''
	set Number of managed applications
	'''
	@num_applications_managed.setter
	def num_applications_managed(self,num_applications_managed):
		try :
			if not isinstance(num_applications_managed,int):
				raise TypeError("num_applications_managed must be set to int value")
			self._num_applications_managed = num_applications_managed
		except Exception as e :
			raise e


	'''
	get Number of total system capacity failures
	'''
	@property
	def num_capacity_errors(self) :
		try:
			return self._num_capacity_errors
		except Exception as e :
			raise e
	'''
	set Number of total system capacity failures
	'''
	@num_capacity_errors.setter
	def num_capacity_errors(self,num_capacity_errors):
		try :
			if not isinstance(num_capacity_errors,int):
				raise TypeError("num_capacity_errors must be set to int value")
			self._num_capacity_errors = num_capacity_errors
		except Exception as e :
			raise e


	'''
	get Total number of erros related to pooled license
	'''
	@property
	def num_pooled_license_events(self) :
		try:
			return self._num_pooled_license_events
		except Exception as e :
			raise e
	'''
	set Total number of erros related to pooled license
	'''
	@num_pooled_license_events.setter
	def num_pooled_license_events(self,num_pooled_license_events):
		try :
			if not isinstance(num_pooled_license_events,int):
				raise TypeError("num_pooled_license_events must be set to int value")
			self._num_pooled_license_events = num_pooled_license_events
		except Exception as e :
			raise e


	'''
	get Number of total system resource failures
	'''
	@property
	def num_systemresource_errors(self) :
		try:
			return self._num_systemresource_errors
		except Exception as e :
			raise e
	'''
	set Number of total system resource failures
	'''
	@num_systemresource_errors.setter
	def num_systemresource_errors(self,num_systemresource_errors):
		try :
			if not isinstance(num_systemresource_errors,int):
				raise TypeError("num_systemresource_errors must be set to int value")
			self._num_systemresource_errors = num_systemresource_errors
		except Exception as e :
			raise e


	'''
	get tcpcurserverconnestablished   Value 
	'''
	@property
	def tcpserver_connection(self) :
		try:
			return self._tcpserver_connection
		except Exception as e :
			raise e
	'''
	set tcpcurserverconnestablished   Value 
	'''
	@tcpserver_connection.setter
	def tcpserver_connection(self,tcpserver_connection):
		try :
			if not isinstance(tcpserver_connection,float):
				raise TypeError("tcpserver_connection must be set to float value")
			self._tcpserver_connection = tcpserver_connection
		except Exception as e :
			raise e


	'''
	get MEM predicted values. Stores comma separated list of data
	'''
	@property
	def data_capacity_mem(self) :
		try:
			return self._data_capacity_mem
		except Exception as e :
			raise e
	'''
	set MEM predicted values. Stores comma separated list of data
	'''
	@data_capacity_mem.setter
	def data_capacity_mem(self,data_capacity_mem):
		try :
			if not isinstance(data_capacity_mem,str):
				raise TypeError("data_capacity_mem must be set to str value")
			self._data_capacity_mem = data_capacity_mem
		except Exception as e :
			raise e


	'''
	get Rules triggered for Networking errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@property
	def data_rule_networking(self) :
		try:
			return self._data_rule_networking
		except Exception as e :
			raise e
	'''
	set Rules triggered for Networking errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@data_rule_networking.setter
	def data_rule_networking(self,data_rule_networking):
		try :
			if not isinstance(data_rule_networking,str):
				raise TypeError("data_rule_networking must be set to str value")
			self._data_rule_networking = data_rule_networking
		except Exception as e :
			raise e


	'''
	get Indicates where ssl certs of not recommended algorithm exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_sslcert_notrecommended_algorithm(self) :
		try:
			return self._ind_sslcert_notrecommended_algorithm
		except Exception as e :
			raise e
	'''
	set Indicates where ssl certs of not recommended algorithm exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_sslcert_notrecommended_algorithm.setter
	def ind_sslcert_notrecommended_algorithm(self,ind_sslcert_notrecommended_algorithm):
		try :
			if not isinstance(ind_sslcert_notrecommended_algorithm,int):
				raise TypeError("ind_sslcert_notrecommended_algorithm must be set to int value")
			self._ind_sslcert_notrecommended_algorithm = ind_sslcert_notrecommended_algorithm
		except Exception as e :
			raise e


	'''
	get Number of rules occuring in the poll cycle for Capacity category
	'''
	@property
	def num_rule_capacity(self) :
		try:
			return self._num_rule_capacity
		except Exception as e :
			raise e
	'''
	set Number of rules occuring in the poll cycle for Capacity category
	'''
	@num_rule_capacity.setter
	def num_rule_capacity(self,num_rule_capacity):
		try :
			if not isinstance(num_rule_capacity,int):
				raise TypeError("num_rule_capacity must be set to int value")
			self._num_rule_capacity = num_rule_capacity
		except Exception as e :
			raise e


	'''
	get Indicates event occurs.0 indicates no ,1 indicates event occurs,-1 indicates not evaluated
	'''
	@property
	def ind_capacity_mem(self) :
		try:
			return self._ind_capacity_mem
		except Exception as e :
			raise e
	'''
	set Indicates event occurs.0 indicates no ,1 indicates event occurs,-1 indicates not evaluated
	'''
	@ind_capacity_mem.setter
	def ind_capacity_mem(self,ind_capacity_mem):
		try :
			if not isinstance(ind_capacity_mem,int):
				raise TypeError("ind_capacity_mem must be set to int value")
			self._ind_capacity_mem = ind_capacity_mem
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to system resource rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@property
	def ind_rule_system_resource(self) :
		try:
			return self._ind_rule_system_resource
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to system resource rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@ind_rule_system_resource.setter
	def ind_rule_system_resource(self,ind_rule_system_resource):
		try :
			if not isinstance(ind_rule_system_resource,int):
				raise TypeError("ind_rule_system_resource must be set to int value")
			self._ind_rule_system_resource = ind_rule_system_resource
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the CPU rate limit was reached
	'''
	@property
	def data_rl_cpu(self) :
		try:
			return self._data_rl_cpu
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the CPU rate limit was reached
	'''
	@data_rl_cpu.setter
	def data_rl_cpu(self,data_rl_cpu):
		try :
			if not isinstance(data_rl_cpu,float):
				raise TypeError("data_rl_cpu must be set to float value")
			self._data_rl_cpu = data_rl_cpu
		except Exception as e :
			raise e


	'''
	get Rules triggered for system resource errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@property
	def data_rule_system_resource(self) :
		try:
			return self._data_rule_system_resource
		except Exception as e :
			raise e
	'''
	set Rules triggered for system resource errors. Stores comma separated list of rules data in the format ruleid:rulename.Example id1:name1,id2:name2
	'''
	@data_rule_system_resource.setter
	def data_rule_system_resource(self,data_rule_system_resource):
		try :
			if not isinstance(data_rule_system_resource,str):
				raise TypeError("data_rule_system_resource must be set to str value")
			self._data_rule_system_resource = data_rule_system_resource
		except Exception as e :
			raise e


	'''
	get Comma separated list of cluster node IPs
	'''
	@property
	def cluster_node_ip_list(self) :
		try:
			return self._cluster_node_ip_list
		except Exception as e :
			raise e
	'''
	set Comma separated list of cluster node IPs
	'''
	@cluster_node_ip_list.setter
	def cluster_node_ip_list(self,cluster_node_ip_list):
		try :
			if not isinstance(cluster_node_ip_list,str):
				raise TypeError("cluster_node_ip_list must be set to str value")
			self._cluster_node_ip_list = cluster_node_ip_list
		except Exception as e :
			raise e


	'''
	get Number of rules occuring in the poll cycle for system resource category
	'''
	@property
	def num_rule_system_resource(self) :
		try:
			return self._num_rule_system_resource
		except Exception as e :
			raise e
	'''
	set Number of rules occuring in the poll cycle for system resource category
	'''
	@num_rule_system_resource.setter
	def num_rule_system_resource(self,num_rule_system_resource):
		try :
			if not isinstance(num_rule_system_resource,int):
				raise TypeError("num_rule_system_resource must be set to int value")
			self._num_rule_system_resource = num_rule_system_resource
		except Exception as e :
			raise e


	'''
	get Number of occuring in the poll cycle
	'''
	@property
	def num_capacity_mem(self) :
		try:
			return self._num_capacity_mem
		except Exception as e :
			raise e
	'''
	set Number of occuring in the poll cycle
	'''
	@num_capacity_mem.setter
	def num_capacity_mem(self,num_capacity_mem):
		try :
			if not isinstance(num_capacity_mem,int):
				raise TypeError("num_capacity_mem must be set to int value")
			self._num_capacity_mem = num_capacity_mem
		except Exception as e :
			raise e


	'''
	get Disk0 used space in percentage
	'''
	@property
	def data_disk0_used(self) :
		try:
			return self._data_disk0_used
		except Exception as e :
			raise e
	'''
	set Disk0 used space in percentage
	'''
	@data_disk0_used.setter
	def data_disk0_used(self,data_disk0_used):
		try :
			if not isinstance(data_disk0_used,float):
				raise TypeError("data_disk0_used must be set to float value")
			self._data_disk0_used = data_disk0_used
		except Exception as e :
			raise e


	'''
	get Number of ssl cards
	'''
	@property
	def num_ssl_cards(self) :
		try:
			return self._num_ssl_cards
		except Exception as e :
			raise e
	'''
	set Number of ssl cards
	'''
	@num_ssl_cards.setter
	def num_ssl_cards(self,num_ssl_cards):
		try :
			if not isinstance(num_ssl_cards,int):
				raise TypeError("num_ssl_cards must be set to int value")
			self._num_ssl_cards = num_ssl_cards
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to Capacity rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@property
	def ind_rule_capacity(self) :
		try:
			return self._ind_rule_capacity
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to Capacity rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@ind_rule_capacity.setter
	def ind_rule_capacity(self,ind_rule_capacity):
		try :
			if not isinstance(ind_rule_capacity,int):
				raise TypeError("ind_rule_capacity must be set to int value")
			self._ind_rule_capacity = ind_rule_capacity
		except Exception as e :
			raise e


	'''
	get Tenant ID
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Datacenter Name
	'''
	@property
	def site_name(self) :
		try:
			return self._site_name
		except Exception as e :
			raise e
	'''
	set Datacenter Name
	'''
	@site_name.setter
	def site_name(self,site_name):
		try :
			if not isinstance(site_name,str):
				raise TypeError("site_name must be set to str value")
			self._site_name = site_name
		except Exception as e :
			raise e


	'''
	get Total Instance score
	'''
	@property
	def score(self) :
		try:
			return self._score
		except Exception as e :
			raise e
	'''
	set Total Instance score
	'''
	@score.setter
	def score(self,score):
		try :
			if not isinstance(score,int):
				raise TypeError("score must be set to int value")
			self._score = score
		except Exception as e :
			raise e


	'''
	get Not recommeded key strength certificates exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_sslcert_notrecommended_keystrengh(self) :
		try:
			return self._ind_sslcert_notrecommended_keystrengh
		except Exception as e :
			raise e
	'''
	set Not recommeded key strength certificates exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_sslcert_notrecommended_keystrengh.setter
	def ind_sslcert_notrecommended_keystrengh(self,ind_sslcert_notrecommended_keystrengh):
		try :
			if not isinstance(ind_sslcert_notrecommended_keystrengh,int):
				raise TypeError("ind_sslcert_notrecommended_keystrengh must be set to int value")
			self._ind_sslcert_notrecommended_keystrengh = ind_sslcert_notrecommended_keystrengh
		except Exception as e :
			raise e


	'''
	get Indicates where ssl certs of not recommended issuer exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_sslcert_notrecommended_issuer(self) :
		try:
			return self._ind_sslcert_notrecommended_issuer
		except Exception as e :
			raise e
	'''
	set Indicates where ssl certs of not recommended issuer exists or not.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_sslcert_notrecommended_issuer.setter
	def ind_sslcert_notrecommended_issuer(self,ind_sslcert_notrecommended_issuer):
		try :
			if not isinstance(ind_sslcert_notrecommended_issuer,int):
				raise TypeError("ind_sslcert_notrecommended_issuer must be set to int value")
			self._ind_sslcert_notrecommended_issuer = ind_sslcert_notrecommended_issuer
		except Exception as e :
			raise e


	'''
	get id of the instance in managed device table
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e
	'''
	set id of the instance in managed device table
	'''
	@managed_device_id.setter
	def managed_device_id(self,managed_device_id):
		try :
			if not isinstance(managed_device_id,str):
				raise TypeError("managed_device_id must be set to str value")
			self._managed_device_id = managed_device_id
		except Exception as e :
			raise e


	'''
	get txmbitsrate Value
	'''
	@property
	def tx_throughput(self) :
		try:
			return self._tx_throughput
		except Exception as e :
			raise e
	'''
	set txmbitsrate Value
	'''
	@tx_throughput.setter
	def tx_throughput(self,tx_throughput):
		try :
			if not isinstance(tx_throughput,float):
				raise TypeError("tx_throughput must be set to float value")
			self._tx_throughput = tx_throughput
		except Exception as e :
			raise e


	'''
	get Memory Available in MB
	'''
	@property
	def data_memory_free(self) :
		try:
			return self._data_memory_free
		except Exception as e :
			raise e
	'''
	set Memory Available in MB
	'''
	@data_memory_free.setter
	def data_memory_free(self,data_memory_free):
		try :
			if not isinstance(data_memory_free,float):
				raise TypeError("data_memory_free must be set to float value")
			self._data_memory_free = data_memory_free
		except Exception as e :
			raise e


	'''
	get Indicates if there are any expired SSL Certs.0 indicates no expiry, 1 indicates expiry and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_sslcert_expired(self) :
		try:
			return self._ind_sslcert_expired
		except Exception as e :
			raise e
	'''
	set Indicates if there are any expired SSL Certs.0 indicates no expiry, 1 indicates expiry and -1 indicates Not-Applicable or Unknown
	'''
	@ind_sslcert_expired.setter
	def ind_sslcert_expired(self,ind_sslcert_expired):
		try :
			if not isinstance(ind_sslcert_expired,int):
				raise TypeError("ind_sslcert_expired must be set to int value")
			self._ind_sslcert_expired = ind_sslcert_expired
		except Exception as e :
			raise e


	'''
	get IP Address for this managed device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for this managed device
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
	get Indicates if the SSL transactions/s(TPS) rate limit was reached
	'''
	@property
	def ind_rl_ssl_tps(self) :
		try:
			return self._ind_rl_ssl_tps
		except Exception as e :
			raise e
	'''
	set Indicates if the SSL transactions/s(TPS) rate limit was reached
	'''
	@ind_rl_ssl_tps.setter
	def ind_rl_ssl_tps(self,ind_rl_ssl_tps):
		try :
			if not isinstance(ind_rl_ssl_tps,int):
				raise TypeError("ind_rl_ssl_tps must be set to int value")
			self._ind_rl_ssl_tps = ind_rl_ssl_tps
		except Exception as e :
			raise e


	'''
	get SSL card failure state indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_ssl_card_error(self) :
		try:
			return self._ind_ssl_card_error
		except Exception as e :
			raise e
	'''
	set SSL card failure state indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_ssl_card_error.setter
	def ind_ssl_card_error(self,ind_ssl_card_error):
		try :
			if not isinstance(ind_ssl_card_error,int):
				raise TypeError("ind_ssl_card_error must be set to int value")
			self._ind_ssl_card_error = ind_ssl_card_error
		except Exception as e :
			raise e


	'''
	get version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to Config rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@property
	def ind_rule_config(self) :
		try:
			return self._ind_rule_config
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to Config rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@ind_rule_config.setter
	def ind_rule_config(self,ind_rule_config):
		try :
			if not isinstance(ind_rule_config,int):
				raise TypeError("ind_rule_config must be set to int value")
			self._ind_rule_config = ind_rule_config
		except Exception as e :
			raise e


	'''
	get Indicator of SSL Cert expiry in the next 7 days
	'''
	@property
	def ind_sslcert_expiry_due(self) :
		try:
			return self._ind_sslcert_expiry_due
		except Exception as e :
			raise e
	'''
	set Indicator of SSL Cert expiry in the next 7 days
	'''
	@ind_sslcert_expiry_due.setter
	def ind_sslcert_expiry_due(self,ind_sslcert_expiry_due):
		try :
			if not isinstance(ind_sslcert_expiry_due,int):
				raise TypeError("ind_sslcert_expiry_due must be set to int value")
			self._ind_sslcert_expiry_due = ind_sslcert_expiry_due
		except Exception as e :
			raise e


	'''
	get Flash Indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_flash_error(self) :
		try:
			return self._ind_flash_error
		except Exception as e :
			raise e
	'''
	set Flash Indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_flash_error.setter
	def ind_flash_error(self,ind_flash_error):
		try :
			if not isinstance(ind_flash_error,int):
				raise TypeError("ind_flash_error must be set to int value")
			self._ind_flash_error = ind_flash_error
		except Exception as e :
			raise e


	'''
	get Total number of errors related to Platform PPS
	'''
	@property
	def num_platform_pps_events(self) :
		try:
			return self._num_platform_pps_events
		except Exception as e :
			raise e
	'''
	set Total number of errors related to Platform PPS
	'''
	@num_platform_pps_events.setter
	def num_platform_pps_events(self,num_platform_pps_events):
		try :
			if not isinstance(num_platform_pps_events,int):
				raise TypeError("num_platform_pps_events must be set to int value")
			self._num_platform_pps_events = num_platform_pps_events
		except Exception as e :
			raise e


	'''
	get Total number of errors related to Aggregate Bandwidth
	'''
	@property
	def num_aggregate_bw_events(self) :
		try:
			return self._num_aggregate_bw_events
		except Exception as e :
			raise e
	'''
	set Total number of errors related to Aggregate Bandwidth
	'''
	@num_aggregate_bw_events.setter
	def num_aggregate_bw_events(self,num_aggregate_bw_events):
		try :
			if not isinstance(num_aggregate_bw_events,int):
				raise TypeError("num_aggregate_bw_events must be set to int value")
			self._num_aggregate_bw_events = num_aggregate_bw_events
		except Exception as e :
			raise e


	'''
	get Number of packets dropped when the packet/s(PPS) rate limit was reached
	'''
	@property
	def data_rl_pps(self) :
		try:
			return self._data_rl_pps
		except Exception as e :
			raise e
	'''
	set Number of packets dropped when the packet/s(PPS) rate limit was reached
	'''
	@data_rl_pps.setter
	def data_rl_pps(self,data_rl_pps):
		try :
			if not isinstance(data_rl_pps,float):
				raise TypeError("data_rl_pps must be set to float value")
			self._data_rl_pps = data_rl_pps
		except Exception as e :
			raise e


	'''
	get Hard disk drive error indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@property
	def ind_harddiskdrive_error(self) :
		try:
			return self._ind_harddiskdrive_error
		except Exception as e :
			raise e
	'''
	set Hard disk drive error indicator.0 indicates no errors, 1 indicate error and -1 indicates Not-Applicable or Unknown
	'''
	@ind_harddiskdrive_error.setter
	def ind_harddiskdrive_error(self,ind_harddiskdrive_error):
		try :
			if not isinstance(ind_harddiskdrive_error,int):
				raise TypeError("ind_harddiskdrive_error must be set to int value")
			self._ind_harddiskdrive_error = ind_harddiskdrive_error
		except Exception as e :
			raise e


	'''
	get Disk0 Free space in MB
	'''
	@property
	def data_disk0_free(self) :
		try:
			return self._data_disk0_free
		except Exception as e :
			raise e
	'''
	set Disk0 Free space in MB
	'''
	@data_disk0_free.setter
	def data_disk0_free(self,data_disk0_free):
		try :
			if not isinstance(data_disk0_free,float):
				raise TypeError("data_disk0_free must be set to float value")
			self._data_disk0_free = data_disk0_free
		except Exception as e :
			raise e


	'''
	get Indicates if errors related to networking rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@property
	def ind_rule_networking(self) :
		try:
			return self._ind_rule_networking
		except Exception as e :
			raise e
	'''
	set Indicates if errors related to networking rules on has occured or not.0 indicates no errors,1 indicates errors,-1 indicates not evaluated
	'''
	@ind_rule_networking.setter
	def ind_rule_networking(self,ind_rule_networking):
		try :
			if not isinstance(ind_rule_networking,int):
				raise TypeError("ind_rule_networking must be set to int value")
			self._ind_rule_networking = ind_rule_networking
		except Exception as e :
			raise e

	'''
	Memory low threshold
	'''
	@property
	def th_memory_used_low(self):
		try:
			return self._th_memory_used_low
		except Exception as e :
			raise e
	'''
	Memory low threshold
	'''
	@th_memory_used_low.setter
	def th_memory_used_low(self,th_memory_used_low):
		try :
			if not isinstance(th_memory_used_low,float):
				raise TypeError("th_memory_used_low must be set to float value")
			self._th_memory_used_low = th_memory_used_low
		except Exception as e :
			raise e

	'''
	RL SSL Throughput high threshold
	'''
	@property
	def th_rl_ssl_throughput_high(self):
		try:
			return self._th_rl_ssl_throughput_high
		except Exception as e :
			raise e
	'''
	RL SSL Throughput high threshold
	'''
	@th_rl_ssl_throughput_high.setter
	def th_rl_ssl_throughput_high(self,th_rl_ssl_throughput_high):
		try :
			if not isinstance(th_rl_ssl_throughput_high,float):
				raise TypeError("th_rl_ssl_throughput_high must be set to float value")
			self._th_rl_ssl_throughput_high = th_rl_ssl_throughput_high
		except Exception as e :
			raise e

	'''
	CPU high threshold
	'''
	@property
	def th_cpu_used_high(self):
		try:
			return self._th_cpu_used_high
		except Exception as e :
			raise e
	'''
	CPU high threshold
	'''
	@th_cpu_used_high.setter
	def th_cpu_used_high(self,th_cpu_used_high):
		try :
			if not isinstance(th_cpu_used_high,float):
				raise TypeError("th_cpu_used_high must be set to float value")
			self._th_cpu_used_high = th_cpu_used_high
		except Exception as e :
			raise e

	'''
	RL CPU high threshold
	'''
	@property
	def th_rl_cpu_high(self):
		try:
			return self._th_rl_cpu_high
		except Exception as e :
			raise e
	'''
	RL CPU high threshold
	'''
	@th_rl_cpu_high.setter
	def th_rl_cpu_high(self,th_rl_cpu_high):
		try :
			if not isinstance(th_rl_cpu_high,float):
				raise TypeError("th_rl_cpu_high must be set to float value")
			self._th_rl_cpu_high = th_rl_cpu_high
		except Exception as e :
			raise e

	'''
	Disk low threshold
	'''
	@property
	def th_disk_used_low(self):
		try:
			return self._th_disk_used_low
		except Exception as e :
			raise e
	'''
	Disk low threshold
	'''
	@th_disk_used_low.setter
	def th_disk_used_low(self,th_disk_used_low):
		try :
			if not isinstance(th_disk_used_low,float):
				raise TypeError("th_disk_used_low must be set to float value")
			self._th_disk_used_low = th_disk_used_low
		except Exception as e :
			raise e

	'''
	Array of tag_name and tag_value pair associated with an instance
	'''
	@property
	def entity_tag(self) :
		try:
			return self._entity_tag
		except Exception as e :
			raise e
	'''
	Array of tag_name and tag_value pair associated with an instance
	'''
	@entity_tag.setter
	def entity_tag(self,entity_tag) :
		try :
			if not isinstance(entity_tag,list):
				raise TypeError("entity_tag must be set to array of property_map value")
			for item in entity_tag :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._entity_tag = entity_tag
		except Exception as e :
			raise e

	'''
	RL PPS high threshold
	'''
	@property
	def th_rl_pps_high(self):
		try:
			return self._th_rl_pps_high
		except Exception as e :
			raise e
	'''
	RL PPS high threshold
	'''
	@th_rl_pps_high.setter
	def th_rl_pps_high(self,th_rl_pps_high):
		try :
			if not isinstance(th_rl_pps_high,float):
				raise TypeError("th_rl_pps_high must be set to float value")
			self._th_rl_pps_high = th_rl_pps_high
		except Exception as e :
			raise e

	'''
	Disk high threshold
	'''
	@property
	def th_disk_used_high(self):
		try:
			return self._th_disk_used_high
		except Exception as e :
			raise e
	'''
	Disk high threshold
	'''
	@th_disk_used_high.setter
	def th_disk_used_high(self,th_disk_used_high):
		try :
			if not isinstance(th_disk_used_high,float):
				raise TypeError("th_disk_used_high must be set to float value")
			self._th_disk_used_high = th_disk_used_high
		except Exception as e :
			raise e

	'''
	RL SSL TPS high threshold
	'''
	@property
	def th_rl_ssl_tps_high(self):
		try:
			return self._th_rl_ssl_tps_high
		except Exception as e :
			raise e
	'''
	RL SSL TPS high threshold
	'''
	@th_rl_ssl_tps_high.setter
	def th_rl_ssl_tps_high(self,th_rl_ssl_tps_high):
		try :
			if not isinstance(th_rl_ssl_tps_high,float):
				raise TypeError("th_rl_ssl_tps_high must be set to float value")
			self._th_rl_ssl_tps_high = th_rl_ssl_tps_high
		except Exception as e :
			raise e

	'''
	Nic discards high threshold
	'''
	@property
	def th_nic_discards_high(self):
		try:
			return self._th_nic_discards_high
		except Exception as e :
			raise e
	'''
	Nic discards high threshold
	'''
	@th_nic_discards_high.setter
	def th_nic_discards_high(self,th_nic_discards_high):
		try :
			if not isinstance(th_nic_discards_high,float):
				raise TypeError("th_nic_discards_high must be set to float value")
			self._th_nic_discards_high = th_nic_discards_high
		except Exception as e :
			raise e

	'''
	Memory high threshold
	'''
	@property
	def th_memory_used_high(self):
		try:
			return self._th_memory_used_high
		except Exception as e :
			raise e
	'''
	Memory high threshold
	'''
	@th_memory_used_high.setter
	def th_memory_used_high(self,th_memory_used_high):
		try :
			if not isinstance(th_memory_used_high,float):
				raise TypeError("th_memory_used_high must be set to float value")
			self._th_memory_used_high = th_memory_used_high
		except Exception as e :
			raise e

	'''
	RL rate high threshold
	'''
	@property
	def th_rl_rate_high(self):
		try:
			return self._th_rl_rate_high
		except Exception as e :
			raise e
	'''
	RL rate high threshold
	'''
	@th_rl_rate_high.setter
	def th_rl_rate_high(self,th_rl_rate_high):
		try :
			if not isinstance(th_rl_rate_high,float):
				raise TypeError("th_rl_rate_high must be set to float value")
			self._th_rl_rate_high = th_rl_rate_high
		except Exception as e :
			raise e

	'''
	CPU low threshold
	'''
	@property
	def th_cpu_used_low(self):
		try:
			return self._th_cpu_used_low
		except Exception as e :
			raise e
	'''
	CPU low threshold
	'''
	@th_cpu_used_low.setter
	def th_cpu_used_low(self,th_cpu_used_low):
		try :
			if not isinstance(th_cpu_used_low,float):
				raise TypeError("th_cpu_used_low must be set to float value")
			self._th_cpu_used_low = th_cpu_used_low
		except Exception as e :
			raise e

	'''
	Use this operation to get device score.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				instance_score_obj=instance_score()
				response = instance_score_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of instance_score resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			instance_score_obj = instance_score()
			option_ = options()
			option_._filter=filter_
			return instance_score_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the instance_score resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			instance_score_obj = instance_score()
			option_ = options()
			option_._count=True
			response = instance_score_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of instance_score resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			instance_score_obj = instance_score()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = instance_score_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(instance_score_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.instance_score
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(instance_score_responses, response, "instance_score_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.instance_score_response_array
				i=0
				error = [instance_score() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.instance_score_response_array
			i=0
			instance_score_objs = [instance_score() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_instance_score'):
					for props in obj._instance_score:
						result = service.payload_formatter.string_to_bulk_resource(instance_score_response,self.__class__.__name__,props)
						instance_score_objs[i] = result.instance_score
						i=i+1
			return instance_score_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(instance_score,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class instance_score_response(base_response):
	def __init__(self,length=1) :
		self.instance_score= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.instance_score= [ instance_score() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class instance_score_responses(base_response):
	def __init__(self,length=1) :
		self.instance_score_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.instance_score_response_array = [ instance_score() for _ in range(length)]
