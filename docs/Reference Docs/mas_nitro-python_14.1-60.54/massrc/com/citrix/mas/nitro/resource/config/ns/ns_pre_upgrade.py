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
Configuration for Pre Upgrade fro NetScaler resource
'''

class ns_pre_upgrade(base_resource):
	_config_error= ""
	_display_name= ""
	_build_image_error= ""
	_act_id= ""
	_uname= ""
	_id= ""
	_disk_space_error= ""
	_policy_check_details= ""
	_hardware_error= ""
	_user_custom_info_details= ""
	_primary_config_error= ""
	_user_custom_info= ""
	_connectivity_error= ""
	_ha_master_state= ""
	_connectivity_error_details= ""
	_policy_check= ""
	_ip_address= ""
	_hardware_error_details= ""
	_disk_space_error_details= ""
	_secondary_config_error= ""
	_image_var_nsinstall= ""
	_ha_ip_address= ""
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
			return "ns_pre_upgrade"
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
			return "ns_pre_upgrades"
		except Exception as e :
			raise e



	'''
	get Config error if compatible configuration file not found
	'''
	@property
	def config_error(self) :
		try:
			return self._config_error
		except Exception as e :
			raise e
	'''
	set Config error if compatible configuration file not found
	'''
	@config_error.setter
	def config_error(self,config_error):
		try :
			if not isinstance(config_error,str):
				raise TypeError("config_error must be set to str value")
			self._config_error = config_error
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
	get Build image error for selected platform
	'''
	@property
	def build_image_error(self) :
		try:
			return self._build_image_error
		except Exception as e :
			raise e
	'''
	set Build image error for selected platform
	'''
	@build_image_error.setter
	def build_image_error(self,build_image_error):
		try :
			if not isinstance(build_image_error,str):
				raise TypeError("build_image_error must be set to str value")
			self._build_image_error = build_image_error
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get System information about FreeBSD or Linux OS kernel
	'''
	@property
	def uname(self) :
		try:
			return self._uname
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
	get Disk space error for /var
	'''
	@property
	def disk_space_error(self) :
		try:
			return self._disk_space_error
		except Exception as e :
			raise e
	'''
	set Disk space error for /var
	'''
	@disk_space_error.setter
	def disk_space_error(self,disk_space_error):
		try :
			if not isinstance(disk_space_error,str):
				raise TypeError("disk_space_error must be set to str value")
			self._disk_space_error = disk_space_error
		except Exception as e :
			raise e


	'''
	get List of unsupported policies.
	'''
	@property
	def policy_check_details(self) :
		try:
			return self._policy_check_details
		except Exception as e :
			raise e
	'''
	set List of unsupported policies.
	'''
	@policy_check_details.setter
	def policy_check_details(self,policy_check_details):
		try :
			if not isinstance(policy_check_details,str):
				raise TypeError("policy_check_details must be set to str value")
			self._policy_check_details = policy_check_details
		except Exception as e :
			raise e


	'''
	get Hardware error like HDD error
	'''
	@property
	def hardware_error(self) :
		try:
			return self._hardware_error
		except Exception as e :
			raise e
	'''
	set Hardware error like HDD error
	'''
	@hardware_error.setter
	def hardware_error(self,hardware_error):
		try :
			if not isinstance(hardware_error,str):
				raise TypeError("hardware_error must be set to str value")
			self._hardware_error = hardware_error
		except Exception as e :
			raise e


	'''
	get User custom info details
	'''
	@property
	def user_custom_info_details(self) :
		try:
			return self._user_custom_info_details
		except Exception as e :
			raise e
	'''
	set User custom info details
	'''
	@user_custom_info_details.setter
	def user_custom_info_details(self,user_custom_info_details):
		try :
			if not isinstance(user_custom_info_details,str):
				raise TypeError("user_custom_info_details must be set to str value")
			self._user_custom_info_details = user_custom_info_details
		except Exception as e :
			raise e


	'''
	get NetScaler HA configuration inconsistency error between primary and secondary server
	'''
	@property
	def primary_config_error(self) :
		try:
			return self._primary_config_error
		except Exception as e :
			raise e
	'''
	set NetScaler HA configuration inconsistency error between primary and secondary server
	'''
	@primary_config_error.setter
	def primary_config_error(self,primary_config_error):
		try :
			if not isinstance(primary_config_error,str):
				raise TypeError("primary_config_error must be set to str value")
			self._primary_config_error = primary_config_error
		except Exception as e :
			raise e


	'''
	get User custom info
	'''
	@property
	def user_custom_info(self) :
		try:
			return self._user_custom_info
		except Exception as e :
			raise e
	'''
	set User custom info
	'''
	@user_custom_info.setter
	def user_custom_info(self,user_custom_info):
		try :
			if not isinstance(user_custom_info,str):
				raise TypeError("user_custom_info must be set to str value")
			self._user_custom_info = user_custom_info
		except Exception as e :
			raise e


	'''
	get NetScaler connectivity error
	'''
	@property
	def connectivity_error(self) :
		try:
			return self._connectivity_error
		except Exception as e :
			raise e
	'''
	set NetScaler connectivity error
	'''
	@connectivity_error.setter
	def connectivity_error(self,connectivity_error):
		try :
			if not isinstance(connectivity_error,str):
				raise TypeError("connectivity_error must be set to str value")
			self._connectivity_error = connectivity_error
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
	set Master State (Primary/Secondary)
	'''
	@ha_master_state.setter
	def ha_master_state(self,ha_master_state):
		try :
			if not isinstance(ha_master_state,str):
				raise TypeError("ha_master_state must be set to str value")
			self._ha_master_state = ha_master_state
		except Exception as e :
			raise e


	'''
	get NetScaler connectivity error details
	'''
	@property
	def connectivity_error_details(self) :
		try:
			return self._connectivity_error_details
		except Exception as e :
			raise e
	'''
	set NetScaler connectivity error details
	'''
	@connectivity_error_details.setter
	def connectivity_error_details(self,connectivity_error_details):
		try :
			if not isinstance(connectivity_error_details,str):
				raise TypeError("connectivity_error_details must be set to str value")
			self._connectivity_error_details = connectivity_error_details
		except Exception as e :
			raise e


	'''
	get Detected unsupported policy
	'''
	@property
	def policy_check(self) :
		try:
			return self._policy_check
		except Exception as e :
			raise e
	'''
	set Detected unsupported policy
	'''
	@policy_check.setter
	def policy_check(self,policy_check):
		try :
			if not isinstance(policy_check,str):
				raise TypeError("policy_check must be set to str value")
			self._policy_check = policy_check
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
	get Hardware error like HDD error details
	'''
	@property
	def hardware_error_details(self) :
		try:
			return self._hardware_error_details
		except Exception as e :
			raise e
	'''
	set Hardware error like HDD error details
	'''
	@hardware_error_details.setter
	def hardware_error_details(self,hardware_error_details):
		try :
			if not isinstance(hardware_error_details,str):
				raise TypeError("hardware_error_details must be set to str value")
			self._hardware_error_details = hardware_error_details
		except Exception as e :
			raise e


	'''
	get Disk space error for /var
	'''
	@property
	def disk_space_error_details(self) :
		try:
			return self._disk_space_error_details
		except Exception as e :
			raise e
	'''
	set Disk space error for /var
	'''
	@disk_space_error_details.setter
	def disk_space_error_details(self,disk_space_error_details):
		try :
			if not isinstance(disk_space_error_details,str):
				raise TypeError("disk_space_error_details must be set to str value")
			self._disk_space_error_details = disk_space_error_details
		except Exception as e :
			raise e


	'''
	get NetScaler HA configuration inconsistency error between primary and secondary server
	'''
	@property
	def secondary_config_error(self) :
		try:
			return self._secondary_config_error
		except Exception as e :
			raise e
	'''
	set NetScaler HA configuration inconsistency error between primary and secondary server
	'''
	@secondary_config_error.setter
	def secondary_config_error(self,secondary_config_error):
		try :
			if not isinstance(secondary_config_error,str):
				raise TypeError("secondary_config_error must be set to str value")
			self._secondary_config_error = secondary_config_error
		except Exception as e :
			raise e


	'''
	get Build images available in /var/nsinstall directory
	'''
	@property
	def image_var_nsinstall(self) :
		try:
			return self._image_var_nsinstall
		except Exception as e :
			raise e
	'''
	set Build images available in /var/nsinstall directory
	'''
	@image_var_nsinstall.setter
	def image_var_nsinstall(self,image_var_nsinstall):
		try :
			if not isinstance(image_var_nsinstall,str):
				raise TypeError("image_var_nsinstall must be set to str value")
			self._image_var_nsinstall = image_var_nsinstall
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
	set Peer IP Address
	'''
	@ha_ip_address.setter
	def ha_ip_address(self,ha_ip_address):
		try :
			if not isinstance(ha_ip_address,str):
				raise TypeError("ha_ip_address must be set to str value")
			self._ha_ip_address = ha_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get pre upgarde .
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_pre_upgrade_obj=ns_pre_upgrade()
				response = ns_pre_upgrade_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete pre upgarde.
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
					ns_pre_upgrade_obj=ns_pre_upgrade()
					return cls.delete_bulk_request(client,resource,ns_pre_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_pre_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_pre_upgrade_obj = ns_pre_upgrade()
			option_ = options()
			option_._filter=filter_
			return ns_pre_upgrade_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_pre_upgrade resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_pre_upgrade_obj = ns_pre_upgrade()
			option_ = options()
			option_._count=True
			response = ns_pre_upgrade_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_pre_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_pre_upgrade_obj = ns_pre_upgrade()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_pre_upgrade_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_pre_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_pre_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_pre_upgrade_responses, response, "ns_pre_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_pre_upgrade_response_array
				i=0
				error = [ns_pre_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_pre_upgrade_response_array
			i=0
			ns_pre_upgrade_objs = [ns_pre_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_pre_upgrade'):
					for props in obj._ns_pre_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(ns_pre_upgrade_response,self.__class__.__name__,props)
						ns_pre_upgrade_objs[i] = result.ns_pre_upgrade
						i=i+1
			return ns_pre_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_pre_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_pre_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.ns_pre_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_pre_upgrade= [ ns_pre_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_pre_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.ns_pre_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_pre_upgrade_response_array = [ ns_pre_upgrade() for _ in range(length)]
