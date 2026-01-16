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
Configuration for SDX SNMP Configuration resource
'''

class sdx_snmp_config(base_resource):
	_sdx_ip_address= ""
	_snmpsecuritylevel= ""
	_snmpauthprotocol= ""
	_snmpcommunity= ""
	_state= ""
	_snmpauthpassword= ""
	_snmpprivpassword= ""
	_snmpprivprotocol= ""
	_trapdestination= ""
	_snmpversion= ""
	_snmpsecurityname= ""
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
			return "sdx_snmp_config"
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
			return "sdx_snmp_configs"
		except Exception as e :
			raise e



	'''
	get SDX IP Address
	'''
	@property
	def sdx_ip_address(self) :
		try:
			return self._sdx_ip_address
		except Exception as e :
			raise e
	'''
	set SDX IP Address
	'''
	@sdx_ip_address.setter
	def sdx_ip_address(self,sdx_ip_address):
		try :
			if not isinstance(sdx_ip_address,str):
				raise TypeError("sdx_ip_address must be set to str value")
			self._sdx_ip_address = sdx_ip_address
		except Exception as e :
			raise e


	'''
	get SNMP v3 security level
	'''
	@property
	def snmpsecuritylevel(self) :
		try:
			return self._snmpsecuritylevel
		except Exception as e :
			raise e
	'''
	set SNMP v3 security level
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
	get SNMP v3 auth protocol
	'''
	@property
	def snmpauthprotocol(self) :
		try:
			return self._snmpauthprotocol
		except Exception as e :
			raise e
	'''
	set SNMP v3 auth protocol
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
	get SNMP community
	'''
	@property
	def snmpcommunity(self) :
		try:
			return self._snmpcommunity
		except Exception as e :
			raise e
	'''
	set SNMP community
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
	get State of configuration (enable/disable)
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of configuration (enable/disable)
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
	get SNMP v3 auth password
	'''
	@property
	def snmpauthpassword(self) :
		try:
			return self._snmpauthpassword
		except Exception as e :
			raise e
	'''
	set SNMP v3 auth password
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
	get SNMP v3 priv password
	'''
	@property
	def snmpprivpassword(self) :
		try:
			return self._snmpprivpassword
		except Exception as e :
			raise e
	'''
	set SNMP v3 priv password
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
	get SNMP v3 priv protocol
	'''
	@property
	def snmpprivprotocol(self) :
		try:
			return self._snmpprivprotocol
		except Exception as e :
			raise e
	'''
	set SNMP v3 priv protocol
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
	get Trapdestination
	'''
	@property
	def trapdestination(self) :
		try:
			return self._trapdestination
		except Exception as e :
			raise e
	'''
	set Trapdestination
	'''
	@trapdestination.setter
	def trapdestination(self,trapdestination):
		try :
			if not isinstance(trapdestination,str):
				raise TypeError("trapdestination must be set to str value")
			self._trapdestination = trapdestination
		except Exception as e :
			raise e


	'''
	get SNMP version
	'''
	@property
	def snmpversion(self) :
		try:
			return self._snmpversion
		except Exception as e :
			raise e
	'''
	set SNMP version
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
	get SNMP v3 security name
	'''
	@property
	def snmpsecurityname(self) :
		try:
			return self._snmpsecurityname
		except Exception as e :
			raise e
	'''
	set SNMP v3 security name
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
	Use this operation to add snmp configuration.
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
				sdx_snmp_config_obj= sdx_snmp_config()
				return cls.perform_operation_bulk_request(service,resource,sdx_snmp_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete snmp configuration.
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
					sdx_snmp_config_obj=sdx_snmp_config()
					return cls.delete_bulk_request(client,resource,sdx_snmp_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp configuration.
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
				sdx_snmp_config_obj=sdx_snmp_config()
				return cls.update_bulk_request(client,resource,sdx_snmp_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get snmp configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				sdx_snmp_config_obj=sdx_snmp_config()
				response = sdx_snmp_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_snmp_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_snmp_config_obj = sdx_snmp_config()
			option_ = options()
			option_._filter=filter_
			return sdx_snmp_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_snmp_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_snmp_config_obj = sdx_snmp_config()
			option_ = options()
			option_._count=True
			response = sdx_snmp_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_snmp_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_snmp_config_obj = sdx_snmp_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_snmp_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_snmp_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_snmp_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_snmp_config_responses, response, "sdx_snmp_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_snmp_config_response_array
				i=0
				error = [sdx_snmp_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_snmp_config_response_array
			i=0
			sdx_snmp_config_objs = [sdx_snmp_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_snmp_config'):
					for props in obj._sdx_snmp_config:
						result = service.payload_formatter.string_to_bulk_resource(sdx_snmp_config_response,self.__class__.__name__,props)
						sdx_snmp_config_objs[i] = result.sdx_snmp_config
						i=i+1
			return sdx_snmp_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_snmp_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_snmp_config_response(base_response):
	def __init__(self,length=1) :
		self.sdx_snmp_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_snmp_config= [ sdx_snmp_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_snmp_config_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_snmp_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_snmp_config_response_array = [ sdx_snmp_config() for _ in range(length)]
