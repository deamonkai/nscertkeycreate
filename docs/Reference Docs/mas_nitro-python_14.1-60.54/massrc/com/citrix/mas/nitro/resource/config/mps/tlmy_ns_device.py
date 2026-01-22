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
Configuration for The table maintained by telemetry insights module which has subset of managed_device table columns. resource
'''

class tlmy_ns_device(base_resource):
	_agent_version= ""
	_org_id= ""
	_id= ""
	_device_state= ""
	_device_ip= ""
	_last_seen= ""
	_md_id= ""
	_agent_ip= ""
	_device_family= ""
	_first_discovered= ""
	_managed_by= ""
	_device_version= ""
	_cc_id= ""
	_agent_state= ""
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
			return "tlmy_ns_device"
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
			return "tlmy_ns_devices"
		except Exception as e :
			raise e



	'''
	get Version of the agent managing the device
	'''
	@property
	def agent_version(self) :
		try:
			return self._agent_version
		except Exception as e :
			raise e
	'''
	set Version of the agent managing the device
	'''
	@agent_version.setter
	def agent_version(self,agent_version):
		try :
			if not isinstance(agent_version,str):
				raise TypeError("agent_version must be set to str value")
			self._agent_version = agent_version
		except Exception as e :
			raise e


	'''
	get Org id to which the device belongs
	'''
	@property
	def org_id(self) :
		try:
			return self._org_id
		except Exception as e :
			raise e
	'''
	set Org id to which the device belongs
	'''
	@org_id.setter
	def org_id(self,org_id):
		try :
			if not isinstance(org_id,str):
				raise TypeError("org_id must be set to str value")
			self._org_id = org_id
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get State of the device - Up/Down
	'''
	@property
	def device_state(self) :
		try:
			return self._device_state
		except Exception as e :
			raise e
	'''
	set State of the device - Up/Down
	'''
	@device_state.setter
	def device_state(self,device_state):
		try :
			if not isinstance(device_state,str):
				raise TypeError("device_state must be set to str value")
			self._device_state = device_state
		except Exception as e :
			raise e


	'''
	get IP address of the device
	'''
	@property
	def device_ip(self) :
		try:
			return self._device_ip
		except Exception as e :
			raise e
	'''
	set IP address of the device
	'''
	@device_ip.setter
	def device_ip(self,device_ip):
		try :
			if not isinstance(device_ip,str):
				raise TypeError("device_ip must be set to str value")
			self._device_ip = device_ip
		except Exception as e :
			raise e


	'''
	get The time specified as epoch in seconds when the device was last seen by tlmy insights
	'''
	@property
	def last_seen(self) :
		try:
			return self._last_seen
		except Exception as e :
			raise e
	'''
	set The time specified as epoch in seconds when the device was last seen by tlmy insights
	'''
	@last_seen.setter
	def last_seen(self,last_seen):
		try :
			if not isinstance(last_seen,long):
				raise TypeError("last_seen must be set to long value")
			self._last_seen = last_seen
		except Exception as e :
			raise e


	'''
	get Device Id from tenant's managed_device table
	'''
	@property
	def md_id(self) :
		try:
			return self._md_id
		except Exception as e :
			raise e
	'''
	set Device Id from tenant's managed_device table
	'''
	@md_id.setter
	def md_id(self,md_id):
		try :
			if not isinstance(md_id,str):
				raise TypeError("md_id must be set to str value")
			self._md_id = md_id
		except Exception as e :
			raise e


	'''
	get IP address of the agent managing the device
	'''
	@property
	def agent_ip(self) :
		try:
			return self._agent_ip
		except Exception as e :
			raise e
	'''
	set IP address of the agent managing the device
	'''
	@agent_ip.setter
	def agent_ip(self,agent_ip):
		try :
			if not isinstance(agent_ip,str):
				raise TypeError("agent_ip must be set to str value")
			self._agent_ip = agent_ip
		except Exception as e :
			raise e


	'''
	get Family of the device - NetScaler/SVM etc.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of the device - NetScaler/SVM etc.
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get The time specified as epoch in seconds when the device was 1st seen by tlmy insights
	'''
	@property
	def first_discovered(self) :
		try:
			return self._first_discovered
		except Exception as e :
			raise e
	'''
	set The time specified as epoch in seconds when the device was 1st seen by tlmy insights
	'''
	@first_discovered.setter
	def first_discovered(self,first_discovered):
		try :
			if not isinstance(first_discovered,long):
				raise TypeError("first_discovered must be set to long value")
			self._first_discovered = first_discovered
		except Exception as e :
			raise e


	'''
	get Type of the agent managing the device
	'''
	@property
	def managed_by(self) :
		try:
			return self._managed_by
		except Exception as e :
			raise e
	'''
	set Type of the agent managing the device
	'''
	@managed_by.setter
	def managed_by(self,managed_by):
		try :
			if not isinstance(managed_by,str):
				raise TypeError("managed_by must be set to str value")
			self._managed_by = managed_by
		except Exception as e :
			raise e


	'''
	get Version of the device
	'''
	@property
	def device_version(self) :
		try:
			return self._device_version
		except Exception as e :
			raise e
	'''
	set Version of the device
	'''
	@device_version.setter
	def device_version(self,device_version):
		try :
			if not isinstance(device_version,str):
				raise TypeError("device_version must be set to str value")
			self._device_version = device_version
		except Exception as e :
			raise e


	'''
	get CCID to which the device belongs; TODO: add UNIQUE (device_id, ccid) constraint through code/SQL
	'''
	@property
	def cc_id(self) :
		try:
			return self._cc_id
		except Exception as e :
			raise e
	'''
	set CCID to which the device belongs; TODO: add UNIQUE (device_id, ccid) constraint through code/SQL
	'''
	@cc_id.setter
	def cc_id(self,cc_id):
		try :
			if not isinstance(cc_id,str):
				raise TypeError("cc_id must be set to str value")
			self._cc_id = cc_id
		except Exception as e :
			raise e


	'''
	get State of the agent managing the device
	'''
	@property
	def agent_state(self) :
		try:
			return self._agent_state
		except Exception as e :
			raise e
	'''
	set State of the agent managing the device
	'''
	@agent_state.setter
	def agent_state(self,agent_state):
		try :
			if not isinstance(agent_state,str):
				raise TypeError("agent_state must be set to str value")
			self._agent_state = agent_state
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_ns_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tlmy_ns_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tlmy_ns_device_responses, response, "tlmy_ns_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tlmy_ns_device_response_array
				i=0
				error = [tlmy_ns_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tlmy_ns_device_response_array
			i=0
			tlmy_ns_device_objs = [tlmy_ns_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tlmy_ns_device'):
					for props in obj._tlmy_ns_device:
						result = service.payload_formatter.string_to_bulk_resource(tlmy_ns_device_response,self.__class__.__name__,props)
						tlmy_ns_device_objs[i] = result.tlmy_ns_device
						i=i+1
			return tlmy_ns_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tlmy_ns_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tlmy_ns_device_response(base_response):
	def __init__(self,length=1) :
		self.tlmy_ns_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tlmy_ns_device= [ tlmy_ns_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tlmy_ns_device_responses(base_response):
	def __init__(self,length=1) :
		self.tlmy_ns_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tlmy_ns_device_response_array = [ tlmy_ns_device() for _ in range(length)]
