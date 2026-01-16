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
from massrc.com.citrix.mas.nitro.resource.config.mps.managed_device import managed_device


'''
Configuration for Agent resource
'''

class mps_agent(base_resource):
	_rpt_sample_time= ""
	_memory_count= ""
	_last_up_time= ""
	_state= ""
	_agent_upgrade_state= ""
	_disk_usage= ""
	_public_key= ""
	_name= ""
	_down_count= ""
	_cpu_usage= ""
	_deployment_status= ""
	_instance_id= ""
	_cpu_count= ""
	_username= ""
	_version= ""
	_tenant= ""
	_memory_usage= ""
	_platform= ""
	_password= ""
	_id= ""
	_upgrade_failure_message= ""
	_disk_count= ""
	_provision_request_id= ""
	_upgrade_timezone= ""
	_datacenter_id= ""
	_hostname= ""
	_discovery_time= ""
	_agent_upgrade_time= ""
	_connector_ips= ""
	_diag_endtime= ""
	_upgrade_version= ""
	_ads_service_type= ""
	_act_id= ""
	_bulk_request_ipaddress= ""
	_url= ""
	_port= ""
	_certificate= ""
	_zipcode= ""
	_registered_devices=[]
	_country= ""
	_new_password= ""
	_agent_msg_router_url= ""
	_loc= ""
	_city= ""
	_server_time= ""
	_mas_version= ""
	_diag_status= ""
	_bulk_request_port= ""
	_region= ""
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
			return "mps_agent"
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
			return "mps_agents"
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
	get Shows for how long agent memory threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def memory_count(self) :
		try:
			return self._memory_count
		except Exception as e :
			raise e
	'''
	set Shows for how long agent memory threshold breach, each value of count increases after every 5 minutes
	'''
	@memory_count.setter
	def memory_count(self,memory_count):
		try :
			if not isinstance(memory_count,int):
				raise TypeError("memory_count must be set to int value")
			self._memory_count = memory_count
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
	get Agent state
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Agent state
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
	get Status of Agent Upgrade(Scheduled/InProgress/Success/Failed).
	'''
	@property
	def agent_upgrade_state(self) :
		try:
			return self._agent_upgrade_state
		except Exception as e :
			raise e
	'''
	set Status of Agent Upgrade(Scheduled/InProgress/Success/Failed).
	'''
	@agent_upgrade_state.setter
	def agent_upgrade_state(self,agent_upgrade_state):
		try :
			if not isinstance(agent_upgrade_state,str):
				raise TypeError("agent_upgrade_state must be set to str value")
			self._agent_upgrade_state = agent_upgrade_state
		except Exception as e :
			raise e


	'''
	get Total disk space usage.
	'''
	@property
	def disk_usage(self) :
		try:
			return self._disk_usage
		except Exception as e :
			raise e
	'''
	set Total disk space usage.
	'''
	@disk_usage.setter
	def disk_usage(self,disk_usage):
		try :
			if not isinstance(disk_usage,long):
				raise TypeError("disk_usage must be set to long value")
			self._disk_usage = disk_usage
		except Exception as e :
			raise e


	'''
	get public key for agent
	'''
	@property
	def public_key(self) :
		try:
			return self._public_key
		except Exception as e :
			raise e
	'''
	set public key for agent
	'''
	@public_key.setter
	def public_key(self,public_key):
		try :
			if not isinstance(public_key,str):
				raise TypeError("public_key must be set to str value")
			self._public_key = public_key
		except Exception as e :
			raise e


	'''
	get Agent IP Address
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Agent IP Address
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
	get Shows for how long agent was down, each value of count increases after every 10 seconds
	'''
	@property
	def down_count(self) :
		try:
			return self._down_count
		except Exception as e :
			raise e
	'''
	set Shows for how long agent was down, each value of count increases after every 10 seconds
	'''
	@down_count.setter
	def down_count(self,down_count):
		try :
			if not isinstance(down_count,int):
				raise TypeError("down_count must be set to int value")
			self._down_count = down_count
		except Exception as e :
			raise e


	'''
	get Total CPU usage.
	'''
	@property
	def cpu_usage(self) :
		try:
			return self._cpu_usage
		except Exception as e :
			raise e
	'''
	set Total CPU usage.
	'''
	@cpu_usage.setter
	def cpu_usage(self,cpu_usage):
		try :
			if not isinstance(cpu_usage,float):
				raise TypeError("cpu_usage must be set to float value")
			self._cpu_usage = cpu_usage
		except Exception as e :
			raise e


	'''
	get Deployment status of this node.
	'''
	@property
	def deployment_status(self) :
		try:
			return self._deployment_status
		except Exception as e :
			raise e
	'''
	set Deployment status of this node.
	'''
	@deployment_status.setter
	def deployment_status(self,deployment_status):
		try :
			if not isinstance(deployment_status,bool):
				raise TypeError("deployment_status must be set to bool value")
			self._deployment_status = deployment_status
		except Exception as e :
			raise e


	'''
	get Unique ID of device provided by Global Trust Service
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e
	'''
	set Unique ID of device provided by Global Trust Service
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
	get Shows for how long agent cpu threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def cpu_count(self) :
		try:
			return self._cpu_count
		except Exception as e :
			raise e
	'''
	set Shows for how long agent cpu threshold breach, each value of count increases after every 5 minutes
	'''
	@cpu_count.setter
	def cpu_count(self,cpu_count):
		try :
			if not isinstance(cpu_count,int):
				raise TypeError("cpu_count must be set to int value")
			self._cpu_count = cpu_count
		except Exception as e :
			raise e


	'''
	get username configured on DB node.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set username configured on DB node.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get version.
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set version.
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
	get Tenant
	'''
	@property
	def tenant(self) :
		try:
			return self._tenant
		except Exception as e :
			raise e
	'''
	set Tenant
	'''
	@tenant.setter
	def tenant(self,tenant):
		try :
			if not isinstance(tenant,str):
				raise TypeError("tenant must be set to str value")
			self._tenant = tenant
		except Exception as e :
			raise e


	'''
	get Total memory usage.
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e
	'''
	set Total memory usage.
	'''
	@memory_usage.setter
	def memory_usage(self,memory_usage):
		try :
			if not isinstance(memory_usage,long):
				raise TypeError("memory_usage must be set to long value")
			self._memory_usage = memory_usage
		except Exception as e :
			raise e


	'''
	get Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e
	'''
	set Platform
	'''
	@platform.setter
	def platform(self,platform):
		try :
			if not isinstance(platform,str):
				raise TypeError("platform must be set to str value")
			self._platform = platform
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Id is system generated key for agent registered with NMX Cloud.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for agent registered with NMX Cloud.
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
	get Agent upgrade failure message.
	'''
	@property
	def upgrade_failure_message(self) :
		try:
			return self._upgrade_failure_message
		except Exception as e :
			raise e
	'''
	set Agent upgrade failure message.
	'''
	@upgrade_failure_message.setter
	def upgrade_failure_message(self,upgrade_failure_message):
		try :
			if not isinstance(upgrade_failure_message,str):
				raise TypeError("upgrade_failure_message must be set to str value")
			self._upgrade_failure_message = upgrade_failure_message
		except Exception as e :
			raise e


	'''
	get Shows for how long agent disk threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def disk_count(self) :
		try:
			return self._disk_count
		except Exception as e :
			raise e
	'''
	set Shows for how long agent disk threshold breach, each value of count increases after every 5 minutes
	'''
	@disk_count.setter
	def disk_count(self,disk_count):
		try :
			if not isinstance(disk_count,int):
				raise TypeError("disk_count must be set to int value")
			self._disk_count = disk_count
		except Exception as e :
			raise e


	'''
	get Value is set only if the instance was provisioned from MAS
	'''
	@property
	def provision_request_id(self) :
		try:
			return self._provision_request_id
		except Exception as e :
			raise e
	'''
	set Value is set only if the instance was provisioned from MAS
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
	get Stores the agent upgrade timezone
	'''
	@property
	def upgrade_timezone(self) :
		try:
			return self._upgrade_timezone
		except Exception as e :
			raise e
	'''
	set Stores the agent upgrade timezone
	'''
	@upgrade_timezone.setter
	def upgrade_timezone(self,upgrade_timezone):
		try :
			if not isinstance(upgrade_timezone,str):
				raise TypeError("upgrade_timezone must be set to str value")
			self._upgrade_timezone = upgrade_timezone
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
	get Hostname of the agent
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of the agent
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
	get Stores the agent upgrade start time
	'''
	@property
	def agent_upgrade_time(self) :
		try:
			return self._agent_upgrade_time
		except Exception as e :
			raise e
	'''
	set Stores the agent upgrade start time
	'''
	@agent_upgrade_time.setter
	def agent_upgrade_time(self,agent_upgrade_time):
		try :
			if not isinstance(agent_upgrade_time,str):
				raise TypeError("agent_upgrade_time must be set to str value")
			self._agent_upgrade_time = agent_upgrade_time
		except Exception as e :
			raise e

	'''
	Comma separated list of connector node IPs.
	'''
	@property
	def connector_ips(self):
		try:
			return self._connector_ips
		except Exception as e :
			raise e
	'''
	Comma separated list of connector node IPs.
	'''
	@connector_ips.setter
	def connector_ips(self,connector_ips):
		try :
			if not isinstance(connector_ips,str):
				raise TypeError("connector_ips must be set to str value")
			self._connector_ips = connector_ips
		except Exception as e :
			raise e

	'''
	Agent diag endtime
	'''
	@property
	def diag_endtime(self):
		try:
			return self._diag_endtime
		except Exception as e :
			raise e
	'''
	Agent diag endtime
	'''
	@diag_endtime.setter
	def diag_endtime(self,diag_endtime):
		try :
			if not isinstance(diag_endtime,str):
				raise TypeError("diag_endtime must be set to str value")
			self._diag_endtime = diag_endtime
		except Exception as e :
			raise e

	'''
	Represents the next version the agent should upgrade to
	'''
	@property
	def upgrade_version(self):
		try:
			return self._upgrade_version
		except Exception as e :
			raise e
	'''
	Represents the next version the agent should upgrade to
	'''
	@upgrade_version.setter
	def upgrade_version(self,upgrade_version):
		try :
			if not isinstance(upgrade_version,str):
				raise TypeError("upgrade_version must be set to str value")
			self._upgrade_version = upgrade_version
		except Exception as e :
			raise e

	'''
	ADS Service Type. Supported Types: NetScaler Console, AUTOMATION, INTENT
	'''
	@property
	def ads_service_type(self):
		try:
			return self._ads_service_type
		except Exception as e :
			raise e
	'''
	ADS Service Type. Supported Types: NetScaler Console, AUTOMATION, INTENT
	'''
	@ads_service_type.setter
	def ads_service_type(self,ads_service_type):
		try :
			if not isinstance(ads_service_type,str):
				raise TypeError("ads_service_type must be set to str value")
			self._ads_service_type = ads_service_type
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
	Activity Id
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	ABDP IP Address.
	'''
	@property
	def bulk_request_ipaddress(self):
		try:
			return self._bulk_request_ipaddress
		except Exception as e :
			raise e
	'''
	ABDP IP Address.
	'''
	@bulk_request_ipaddress.setter
	def bulk_request_ipaddress(self,bulk_request_ipaddress):
		try :
			if not isinstance(bulk_request_ipaddress,str):
				raise TypeError("bulk_request_ipaddress must be set to str value")
			self._bulk_request_ipaddress = bulk_request_ipaddress
		except Exception as e :
			raise e

	'''
	URL of ABDP Certificate File Location
	'''
	@property
	def url(self):
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	URL of ABDP Certificate File Location
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
	Port number for ABDP Certificate file location
	'''
	@property
	def port(self):
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	Port number for ABDP Certificate file location
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e

	'''
	Name of ABDP Certificate File
	'''
	@property
	def certificate(self):
		try:
			return self._certificate
		except Exception as e :
			raise e
	'''
	Name of ABDP Certificate File
	'''
	@certificate.setter
	def certificate(self,certificate):
		try :
			if not isinstance(certificate,str):
				raise TypeError("certificate must be set to str value")
			self._certificate = certificate
		except Exception as e :
			raise e

	'''
	Zipcode of location
	'''
	@property
	def zipcode(self):
		try:
			return self._zipcode
		except Exception as e :
			raise e
	'''
	Zipcode of location
	'''
	@zipcode.setter
	def zipcode(self,zipcode):
		try :
			if not isinstance(zipcode,str):
				raise TypeError("zipcode must be set to str value")
			self._zipcode = zipcode
		except Exception as e :
			raise e

	'''
	List of registered devices.
	'''
	@property
	def registered_devices(self) :
		try:
			return self._registered_devices
		except Exception as e :
			raise e
	'''
	List of registered devices.
	'''
	@registered_devices.setter
	def registered_devices(self,registered_devices) :
		try :
			if not isinstance(registered_devices,list):
				raise TypeError("registered_devices must be set to array of managed_device value")
			for item in registered_devices :
				if not isinstance(item,managed_device):
					raise TypeError("item must be set to managed_device value")
			self._registered_devices = registered_devices
		except Exception as e :
			raise e

	'''
	Country
	'''
	@property
	def country(self):
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	Country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e

	'''
	new password
	'''
	@property
	def new_password(self):
		try:
			return self._new_password
		except Exception as e :
			raise e
	'''
	new password
	'''
	@new_password.setter
	def new_password(self,new_password):
		try :
			if not isinstance(new_password,str):
				raise TypeError("new_password must be set to str value")
			self._new_password = new_password
		except Exception as e :
			raise e

	'''
	URL for router
	'''
	@property
	def agent_msg_router_url(self):
		try:
			return self._agent_msg_router_url
		except Exception as e :
			raise e
	'''
	URL for router
	'''
	@agent_msg_router_url.setter
	def agent_msg_router_url(self,agent_msg_router_url):
		try :
			if not isinstance(agent_msg_router_url,str):
				raise TypeError("agent_msg_router_url must be set to str value")
			self._agent_msg_router_url = agent_msg_router_url
		except Exception as e :
			raise e

	'''
	Location - latitude and longitude
	'''
	@property
	def loc(self):
		try:
			return self._loc
		except Exception as e :
			raise e
	'''
	Location - latitude and longitude
	'''
	@loc.setter
	def loc(self,loc):
		try :
			if not isinstance(loc,str):
				raise TypeError("loc must be set to str value")
			self._loc = loc
		except Exception as e :
			raise e

	'''
	City
	'''
	@property
	def city(self):
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	City
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
	NetScaler Console server's Epoch time
	'''
	@property
	def server_time(self):
		try:
			return self._server_time
		except Exception as e :
			raise e
	'''
	NetScaler Console server's Epoch time
	'''
	@server_time.setter
	def server_time(self,server_time):
		try :
			if not isinstance(server_time,long):
				raise TypeError("server_time must be set to long value")
			self._server_time = server_time
		except Exception as e :
			raise e

	'''
	NetScaler Console server's current version
	'''
	@property
	def mas_version(self):
		try:
			return self._mas_version
		except Exception as e :
			raise e
	'''
	NetScaler Console server's current version
	'''
	@mas_version.setter
	def mas_version(self,mas_version):
		try :
			if not isinstance(mas_version,str):
				raise TypeError("mas_version must be set to str value")
			self._mas_version = mas_version
		except Exception as e :
			raise e

	'''
	Agent diag status
	'''
	@property
	def diag_status(self):
		try:
			return self._diag_status
		except Exception as e :
			raise e
	'''
	Agent diag status
	'''
	@diag_status.setter
	def diag_status(self,diag_status):
		try :
			if not isinstance(diag_status,int):
				raise TypeError("diag_status must be set to int value")
			self._diag_status = diag_status
		except Exception as e :
			raise e

	'''
	Port number for ABDP
	'''
	@property
	def bulk_request_port(self):
		try:
			return self._bulk_request_port
		except Exception as e :
			raise e
	'''
	Port number for ABDP
	'''
	@bulk_request_port.setter
	def bulk_request_port(self,bulk_request_port):
		try :
			if not isinstance(bulk_request_port,int):
				raise TypeError("bulk_request_port must be set to int value")
			self._bulk_request_port = bulk_request_port
		except Exception as e :
			raise e

	'''
	Region
	'''
	@property
	def region(self):
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	Region
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_agent_obj=mps_agent()
				response = mps_agent_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to reboot the Agent.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"reboot")
				return res
			else : 
				mps_agent_obj= mps_agent()
				return cls.perform_operation_bulk_request(service,"reboot",resource,mps_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Agent information.
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
					mps_agent_obj=mps_agent()
					return cls.delete_bulk_request(client,resource,mps_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add Agent information.
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
				mps_agent_obj= mps_agent()
				return cls.perform_operation_bulk_request(service,resource,mps_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify Agent information.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				mps_agent_obj=mps_agent()
				return cls.update_bulk_request(client,resource,mps_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to restart of Agent daemons.
	'''
	@classmethod
	def restart(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"restart")
				return res
			else : 
				mps_agent_obj= mps_agent()
				return cls.perform_operation_bulk_request(service,"restart",resource,mps_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_agent_obj = mps_agent()
			option_ = options()
			option_._filter=filter_
			return mps_agent_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_agent resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_agent_obj = mps_agent()
			option_ = options()
			option_._count=True
			response = mps_agent_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_agent_obj = mps_agent()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_agent_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_agent_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_agent
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_agent_responses, response, "mps_agent_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_agent_response_array
				i=0
				error = [mps_agent() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_agent_response_array
			i=0
			mps_agent_objs = [mps_agent() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_agent'):
					for props in obj._mps_agent:
						result = service.payload_formatter.string_to_bulk_resource(mps_agent_response,self.__class__.__name__,props)
						mps_agent_objs[i] = result.mps_agent
						i=i+1
			return mps_agent_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_agent,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_agent_response(base_response):
	def __init__(self,length=1) :
		self.mps_agent= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_agent= [ mps_agent() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_agent_responses(base_response):
	def __init__(self,length=1) :
		self.mps_agent_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_agent_response_array = [ mps_agent() for _ in range(length)]
