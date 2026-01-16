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
Configuration for Device Profile resource
'''

class device_profile(base_resource):
	_is_backup= ""
	_svm_ns_comm= ""
	_name= ""
	_use_global_setting_for_communication_with_ns= ""
	_is_default= ""
	_id= ""
	_tenant_id= ""
	_type= ""
	_username= ""
	_host_username= ""
	_password= ""
	_snmpprivpassword= ""
	_max_wait_time_reboot= ""
	_http_port= ""
	_snmpauthpassword= ""
	_snmpsecuritylevel= ""
	_ssh_port= ""
	_snmpprivprotocol= ""
	_act_id= ""
	_snmpauthprotocol= ""
	_host_password= ""
	_snmpsecurityname= ""
	_ssl_cert= ""
	_ns_profile_name= ""
	_passphrase= ""
	_https_port= ""
	_snmpcommunity= ""
	_sync_operation= ""
	_snmpversion= ""
	_cb_profile_name= ""
	_ssl_private_key= ""
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
			return "device_profile"
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
			return "device_profiles"
		except Exception as e :
			raise e



	'''
	get true, if this profile is a generated back up profile of user created profile
	'''
	@property
	def is_backup(self) :
		try:
			return self._is_backup
		except Exception as e :
			raise e


	'''
	get Communication protocol (http or https) with Instances
	'''
	@property
	def svm_ns_comm(self) :
		try:
			return self._svm_ns_comm
		except Exception as e :
			raise e
	'''
	set Communication protocol (http or https) with Instances
	'''
	@svm_ns_comm.setter
	def svm_ns_comm(self,svm_ns_comm):
		try :
			if not isinstance(svm_ns_comm,str):
				raise TypeError("svm_ns_comm must be set to str value")
			self._svm_ns_comm = svm_ns_comm
		except Exception as e :
			raise e


	'''
	get Profile Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Profile Name
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
	get True, if the communication with Instance needs to be global and not device specific
	'''
	@property
	def use_global_setting_for_communication_with_ns(self) :
		try:
			return self._use_global_setting_for_communication_with_ns
		except Exception as e :
			raise e
	'''
	set True, if the communication with Instance needs to be global and not device specific
	'''
	@use_global_setting_for_communication_with_ns.setter
	def use_global_setting_for_communication_with_ns(self,use_global_setting_for_communication_with_ns):
		try :
			if not isinstance(use_global_setting_for_communication_with_ns,bool):
				raise TypeError("use_global_setting_for_communication_with_ns must be set to bool value")
			self._use_global_setting_for_communication_with_ns = use_global_setting_for_communication_with_ns
		except Exception as e :
			raise e


	'''
	get True, if this profile is system generated and can not be deleted
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the device profiles
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the device profiles
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
	get Tenant Id of device profile
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Profile Type, This must be with in specified supported instance types: blx,ns,nssdx,cpx
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Profile Type, This must be with in specified supported instance types: blx,ns,nssdx,cpx
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
	Instance credentials.Username provided in the profile will be used to contact the instance
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	Instance credentials.Username provided in the profile will be used to contact the instance
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
	Host User Name for this profile.Used for BLX form factor of ADC
	'''
	@property
	def host_username(self):
		try:
			return self._host_username
		except Exception as e :
			raise e
	'''
	Host User Name for this profile.Used for BLX form factor of ADC
	'''
	@host_username.setter
	def host_username(self,host_username):
		try :
			if not isinstance(host_username,str):
				raise TypeError("host_username must be set to str value")
			self._host_username = host_username
		except Exception as e :
			raise e

	'''
	Instance credentials.Password for this profile
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	Instance credentials.Password for this profile
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
	SNMP v3 priv password for this profile
	'''
	@property
	def snmpprivpassword(self):
		try:
			return self._snmpprivpassword
		except Exception as e :
			raise e
	'''
	SNMP v3 priv password for this profile
	'''
	@snmpprivpassword.setter
	def snmpprivpassword(self,snmpprivpassword):
		try :
			if not isinstance(snmpprivpassword,str):
				raise TypeError("snmpprivpassword must be set to str value")
			self._snmpprivpassword = snmpprivpassword
		except Exception as e :
			raise e

	'''
	Max waiting time to reboot NetScaler
	'''
	@property
	def max_wait_time_reboot(self):
		try:
			return self._max_wait_time_reboot
		except Exception as e :
			raise e
	'''
	Max waiting time to reboot NetScaler
	'''
	@max_wait_time_reboot.setter
	def max_wait_time_reboot(self,max_wait_time_reboot):
		try :
			if not isinstance(max_wait_time_reboot,str):
				raise TypeError("max_wait_time_reboot must be set to str value")
			self._max_wait_time_reboot = max_wait_time_reboot
		except Exception as e :
			raise e

	'''
	HTTP port to connect to the device
	'''
	@property
	def http_port(self):
		try:
			return self._http_port
		except Exception as e :
			raise e
	'''
	HTTP port to connect to the device
	'''
	@http_port.setter
	def http_port(self,http_port):
		try :
			if not isinstance(http_port,int):
				raise TypeError("http_port must be set to int value")
			self._http_port = http_port
		except Exception as e :
			raise e

	'''
	SNMP v3 auth password for this profile
	'''
	@property
	def snmpauthpassword(self):
		try:
			return self._snmpauthpassword
		except Exception as e :
			raise e
	'''
	SNMP v3 auth password for this profile
	'''
	@snmpauthpassword.setter
	def snmpauthpassword(self,snmpauthpassword):
		try :
			if not isinstance(snmpauthpassword,str):
				raise TypeError("snmpauthpassword must be set to str value")
			self._snmpauthpassword = snmpauthpassword
		except Exception as e :
			raise e

	'''
	SNMP v3 security level for this profile
	'''
	@property
	def snmpsecuritylevel(self):
		try:
			return self._snmpsecuritylevel
		except Exception as e :
			raise e
	'''
	SNMP v3 security level for this profile
	'''
	@snmpsecuritylevel.setter
	def snmpsecuritylevel(self,snmpsecuritylevel):
		try :
			if not isinstance(snmpsecuritylevel,str):
				raise TypeError("snmpsecuritylevel must be set to str value")
			self._snmpsecuritylevel = snmpsecuritylevel
		except Exception as e :
			raise e

	'''
	SSH port to connect to the device
	'''
	@property
	def ssh_port(self):
		try:
			return self._ssh_port
		except Exception as e :
			raise e
	'''
	SSH port to connect to the device
	'''
	@ssh_port.setter
	def ssh_port(self,ssh_port):
		try :
			if not isinstance(ssh_port,str):
				raise TypeError("ssh_port must be set to str value")
			self._ssh_port = ssh_port
		except Exception as e :
			raise e

	'''
	SNMP v3 priv protocol for this profile
	'''
	@property
	def snmpprivprotocol(self):
		try:
			return self._snmpprivprotocol
		except Exception as e :
			raise e
	'''
	SNMP v3 priv protocol for this profile
	'''
	@snmpprivprotocol.setter
	def snmpprivprotocol(self,snmpprivprotocol):
		try :
			if not isinstance(snmpprivprotocol,str):
				raise TypeError("snmpprivprotocol must be set to str value")
			self._snmpprivprotocol = snmpprivprotocol
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
	SNMP v3 auth protocol for this profile
	'''
	@property
	def snmpauthprotocol(self):
		try:
			return self._snmpauthprotocol
		except Exception as e :
			raise e
	'''
	SNMP v3 auth protocol for this profile
	'''
	@snmpauthprotocol.setter
	def snmpauthprotocol(self,snmpauthprotocol):
		try :
			if not isinstance(snmpauthprotocol,str):
				raise TypeError("snmpauthprotocol must be set to str value")
			self._snmpauthprotocol = snmpauthprotocol
		except Exception as e :
			raise e

	'''
	Host Password for this profile.Used for BLX form factor of ADC
	'''
	@property
	def host_password(self):
		try:
			return self._host_password
		except Exception as e :
			raise e
	'''
	Host Password for this profile.Used for BLX form factor of ADC
	'''
	@host_password.setter
	def host_password(self,host_password):
		try :
			if not isinstance(host_password,str):
				raise TypeError("host_password must be set to str value")
			self._host_password = host_password
		except Exception as e :
			raise e

	'''
	SNMP v3 security name for this profile
	'''
	@property
	def snmpsecurityname(self):
		try:
			return self._snmpsecurityname
		except Exception as e :
			raise e
	'''
	SNMP v3 security name for this profile
	'''
	@snmpsecurityname.setter
	def snmpsecurityname(self,snmpsecurityname):
		try :
			if not isinstance(snmpsecurityname,str):
				raise TypeError("snmpsecurityname must be set to str value")
			self._snmpsecurityname = snmpsecurityname
		except Exception as e :
			raise e

	'''
	SSL Certificate for certificate based authentication
	'''
	@property
	def ssl_cert(self):
		try:
			return self._ssl_cert
		except Exception as e :
			raise e
	'''
	SSL Certificate for certificate based authentication
	'''
	@ssl_cert.setter
	def ssl_cert(self,ssl_cert):
		try :
			if not isinstance(ssl_cert,str):
				raise TypeError("ssl_cert must be set to str value")
			self._ssl_cert = ssl_cert
		except Exception as e :
			raise e

	'''
	Profile Name, This is one of the already created NetScaler profiles
	'''
	@property
	def ns_profile_name(self):
		try:
			return self._ns_profile_name
		except Exception as e :
			raise e
	'''
	Profile Name, This is one of the already created NetScaler profiles
	'''
	@ns_profile_name.setter
	def ns_profile_name(self,ns_profile_name):
		try :
			if not isinstance(ns_profile_name,str):
				raise TypeError("ns_profile_name must be set to str value")
			self._ns_profile_name = ns_profile_name
		except Exception as e :
			raise e

	'''
	Passphrase with which private key is encrypted
	'''
	@property
	def passphrase(self):
		try:
			return self._passphrase
		except Exception as e :
			raise e
	'''
	Passphrase with which private key is encrypted
	'''
	@passphrase.setter
	def passphrase(self,passphrase):
		try :
			if not isinstance(passphrase,str):
				raise TypeError("passphrase must be set to str value")
			self._passphrase = passphrase
		except Exception as e :
			raise e

	'''
	HTTPS port to connect to the device
	'''
	@property
	def https_port(self):
		try:
			return self._https_port
		except Exception as e :
			raise e
	'''
	HTTPS port to connect to the device
	'''
	@https_port.setter
	def https_port(self,https_port):
		try :
			if not isinstance(https_port,int):
				raise TypeError("https_port must be set to int value")
			self._https_port = https_port
		except Exception as e :
			raise e

	'''
	SNMP community for this profile
	'''
	@property
	def snmpcommunity(self):
		try:
			return self._snmpcommunity
		except Exception as e :
			raise e
	'''
	SNMP community for this profile
	'''
	@snmpcommunity.setter
	def snmpcommunity(self,snmpcommunity):
		try :
			if not isinstance(snmpcommunity,str):
				raise TypeError("snmpcommunity must be set to str value")
			self._snmpcommunity = snmpcommunity
		except Exception as e :
			raise e

	'''
	Flag to indicate whether operation should be performed in sync/async mode
	'''
	@property
	def sync_operation(self):
		try:
			return self._sync_operation
		except Exception as e :
			raise e
	'''
	Flag to indicate whether operation should be performed in sync/async mode
	'''
	@sync_operation.setter
	def sync_operation(self,sync_operation):
		try :
			if not isinstance(sync_operation,bool):
				raise TypeError("sync_operation must be set to bool value")
			self._sync_operation = sync_operation
		except Exception as e :
			raise e

	'''
	SNMP version for this profile
	'''
	@property
	def snmpversion(self):
		try:
			return self._snmpversion
		except Exception as e :
			raise e
	'''
	SNMP version for this profile
	'''
	@snmpversion.setter
	def snmpversion(self,snmpversion):
		try :
			if not isinstance(snmpversion,str):
				raise TypeError("snmpversion must be set to str value")
			self._snmpversion = snmpversion
		except Exception as e :
			raise e

	'''
	Profile Name, This is one of the already created NetScaler profiles
	'''
	@property
	def cb_profile_name(self):
		try:
			return self._cb_profile_name
		except Exception as e :
			raise e
	'''
	Profile Name, This is one of the already created NetScaler profiles
	'''
	@cb_profile_name.setter
	def cb_profile_name(self,cb_profile_name):
		try :
			if not isinstance(cb_profile_name,str):
				raise TypeError("cb_profile_name must be set to str value")
			self._cb_profile_name = cb_profile_name
		except Exception as e :
			raise e

	'''
	SSL Private Key for key based authentication
	'''
	@property
	def ssl_private_key(self):
		try:
			return self._ssl_private_key
		except Exception as e :
			raise e
	'''
	SSL Private Key for key based authentication
	'''
	@ssl_private_key.setter
	def ssl_private_key(self,ssl_private_key):
		try :
			if not isinstance(ssl_private_key,str):
				raise TypeError("ssl_private_key must be set to str value")
			self._ssl_private_key = ssl_private_key
		except Exception as e :
			raise e

	'''
	Use this operation to delete device profile(s).
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
					device_profile_obj=device_profile()
					return cls.delete_bulk_request(client,resource,device_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify device profile.
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
				device_profile_obj=device_profile()
				return cls.update_bulk_request(client,resource,device_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add device profile.
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
				device_profile_obj= device_profile()
				return cls.perform_operation_bulk_request(service,resource,device_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get device profiles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				device_profile_obj=device_profile()
				response = device_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_profile_obj = device_profile()
			option_ = options()
			option_._filter=filter_
			return device_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_profile_obj = device_profile()
			option_ = options()
			option_._count=True
			response = device_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_profile_obj = device_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_profile_responses, response, "device_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_profile_response_array
				i=0
				error = [device_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_profile_response_array
			i=0
			device_profile_objs = [device_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_profile'):
					for props in obj._device_profile:
						result = service.payload_formatter.string_to_bulk_resource(device_profile_response,self.__class__.__name__,props)
						device_profile_objs[i] = result.device_profile
						i=i+1
			return device_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_profile_response(base_response):
	def __init__(self,length=1) :
		self.device_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_profile= [ device_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_profile_responses(base_response):
	def __init__(self,length=1) :
		self.device_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_profile_response_array = [ device_profile() for _ in range(length)]
