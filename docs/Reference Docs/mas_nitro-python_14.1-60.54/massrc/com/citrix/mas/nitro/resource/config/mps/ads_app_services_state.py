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
Configuration for ADS Application Services State resource
'''

class ads_app_services_state(base_resource):
	_service_name= ""
	_availability_zone= ""
	_app_server_type= ""
	_customer_name= ""
	_service_group_name= ""
	_svc_port= ""
	_parent_app_name= ""
	_svc_protocol= ""
	_service_state= ""
	_parent_app_id= ""
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
			return "ads_app_services_state"
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
			return "ads_app_services_states"
		except Exception as e :
			raise e



	'''
	get Name of Service under the ADS Application
	'''
	@property
	def service_name(self) :
		try:
			return self._service_name
		except Exception as e :
			raise e
	'''
	set Name of Service under the ADS Application
	'''
	@service_name.setter
	def service_name(self,service_name):
		try :
			if not isinstance(service_name,str):
				raise TypeError("service_name must be set to str value")
			self._service_name = service_name
		except Exception as e :
			raise e


	'''
	get Availability Zone
	'''
	@property
	def availability_zone(self) :
		try:
			return self._availability_zone
		except Exception as e :
			raise e
	'''
	set Availability Zone
	'''
	@availability_zone.setter
	def availability_zone(self,availability_zone):
		try :
			if not isinstance(availability_zone,str):
				raise TypeError("availability_zone must be set to str value")
			self._availability_zone = availability_zone
		except Exception as e :
			raise e


	'''
	get App Server Type
	'''
	@property
	def app_server_type(self) :
		try:
			return self._app_server_type
		except Exception as e :
			raise e
	'''
	set App Server Type
	'''
	@app_server_type.setter
	def app_server_type(self,app_server_type):
		try :
			if not isinstance(app_server_type,str):
				raise TypeError("app_server_type must be set to str value")
			self._app_server_type = app_server_type
		except Exception as e :
			raise e


	'''
	get Customer name
	'''
	@property
	def customer_name(self) :
		try:
			return self._customer_name
		except Exception as e :
			raise e
	'''
	set Customer name
	'''
	@customer_name.setter
	def customer_name(self,customer_name):
		try :
			if not isinstance(customer_name,str):
				raise TypeError("customer_name must be set to str value")
			self._customer_name = customer_name
		except Exception as e :
			raise e


	'''
	get Service Group Name in NetScaler Console format
	'''
	@property
	def service_group_name(self) :
		try:
			return self._service_group_name
		except Exception as e :
			raise e
	'''
	set Service Group Name in NetScaler Console format
	'''
	@service_group_name.setter
	def service_group_name(self,service_group_name):
		try :
			if not isinstance(service_group_name,str):
				raise TypeError("service_group_name must be set to str value")
			self._service_group_name = service_group_name
		except Exception as e :
			raise e


	'''
	get Service Port
	'''
	@property
	def svc_port(self) :
		try:
			return self._svc_port
		except Exception as e :
			raise e
	'''
	set Service Port
	'''
	@svc_port.setter
	def svc_port(self,svc_port):
		try :
			if not isinstance(svc_port,int):
				raise TypeError("svc_port must be set to int value")
			self._svc_port = svc_port
		except Exception as e :
			raise e


	'''
	get Name of Application that the Service is bound with
	'''
	@property
	def parent_app_name(self) :
		try:
			return self._parent_app_name
		except Exception as e :
			raise e
	'''
	set Name of Application that the Service is bound with
	'''
	@parent_app_name.setter
	def parent_app_name(self,parent_app_name):
		try :
			if not isinstance(parent_app_name,str):
				raise TypeError("parent_app_name must be set to str value")
			self._parent_app_name = parent_app_name
		except Exception as e :
			raise e


	'''
	get Service Protocol (HTTP|FTP)
	'''
	@property
	def svc_protocol(self) :
		try:
			return self._svc_protocol
		except Exception as e :
			raise e
	'''
	set Service Protocol (HTTP|FTP)
	'''
	@svc_protocol.setter
	def svc_protocol(self,svc_protocol):
		try :
			if not isinstance(svc_protocol,str):
				raise TypeError("svc_protocol must be set to str value")
			self._svc_protocol = svc_protocol
		except Exception as e :
			raise e


	'''
	get State of the overall service
	'''
	@property
	def service_state(self) :
		try:
			return self._service_state
		except Exception as e :
			raise e
	'''
	set State of the overall service
	'''
	@service_state.setter
	def service_state(self,service_state):
		try :
			if not isinstance(service_state,str):
				raise TypeError("service_state must be set to str value")
			self._service_state = service_state
		except Exception as e :
			raise e


	'''
	get ID of Application that the Service is bound with
	'''
	@property
	def parent_app_id(self) :
		try:
			return self._parent_app_id
		except Exception as e :
			raise e
	'''
	set ID of Application that the Service is bound with
	'''
	@parent_app_id.setter
	def parent_app_id(self,parent_app_id):
		try :
			if not isinstance(parent_app_id,str):
				raise TypeError("parent_app_id must be set to str value")
			self._parent_app_id = parent_app_id
		except Exception as e :
			raise e

	'''
	Use this operation to get Service Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ads_app_services_state_obj=ads_app_services_state()
				response = ads_app_services_state_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ads_app_services_state resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ads_app_services_state_obj = ads_app_services_state()
			option_ = options()
			option_._filter=filter_
			return ads_app_services_state_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ads_app_services_state resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ads_app_services_state_obj = ads_app_services_state()
			option_ = options()
			option_._count=True
			response = ads_app_services_state_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ads_app_services_state resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ads_app_services_state_obj = ads_app_services_state()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ads_app_services_state_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ads_app_services_state_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ads_app_services_state
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ads_app_services_state_responses, response, "ads_app_services_state_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ads_app_services_state_response_array
				i=0
				error = [ads_app_services_state() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ads_app_services_state_response_array
			i=0
			ads_app_services_state_objs = [ads_app_services_state() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ads_app_services_state'):
					for props in obj._ads_app_services_state:
						result = service.payload_formatter.string_to_bulk_resource(ads_app_services_state_response,self.__class__.__name__,props)
						ads_app_services_state_objs[i] = result.ads_app_services_state
						i=i+1
			return ads_app_services_state_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ads_app_services_state,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ads_app_services_state_response(base_response):
	def __init__(self,length=1) :
		self.ads_app_services_state= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ads_app_services_state= [ ads_app_services_state() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ads_app_services_state_responses(base_response):
	def __init__(self,length=1) :
		self.ads_app_services_state_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ads_app_services_state_response_array = [ ads_app_services_state() for _ in range(length)]
