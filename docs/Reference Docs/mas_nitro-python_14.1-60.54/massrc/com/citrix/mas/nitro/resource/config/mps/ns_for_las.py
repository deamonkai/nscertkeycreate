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
Configuration for ns_for_las resource
'''

class ns_for_las(base_resource):
	_reason= ""
	_id= ""
	_status= ""
	_ip_address= ""
	_md_id= ""
	_version= ""
	_type= ""
	_license_mode= ""
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
			return "ns_for_las"
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
			return "ns_for_lass"
		except Exception as e :
			raise e



	'''
	get Device migration failure reason
	'''
	@property
	def reason(self) :
		try:
			return self._reason
		except Exception as e :
			raise e
	'''
	set Device migration failure reason
	'''
	@reason.setter
	def reason(self,reason):
		try :
			if not isinstance(reason,str):
				raise TypeError("reason must be set to str value")
			self._reason = reason
		except Exception as e :
			raise e


	'''
	get Id is system generated key for protection
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for protection
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
	get Device migration status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Device migration status
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
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
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
	Managed Device ID
	'''
	@property
	def md_id(self):
		try:
			return self._md_id
		except Exception as e :
			raise e
	'''
	Managed Device ID
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
	NS version
	'''
	@property
	def version(self):
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	NS version
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
	License Type
	'''
	@property
	def type(self):
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	License Type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e

	'''
	License Mode
	'''
	@property
	def license_mode(self):
		try:
			return self._license_mode
		except Exception as e :
			raise e
	'''
	License Mode
	'''
	@license_mode.setter
	def license_mode(self,license_mode):
		try :
			if not isinstance(license_mode,str):
				raise TypeError("license_mode must be set to str value")
			self._license_mode = license_mode
		except Exception as e :
			raise e

	'''
	Use this operation to get ns for las device.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_for_las_obj=ns_for_las()
				response = ns_for_las_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add ns for las device.
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
				ns_for_las_obj= ns_for_las()
				return cls.perform_operation_bulk_request(service,resource,ns_for_las_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify ns for las device.
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
				ns_for_las_obj=ns_for_las()
				return cls.update_bulk_request(client,resource,ns_for_las_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete ns for las device.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					ns_for_las_obj=ns_for_las()
					return cls.delete_bulk_request(client,resource,ns_for_las_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_for_las resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_for_las_obj = ns_for_las()
			option_ = options()
			option_._filter=filter_
			return ns_for_las_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_for_las resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_for_las_obj = ns_for_las()
			option_ = options()
			option_._count=True
			response = ns_for_las_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_for_las resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_for_las_obj = ns_for_las()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_for_las_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_for_las_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_for_las
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_for_las_responses, response, "ns_for_las_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_for_las_response_array
				i=0
				error = [ns_for_las() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_for_las_response_array
			i=0
			ns_for_las_objs = [ns_for_las() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_for_las'):
					for props in obj._ns_for_las:
						result = service.payload_formatter.string_to_bulk_resource(ns_for_las_response,self.__class__.__name__,props)
						ns_for_las_objs[i] = result.ns_for_las
						i=i+1
			return ns_for_las_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_for_las,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_for_las_response(base_response):
	def __init__(self,length=1) :
		self.ns_for_las= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_for_las= [ ns_for_las() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_for_las_responses(base_response):
	def __init__(self,length=1) :
		self.ns_for_las_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_for_las_response_array = [ ns_for_las() for _ in range(length)]
