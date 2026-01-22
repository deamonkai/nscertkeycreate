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
Configuration for AppFlow Collector for NetScaler resource
'''

class ns_ns_appflowcollector(base_resource):
	_transport= ""
	_port= ""
	_partition_name= ""
	_display_name= ""
	_id= ""
	_poll_time= ""
	_name= ""
	_state= ""
	_ipaddress= ""
	_ns_ip_address= ""
	_netprofile= ""
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
			return "ns_ns_appflowcollector"
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
			return "ns_ns_appflowcollectors"
		except Exception as e :
			raise e



	'''
	get Transport type like logstream, IPfix
	'''
	@property
	def transport(self) :
		try:
			return self._transport
		except Exception as e :
			raise e
	'''
	set Transport type like logstream, IPfix
	'''
	@transport.setter
	def transport(self,transport):
		try :
			if not isinstance(transport,str):
				raise TypeError("transport must be set to str value")
			self._transport = transport
		except Exception as e :
			raise e


	'''
	get port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set port
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
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
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
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
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
	get state of the collector
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set state of the collector
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
	get ipaddress
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set ipaddress
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress):
		try :
			if not isinstance(ipaddress,str):
				raise TypeError("ipaddress must be set to str value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
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
	get Net Profile
	'''
	@property
	def netprofile(self) :
		try:
			return self._netprofile
		except Exception as e :
			raise e

	'''
	Use this operation to get appflow collector details from NetScaler Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_ns_appflowcollector_obj=ns_ns_appflowcollector()
				response = ns_ns_appflowcollector_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ns_appflowcollector resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ns_appflowcollector_obj = ns_ns_appflowcollector()
			option_ = options()
			option_._filter=filter_
			return ns_ns_appflowcollector_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ns_appflowcollector resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ns_appflowcollector_obj = ns_ns_appflowcollector()
			option_ = options()
			option_._count=True
			response = ns_ns_appflowcollector_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ns_appflowcollector resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ns_appflowcollector_obj = ns_ns_appflowcollector()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ns_appflowcollector_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ns_appflowcollector_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ns_appflowcollector
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ns_appflowcollector_responses, response, "ns_ns_appflowcollector_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ns_appflowcollector_response_array
				i=0
				error = [ns_ns_appflowcollector() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ns_appflowcollector_response_array
			i=0
			ns_ns_appflowcollector_objs = [ns_ns_appflowcollector() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ns_appflowcollector'):
					for props in obj._ns_ns_appflowcollector:
						result = service.payload_formatter.string_to_bulk_resource(ns_ns_appflowcollector_response,self.__class__.__name__,props)
						ns_ns_appflowcollector_objs[i] = result.ns_ns_appflowcollector
						i=i+1
			return ns_ns_appflowcollector_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ns_appflowcollector,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ns_appflowcollector_response(base_response):
	def __init__(self,length=1) :
		self.ns_ns_appflowcollector= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ns_appflowcollector= [ ns_ns_appflowcollector() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ns_appflowcollector_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ns_appflowcollector_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ns_appflowcollector_response_array = [ ns_ns_appflowcollector() for _ in range(length)]
