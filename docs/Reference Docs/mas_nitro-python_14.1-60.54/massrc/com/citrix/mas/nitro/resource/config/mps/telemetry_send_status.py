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
Configuration for Telemetry Send Status resource
'''

class telemetry_send_status(base_resource):
	_message= ""
	_status= ""
	_timestamp= ""
	_id= ""
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
			return "telemetry_send_status"
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
			return "telemetry_send_statuss"
		except Exception as e :
			raise e



	'''
	get telemetry send message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set telemetry send message
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
		except Exception as e :
			raise e


	'''
	get telemetry send status (true or false)
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set telemetry send status (true or false)
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Timestamp of AUTOMATIC upload (EPOCH)
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set Timestamp of AUTOMATIC upload (EPOCH)
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,str):
				raise TypeError("timestamp must be set to str value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get id of telemetry send status to service
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set id of telemetry send status to service
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
	Use this operation to get telemetry upload status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				telemetry_send_status_obj=telemetry_send_status()
				response = telemetry_send_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of telemetry_send_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			telemetry_send_status_obj = telemetry_send_status()
			option_ = options()
			option_._filter=filter_
			return telemetry_send_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the telemetry_send_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			telemetry_send_status_obj = telemetry_send_status()
			option_ = options()
			option_._count=True
			response = telemetry_send_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of telemetry_send_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			telemetry_send_status_obj = telemetry_send_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = telemetry_send_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(telemetry_send_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.telemetry_send_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(telemetry_send_status_responses, response, "telemetry_send_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.telemetry_send_status_response_array
				i=0
				error = [telemetry_send_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.telemetry_send_status_response_array
			i=0
			telemetry_send_status_objs = [telemetry_send_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_telemetry_send_status'):
					for props in obj._telemetry_send_status:
						result = service.payload_formatter.string_to_bulk_resource(telemetry_send_status_response,self.__class__.__name__,props)
						telemetry_send_status_objs[i] = result.telemetry_send_status
						i=i+1
			return telemetry_send_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(telemetry_send_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class telemetry_send_status_response(base_response):
	def __init__(self,length=1) :
		self.telemetry_send_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.telemetry_send_status= [ telemetry_send_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class telemetry_send_status_responses(base_response):
	def __init__(self,length=1) :
		self.telemetry_send_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.telemetry_send_status_response_array = [ telemetry_send_status() for _ in range(length)]
