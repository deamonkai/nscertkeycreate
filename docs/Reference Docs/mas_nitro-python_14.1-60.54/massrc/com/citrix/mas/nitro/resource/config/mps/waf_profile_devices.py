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
Configuration for Mapping NetScaler IPs to configured WAF Profile names resource
'''

class waf_profile_devices(base_resource):
	_waf_profile_name= ""
	_id= ""
	_parent_id= ""
	_parent_name= ""
	_si_device_ip_address= ""
	_ctnsappname= ""
	_parent_profname= ""
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
			return "waf_profile_devices"
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
			return "waf_profile_devicess"
		except Exception as e :
			raise e



	'''
	get NetScaler WAF Profile name
	'''
	@property
	def waf_profile_name(self) :
		try:
			return self._waf_profile_name
		except Exception as e :
			raise e
	'''
	set NetScaler WAF Profile name
	'''
	@waf_profile_name.setter
	def waf_profile_name(self,waf_profile_name):
		try :
			if not isinstance(waf_profile_name,str):
				raise TypeError("waf_profile_name must be set to str value")
			self._waf_profile_name = waf_profile_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for WAF Profile - ADC map
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for WAF Profile - ADC map
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
	get Id of the parent resource
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id of the parent resource
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Resource name of parent resource
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Resource name of parent resource
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def si_device_ip_address(self) :
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@si_device_ip_address.setter
	def si_device_ip_address(self,si_device_ip_address):
		try :
			if not isinstance(si_device_ip_address,str):
				raise TypeError("si_device_ip_address must be set to str value")
			self._si_device_ip_address = si_device_ip_address
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Profile Name used for naming a learning group
	'''
	@property
	def parent_profname(self) :
		try:
			return self._parent_profname
		except Exception as e :
			raise e
	'''
	set Profile Name used for naming a learning group
	'''
	@parent_profname.setter
	def parent_profname(self,parent_profname):
		try :
			if not isinstance(parent_profname,str):
				raise TypeError("parent_profname must be set to str value")
			self._parent_profname = parent_profname
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler IP - WAF Profile names.
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
				waf_profile_devices_obj=waf_profile_devices()
				return cls.update_bulk_request(client,resource,waf_profile_devices_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to display NetScaler IP - WAF Profile names.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				waf_profile_devices_obj=waf_profile_devices()
				response = waf_profile_devices_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of waf_profile_devices resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			waf_profile_devices_obj = waf_profile_devices()
			option_ = options()
			option_._filter=filter_
			return waf_profile_devices_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the waf_profile_devices resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			waf_profile_devices_obj = waf_profile_devices()
			option_ = options()
			option_._count=True
			response = waf_profile_devices_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of waf_profile_devices resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			waf_profile_devices_obj = waf_profile_devices()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = waf_profile_devices_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(waf_profile_devices_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.waf_profile_devices
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(waf_profile_devices_responses, response, "waf_profile_devices_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.waf_profile_devices_response_array
				i=0
				error = [waf_profile_devices() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.waf_profile_devices_response_array
			i=0
			waf_profile_devices_objs = [waf_profile_devices() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_waf_profile_devices'):
					for props in obj._waf_profile_devices:
						result = service.payload_formatter.string_to_bulk_resource(waf_profile_devices_response,self.__class__.__name__,props)
						waf_profile_devices_objs[i] = result.waf_profile_devices
						i=i+1
			return waf_profile_devices_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(waf_profile_devices,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class waf_profile_devices_response(base_response):
	def __init__(self,length=1) :
		self.waf_profile_devices= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.waf_profile_devices= [ waf_profile_devices() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class waf_profile_devices_responses(base_response):
	def __init__(self,length=1) :
		self.waf_profile_devices_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.waf_profile_devices_response_array = [ waf_profile_devices() for _ in range(length)]
