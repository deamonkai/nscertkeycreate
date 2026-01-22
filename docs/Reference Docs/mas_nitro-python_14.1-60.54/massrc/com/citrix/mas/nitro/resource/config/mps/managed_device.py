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
Configuration for Managed Device resource
'''

class managed_device(base_resource):
	_internal_annotation= ""
	_httpxforwardedfor= ""
	_httpcookie= ""
	_cpu_license_type= ""
	_version= ""
	_las_cpx_bw= ""
	_ip_address= ""
	_license_edition= ""
	_sslvpn_config= ""
	_gateway_deployment= ""
	_model_id= ""
	_vpx_on_sdx= ""
	_manufacturedate= ""
	_profile_name= ""
	_ssh_status= ""
	_upsince= ""
	_geo_support= ""
	_private_ip= ""
	_gateway_ipv6= ""
	_serialnumber= ""
	_las_cpx_edition= ""
	_last_up_time= ""
	_burnin_date= ""
	_agent_id= ""
	_node_id= ""
	_tenant_id= ""
	_lm_serialnumber= ""
	_instance_config= ""
	_device_family= ""
	_instance_available= ""
	_region= ""
	_vcpu_config= ""
	_std_bw_total= ""
	_cloud= ""
	_security_group= ""
	_gateway= ""
	_trust_id= ""
	_plt_bw_config= ""
	_autoscalegroup_id= ""
	_ent_bw_total= ""
	_instance_total= ""
	_device_uuid= ""
	_zone= ""
	_license_server= ""
	_provision_request_id= ""
	_vpc_id= ""
	_config_type= ""
	_cpufrequncy= ""
	_encoded_serialnumber= ""
	_public_dns= ""
	_type= ""
	_plt_bw_available= ""
	_ha_ip_address= ""
	_mastools_version= ""
	_status= ""
	_is_fips_pooled_license_type= ""
	_ha_sync= ""
	_partition_id= ""
	_id= ""
	_location= ""
	_device_finger_print= ""
	_lpeid= ""
	_description= ""
	_template_interval= ""
	_mpx_encryption_status= ""
	_is_managed= ""
	_sslvpn_total= ""
	_partition_name= ""
	_bmcrevision= ""
	_datacenter_id= ""
	_servicepackage= ""
	_is_pooled_saas= ""
	_license_grace_time= ""
	_is_autoscale_group= ""
	_netmask= ""
	_autoprovisioned= ""
	_sysservices= ""
	_systemname= ""
	_contactperson= ""
	_host_id= ""
	_instance_state= ""
	_ipv4_address= ""
	_name= ""
	_ami_id= ""
	_instance_unique_id= ""
	_geo_location= ""
	_isolation_policy= ""
	_sysid= ""
	_ent_bw_config= ""
	_instance_mode= ""
	_last_updated_time= ""
	_discovery_time= ""
	_do_config= ""
	_ha_master_state= ""
	_plt_bw_total= ""
	_subnet_id= ""
	_std_bw_config= ""
	_uptime= ""
	_hostname= ""
	_maintenance_status= ""
	_reason= ""
	_vpx_on_cloud= ""
	_std_bw_available= ""
	_is_ha_configured= ""
	_license_mode= ""
	_instance_type= ""
	_private_dns= ""
	_display_name= ""
	_ent_bw_available= ""
	_mgmt_ip_address= ""
	_lm_host_id= ""
	_httpquerywithurl= ""
	_ipv6_address= ""
	_public_ip= ""
	_instance_classifier= ""
	_is_re_register= ""
	_peer_host_device_ip= ""
	_entity_tag=[]
	_prev_trust_id= ""
	_device_host_ip= ""
	_peer_device_ip= ""
	_file_name= ""
	_file_location_path= ""
	_tr_task_id= ""
	_profile_username= ""
	_act_id= ""
	_profile_password= ""
	_manual_inventory= ""
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
			return "managed_device"
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
			return "managed_device"
		except Exception as e :
			raise e



	'''
	get Internal annotation used by NetScaler Console.Example, if a device is marked for delete
	'''
	@property
	def internal_annotation(self) :
		try:
			return self._internal_annotation
		except Exception as e :
			raise e
	'''
	set Internal annotation used by NetScaler Console.Example, if a device is marked for delete
	'''
	@internal_annotation.setter
	def internal_annotation(self,internal_annotation):
		try :
			if not isinstance(internal_annotation,str):
				raise TypeError("internal_annotation must be set to str value")
			self._internal_annotation = internal_annotation
		except Exception as e :
			raise e


	'''
	get HTTP x-Forwardedfor header flag.
	'''
	@property
	def httpxforwardedfor(self) :
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	set HTTP x-Forwardedfor header flag.
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
	get Cookie-Header flag.
	'''
	@property
	def httpcookie(self) :
		try:
			return self._httpcookie
		except Exception as e :
			raise e


	'''
	get VCPU license 0 = No VCPU License, 1 = VCPU Pool license
	'''
	@property
	def cpu_license_type(self) :
		try:
			return self._cpu_license_type
		except Exception as e :
			raise e


	'''
	get Device Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get lascpxbw for CPX devices requesting LAS capacity during registration
	'''
	@property
	def las_cpx_bw(self) :
		try:
			return self._las_cpx_bw
		except Exception as e :
			raise e
	'''
	set lascpxbw for CPX devices requesting LAS capacity during registration
	'''
	@las_cpx_bw.setter
	def las_cpx_bw(self,las_cpx_bw):
		try :
			if not isinstance(las_cpx_bw,int):
				raise TypeError("las_cpx_bw must be set to int value")
			self._las_cpx_bw = las_cpx_bw
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
	get Edition of instance
	'''
	@property
	def license_edition(self) :
		try:
			return self._license_edition
		except Exception as e :
			raise e
	'''
	set Edition of instance
	'''
	@license_edition.setter
	def license_edition(self,license_edition):
		try :
			if not isinstance(license_edition,str):
				raise TypeError("license_edition must be set to str value")
			self._license_edition = license_edition
		except Exception as e :
			raise e


	'''
	get sslvpn license maximum
	'''
	@property
	def sslvpn_config(self) :
		try:
			return self._sslvpn_config
		except Exception as e :
			raise e
	'''
	set sslvpn license maximum
	'''
	@sslvpn_config.setter
	def sslvpn_config(self,sslvpn_config):
		try :
			if not isinstance(sslvpn_config,int):
				raise TypeError("sslvpn_config must be set to int value")
			self._sslvpn_config = sslvpn_config
		except Exception as e :
			raise e


	'''
	get Is this device acting as Gateway.
	'''
	@property
	def gateway_deployment(self) :
		try:
			return self._gateway_deployment
		except Exception as e :
			raise e
	'''
	set Is this device acting as Gateway.
	'''
	@gateway_deployment.setter
	def gateway_deployment(self,gateway_deployment):
		try :
			if not isinstance(gateway_deployment,bool):
				raise TypeError("gateway_deployment must be set to bool value")
			self._gateway_deployment = gateway_deployment
		except Exception as e :
			raise e


	'''
	get Device Model Id
	'''
	@property
	def model_id(self) :
		try:
			return self._model_id
		except Exception as e :
			raise e


	'''
	get VPX hosted on SDX: 1= Yes, 0= No
	'''
	@property
	def vpx_on_sdx(self) :
		try:
			return self._vpx_on_sdx
		except Exception as e :
			raise e


	'''
	get Manufacture Date
	'''
	@property
	def manufacturedate(self) :
		try:
			return self._manufacturedate
		except Exception as e :
			raise e


	'''
	get Device Profile Name that is attached with this managed device
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Device Profile Name that is attached with this managed device
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get SSH Status of device, UP only if device accessible on SSH
	'''
	@property
	def ssh_status(self) :
		try:
			return self._ssh_status
		except Exception as e :
			raise e


	'''
	get Upsince of managed device
	'''
	@property
	def upsince(self) :
		try:
			return self._upsince
		except Exception as e :
			raise e


	'''
	get Is this device configured to support GEO location.
	'''
	@property
	def geo_support(self) :
		try:
			return self._geo_support
		except Exception as e :
			raise e
	'''
	set Is this device configured to support GEO location.
	'''
	@geo_support.setter
	def geo_support(self,geo_support):
		try :
			if not isinstance(geo_support,bool):
				raise TypeError("geo_support must be set to bool value")
			self._geo_support = geo_support
		except Exception as e :
			raise e


	'''
	get Private IP of the managed device
	'''
	@property
	def private_ip(self) :
		try:
			return self._private_ip
		except Exception as e :
			raise e


	'''
	get Gateway IPv6 Address
	'''
	@property
	def gateway_ipv6(self) :
		try:
			return self._gateway_ipv6
		except Exception as e :
			raise e
	'''
	set Gateway IPv6 Address
	'''
	@gateway_ipv6.setter
	def gateway_ipv6(self,gateway_ipv6):
		try :
			if not isinstance(gateway_ipv6,str):
				raise TypeError("gateway_ipv6 must be set to str value")
			self._gateway_ipv6 = gateway_ipv6
		except Exception as e :
			raise e


	'''
	get Device Serial Number
	'''
	@property
	def serialnumber(self) :
		try:
			return self._serialnumber
		except Exception as e :
			raise e


	'''
	get las_cpx_edition for CPX devices requesting LAS capacity during registration
	'''
	@property
	def las_cpx_edition(self) :
		try:
			return self._las_cpx_edition
		except Exception as e :
			raise e


	'''
	get Last time when the device was seen up
	'''
	@property
	def last_up_time(self) :
		try:
			return self._last_up_time
		except Exception as e :
			raise e
	'''
	set Last time when the device was seen up
	'''
	@last_up_time.setter
	def last_up_time(self,last_up_time):
		try :
			if not isinstance(last_up_time,long):
				raise TypeError("last_up_time must be set to long value")
			self._last_up_time = last_up_time
		except Exception as e :
			raise e


	'''
	get burnin_date for devices using LAS license
	'''
	@property
	def burnin_date(self) :
		try:
			return self._burnin_date
		except Exception as e :
			raise e


	'''
	get Agent Id
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Agent Id
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get Node identification of a device
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Node identification of a device
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
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
	get LM Serial Number
	'''
	@property
	def lm_serialnumber(self) :
		try:
			return self._lm_serialnumber
		except Exception as e :
			raise e


	'''
	get Instance license running
	'''
	@property
	def instance_config(self) :
		try:
			return self._instance_config
		except Exception as e :
			raise e
	'''
	set Instance license running
	'''
	@instance_config.setter
	def instance_config(self,instance_config):
		try :
			if not isinstance(instance_config,int):
				raise TypeError("instance_config must be set to int value")
			self._instance_config = instance_config
		except Exception as e :
			raise e


	'''
	get Device Family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Instance license available
	'''
	@property
	def instance_available(self) :
		try:
			return self._instance_available
		except Exception as e :
			raise e
	'''
	set Instance license available
	'''
	@instance_available.setter
	def instance_available(self,instance_available):
		try :
			if not isinstance(instance_available,int):
				raise TypeError("instance_available must be set to int value")
			self._instance_available = instance_available
		except Exception as e :
			raise e


	'''
	get Region in which the managed device is hosted
	'''
	@property
	def region(self) :
		try:
			return self._region
		except Exception as e :
			raise e


	'''
	get Number of vCPU allocated for the device
	'''
	@property
	def vcpu_config(self) :
		try:
			return self._vcpu_config
		except Exception as e :
			raise e
	'''
	set Number of vCPU allocated for the device
	'''
	@vcpu_config.setter
	def vcpu_config(self,vcpu_config):
		try :
			if not isinstance(vcpu_config,int):
				raise TypeError("vcpu_config must be set to int value")
			self._vcpu_config = vcpu_config
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth
	'''
	@property
	def std_bw_total(self) :
		try:
			return self._std_bw_total
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth
	'''
	@std_bw_total.setter
	def std_bw_total(self,std_bw_total):
		try :
			if not isinstance(std_bw_total,int):
				raise TypeError("std_bw_total must be set to int value")
			self._std_bw_total = std_bw_total
		except Exception as e :
			raise e


	'''
	get Cloud on which the managed device is hosted
	'''
	@property
	def cloud(self) :
		try:
			return self._cloud
		except Exception as e :
			raise e


	'''
	get virtual firewall that controls the traffic for one or more managed devices (if hosted on AWS)
	'''
	@property
	def security_group(self) :
		try:
			return self._security_group
		except Exception as e :
			raise e


	'''
	get Default Gateway of managed device
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set Default Gateway of managed device
	'''
	@gateway.setter
	def gateway(self,gateway):
		try :
			if not isinstance(gateway,str):
				raise TypeError("gateway must be set to str value")
			self._gateway = gateway
		except Exception as e :
			raise e


	'''
	get Device ID obtained from trust service
	'''
	@property
	def trust_id(self) :
		try:
			return self._trust_id
		except Exception as e :
			raise e
	'''
	set Device ID obtained from trust service
	'''
	@trust_id.setter
	def trust_id(self,trust_id):
		try :
			if not isinstance(trust_id,str):
				raise TypeError("trust_id must be set to str value")
			self._trust_id = trust_id
		except Exception as e :
			raise e


	'''
	get Platinum Bandwidth configured
	'''
	@property
	def plt_bw_config(self) :
		try:
			return self._plt_bw_config
		except Exception as e :
			raise e
	'''
	set Platinum Bandwidth configured
	'''
	@plt_bw_config.setter
	def plt_bw_config(self,plt_bw_config):
		try :
			if not isinstance(plt_bw_config,int):
				raise TypeError("plt_bw_config must be set to int value")
			self._plt_bw_config = plt_bw_config
		except Exception as e :
			raise e


	'''
	get Autoscalegroup ID
	'''
	@property
	def autoscalegroup_id(self) :
		try:
			return self._autoscalegroup_id
		except Exception as e :
			raise e
	'''
	set Autoscalegroup ID
	'''
	@autoscalegroup_id.setter
	def autoscalegroup_id(self,autoscalegroup_id):
		try :
			if not isinstance(autoscalegroup_id,str):
				raise TypeError("autoscalegroup_id must be set to str value")
			self._autoscalegroup_id = autoscalegroup_id
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth Total
	'''
	@property
	def ent_bw_total(self) :
		try:
			return self._ent_bw_total
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth Total
	'''
	@ent_bw_total.setter
	def ent_bw_total(self,ent_bw_total):
		try :
			if not isinstance(ent_bw_total,int):
				raise TypeError("ent_bw_total must be set to int value")
			self._ent_bw_total = ent_bw_total
		except Exception as e :
			raise e


	'''
	get Instance license
	'''
	@property
	def instance_total(self) :
		try:
			return self._instance_total
		except Exception as e :
			raise e
	'''
	set Instance license
	'''
	@instance_total.setter
	def instance_total(self,instance_total):
		try :
			if not isinstance(instance_total,int):
				raise TypeError("instance_total must be set to int value")
			self._instance_total = instance_total
		except Exception as e :
			raise e


	'''
	get Device UUID
	'''
	@property
	def device_uuid(self) :
		try:
			return self._device_uuid
		except Exception as e :
			raise e


	'''
	get Zone in which the managed device is hosted
	'''
	@property
	def zone(self) :
		try:
			return self._zone
		except Exception as e :
			raise e


	'''
	get License Server Configured
	'''
	@property
	def license_server(self) :
		try:
			return self._license_server
		except Exception as e :
			raise e
	'''
	set License Server Configured
	'''
	@license_server.setter
	def license_server(self,license_server):
		try :
			if not isinstance(license_server,str):
				raise TypeError("license_server must be set to str value")
			self._license_server = license_server
		except Exception as e :
			raise e


	'''
	get Value is set only if the instance was provisioned from NetScaler Console
	'''
	@property
	def provision_request_id(self) :
		try:
			return self._provision_request_id
		except Exception as e :
			raise e
	'''
	set Value is set only if the instance was provisioned from NetScaler Console
	'''
	@provision_request_id.setter
	def provision_request_id(self,provision_request_id):
		try :
			if not isinstance(provision_request_id,str):
				raise TypeError("provision_request_id must be set to str value")
			self._provision_request_id = provision_request_id
		except Exception as e :
			raise e


	'''
	get VPC ID of the managed device
	'''
	@property
	def vpc_id(self) :
		try:
			return self._vpc_id
		except Exception as e :
			raise e


	'''
	get Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@property
	def config_type(self) :
		try:
			return self._config_type
		except Exception as e :
			raise e
	'''
	set Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@config_type.setter
	def config_type(self,config_type):
		try :
			if not isinstance(config_type,int):
				raise TypeError("config_type must be set to int value")
			self._config_type = config_type
		except Exception as e :
			raise e


	'''
	get CPU Frequency (MHZ)
	'''
	@property
	def cpufrequncy(self) :
		try:
			return self._cpufrequncy
		except Exception as e :
			raise e


	'''
	get Encoded Serial Number
	'''
	@property
	def encoded_serialnumber(self) :
		try:
			return self._encoded_serialnumber
		except Exception as e :
			raise e


	'''
	get Public DNS of the managed device
	'''
	@property
	def public_dns(self) :
		try:
			return self._public_dns
		except Exception as e :
			raise e


	'''
	get Type of device, (Xen | NS)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of device, (Xen | NS)
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
	get Platinum Bandwidth Available
	'''
	@property
	def plt_bw_available(self) :
		try:
			return self._plt_bw_available
		except Exception as e :
			raise e
	'''
	set Platinum Bandwidth Available
	'''
	@plt_bw_available.setter
	def plt_bw_available(self,plt_bw_available):
		try :
			if not isinstance(plt_bw_available,int):
				raise TypeError("plt_bw_available must be set to int value")
			self._plt_bw_available = plt_bw_available
		except Exception as e :
			raise e


	'''
	get Peer IP Address
	'''
	@property
	def ha_ip_address(self) :
		try:
			return self._ha_ip_address
		except Exception as e :
			raise e


	'''
	get Mastools version if the device is embedded agent
	'''
	@property
	def mastools_version(self) :
		try:
			return self._mastools_version
		except Exception as e :
			raise e
	'''
	set Mastools version if the device is embedded agent
	'''
	@mastools_version.setter
	def mastools_version(self,mastools_version):
		try :
			if not isinstance(mastools_version,str):
				raise TypeError("mastools_version must be set to str value")
			self._mastools_version = mastools_version
		except Exception as e :
			raise e


	'''
	get Status of managed device
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get FIPS BW license : 0 = No FIPS BW License, 1 = FIPS BW Pool license
	'''
	@property
	def is_fips_pooled_license_type(self) :
		try:
			return self._is_fips_pooled_license_type
		except Exception as e :
			raise e


	'''
	get HA Synchronization State
	'''
	@property
	def ha_sync(self) :
		try:
			return self._ha_sync
		except Exception as e :
			raise e


	'''
	get ID of admin partition
	'''
	@property
	def partition_id(self) :
		try:
			return self._partition_id
		except Exception as e :
			raise e
	'''
	set ID of admin partition
	'''
	@partition_id.setter
	def partition_id(self,partition_id):
		try :
			if not isinstance(partition_id,str):
				raise TypeError("partition_id must be set to str value")
			self._partition_id = partition_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the managed devices
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the managed devices
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
	get Device Location
	'''
	@property
	def location(self) :
		try:
			return self._location
		except Exception as e :
			raise e


	'''
	get Fingerprint/thumb-print from UMS public certificate for SSL communication
	'''
	@property
	def device_finger_print(self) :
		try:
			return self._device_finger_print
		except Exception as e :
			raise e
	'''
	set Fingerprint/thumb-print from UMS public certificate for SSL communication
	'''
	@device_finger_print.setter
	def device_finger_print(self,device_finger_print):
		try :
			if not isinstance(device_finger_print,str):
				raise TypeError("device_finger_print must be set to str value")
			self._device_finger_print = device_finger_print
		except Exception as e :
			raise e


	'''
	get LPEID for devices using LAS license
	'''
	@property
	def lpeid(self) :
		try:
			return self._lpeid
		except Exception as e :
			raise e


	'''
	get Description of managed device
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of managed device
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Template refresh interval
	'''
	@property
	def template_interval(self) :
		try:
			return self._template_interval
		except Exception as e :
			raise e
	'''
	set Template refresh interval
	'''
	@template_interval.setter
	def template_interval(self,template_interval):
		try :
			if not isinstance(template_interval,int):
				raise TypeError("template_interval must be set to int value")
			self._template_interval = template_interval
		except Exception as e :
			raise e


	'''
	get Encryption status of the filesystem of MPX device
	'''
	@property
	def mpx_encryption_status(self) :
		try:
			return self._mpx_encryption_status
		except Exception as e :
			raise e


	'''
	get Is Managed
	'''
	@property
	def is_managed(self) :
		try:
			return self._is_managed
		except Exception as e :
			raise e
	'''
	set Is Managed
	'''
	@is_managed.setter
	def is_managed(self,is_managed):
		try :
			if not isinstance(is_managed,bool):
				raise TypeError("is_managed must be set to bool value")
			self._is_managed = is_managed
		except Exception as e :
			raise e


	'''
	get sslvpn license
	'''
	@property
	def sslvpn_total(self) :
		try:
			return self._sslvpn_total
		except Exception as e :
			raise e
	'''
	set sslvpn license
	'''
	@sslvpn_total.setter
	def sslvpn_total(self,sslvpn_total):
		try :
			if not isinstance(sslvpn_total,int):
				raise TypeError("sslvpn_total must be set to int value")
			self._sslvpn_total = sslvpn_total
		except Exception as e :
			raise e


	'''
	get NetScaler Admin Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e
	'''
	set NetScaler Admin Partition Name
	'''
	@partition_name.setter
	def partition_name(self,partition_name):
		try :
			if not isinstance(partition_name,str):
				raise TypeError("partition_name must be set to str value")
			self._partition_name = partition_name
		except Exception as e :
			raise e


	'''
	get BMC Firmware Version
	'''
	@property
	def bmcrevision(self) :
		try:
			return self._bmcrevision
		except Exception as e :
			raise e


	'''
	get Datacenter Id is system generated key for data center
	'''
	@property
	def datacenter_id(self) :
		try:
			return self._datacenter_id
		except Exception as e :
			raise e
	'''
	set Datacenter Id is system generated key for data center
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
	get Service Package Name of the device
	'''
	@property
	def servicepackage(self) :
		try:
			return self._servicepackage
		except Exception as e :
			raise e
	'''
	set Service Package Name of the device
	'''
	@servicepackage.setter
	def servicepackage(self,servicepackage):
		try :
			if not isinstance(servicepackage,str):
				raise TypeError("servicepackage must be set to str value")
			self._servicepackage = servicepackage
		except Exception as e :
			raise e


	'''
	get Pooled Saas License available : 1, No Pooled Saas License available : 0
	'''
	@property
	def is_pooled_saas(self) :
		try:
			return self._is_pooled_saas
		except Exception as e :
			raise e


	'''
	get Grace for this NetScaler Instance.
	'''
	@property
	def license_grace_time(self) :
		try:
			return self._license_grace_time
		except Exception as e :
			raise e


	'''
	get Does this device belong to an Autoscale Group.
	'''
	@property
	def is_autoscale_group(self) :
		try:
			return self._is_autoscale_group
		except Exception as e :
			raise e
	'''
	set Does this device belong to an Autoscale Group.
	'''
	@is_autoscale_group.setter
	def is_autoscale_group(self,is_autoscale_group):
		try :
			if not isinstance(is_autoscale_group,bool):
				raise TypeError("is_autoscale_group must be set to bool value")
			self._is_autoscale_group = is_autoscale_group
		except Exception as e :
			raise e


	'''
	get Netmask of managed device
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set Netmask of managed device
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Device is auto-provisioned or not
	'''
	@property
	def autoprovisioned(self) :
		try:
			return self._autoprovisioned
		except Exception as e :
			raise e
	'''
	set Device is auto-provisioned or not
	'''
	@autoprovisioned.setter
	def autoprovisioned(self,autoprovisioned):
		try :
			if not isinstance(autoprovisioned,bool):
				raise TypeError("autoprovisioned must be set to bool value")
			self._autoprovisioned = autoprovisioned
		except Exception as e :
			raise e


	'''
	get System Services
	'''
	@property
	def sysservices(self) :
		try:
			return self._sysservices
		except Exception as e :
			raise e
	'''
	set System Services
	'''
	@sysservices.setter
	def sysservices(self,sysservices):
		try :
			if not isinstance(sysservices,long):
				raise TypeError("sysservices must be set to long value")
			self._sysservices = sysservices
		except Exception as e :
			raise e


	'''
	get Device System Name
	'''
	@property
	def systemname(self) :
		try:
			return self._systemname
		except Exception as e :
			raise e


	'''
	get Device contact person
	'''
	@property
	def contactperson(self) :
		try:
			return self._contactperson
		except Exception as e :
			raise e


	'''
	get Host ID
	'''
	@property
	def host_id(self) :
		try:
			return self._host_id
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
	get IPv4 Address
	'''
	@property
	def ipv4_address(self) :
		try:
			return self._ipv4_address
		except Exception as e :
			raise e
	'''
	set IPv4 Address
	'''
	@ipv4_address.setter
	def ipv4_address(self,ipv4_address):
		try :
			if not isinstance(ipv4_address,str):
				raise TypeError("ipv4_address must be set to str value")
			self._ipv4_address = ipv4_address
		except Exception as e :
			raise e


	'''
	get Name of managed device
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of managed device
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
	get AMI ID of the managed device (if hosted on AWS)
	'''
	@property
	def ami_id(self) :
		try:
			return self._ami_id
		except Exception as e :
			raise e


	'''
	get 32 bit unique Integer id generated by NetScaler NetScaler Console for this device
	'''
	@property
	def instance_unique_id(self) :
		try:
			return self._instance_unique_id
		except Exception as e :
			raise e


	'''
	get Geo location of the managed device
	'''
	@property
	def geo_location(self) :
		try:
			return self._geo_location
		except Exception as e :
			raise e


	'''
	get Isolation Policy of the Device
	'''
	@property
	def isolation_policy(self) :
		try:
			return self._isolation_policy
		except Exception as e :
			raise e
	'''
	set Isolation Policy of the Device
	'''
	@isolation_policy.setter
	def isolation_policy(self,isolation_policy):
		try :
			if not isinstance(isolation_policy,str):
				raise TypeError("isolation_policy must be set to str value")
			self._isolation_policy = isolation_policy
		except Exception as e :
			raise e


	'''
	get System ID
	'''
	@property
	def sysid(self) :
		try:
			return self._sysid
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth configured
	'''
	@property
	def ent_bw_config(self) :
		try:
			return self._ent_bw_config
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth configured
	'''
	@ent_bw_config.setter
	def ent_bw_config(self,ent_bw_config):
		try :
			if not isinstance(ent_bw_config,int):
				raise TypeError("ent_bw_config must be set to int value")
			self._ent_bw_config = ent_bw_config
		except Exception as e :
			raise e


	'''
	get Denotes state- primary,secondary,clip,clusternode
	'''
	@property
	def instance_mode(self) :
		try:
			return self._instance_mode
		except Exception as e :
			raise e
	'''
	set Denotes state- primary,secondary,clip,clusternode
	'''
	@instance_mode.setter
	def instance_mode(self,instance_mode):
		try :
			if not isinstance(instance_mode,str):
				raise TypeError("instance_mode must be set to str value")
			self._instance_mode = instance_mode
		except Exception as e :
			raise e


	'''
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
		except Exception as e :
			raise e
	'''
	set Last Updated Time
	'''
	@last_updated_time.setter
	def last_updated_time(self,last_updated_time):
		try :
			if not isinstance(last_updated_time,long):
				raise TypeError("last_updated_time must be set to long value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get discovery time
	'''
	@property
	def discovery_time(self) :
		try:
			return self._discovery_time
		except Exception as e :
			raise e
	'''
	set discovery time
	'''
	@discovery_time.setter
	def discovery_time(self,discovery_time):
		try :
			if not isinstance(discovery_time,long):
				raise TypeError("discovery_time must be set to long value")
			self._discovery_time = discovery_time
		except Exception as e :
			raise e


	'''
	get Do default config for managed device
	'''
	@property
	def do_config(self) :
		try:
			return self._do_config
		except Exception as e :
			raise e


	'''
	get Master State (Primary/Secondary)
	'''
	@property
	def ha_master_state(self) :
		try:
			return self._ha_master_state
		except Exception as e :
			raise e


	'''
	get Total Platinum Bandwidth
	'''
	@property
	def plt_bw_total(self) :
		try:
			return self._plt_bw_total
		except Exception as e :
			raise e
	'''
	set Total Platinum Bandwidth
	'''
	@plt_bw_total.setter
	def plt_bw_total(self,plt_bw_total):
		try :
			if not isinstance(plt_bw_total,int):
				raise TypeError("plt_bw_total must be set to int value")
			self._plt_bw_total = plt_bw_total
		except Exception as e :
			raise e


	'''
	get in which the instance was launched. Subnet is a Range of IP addresses in a VPC (if hosted on AWS)
	'''
	@property
	def subnet_id(self) :
		try:
			return self._subnet_id
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth running
	'''
	@property
	def std_bw_config(self) :
		try:
			return self._std_bw_config
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth running
	'''
	@std_bw_config.setter
	def std_bw_config(self,std_bw_config):
		try :
			if not isinstance(std_bw_config,int):
				raise TypeError("std_bw_config must be set to int value")
			self._std_bw_config = std_bw_config
		except Exception as e :
			raise e


	'''
	get Uptime of device
	'''
	@property
	def uptime(self) :
		try:
			return self._uptime
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
	get The status if the device is within the maintenance window
	'''
	@property
	def maintenance_status(self) :
		try:
			return self._maintenance_status
		except Exception as e :
			raise e
	'''
	set The status if the device is within the maintenance window
	'''
	@maintenance_status.setter
	def maintenance_status(self,maintenance_status):
		try :
			if not isinstance(maintenance_status,bool):
				raise TypeError("maintenance_status must be set to bool value")
			self._maintenance_status = maintenance_status
		except Exception as e :
			raise e


	'''
	get Reason of failure for this managed device
	'''
	@property
	def reason(self) :
		try:
			return self._reason
		except Exception as e :
			raise e


	'''
	get Cloud Platform of vpx: 0= On-Prem vpx, 1= AWS, 3=Azure, 4=GCP
	'''
	@property
	def vpx_on_cloud(self) :
		try:
			return self._vpx_on_cloud
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth Available
	'''
	@property
	def std_bw_available(self) :
		try:
			return self._std_bw_available
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth Available
	'''
	@std_bw_available.setter
	def std_bw_available(self,std_bw_available):
		try :
			if not isinstance(std_bw_available,int):
				raise TypeError("std_bw_available must be set to int value")
			self._std_bw_available = std_bw_available
		except Exception as e :
			raise e


	'''
	get Is HA configured
	'''
	@property
	def is_ha_configured(self) :
		try:
			return self._is_ha_configured
		except Exception as e :
			raise e
	'''
	set Is HA configured
	'''
	@is_ha_configured.setter
	def is_ha_configured(self,is_ha_configured):
		try :
			if not isinstance(is_ha_configured,bool):
				raise TypeError("is_ha_configured must be set to bool value")
			self._is_ha_configured = is_ha_configured
		except Exception as e :
			raise e


	'''
	get license mode: FOREIGN_POOL, FOREIGN_LAS, EXPRESS, POOLED, LAS, LOCAL, CICO etc.
	'''
	@property
	def license_mode(self) :
		try:
			return self._license_mode
		except Exception as e :
			raise e
	'''
	set license mode: FOREIGN_POOL, FOREIGN_LAS, EXPRESS, POOLED, LAS, LOCAL, CICO etc.
	'''
	@license_mode.setter
	def license_mode(self,license_mode):
		try :
			if not isinstance(license_mode,str):
				raise TypeError("license_mode must be set to str value")
			self._license_mode = license_mode
		except Exception as e :
			raise e


	'''
	get Instance type indicates the deployment type of CPX
	'''
	@property
	def instance_type(self) :
		try:
			return self._instance_type
		except Exception as e :
			raise e


	'''
	get Private DNS of the managed device
	'''
	@property
	def private_dns(self) :
		try:
			return self._private_dns
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
	get Enterprise Bandwidth configured
	'''
	@property
	def ent_bw_available(self) :
		try:
			return self._ent_bw_available
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth configured
	'''
	@ent_bw_available.setter
	def ent_bw_available(self,ent_bw_available):
		try :
			if not isinstance(ent_bw_available,int):
				raise TypeError("ent_bw_available must be set to int value")
			self._ent_bw_available = ent_bw_available
		except Exception as e :
			raise e


	'''
	get Management IP Address for this Managed Device
	'''
	@property
	def mgmt_ip_address(self) :
		try:
			return self._mgmt_ip_address
		except Exception as e :
			raise e
	'''
	set Management IP Address for this Managed Device
	'''
	@mgmt_ip_address.setter
	def mgmt_ip_address(self,mgmt_ip_address):
		try :
			if not isinstance(mgmt_ip_address,str):
				raise TypeError("mgmt_ip_address must be set to str value")
			self._mgmt_ip_address = mgmt_ip_address
		except Exception as e :
			raise e


	'''
	get LM Host ID
	'''
	@property
	def lm_host_id(self) :
		try:
			return self._lm_host_id
		except Exception as e :
			raise e


	'''
	get URL query params flag.
	'''
	@property
	def httpquerywithurl(self) :
		try:
			return self._httpquerywithurl
		except Exception as e :
			raise e


	'''
	get IPv6 Address
	'''
	@property
	def ipv6_address(self) :
		try:
			return self._ipv6_address
		except Exception as e :
			raise e
	'''
	set IPv6 Address
	'''
	@ipv6_address.setter
	def ipv6_address(self,ipv6_address):
		try :
			if not isinstance(ipv6_address,str):
				raise TypeError("ipv6_address must be set to str value")
			self._ipv6_address = ipv6_address
		except Exception as e :
			raise e


	'''
	get Public IP of the managed device
	'''
	@property
	def public_ip(self) :
		try:
			return self._public_ip
		except Exception as e :
			raise e


	'''
	get Value based on which certain features may be enabled/disabled in NetScaler Console for the instance
	'''
	@property
	def instance_classifier(self) :
		try:
			return self._instance_classifier
		except Exception as e :
			raise e
	'''
	set Value based on which certain features may be enabled/disabled in NetScaler Console for the instance
	'''
	@instance_classifier.setter
	def instance_classifier(self,instance_classifier):
		try :
			if not isinstance(instance_classifier,int):
				raise TypeError("instance_classifier must be set to int value")
			self._instance_classifier = instance_classifier
		except Exception as e :
			raise e

	'''
	If set to true, NetScaler Console will re-register the instance by first deleting it then adding it
	'''
	@property
	def is_re_register(self):
		try:
			return self._is_re_register
		except Exception as e :
			raise e
	'''
	If set to true, NetScaler Console will re-register the instance by first deleting it then adding it
	'''
	@is_re_register.setter
	def is_re_register(self,is_re_register):
		try :
			if not isinstance(is_re_register,bool):
				raise TypeError("is_re_register must be set to bool value")
			self._is_re_register = is_re_register
		except Exception as e :
			raise e

	'''
	Peer Host Device IP Address for instance of type BLX ADC.
	'''
	@property
	def peer_host_device_ip(self):
		try:
			return self._peer_host_device_ip
		except Exception as e :
			raise e
	'''
	Peer Host Device IP Address for instance of type BLX ADC.
	'''
	@peer_host_device_ip.setter
	def peer_host_device_ip(self,peer_host_device_ip):
		try :
			if not isinstance(peer_host_device_ip,str):
				raise TypeError("peer_host_device_ip must be set to str value")
			self._peer_host_device_ip = peer_host_device_ip
		except Exception as e :
			raise e

	'''
	Array of tag_name and tag_value pair assocaited with an entity
	'''
	@property
	def entity_tag(self) :
		try:
			return self._entity_tag
		except Exception as e :
			raise e
	'''
	Array of tag_name and tag_value pair assocaited with an entity
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
	Previous trust ID of the mastools device
	'''
	@property
	def prev_trust_id(self):
		try:
			return self._prev_trust_id
		except Exception as e :
			raise e
	'''
	Previous trust ID of the mastools device
	'''
	@prev_trust_id.setter
	def prev_trust_id(self,prev_trust_id):
		try :
			if not isinstance(prev_trust_id,str):
				raise TypeError("prev_trust_id must be set to str value")
			self._prev_trust_id = prev_trust_id
		except Exception as e :
			raise e

	'''
	Device Host IP Address for instance of type BLX ADC.
	'''
	@property
	def device_host_ip(self):
		try:
			return self._device_host_ip
		except Exception as e :
			raise e
	'''
	Device Host IP Address for instance of type BLX ADC.
	'''
	@device_host_ip.setter
	def device_host_ip(self,device_host_ip):
		try :
			if not isinstance(device_host_ip,str):
				raise TypeError("device_host_ip must be set to str value")
			self._device_host_ip = device_host_ip
		except Exception as e :
			raise e

	'''
	Peer Device IP address for instance of type BLX ADC.
	'''
	@property
	def peer_device_ip(self):
		try:
			return self._peer_device_ip
		except Exception as e :
			raise e
	'''
	Peer Device IP address for instance of type BLX ADC.
	'''
	@peer_device_ip.setter
	def peer_device_ip(self,peer_device_ip):
		try :
			if not isinstance(peer_device_ip,str):
				raise TypeError("peer_device_ip must be set to str value")
			self._peer_device_ip = peer_device_ip
		except Exception as e :
			raise e

	'''
	File name which contains comma separated instances to be  discovered
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	File name which contains comma separated instances to be  discovered
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	File Location on Client for upload/download
	'''
	@property
	def file_location_path(self):
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e

	'''
	Task Id used by Triton to identify NS
	'''
	@property
	def tr_task_id(self):
		try:
			return self._tr_task_id
		except Exception as e :
			raise e
	'''
	Task Id used by Triton to identify NS
	'''
	@tr_task_id.setter
	def tr_task_id(self,tr_task_id):
		try :
			if not isinstance(tr_task_id,str):
				raise TypeError("tr_task_id must be set to str value")
			self._tr_task_id = tr_task_id
		except Exception as e :
			raise e

	'''
	User Name specified by the user for this NetScaler Instance.
	'''
	@property
	def profile_username(self):
		try:
			return self._profile_username
		except Exception as e :
			raise e
	'''
	User Name specified by the user for this NetScaler Instance.
	'''
	@profile_username.setter
	def profile_username(self,profile_username):
		try :
			if not isinstance(profile_username,str):
				raise TypeError("profile_username must be set to str value")
			self._profile_username = profile_username
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	Password specified by the user for this NetScaler Instance.
	'''
	@property
	def profile_password(self):
		try:
			return self._profile_password
		except Exception as e :
			raise e
	'''
	Password specified by the user for this NetScaler Instance.
	'''
	@profile_password.setter
	def profile_password(self,profile_password):
		try :
			if not isinstance(profile_password,str):
				raise TypeError("profile_password must be set to str value")
			self._profile_password = profile_password
		except Exception as e :
			raise e

	'''
	manual_inventory
	'''
	@property
	def manual_inventory(self):
		try:
			return self._manual_inventory
		except Exception as e :
			raise e
	'''
	manual_inventory
	'''
	@manual_inventory.setter
	def manual_inventory(self,manual_inventory):
		try :
			if not isinstance(manual_inventory,bool):
				raise TypeError("manual_inventory must be set to bool value")
			self._manual_inventory = manual_inventory
		except Exception as e :
			raise e

	'''
	Use this operation to annotate managed device.Use description property to annotate.
	'''

	'''
	Use this operation to annotate managed device.Use description property to annotate.
	'''
	@classmethod
	def annotate(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"annotate")
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"annotate", resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete managed device.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					managed_device_obj=managed_device()
					return cls.delete_bulk_request(client,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to restart of mastools device.
	'''
	@classmethod
	def mastools_restart(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"mastools_restart")
				return res
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"mastools_restart",resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete managed device asynchronously.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					managed_device_obj=managed_device()
					return cls.delete_bulk_request(client,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get managed devices.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				managed_device_obj=managed_device()
				response = managed_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update managed device.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				managed_device_obj=managed_device()
				return cls.update_bulk_request(client,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload build file.
	'''

	'''
	Use this operation to upload build file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to allocate/release licenses.
	'''
	@classmethod
	def allocate_license(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"allocate_license")
				return res
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"allocate_license",resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to allocate/release vpcu licenses.
	'''
	@classmethod
	def allocate_vcpu_license(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"allocate_vcpu_license")
				return res
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"allocate_vcpu_license",resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add managed device.Required properties are: ip_address,profile_name.Optional params: agent_id,file_name.For NetScaler BLX HA,device_host_ip,peer_device_ip,peer_host_ip are the additional required params.
	'''
	@classmethod
	def add_device(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"add_device")
				return res
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"add_device",resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add managed device.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of managed_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._filter=filter_
			return managed_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the managed_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._count=True
			response = managed_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of managed_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = managed_device_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(managed_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.managed_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_device_responses, response, "managed_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.managed_device_response_array
				i=0
				error = [managed_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.managed_device_response_array
			i=0
			managed_device_objs = [managed_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_managed_device'):
					for props in obj._managed_device:
						result = service.payload_formatter.string_to_bulk_resource(managed_device_response,self.__class__.__name__,props)
						managed_device_objs[i] = result.managed_device
						i=i+1
			return managed_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(managed_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class managed_device_response(base_response):
	def __init__(self,length=1) :
		self.managed_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.managed_device= [ managed_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class managed_device_responses(base_response):
	def __init__(self,length=1) :
		self.managed_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.managed_device_response_array = [ managed_device() for _ in range(length)]
