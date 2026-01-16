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
Configuration for License pool capacity of appliance resource
'''

class capacity(base_resource):
	_plt_bw= ""
	_daystoexpiration= ""
	_ent_bw= ""
	_id= ""
	_instance= ""
	_std_bw= ""
	_username= ""
	_password= ""
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
			return "capacity"
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
			return "capacitys"
		except Exception as e :
			raise e



	'''
	get Platinum Bandwidth pool in Gbps
	'''
	@property
	def plt_bw(self) :
		try:
			return self._plt_bw
		except Exception as e :
			raise e
	'''
	set Platinum Bandwidth pool in Gbps
	'''
	@plt_bw.setter
	def plt_bw(self,plt_bw):
		try :
			if not isinstance(plt_bw,int):
				raise TypeError("plt_bw must be set to int value")
			self._plt_bw = plt_bw
		except Exception as e :
			raise e


	'''
	get Days to expiration
	'''
	@property
	def daystoexpiration(self) :
		try:
			return self._daystoexpiration
		except Exception as e :
			raise e
	'''
	set Days to expiration
	'''
	@daystoexpiration.setter
	def daystoexpiration(self,daystoexpiration):
		try :
			if not isinstance(daystoexpiration,int):
				raise TypeError("daystoexpiration must be set to int value")
			self._daystoexpiration = daystoexpiration
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth pool in Gbps
	'''
	@property
	def ent_bw(self) :
		try:
			return self._ent_bw
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth pool in Gbps
	'''
	@ent_bw.setter
	def ent_bw(self,ent_bw):
		try :
			if not isinstance(ent_bw,int):
				raise TypeError("ent_bw must be set to int value")
			self._ent_bw = ent_bw
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
	get Instance bandwidth pool
	'''
	@property
	def instance(self) :
		try:
			return self._instance
		except Exception as e :
			raise e
	'''
	set Instance bandwidth pool
	'''
	@instance.setter
	def instance(self,instance):
		try :
			if not isinstance(instance,int):
				raise TypeError("instance must be set to int value")
			self._instance = instance
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth pool in Gbps
	'''
	@property
	def std_bw(self) :
		try:
			return self._std_bw
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth pool in Gbps
	'''
	@std_bw.setter
	def std_bw(self,std_bw):
		try :
			if not isinstance(std_bw,int):
				raise TypeError("std_bw must be set to int value")
			self._std_bw = std_bw
		except Exception as e :
			raise e

	'''
	username for license server
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	username for license server
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e

	'''
	password for license server
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	password for license server
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e

	'''
	Use this operation to modify license capacity.
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
				capacity_obj=capacity()
				return cls.update_bulk_request(client,resource,capacity_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get license pool details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				capacity_obj=capacity()
				response = capacity_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of capacity resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			capacity_obj = capacity()
			option_ = options()
			option_._filter=filter_
			return capacity_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the capacity resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			capacity_obj = capacity()
			option_ = options()
			option_._count=True
			response = capacity_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of capacity resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			capacity_obj = capacity()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = capacity_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(capacity_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.capacity
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(capacity_responses, response, "capacity_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.capacity_response_array
				i=0
				error = [capacity() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.capacity_response_array
			i=0
			capacity_objs = [capacity() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_capacity'):
					for props in obj._capacity:
						result = service.payload_formatter.string_to_bulk_resource(capacity_response,self.__class__.__name__,props)
						capacity_objs[i] = result.capacity
						i=i+1
			return capacity_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(capacity,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class capacity_response(base_response):
	def __init__(self,length=1) :
		self.capacity= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.capacity= [ capacity() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class capacity_responses(base_response):
	def __init__(self,length=1) :
		self.capacity_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.capacity_response_array = [ capacity() for _ in range(length)]
