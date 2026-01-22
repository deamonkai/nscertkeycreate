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
Configuration for MPS CCP client information resource
'''

class mps_ccp_client(base_resource):
	_enable_telemetry= ""
	_id= ""
	_version= ""
	_customer_name= ""
	_last_up_time= ""
	_state= ""
	_name= ""
	_instance_id= ""
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
			return "mps_ccp_client"
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
			return "mps_ccp_clients"
		except Exception as e :
			raise e



	'''
	get enable telemetry
	'''
	@property
	def enable_telemetry(self) :
		try:
			return self._enable_telemetry
		except Exception as e :
			raise e
	'''
	set enable telemetry
	'''
	@enable_telemetry.setter
	def enable_telemetry(self,enable_telemetry):
		try :
			if not isinstance(enable_telemetry,bool):
				raise TypeError("enable_telemetry must be set to bool value")
			self._enable_telemetry = enable_telemetry
		except Exception as e :
			raise e


	'''
	get Id is system generated key for CCP client registered with NMX Cloud.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for CCP client registered with NMX Cloud.
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
	get version.
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set version.
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
	get customer display name
	'''
	@property
	def customer_name(self) :
		try:
			return self._customer_name
		except Exception as e :
			raise e
	'''
	set customer display name
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
	get Last time when the On-prem Console was seen up
	'''
	@property
	def last_up_time(self) :
		try:
			return self._last_up_time
		except Exception as e :
			raise e
	'''
	set Last time when the On-prem Console was seen up
	'''
	@last_up_time.setter
	def last_up_time(self,last_up_time):
		try :
			if not isinstance(last_up_time,long):
				raise TypeError("last_up_time must be set to long value")
			self._last_up_time = last_up_time
		except Exception as e :
			raise e


	'''
	get Agent state
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Agent state
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
	get Agent IP Address
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Agent IP Address
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
	get Instance ID from CC Profile
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e
	'''
	set Instance ID from CC Profile
	'''
	@instance_id.setter
	def instance_id(self,instance_id):
		try :
			if not isinstance(instance_id,str):
				raise TypeError("instance_id must be set to str value")
			self._instance_id = instance_id
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_ccp_client_obj=mps_ccp_client()
				response = mps_ccp_client_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add Agent information.
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
				mps_ccp_client_obj= mps_ccp_client()
				return cls.perform_operation_bulk_request(service,resource,mps_ccp_client_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_ccp_client resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_ccp_client_obj = mps_ccp_client()
			option_ = options()
			option_._filter=filter_
			return mps_ccp_client_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_ccp_client resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_ccp_client_obj = mps_ccp_client()
			option_ = options()
			option_._count=True
			response = mps_ccp_client_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_ccp_client resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_ccp_client_obj = mps_ccp_client()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_ccp_client_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_ccp_client_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_ccp_client
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_ccp_client_responses, response, "mps_ccp_client_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_ccp_client_response_array
				i=0
				error = [mps_ccp_client() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_ccp_client_response_array
			i=0
			mps_ccp_client_objs = [mps_ccp_client() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_ccp_client'):
					for props in obj._mps_ccp_client:
						result = service.payload_formatter.string_to_bulk_resource(mps_ccp_client_response,self.__class__.__name__,props)
						mps_ccp_client_objs[i] = result.mps_ccp_client
						i=i+1
			return mps_ccp_client_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_ccp_client,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_ccp_client_response(base_response):
	def __init__(self,length=1) :
		self.mps_ccp_client= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_ccp_client= [ mps_ccp_client() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_ccp_client_responses(base_response):
	def __init__(self,length=1) :
		self.mps_ccp_client_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_ccp_client_response_array = [ mps_ccp_client() for _ in range(length)]
