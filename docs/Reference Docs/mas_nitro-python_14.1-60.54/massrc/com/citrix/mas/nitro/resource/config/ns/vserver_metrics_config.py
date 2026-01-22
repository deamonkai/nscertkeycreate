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
Configuration for Metrics Enabled Vserver Information resource
'''

class vserver_metrics_config(base_resource):
	_enable= ""
	_vservers=[]
	_metrics_option_list=[]
	_act_id= ""
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
			return "vserver_metrics_config"
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
			return "vserver_metrics_configs"
		except Exception as e :
			raise e



	'''
	get enable status (true/false)
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set enable status (true/false)
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e


	'''
	get vserver uuids list
	'''
	@property
	def vservers(self) :
		try:
			return self._vservers
		except Exception as e :
			raise e
	'''
	set vserver uuids list
	'''
	@vservers.setter
	def vservers(self,vservers) :
		try :
			if not isinstance(vservers,list):
				raise TypeError("vservers must be set to array of str value")
			for item in vservers :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vservers = vservers
		except Exception as e :
			raise e


	'''
	get Metric usecases user wants to enable
	'''
	@property
	def metrics_option_list(self) :
		try:
			return self._metrics_option_list
		except Exception as e :
			raise e
	'''
	set Metric usecases user wants to enable
	'''
	@metrics_option_list.setter
	def metrics_option_list(self,metrics_option_list) :
		try :
			if not isinstance(metrics_option_list,list):
				raise TypeError("metrics_option_list must be set to array of str value")
			for item in metrics_option_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._metrics_option_list = metrics_option_list
		except Exception as e :
			raise e


	'''
	get Activity ID that is used to track the polling status
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e
	'''
	set Activity ID that is used to track the polling status
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	Use this operation to enable/disable vservers metrics processing.
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
				vserver_metrics_config_obj= vserver_metrics_config()
				return cls.perform_operation_bulk_request(service,resource,vserver_metrics_config_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vserver_metrics_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vserver_metrics_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vserver_metrics_config_responses, response, "vserver_metrics_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vserver_metrics_config_response_array
				i=0
				error = [vserver_metrics_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vserver_metrics_config_response_array
			i=0
			vserver_metrics_config_objs = [vserver_metrics_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vserver_metrics_config'):
					for props in obj._vserver_metrics_config:
						result = service.payload_formatter.string_to_bulk_resource(vserver_metrics_config_response,self.__class__.__name__,props)
						vserver_metrics_config_objs[i] = result.vserver_metrics_config
						i=i+1
			return vserver_metrics_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vserver_metrics_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vserver_metrics_config_response(base_response):
	def __init__(self,length=1) :
		self.vserver_metrics_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vserver_metrics_config= [ vserver_metrics_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vserver_metrics_config_responses(base_response):
	def __init__(self,length=1) :
		self.vserver_metrics_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vserver_metrics_config_response_array = [ vserver_metrics_config() for _ in range(length)]
