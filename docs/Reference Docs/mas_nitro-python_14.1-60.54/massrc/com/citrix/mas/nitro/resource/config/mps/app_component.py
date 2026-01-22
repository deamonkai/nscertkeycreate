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
Configuration for This includes the application components (virtual servers) resource
'''

class app_component(base_resource):
	_configuration_path= ""
	_display_name= ""
	_type= ""
	_transaction_log_effective= ""
	_name= ""
	_hostname= ""
	_metrics_option= ""
	_client_header= ""
	_vsvr_type= ""
	_httpxforwardedfor= ""
	_vsvr_ip_address= ""
	_id= ""
	_metrics_enabled= ""
	_ns_ip_address= ""
	_export_option= ""
	_state= ""
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
			return "app_component"
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
			return "app_components"
		except Exception as e :
			raise e



	'''
	get Config Path of HA Proxies on this HAPRoxy Host.
	'''
	@property
	def configuration_path(self) :
		try:
			return self._configuration_path
		except Exception as e :
			raise e


	'''
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get Application type ( CS/LB/GSLB etc.)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Application type ( CS/LB/GSLB etc.)
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
	get DETAIL Transaction - enabled, disabled.
	'''
	@property
	def transaction_log_effective(self) :
		try:
			return self._transaction_log_effective
		except Exception as e :
			raise e
	'''
	set DETAIL Transaction - enabled, disabled.
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
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get Hostname of NetScaler on which vserver created.
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of NetScaler on which vserver created.
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
	get Metrics Option
	'''
	@property
	def metrics_option(self) :
		try:
			return self._metrics_option
		except Exception as e :
			raise e
	'''
	set Metrics Option
	'''
	@metrics_option.setter
	def metrics_option(self,metrics_option):
		try :
			if not isinstance(metrics_option,str):
				raise TypeError("metrics_option must be set to str value")
			self._metrics_option = metrics_option
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
	get Vserver type Eg. HTTP
	'''
	@property
	def vsvr_type(self) :
		try:
			return self._vsvr_type
		except Exception as e :
			raise e
	'''
	set Vserver type Eg. HTTP
	'''
	@vsvr_type.setter
	def vsvr_type(self,vsvr_type):
		try :
			if not isinstance(vsvr_type,str):
				raise TypeError("vsvr_type must be set to str value")
			self._vsvr_type = vsvr_type
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
	get ID
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID
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
	get Metrics Enabled status
	'''
	@property
	def metrics_enabled(self) :
		try:
			return self._metrics_enabled
		except Exception as e :
			raise e
	'''
	set Metrics Enabled status
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
	get Device IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
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
	get Export Options - webinsight, securityinsight.
	'''
	@property
	def export_option(self) :
		try:
			return self._export_option
		except Exception as e :
			raise e
	'''
	set Export Options - webinsight, securityinsight.
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
	get state
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set state
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_component_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_component
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_component_responses, response, "app_component_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_component_response_array
				i=0
				error = [app_component() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_component_response_array
			i=0
			app_component_objs = [app_component() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_component'):
					for props in obj._app_component:
						result = service.payload_formatter.string_to_bulk_resource(app_component_response,self.__class__.__name__,props)
						app_component_objs[i] = result.app_component
						i=i+1
			return app_component_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_component,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_component_response(base_response):
	def __init__(self,length=1) :
		self.app_component= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_component= [ app_component() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_component_responses(base_response):
	def __init__(self,length=1) :
		self.app_component_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_component_response_array = [ app_component() for _ in range(length)]
