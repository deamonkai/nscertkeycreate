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
Configuration for NetScaler Events resource
'''

class ns_event_message(base_resource):
	_counter_threshold_value= ""
	_history= ""
	_user_name= ""
	_entity= ""
	_operation_type= ""
	_source= ""
	_failureobj= ""
	_device_family= ""
	_timestamp= ""
	_cmd_auth_status= ""
	_category= ""
	_device_entity_type= ""
	_source_event_id= ""
	_cmd_exec_status= ""
	_id= ""
	_device_entity_name= ""
	_total_count= ""
	_device_type= ""
	_message= ""
	_counter_actual_value= ""
	_severity= ""
	_config_cmd= ""
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
			return "ns_event_message"
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
			return "ns_event_messages"
		except Exception as e :
			raise e



	'''
	get device threshold value for any threadhold violated traps
	'''
	@property
	def counter_threshold_value(self) :
		try:
			return self._counter_threshold_value
		except Exception as e :
			raise e


	'''
	get History of the Event with same entity
	'''
	@property
	def history(self) :
		try:
			return self._history
		except Exception as e :
			raise e


	'''
	get Username
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e


	'''
	get Entity of Event
	'''
	@property
	def entity(self) :
		try:
			return self._entity
		except Exception as e :
			raise e


	'''
	get Operation Type
	'''
	@property
	def operation_type(self) :
		try:
			return self._operation_type
		except Exception as e :
			raise e


	'''
	get Source
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e


	'''
	get Failure objects are entity instances or counters for which an event has been generated, for example entity name
	'''
	@property
	def failureobj(self) :
		try:
			return self._failureobj
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
	get Time when the event occured
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Command Authorization Status if the event is generated for any config change or config save in device
	'''
	@property
	def cmd_auth_status(self) :
		try:
			return self._cmd_auth_status
		except Exception as e :
			raise e


	'''
	get Category of Event
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e


	'''
	get Device Entity Type
	'''
	@property
	def device_entity_type(self) :
		try:
			return self._device_entity_type
		except Exception as e :
			raise e


	'''
	get Internal Event ID used in the source device.
	'''
	@property
	def source_event_id(self) :
		try:
			return self._source_event_id
		except Exception as e :
			raise e


	'''
	get Command Execution Status if the event is generated for any config change or config save in device
	'''
	@property
	def cmd_exec_status(self) :
		try:
			return self._cmd_exec_status
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the events
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the events
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
	get Device Entity Name
	'''
	@property
	def device_entity_name(self) :
		try:
			return self._device_entity_name
		except Exception as e :
			raise e


	'''
	get total_count
	'''
	@property
	def total_count(self) :
		try:
			return self._total_count
		except Exception as e :
			raise e


	'''
	get Device Type
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e


	'''
	get Event Message - All the other properties recevied in event trap which do not specific fields in this resource(In key : value pair)
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e


	'''
	get device actual value for any threadhold violated traps
	'''
	@property
	def counter_actual_value(self) :
		try:
			return self._counter_actual_value
		except Exception as e :
			raise e


	'''
	get Severity of Event
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e


	'''
	get Config Command if the event is generated for any config change in device
	'''
	@property
	def config_cmd(self) :
		try:
			return self._config_cmd
		except Exception as e :
			raise e

	'''
	Use this operation to get events.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_event_message_obj=ns_event_message()
				response = ns_event_message_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_event_message resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_event_message_obj = ns_event_message()
			option_ = options()
			option_._filter=filter_
			return ns_event_message_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_event_message resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_event_message_obj = ns_event_message()
			option_ = options()
			option_._count=True
			response = ns_event_message_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_event_message resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_event_message_obj = ns_event_message()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_event_message_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_event_message_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_event_message
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_event_message_responses, response, "ns_event_message_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_event_message_response_array
				i=0
				error = [ns_event_message() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_event_message_response_array
			i=0
			ns_event_message_objs = [ns_event_message() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_event_message'):
					for props in obj._ns_event_message:
						result = service.payload_formatter.string_to_bulk_resource(ns_event_message_response,self.__class__.__name__,props)
						ns_event_message_objs[i] = result.ns_event_message
						i=i+1
			return ns_event_message_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_event_message,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_event_message_response(base_response):
	def __init__(self,length=1) :
		self.ns_event_message= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_event_message= [ ns_event_message() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_event_message_responses(base_response):
	def __init__(self,length=1) :
		self.ns_event_message_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_event_message_response_array = [ ns_event_message() for _ in range(length)]
