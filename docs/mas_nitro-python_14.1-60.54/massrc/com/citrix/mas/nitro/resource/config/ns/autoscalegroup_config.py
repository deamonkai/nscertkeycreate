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
Configuration for Auto-Scale Group configuration/stylebook parameters resource
'''

class autoscalegroup_config(base_resource):
	_backend_port= ""
	_domain_name= ""
	_access_type= ""
	_redirect_port= ""
	_generated_domain_name= ""
	_is_https_redirect= ""
	_id= ""
	_backend_probe_port= ""
	_stylebook_name= ""
	_virtual_port= ""
	_ipset_name= ""
	_autoscalegroup_id= ""
	_app_name= ""
	_zone_name= ""
	_url= ""
	_frontend_ip= ""
	_activity_id= ""
	_is_endpoint= ""
	_version= ""
	_frontend_name= ""
	_probe_port= ""
	_service_type= ""
	_ip_address= ""
	_configpack_id= ""
	_backend_http_redirect_port= ""
	_probe_protocol= ""
	_last_modified_time= ""
	_stylebook_namespace= ""
	_autoscalegroup_name= ""
	_force_delete= ""
	_probe_enabled= ""
	_stylebook_params= ""
	_is_migration= ""
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
			return "autoscalegroup_config"
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
			return "autoscalegroup_configs"
		except Exception as e :
			raise e



	'''
	get Backend Port
	'''
	@property
	def backend_port(self) :
		try:
			return self._backend_port
		except Exception as e :
			raise e
	'''
	set Backend Port
	'''
	@backend_port.setter
	def backend_port(self,backend_port):
		try :
			if not isinstance(backend_port,int):
				raise TypeError("backend_port must be set to int value")
			self._backend_port = backend_port
		except Exception as e :
			raise e


	'''
	get Name of domain
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set Name of domain
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
		except Exception as e :
			raise e


	'''
	get Access Type (0.External(public)/1.Internal(private)/2.None)
	'''
	@property
	def access_type(self) :
		try:
			return self._access_type
		except Exception as e :
			raise e
	'''
	set Access Type (0.External(public)/1.Internal(private)/2.None)
	'''
	@access_type.setter
	def access_type(self,access_type):
		try :
			if not isinstance(access_type,int):
				raise TypeError("access_type must be set to int value")
			self._access_type = access_type
		except Exception as e :
			raise e


	'''
	get redirect_port
	'''
	@property
	def redirect_port(self) :
		try:
			return self._redirect_port
		except Exception as e :
			raise e
	'''
	set redirect_port
	'''
	@redirect_port.setter
	def redirect_port(self,redirect_port):
		try :
			if not isinstance(redirect_port,int):
				raise TypeError("redirect_port must be set to int value")
			self._redirect_port = redirect_port
		except Exception as e :
			raise e


	'''
	get Name of generated domain
	'''
	@property
	def generated_domain_name(self) :
		try:
			return self._generated_domain_name
		except Exception as e :
			raise e
	'''
	set Name of generated domain
	'''
	@generated_domain_name.setter
	def generated_domain_name(self,generated_domain_name):
		try :
			if not isinstance(generated_domain_name,str):
				raise TypeError("generated_domain_name must be set to str value")
			self._generated_domain_name = generated_domain_name
		except Exception as e :
			raise e


	'''
	get Enabled for https redirect
	'''
	@property
	def is_https_redirect(self) :
		try:
			return self._is_https_redirect
		except Exception as e :
			raise e
	'''
	set Enabled for https redirect
	'''
	@is_https_redirect.setter
	def is_https_redirect(self,is_https_redirect):
		try :
			if not isinstance(is_https_redirect,bool):
				raise TypeError("is_https_redirect must be set to bool value")
			self._is_https_redirect = is_https_redirect
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the auto-scale group config
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the auto-scale group config
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
	get Backend Probe Port
	'''
	@property
	def backend_probe_port(self) :
		try:
			return self._backend_probe_port
		except Exception as e :
			raise e
	'''
	set Backend Probe Port
	'''
	@backend_probe_port.setter
	def backend_probe_port(self,backend_probe_port):
		try :
			if not isinstance(backend_probe_port,int):
				raise TypeError("backend_probe_port must be set to int value")
			self._backend_probe_port = backend_probe_port
		except Exception as e :
			raise e


	'''
	get Stylebook Name
	'''
	@property
	def stylebook_name(self) :
		try:
			return self._stylebook_name
		except Exception as e :
			raise e
	'''
	set Stylebook Name
	'''
	@stylebook_name.setter
	def stylebook_name(self,stylebook_name):
		try :
			if not isinstance(stylebook_name,str):
				raise TypeError("stylebook_name must be set to str value")
			self._stylebook_name = stylebook_name
		except Exception as e :
			raise e


	'''
	get Virtual Port
	'''
	@property
	def virtual_port(self) :
		try:
			return self._virtual_port
		except Exception as e :
			raise e
	'''
	set Virtual Port
	'''
	@virtual_port.setter
	def virtual_port(self,virtual_port):
		try :
			if not isinstance(virtual_port,int):
				raise TypeError("virtual_port must be set to int value")
			self._virtual_port = virtual_port
		except Exception as e :
			raise e


	'''
	get Name of IPSet
	'''
	@property
	def ipset_name(self) :
		try:
			return self._ipset_name
		except Exception as e :
			raise e
	'''
	set Name of IPSet
	'''
	@ipset_name.setter
	def ipset_name(self,ipset_name):
		try :
			if not isinstance(ipset_name,str):
				raise TypeError("ipset_name must be set to str value")
			self._ipset_name = ipset_name
		except Exception as e :
			raise e


	'''
	get ID of autoscalegroup
	'''
	@property
	def autoscalegroup_id(self) :
		try:
			return self._autoscalegroup_id
		except Exception as e :
			raise e
	'''
	set ID of autoscalegroup
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
	get Name of application
	'''
	@property
	def app_name(self) :
		try:
			return self._app_name
		except Exception as e :
			raise e
	'''
	set Name of application
	'''
	@app_name.setter
	def app_name(self,app_name):
		try :
			if not isinstance(app_name,str):
				raise TypeError("app_name must be set to str value")
			self._app_name = app_name
		except Exception as e :
			raise e


	'''
	get Name of zone
	'''
	@property
	def zone_name(self) :
		try:
			return self._zone_name
		except Exception as e :
			raise e
	'''
	set Name of zone
	'''
	@zone_name.setter
	def zone_name(self,zone_name):
		try :
			if not isinstance(zone_name,str):
				raise TypeError("zone_name must be set to str value")
			self._zone_name = zone_name
		except Exception as e :
			raise e


	'''
	get Stylebook URL which has namespace, version and stylebook_name
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set Stylebook URL which has namespace, version and stylebook_name
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
	get The frontend IP of Azure ALB applications
	'''
	@property
	def frontend_ip(self) :
		try:
			return self._frontend_ip
		except Exception as e :
			raise e
	'''
	set The frontend IP of Azure ALB applications
	'''
	@frontend_ip.setter
	def frontend_ip(self,frontend_ip):
		try :
			if not isinstance(frontend_ip,str):
				raise TypeError("frontend_ip must be set to str value")
			self._frontend_ip = frontend_ip
		except Exception as e :
			raise e


	'''
	get Most recent activity_id of this autoscalegroup config
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Most recent activity_id of this autoscalegroup config
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
		except Exception as e :
			raise e


	'''
	get Enabled for End Point Application
	'''
	@property
	def is_endpoint(self) :
		try:
			return self._is_endpoint
		except Exception as e :
			raise e
	'''
	set Enabled for End Point Application
	'''
	@is_endpoint.setter
	def is_endpoint(self,is_endpoint):
		try :
			if not isinstance(is_endpoint,bool):
				raise TypeError("is_endpoint must be set to bool value")
			self._is_endpoint = is_endpoint
		except Exception as e :
			raise e


	'''
	get Stylebook version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Stylebook version
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
	get The frontend name of application
	'''
	@property
	def frontend_name(self) :
		try:
			return self._frontend_name
		except Exception as e :
			raise e
	'''
	set The frontend name of application
	'''
	@frontend_name.setter
	def frontend_name(self,frontend_name):
		try :
			if not isinstance(frontend_name,str):
				raise TypeError("frontend_name must be set to str value")
			self._frontend_name = frontend_name
		except Exception as e :
			raise e


	'''
	get Probe Port
	'''
	@property
	def probe_port(self) :
		try:
			return self._probe_port
		except Exception as e :
			raise e
	'''
	set Probe Port
	'''
	@probe_port.setter
	def probe_port(self,probe_port):
		try :
			if not isinstance(probe_port,int):
				raise TypeError("probe_port must be set to int value")
			self._probe_port = probe_port
		except Exception as e :
			raise e


	'''
	get Service Type
	'''
	@property
	def service_type(self) :
		try:
			return self._service_type
		except Exception as e :
			raise e
	'''
	set Service Type
	'''
	@service_type.setter
	def service_type(self,service_type):
		try :
			if not isinstance(service_type,str):
				raise TypeError("service_type must be set to str value")
			self._service_type = service_type
		except Exception as e :
			raise e


	'''
	get IP of VIP
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP of VIP
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
	get ID of deployed configpack on autoscalegroup
	'''
	@property
	def configpack_id(self) :
		try:
			return self._configpack_id
		except Exception as e :
			raise e
	'''
	set ID of deployed configpack on autoscalegroup
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
	get Backend HTTP Redirect Port
	'''
	@property
	def backend_http_redirect_port(self) :
		try:
			return self._backend_http_redirect_port
		except Exception as e :
			raise e
	'''
	set Backend HTTP Redirect Port
	'''
	@backend_http_redirect_port.setter
	def backend_http_redirect_port(self,backend_http_redirect_port):
		try :
			if not isinstance(backend_http_redirect_port,int):
				raise TypeError("backend_http_redirect_port must be set to int value")
			self._backend_http_redirect_port = backend_http_redirect_port
		except Exception as e :
			raise e


	'''
	get Probe Protocol
	'''
	@property
	def probe_protocol(self) :
		try:
			return self._probe_protocol
		except Exception as e :
			raise e
	'''
	set Probe Protocol
	'''
	@probe_protocol.setter
	def probe_protocol(self,probe_protocol):
		try :
			if not isinstance(probe_protocol,str):
				raise TypeError("probe_protocol must be set to str value")
			self._probe_protocol = probe_protocol
		except Exception as e :
			raise e


	'''
	get last modified time in seconds
	'''
	@property
	def last_modified_time(self) :
		try:
			return self._last_modified_time
		except Exception as e :
			raise e
	'''
	set last modified time in seconds
	'''
	@last_modified_time.setter
	def last_modified_time(self,last_modified_time):
		try :
			if not isinstance(last_modified_time,float):
				raise TypeError("last_modified_time must be set to float value")
			self._last_modified_time = last_modified_time
		except Exception as e :
			raise e

	'''
	Stylebook Namespace
	'''
	@property
	def stylebook_namespace(self):
		try:
			return self._stylebook_namespace
		except Exception as e :
			raise e
	'''
	Stylebook Namespace
	'''
	@stylebook_namespace.setter
	def stylebook_namespace(self,stylebook_namespace):
		try :
			if not isinstance(stylebook_namespace,str):
				raise TypeError("stylebook_namespace must be set to str value")
			self._stylebook_namespace = stylebook_namespace
		except Exception as e :
			raise e

	'''
	Name of autoscalegroup
	'''
	@property
	def autoscalegroup_name(self):
		try:
			return self._autoscalegroup_name
		except Exception as e :
			raise e
	'''
	Name of autoscalegroup
	'''
	@autoscalegroup_name.setter
	def autoscalegroup_name(self,autoscalegroup_name):
		try :
			if not isinstance(autoscalegroup_name,str):
				raise TypeError("autoscalegroup_name must be set to str value")
			self._autoscalegroup_name = autoscalegroup_name
		except Exception as e :
			raise e

	'''
	Option to delete the configpack forcefully
	'''
	@property
	def force_delete(self):
		try:
			return self._force_delete
		except Exception as e :
			raise e
	'''
	Option to delete the configpack forcefully
	'''
	@force_delete.setter
	def force_delete(self,force_delete):
		try :
			if not isinstance(force_delete,bool):
				raise TypeError("force_delete must be set to bool value")
			self._force_delete = force_delete
		except Exception as e :
			raise e

	'''
	This flag is set to true if the NetScaler version (13.0.76.0 and above) has support for probe port and protocol
	'''
	@property
	def probe_enabled(self):
		try:
			return self._probe_enabled
		except Exception as e :
			raise e
	'''
	This flag is set to true if the NetScaler version (13.0.76.0 and above) has support for probe port and protocol
	'''
	@probe_enabled.setter
	def probe_enabled(self,probe_enabled):
		try :
			if not isinstance(probe_enabled,bool):
				raise TypeError("probe_enabled must be set to bool value")
			self._probe_enabled = probe_enabled
		except Exception as e :
			raise e

	'''
	Inlcudes all the Stylebook parameters
	'''
	@property
	def stylebook_params(self):
		try:
			return self._stylebook_params
		except Exception as e :
			raise e
	'''
	Inlcudes all the Stylebook parameters
	'''
	@stylebook_params.setter
	def stylebook_params(self,stylebook_params):
		try :
			if not isinstance(stylebook_params,str):
				raise TypeError("stylebook_params must be set to str value")
			self._stylebook_params = stylebook_params
		except Exception as e :
			raise e

	'''
	Enabled for configpack migration
	'''
	@property
	def is_migration(self):
		try:
			return self._is_migration
		except Exception as e :
			raise e
	'''
	Enabled for configpack migration
	'''
	@is_migration.setter
	def is_migration(self,is_migration):
		try :
			if not isinstance(is_migration,bool):
				raise TypeError("is_migration must be set to bool value")
			self._is_migration = is_migration
		except Exception as e :
			raise e

	'''
	Use this operation to delete auto-scale group configurations.
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
					autoscalegroup_config_obj=autoscalegroup_config()
					return cls.delete_bulk_request(client,resource,autoscalegroup_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get auto-scale group configurations.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscalegroup_config_obj=autoscalegroup_config()
				response = autoscalegroup_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify auto-scale group configurations.
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
				autoscalegroup_config_obj=autoscalegroup_config()
				return cls.update_bulk_request(client,resource,autoscalegroup_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add auto-scale group configurations.
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
				autoscalegroup_config_obj= autoscalegroup_config()
				return cls.perform_operation_bulk_request(service,resource,autoscalegroup_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscalegroup_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscalegroup_config_obj = autoscalegroup_config()
			option_ = options()
			option_._filter=filter_
			return autoscalegroup_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscalegroup_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscalegroup_config_obj = autoscalegroup_config()
			option_ = options()
			option_._count=True
			response = autoscalegroup_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscalegroup_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscalegroup_config_obj = autoscalegroup_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscalegroup_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscalegroup_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscalegroup_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscalegroup_config_responses, response, "autoscalegroup_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscalegroup_config_response_array
				i=0
				error = [autoscalegroup_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscalegroup_config_response_array
			i=0
			autoscalegroup_config_objs = [autoscalegroup_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscalegroup_config'):
					for props in obj._autoscalegroup_config:
						result = service.payload_formatter.string_to_bulk_resource(autoscalegroup_config_response,self.__class__.__name__,props)
						autoscalegroup_config_objs[i] = result.autoscalegroup_config
						i=i+1
			return autoscalegroup_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscalegroup_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscalegroup_config_response(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscalegroup_config= [ autoscalegroup_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscalegroup_config_responses(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscalegroup_config_response_array = [ autoscalegroup_config() for _ in range(length)]
