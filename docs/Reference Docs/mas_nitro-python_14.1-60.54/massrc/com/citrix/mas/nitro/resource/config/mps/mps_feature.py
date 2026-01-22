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
Configuration for Feature Toggle resource
'''

class mps_feature(base_resource):
	_feature_name= ""
	_id= ""
	_admin_toggle= ""
	_description= ""
	_ops_toggle= ""
	_built_in= ""
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
			return "mps_feature"
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
			return "mps_features"
		except Exception as e :
			raise e



	'''
	get Feature Name
	'''
	@property
	def feature_name(self) :
		try:
			return self._feature_name
		except Exception as e :
			raise e
	'''
	set Feature Name
	'''
	@feature_name.setter
	def feature_name(self,feature_name):
		try :
			if not isinstance(feature_name,str):
				raise TypeError("feature_name must be set to str value")
			self._feature_name = feature_name
		except Exception as e :
			raise e


	'''
	get Feature ID
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Feature ID
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
	get This is Admin controllable. 0: Disable UI and Backend, 1: Disable UI and enable Backend, 2: Enable UI and disable Backend, 3: Enable UI and Backend.
	'''
	@property
	def admin_toggle(self) :
		try:
			return self._admin_toggle
		except Exception as e :
			raise e
	'''
	set This is Admin controllable. 0: Disable UI and Backend, 1: Disable UI and enable Backend, 2: Enable UI and disable Backend, 3: Enable UI and Backend.
	'''
	@admin_toggle.setter
	def admin_toggle(self,admin_toggle):
		try :
			if not isinstance(admin_toggle,int):
				raise TypeError("admin_toggle must be set to int value")
			self._admin_toggle = admin_toggle
		except Exception as e :
			raise e


	'''
	get Feature Description.
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Feature Description.
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get This is Ops controllable. 0: Disable UI and Backend, 1: Disable UI and enable Backend, 2: Enable UI and disable Backend, 3: Enable UI and Backend. Ops controlled takes higher precedence than Admin Controlled.
	'''
	@property
	def ops_toggle(self) :
		try:
			return self._ops_toggle
		except Exception as e :
			raise e
	'''
	set This is Ops controllable. 0: Disable UI and Backend, 1: Disable UI and enable Backend, 2: Enable UI and disable Backend, 3: Enable UI and Backend. Ops controlled takes higher precedence than Admin Controlled.
	'''
	@ops_toggle.setter
	def ops_toggle(self,ops_toggle):
		try :
			if not isinstance(ops_toggle,int):
				raise TypeError("ops_toggle must be set to int value")
			self._ops_toggle = ops_toggle
		except Exception as e :
			raise e


	'''
	get This is Ops controllable and will not be visible to the Admin to control. If true: Ops controllable feature, false: Admin controllable feature.
	'''
	@property
	def built_in(self) :
		try:
			return self._built_in
		except Exception as e :
			raise e
	'''
	set This is Ops controllable and will not be visible to the Admin to control. If true: Ops controllable feature, false: Admin controllable feature.
	'''
	@built_in.setter
	def built_in(self,built_in):
		try :
			if not isinstance(built_in,bool):
				raise TypeError("built_in must be set to bool value")
			self._built_in = built_in
		except Exception as e :
			raise e

	'''
	Use this operation to delete a feature toggle..
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
					mps_feature_obj=mps_feature()
					return cls.delete_bulk_request(client,resource,mps_feature_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify a feature toggle..
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
				mps_feature_obj=mps_feature()
				return cls.update_bulk_request(client,resource,mps_feature_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get feature toggles status..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_feature_obj=mps_feature()
				response = mps_feature_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add a feature toggle..
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
				mps_feature_obj= mps_feature()
				return cls.perform_operation_bulk_request(service,resource,mps_feature_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_feature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_feature_obj = mps_feature()
			option_ = options()
			option_._filter=filter_
			return mps_feature_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_feature resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_feature_obj = mps_feature()
			option_ = options()
			option_._count=True
			response = mps_feature_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_feature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_feature_obj = mps_feature()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_feature_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_feature_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_feature
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_feature_responses, response, "mps_feature_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_feature_response_array
				i=0
				error = [mps_feature() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_feature_response_array
			i=0
			mps_feature_objs = [mps_feature() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_feature'):
					for props in obj._mps_feature:
						result = service.payload_formatter.string_to_bulk_resource(mps_feature_response,self.__class__.__name__,props)
						mps_feature_objs[i] = result.mps_feature
						i=i+1
			return mps_feature_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_feature,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_feature_response(base_response):
	def __init__(self,length=1) :
		self.mps_feature= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_feature= [ mps_feature() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_feature_responses(base_response):
	def __init__(self,length=1) :
		self.mps_feature_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_feature_response_array = [ mps_feature() for _ in range(length)]
