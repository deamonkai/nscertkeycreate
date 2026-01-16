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
Configuration for Mapping NetScaler IPs to configured Applications resource
'''

class app_devices_info(base_resource):
	_ctnsappname= ""
	_ns_ip_address= ""
	_parent_id= ""
	_parent_name= ""
	_ip_address= ""
	_session_track_method= ""
	_id= ""
	_session_attribute= ""
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
			return "app_devices_info"
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
			return "app_devices_infos"
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
	get NetScaler Display Name
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler Display Name
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
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Method to track session, e.g., Cookie-Header/URL
	'''
	@property
	def session_track_method(self) :
		try:
			return self._session_track_method
		except Exception as e :
			raise e
	'''
	set Method to track session, e.g., Cookie-Header/URL
	'''
	@session_track_method.setter
	def session_track_method(self,session_track_method):
		try :
			if not isinstance(session_track_method,str):
				raise TypeError("session_track_method must be set to str value")
			self._session_track_method = session_track_method
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
	get attribute to identify the session
	'''
	@property
	def session_attribute(self) :
		try:
			return self._session_attribute
		except Exception as e :
			raise e
	'''
	set attribute to identify the session
	'''
	@session_attribute.setter
	def session_attribute(self,session_attribute):
		try :
			if not isinstance(session_attribute,str):
				raise TypeError("session_attribute must be set to str value")
			self._session_attribute = session_attribute
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler IP - Application names.
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
				app_devices_info_obj=app_devices_info()
				return cls.update_bulk_request(client,resource,app_devices_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to display NetScaler IP - Application names.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				app_devices_info_obj=app_devices_info()
				response = app_devices_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_devices_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_devices_info_obj = app_devices_info()
			option_ = options()
			option_._filter=filter_
			return app_devices_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_devices_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_devices_info_obj = app_devices_info()
			option_ = options()
			option_._count=True
			response = app_devices_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_devices_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_devices_info_obj = app_devices_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_devices_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(app_devices_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_devices_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_devices_info_responses, response, "app_devices_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_devices_info_response_array
				i=0
				error = [app_devices_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_devices_info_response_array
			i=0
			app_devices_info_objs = [app_devices_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_devices_info'):
					for props in obj._app_devices_info:
						result = service.payload_formatter.string_to_bulk_resource(app_devices_info_response,self.__class__.__name__,props)
						app_devices_info_objs[i] = result.app_devices_info
						i=i+1
			return app_devices_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_devices_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_devices_info_response(base_response):
	def __init__(self,length=1) :
		self.app_devices_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_devices_info= [ app_devices_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_devices_info_responses(base_response):
	def __init__(self,length=1) :
		self.app_devices_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_devices_info_response_array = [ app_devices_info() for _ in range(length)]
