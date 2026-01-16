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
Configuration for Activity Status resource
'''

class tenant_provisioning_status(base_resource):
	_status= ""
	_message= ""
	_activity= ""
	_id= ""
	_timestamp= ""
	_act_id= ""
	_priority= ""
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
			return "tenant_provisioning_status"
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
			return "tenant_provisioning_statuss"
		except Exception as e :
			raise e



	'''
	get Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status
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
	get Message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Message
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
	get activity
	'''
	@property
	def activity(self) :
		try:
			return self._activity
		except Exception as e :
			raise e
	'''
	set activity
	'''
	@activity.setter
	def activity(self,activity):
		try :
			if not isinstance(activity,str):
				raise TypeError("activity must be set to str value")
			self._activity = activity
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the task logs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the task logs
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
	get timestamp in seconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in seconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
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
	get priority of the steps
	'''
	@property
	def priority(self) :
		try:
			return self._priority
		except Exception as e :
			raise e
	'''
	set priority of the steps
	'''
	@priority.setter
	def priority(self,priority):
		try :
			if not isinstance(priority,int):
				raise TypeError("priority must be set to int value")
			self._priority = priority
		except Exception as e :
			raise e

	'''
	Use this operation to get activity status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				tenant_provisioning_status_obj=tenant_provisioning_status()
				response = tenant_provisioning_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant_provisioning_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_provisioning_status_obj = tenant_provisioning_status()
			option_ = options()
			option_._filter=filter_
			return tenant_provisioning_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant_provisioning_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_provisioning_status_obj = tenant_provisioning_status()
			option_ = options()
			option_._count=True
			response = tenant_provisioning_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant_provisioning_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_provisioning_status_obj = tenant_provisioning_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_provisioning_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_provisioning_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_provisioning_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_provisioning_status_responses, response, "tenant_provisioning_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_provisioning_status_response_array
				i=0
				error = [tenant_provisioning_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_provisioning_status_response_array
			i=0
			tenant_provisioning_status_objs = [tenant_provisioning_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_provisioning_status'):
					for props in obj._tenant_provisioning_status:
						result = service.payload_formatter.string_to_bulk_resource(tenant_provisioning_status_response,self.__class__.__name__,props)
						tenant_provisioning_status_objs[i] = result.tenant_provisioning_status
						i=i+1
			return tenant_provisioning_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_provisioning_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_provisioning_status_response(base_response):
	def __init__(self,length=1) :
		self.tenant_provisioning_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_provisioning_status= [ tenant_provisioning_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_provisioning_status_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_provisioning_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_provisioning_status_response_array = [ tenant_provisioning_status() for _ in range(length)]
