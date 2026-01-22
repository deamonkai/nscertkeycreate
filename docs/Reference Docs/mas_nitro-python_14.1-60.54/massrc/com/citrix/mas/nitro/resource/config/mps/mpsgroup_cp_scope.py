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
Configuration for Configpack Scope for MPSGroup resource
'''

class mpsgroup_cp_scope(base_resource):
	_task_type= ""
	_operation= ""
	_id= ""
	_operation_status= ""
	_group_id= ""
	_sb_info= ""
	_last_modified_datetime= ""
	_sb_id= ""
	_status= ""
	_sbuser= ""
	_configpack_id= ""
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
			return "mpsgroup_cp_scope"
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
			return "mpsgroup_cp_scopes"
		except Exception as e :
			raise e



	'''
	get Type of the task: Stylebook or Configpack
	'''
	@property
	def task_type(self) :
		try:
			return self._task_type
		except Exception as e :
			raise e
	'''
	set Type of the task: Stylebook or Configpack
	'''
	@task_type.setter
	def task_type(self,task_type):
		try :
			if not isinstance(task_type,str):
				raise TypeError("task_type must be set to str value")
			self._task_type = task_type
		except Exception as e :
			raise e


	'''
	get Operation performed on the configpack
	'''
	@property
	def operation(self) :
		try:
			return self._operation
		except Exception as e :
			raise e
	'''
	set Operation performed on the configpack
	'''
	@operation.setter
	def operation(self,operation):
		try :
			if not isinstance(operation,str):
				raise TypeError("operation must be set to str value")
			self._operation = operation
		except Exception as e :
			raise e


	'''
	get Auto generated ID.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Auto generated ID.
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
	get Status of the operation performed on the configpack
	'''
	@property
	def operation_status(self) :
		try:
			return self._operation_status
		except Exception as e :
			raise e
	'''
	set Status of the operation performed on the configpack
	'''
	@operation_status.setter
	def operation_status(self,operation_status):
		try :
			if not isinstance(operation_status,str):
				raise TypeError("operation_status must be set to str value")
			self._operation_status = operation_status
		except Exception as e :
			raise e


	'''
	get Id of the group
	'''
	@property
	def group_id(self) :
		try:
			return self._group_id
		except Exception as e :
			raise e
	'''
	set Id of the group
	'''
	@group_id.setter
	def group_id(self,group_id):
		try :
			if not isinstance(group_id,str):
				raise TypeError("group_id must be set to str value")
			self._group_id = group_id
		except Exception as e :
			raise e


	'''
	get Stylebook details
	'''
	@property
	def sb_info(self) :
		try:
			return self._sb_info
		except Exception as e :
			raise e
	'''
	set Stylebook details
	'''
	@sb_info.setter
	def sb_info(self,sb_info):
		try :
			if not isinstance(sb_info,str):
				raise TypeError("sb_info must be set to str value")
			self._sb_info = sb_info
		except Exception as e :
			raise e


	'''
	get Last modified datetime
	'''
	@property
	def last_modified_datetime(self) :
		try:
			return self._last_modified_datetime
		except Exception as e :
			raise e
	'''
	set Last modified datetime
	'''
	@last_modified_datetime.setter
	def last_modified_datetime(self,last_modified_datetime):
		try :
			if not isinstance(last_modified_datetime,str):
				raise TypeError("last_modified_datetime must be set to str value")
			self._last_modified_datetime = last_modified_datetime
		except Exception as e :
			raise e


	'''
	get Stylebook ID
	'''
	@property
	def sb_id(self) :
		try:
			return self._sb_id
		except Exception as e :
			raise e
	'''
	set Stylebook ID
	'''
	@sb_id.setter
	def sb_id(self,sb_id):
		try :
			if not isinstance(sb_id,str):
				raise TypeError("sb_id must be set to str value")
			self._sb_id = sb_id
		except Exception as e :
			raise e


	'''
	get Status of the configpack
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of the configpack
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
	get User who performed the operation
	'''
	@property
	def sbuser(self) :
		try:
			return self._sbuser
		except Exception as e :
			raise e
	'''
	set User who performed the operation
	'''
	@sbuser.setter
	def sbuser(self,sbuser):
		try :
			if not isinstance(sbuser,str):
				raise TypeError("sbuser must be set to str value")
			self._sbuser = sbuser
		except Exception as e :
			raise e


	'''
	get ID of the configpack
	'''
	@property
	def configpack_id(self) :
		try:
			return self._configpack_id
		except Exception as e :
			raise e
	'''
	set ID of the configpack
	'''
	@configpack_id.setter
	def configpack_id(self,configpack_id):
		try :
			if not isinstance(configpack_id,str):
				raise TypeError("configpack_id must be set to str value")
			self._configpack_id = configpack_id
		except Exception as e :
			raise e

	'''
	Use this operation to get cp scope for mpsgroup.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mpsgroup_cp_scope_obj=mpsgroup_cp_scope()
				response = mpsgroup_cp_scope_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add cp scope for mpsgroup.
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
				mpsgroup_cp_scope_obj= mpsgroup_cp_scope()
				return cls.perform_operation_bulk_request(service,resource,mpsgroup_cp_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete cp scope for mpsgroup.
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
					mpsgroup_cp_scope_obj=mpsgroup_cp_scope()
					return cls.delete_bulk_request(client,resource,mpsgroup_cp_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get cp scope for mpsgroup.
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
				mpsgroup_cp_scope_obj=mpsgroup_cp_scope()
				return cls.update_bulk_request(client,resource,mpsgroup_cp_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mpsgroup_cp_scope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mpsgroup_cp_scope_obj = mpsgroup_cp_scope()
			option_ = options()
			option_._filter=filter_
			return mpsgroup_cp_scope_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mpsgroup_cp_scope resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mpsgroup_cp_scope_obj = mpsgroup_cp_scope()
			option_ = options()
			option_._count=True
			response = mpsgroup_cp_scope_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mpsgroup_cp_scope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mpsgroup_cp_scope_obj = mpsgroup_cp_scope()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mpsgroup_cp_scope_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mpsgroup_cp_scope_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mpsgroup_cp_scope
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mpsgroup_cp_scope_responses, response, "mpsgroup_cp_scope_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mpsgroup_cp_scope_response_array
				i=0
				error = [mpsgroup_cp_scope() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mpsgroup_cp_scope_response_array
			i=0
			mpsgroup_cp_scope_objs = [mpsgroup_cp_scope() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mpsgroup_cp_scope'):
					for props in obj._mpsgroup_cp_scope:
						result = service.payload_formatter.string_to_bulk_resource(mpsgroup_cp_scope_response,self.__class__.__name__,props)
						mpsgroup_cp_scope_objs[i] = result.mpsgroup_cp_scope
						i=i+1
			return mpsgroup_cp_scope_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mpsgroup_cp_scope,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mpsgroup_cp_scope_response(base_response):
	def __init__(self,length=1) :
		self.mpsgroup_cp_scope= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mpsgroup_cp_scope= [ mpsgroup_cp_scope() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mpsgroup_cp_scope_responses(base_response):
	def __init__(self,length=1) :
		self.mpsgroup_cp_scope_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mpsgroup_cp_scope_response_array = [ mpsgroup_cp_scope() for _ in range(length)]
