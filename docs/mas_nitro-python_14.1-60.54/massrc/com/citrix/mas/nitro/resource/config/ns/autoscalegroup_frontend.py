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
Configuration for Autoscalegroup Frontend resource
'''

class autoscalegroup_frontend(base_resource):
	_ipaddress_id= ""
	_autoscalegroup_id= ""
	_access_type= ""
	_id= ""
	_frontend_name= ""
	_ip_address= ""
	_ipaddress_id_list=[]
	_ip_address_list=[]
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
			return "autoscalegroup_frontend"
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
			return "autoscalegroup_frontends"
		except Exception as e :
			raise e



	'''
	get One or more ipaddress id
	'''
	@property
	def ipaddress_id(self) :
		try:
			return self._ipaddress_id
		except Exception as e :
			raise e
	'''
	set One or more ipaddress id
	'''
	@ipaddress_id.setter
	def ipaddress_id(self,ipaddress_id):
		try :
			if not isinstance(ipaddress_id,str):
				raise TypeError("ipaddress_id must be set to str value")
			self._ipaddress_id = ipaddress_id
		except Exception as e :
			raise e


	'''
	get ID of autoscalegroup
	'''
	@property
	def autoscalegroup_id(self) :
		try:
			return self._autoscalegroup_id
		except Exception as e :
			raise e
	'''
	set ID of autoscalegroup
	'''
	@autoscalegroup_id.setter
	def autoscalegroup_id(self,autoscalegroup_id):
		try :
			if not isinstance(autoscalegroup_id,str):
				raise TypeError("autoscalegroup_id must be set to str value")
			self._autoscalegroup_id = autoscalegroup_id
		except Exception as e :
			raise e


	'''
	get Access Type (0.External(public)/1.Internal(private)/2.None)
	'''
	@property
	def access_type(self) :
		try:
			return self._access_type
		except Exception as e :
			raise e
	'''
	set Access Type (0.External(public)/1.Internal(private)/2.None)
	'''
	@access_type.setter
	def access_type(self,access_type):
		try :
			if not isinstance(access_type,int):
				raise TypeError("access_type must be set to int value")
			self._access_type = access_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the auto-scale groups frontends
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the auto-scale groups frontends
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
	get Frontend Name
	'''
	@property
	def frontend_name(self) :
		try:
			return self._frontend_name
		except Exception as e :
			raise e
	'''
	set Frontend Name
	'''
	@frontend_name.setter
	def frontend_name(self,frontend_name):
		try :
			if not isinstance(frontend_name,str):
				raise TypeError("frontend_name must be set to str value")
			self._frontend_name = frontend_name
		except Exception as e :
			raise e


	'''
	get One or more ipaddress
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set One or more ipaddress
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
	One or more ipaddress id
	'''
	@property
	def ipaddress_id_list(self) :
		try:
			return self._ipaddress_id_list
		except Exception as e :
			raise e
	'''
	One or more ipaddress id
	'''
	@ipaddress_id_list.setter
	def ipaddress_id_list(self,ipaddress_id_list) :
		try :
			if not isinstance(ipaddress_id_list,list):
				raise TypeError("ipaddress_id_list must be set to array of str value")
			for item in ipaddress_id_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ipaddress_id_list = ipaddress_id_list
		except Exception as e :
			raise e

	'''
	One or more ipaddress
	'''
	@property
	def ip_address_list(self) :
		try:
			return self._ip_address_list
		except Exception as e :
			raise e
	'''
	One or more ipaddress
	'''
	@ip_address_list.setter
	def ip_address_list(self,ip_address_list) :
		try :
			if not isinstance(ip_address_list,list):
				raise TypeError("ip_address_list must be set to array of str value")
			for item in ip_address_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ip_address_list = ip_address_list
		except Exception as e :
			raise e

	'''
	Use this operation to get autoscalegroup_frontend.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscalegroup_frontend_obj=autoscalegroup_frontend()
				response = autoscalegroup_frontend_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete autoscalegroup_frontend(s).
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
					autoscalegroup_frontend_obj=autoscalegroup_frontend()
					return cls.delete_bulk_request(client,resource,autoscalegroup_frontend_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add autoscalegroup_frontend.
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
				autoscalegroup_frontend_obj= autoscalegroup_frontend()
				return cls.perform_operation_bulk_request(service,resource,autoscalegroup_frontend_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscalegroup_frontend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscalegroup_frontend_obj = autoscalegroup_frontend()
			option_ = options()
			option_._filter=filter_
			return autoscalegroup_frontend_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscalegroup_frontend resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscalegroup_frontend_obj = autoscalegroup_frontend()
			option_ = options()
			option_._count=True
			response = autoscalegroup_frontend_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscalegroup_frontend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscalegroup_frontend_obj = autoscalegroup_frontend()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscalegroup_frontend_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscalegroup_frontend_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscalegroup_frontend
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscalegroup_frontend_responses, response, "autoscalegroup_frontend_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscalegroup_frontend_response_array
				i=0
				error = [autoscalegroup_frontend() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscalegroup_frontend_response_array
			i=0
			autoscalegroup_frontend_objs = [autoscalegroup_frontend() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscalegroup_frontend'):
					for props in obj._autoscalegroup_frontend:
						result = service.payload_formatter.string_to_bulk_resource(autoscalegroup_frontend_response,self.__class__.__name__,props)
						autoscalegroup_frontend_objs[i] = result.autoscalegroup_frontend
						i=i+1
			return autoscalegroup_frontend_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscalegroup_frontend,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscalegroup_frontend_response(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_frontend= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscalegroup_frontend= [ autoscalegroup_frontend() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscalegroup_frontend_responses(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_frontend_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscalegroup_frontend_response_array = [ autoscalegroup_frontend() for _ in range(length)]
