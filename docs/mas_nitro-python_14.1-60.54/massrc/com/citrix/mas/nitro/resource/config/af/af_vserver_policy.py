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
Configuration for Virtual server Policy resource
'''

class af_vserver_policy(base_resource):
	_vserver_type= ""
	_id= ""
	_policy_rule= ""
	_servicetype= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_vserver_policy"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "af_vserver_policys"
		except Exception as e :
			raise e


	'''
	virtual server type
	'''
	@property
	def vserver_type(self):
		try:
			return self._vserver_type
		except Exception as e :
			raise e
	'''
	virtual server type
	'''
	@vserver_type.setter
	def vserver_type(self,vserver_type):
		try :
			if not isinstance(vserver_type,str):
				raise TypeError("vserver_type must be set to str value")
			self._vserver_type = vserver_type
		except Exception as e :
			raise e

	'''
	Id is type of policy rule
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is type of policy rule
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
	Policy rule
	'''
	@property
	def policy_rule(self):
		try:
			return self._policy_rule
		except Exception as e :
			raise e
	'''
	Policy rule
	'''
	@policy_rule.setter
	def policy_rule(self,policy_rule):
		try :
			if not isinstance(policy_rule,str):
				raise TypeError("policy_rule must be set to str value")
			self._policy_rule = policy_rule
		except Exception as e :
			raise e

	'''
	Type of Service
	'''
	@property
	def servicetype(self):
		try:
			return self._servicetype
		except Exception as e :
			raise e
	'''
	Type of Service
	'''
	@servicetype.setter
	def servicetype(self,servicetype):
		try :
			if not isinstance(servicetype,str):
				raise TypeError("servicetype must be set to str value")
			self._servicetype = servicetype
		except Exception as e :
			raise e

	'''
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	get virtual server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_vserver_policy_obj=af_vserver_policy()
				response = af_vserver_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_vserver_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_vserver_policy_obj = af_vserver_policy()
			option_ = options()
			option_._filter=filter_
			return af_vserver_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_vserver_policy resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_vserver_policy_obj = af_vserver_policy()
			option_ = options()
			option_._count=True
			response = af_vserver_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_vserver_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_vserver_policy_obj = af_vserver_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_vserver_policy_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_vserver_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_vserver_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_vserver_policy_responses, response, "af_vserver_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_vserver_policy_response_array
				i=0
				error = [af_vserver_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_vserver_policy_response_array
			i=0
			af_vserver_policy_objs = [af_vserver_policy() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_vserver_policy:
					result = service.payload_formatter.string_to_bulk_resource(af_vserver_policy_response,self.__class__.__name__,props)
					af_vserver_policy_objs[i] = result.af_vserver_policy
					i=i+1
			return af_vserver_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_vserver_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_vserver_policy_response(base_response):
	def __init__(self,length=1) :
		self.af_vserver_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_vserver_policy= [ af_vserver_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_vserver_policy_responses(base_response):
	def __init__(self,length=1) :
		self.af_vserver_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_vserver_policy_response_array = [ af_vserver_policy() for _ in range(length)]
