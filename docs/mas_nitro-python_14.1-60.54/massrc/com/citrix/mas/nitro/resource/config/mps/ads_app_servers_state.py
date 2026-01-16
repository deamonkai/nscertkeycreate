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
Configuration for ADS Application Server State resource
'''

class ads_app_servers_state(base_resource):
	_port= ""
	_svc_grp_name= ""
	_server_name= ""
	_ns_ip_address= ""
	_monitor_name= ""
	_monitortotalfailedprobes= ""
	_availability_zone= ""
	_monitor_state= ""
	_server_state= ""
	_monitorcurrentfailedprobes= ""
	_lastresponse= ""
	_poll_time= ""
	_customer_name= ""
	_monitortotalprobes= ""
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
			return "ads_app_servers_state"
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
			return "ads_app_servers_states"
		except Exception as e :
			raise e



	'''
	get Server Port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Server Port
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
	get Service Group Name of the Server
	'''
	@property
	def svc_grp_name(self) :
		try:
			return self._svc_grp_name
		except Exception as e :
			raise e
	'''
	set Service Group Name of the Server
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
	get IP Address of the Server
	'''
	@property
	def server_name(self) :
		try:
			return self._server_name
		except Exception as e :
			raise e
	'''
	set IP Address of the Server
	'''
	@server_name.setter
	def server_name(self,server_name):
		try :
			if not isinstance(server_name,str):
				raise TypeError("server_name must be set to str value")
			self._server_name = server_name
		except Exception as e :
			raise e


	'''
	get NetScaler Console Name
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler Console Name
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
	get Monitor Name
	'''
	@property
	def monitor_name(self) :
		try:
			return self._monitor_name
		except Exception as e :
			raise e
	'''
	set Monitor Name
	'''
	@monitor_name.setter
	def monitor_name(self,monitor_name):
		try :
			if not isinstance(monitor_name,str):
				raise TypeError("monitor_name must be set to str value")
			self._monitor_name = monitor_name
		except Exception as e :
			raise e


	'''
	get Total number of failed probes by Monitor
	'''
	@property
	def monitortotalfailedprobes(self) :
		try:
			return self._monitortotalfailedprobes
		except Exception as e :
			raise e
	'''
	set Total number of failed probes by Monitor
	'''
	@monitortotalfailedprobes.setter
	def monitortotalfailedprobes(self,monitortotalfailedprobes):
		try :
			if not isinstance(monitortotalfailedprobes,int):
				raise TypeError("monitortotalfailedprobes must be set to int value")
			self._monitortotalfailedprobes = monitortotalfailedprobes
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
	get Current state of the Monitor
	'''
	@property
	def monitor_state(self) :
		try:
			return self._monitor_state
		except Exception as e :
			raise e
	'''
	set Current state of the Monitor
	'''
	@monitor_state.setter
	def monitor_state(self,monitor_state):
		try :
			if not isinstance(monitor_state,str):
				raise TypeError("monitor_state must be set to str value")
			self._monitor_state = monitor_state
		except Exception as e :
			raise e


	'''
	get State of server
	'''
	@property
	def server_state(self) :
		try:
			return self._server_state
		except Exception as e :
			raise e
	'''
	set State of server
	'''
	@server_state.setter
	def server_state(self,server_state):
		try :
			if not isinstance(server_state,str):
				raise TypeError("server_state must be set to str value")
			self._server_state = server_state
		except Exception as e :
			raise e


	'''
	get Current number of failed probes by Monitor
	'''
	@property
	def monitorcurrentfailedprobes(self) :
		try:
			return self._monitorcurrentfailedprobes
		except Exception as e :
			raise e
	'''
	set Current number of failed probes by Monitor
	'''
	@monitorcurrentfailedprobes.setter
	def monitorcurrentfailedprobes(self,monitorcurrentfailedprobes):
		try :
			if not isinstance(monitorcurrentfailedprobes,int):
				raise TypeError("monitorcurrentfailedprobes must be set to int value")
			self._monitorcurrentfailedprobes = monitorcurrentfailedprobes
		except Exception as e :
			raise e


	'''
	get Last Response from the server
	'''
	@property
	def lastresponse(self) :
		try:
			return self._lastresponse
		except Exception as e :
			raise e
	'''
	set Last Response from the server
	'''
	@lastresponse.setter
	def lastresponse(self,lastresponse):
		try :
			if not isinstance(lastresponse,str):
				raise TypeError("lastresponse must be set to str value")
			self._lastresponse = lastresponse
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e
	'''
	set Last Polling Time
	'''
	@poll_time.setter
	def poll_time(self,poll_time):
		try :
			if not isinstance(poll_time,int):
				raise TypeError("poll_time must be set to int value")
			self._poll_time = poll_time
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
	get Total number of probes by Monitor
	'''
	@property
	def monitortotalprobes(self) :
		try:
			return self._monitortotalprobes
		except Exception as e :
			raise e
	'''
	set Total number of probes by Monitor
	'''
	@monitortotalprobes.setter
	def monitortotalprobes(self,monitortotalprobes):
		try :
			if not isinstance(monitortotalprobes,int):
				raise TypeError("monitortotalprobes must be set to int value")
			self._monitortotalprobes = monitortotalprobes
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
				ads_app_servers_state_obj=ads_app_servers_state()
				response = ads_app_servers_state_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ads_app_servers_state resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ads_app_servers_state_obj = ads_app_servers_state()
			option_ = options()
			option_._filter=filter_
			return ads_app_servers_state_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ads_app_servers_state resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ads_app_servers_state_obj = ads_app_servers_state()
			option_ = options()
			option_._count=True
			response = ads_app_servers_state_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ads_app_servers_state resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ads_app_servers_state_obj = ads_app_servers_state()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ads_app_servers_state_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ads_app_servers_state_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ads_app_servers_state
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ads_app_servers_state_responses, response, "ads_app_servers_state_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ads_app_servers_state_response_array
				i=0
				error = [ads_app_servers_state() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ads_app_servers_state_response_array
			i=0
			ads_app_servers_state_objs = [ads_app_servers_state() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ads_app_servers_state'):
					for props in obj._ads_app_servers_state:
						result = service.payload_formatter.string_to_bulk_resource(ads_app_servers_state_response,self.__class__.__name__,props)
						ads_app_servers_state_objs[i] = result.ads_app_servers_state
						i=i+1
			return ads_app_servers_state_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ads_app_servers_state,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ads_app_servers_state_response(base_response):
	def __init__(self,length=1) :
		self.ads_app_servers_state= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ads_app_servers_state= [ ads_app_servers_state() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ads_app_servers_state_responses(base_response):
	def __init__(self,length=1) :
		self.ads_app_servers_state_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ads_app_servers_state_response_array = [ ads_app_servers_state() for _ in range(length)]
