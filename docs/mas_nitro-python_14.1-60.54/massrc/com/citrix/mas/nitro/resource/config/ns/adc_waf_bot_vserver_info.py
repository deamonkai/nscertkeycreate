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
Configuration for Bot Profile Vserver Configuration Info resource
'''

class adc_waf_bot_vserver_info(base_resource):
	_ns_ip_address= ""
	_instance_id= ""
	_vserver_name= ""
	_vserver_type= ""
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
			return "adc_waf_bot_vserver_info"
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
			return "adc_waf_bot_vserver_infos"
		except Exception as e :
			raise e


	'''
	NetScaler IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
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
	Instance id of ADC
	'''
	@property
	def instance_id(self):
		try:
			return self._instance_id
		except Exception as e :
			raise e
	'''
	Instance id of ADC
	'''
	@instance_id.setter
	def instance_id(self,instance_id):
		try :
			if not isinstance(instance_id,str):
				raise TypeError("instance_id must be set to str value")
			self._instance_id = instance_id
		except Exception as e :
			raise e

	'''
	Virtual server name
	'''
	@property
	def vserver_name(self):
		try:
			return self._vserver_name
		except Exception as e :
			raise e
	'''
	Virtual server name
	'''
	@vserver_name.setter
	def vserver_name(self,vserver_name):
		try :
			if not isinstance(vserver_name,str):
				raise TypeError("vserver_name must be set to str value")
			self._vserver_name = vserver_name
		except Exception as e :
			raise e

	'''
	Type of vserver
	'''
	@property
	def vserver_type(self):
		try:
			return self._vserver_type
		except Exception as e :
			raise e
	'''
	Type of vserver
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
	Add virtual server info.
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
				adc_waf_bot_vserver_info_obj= adc_waf_bot_vserver_info()
				return cls.perform_operation_bulk_request(service,resource,adc_waf_bot_vserver_info_obj)
		except Exception as e :
			raise e

	'''
	modify virtual server info.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				adc_waf_bot_vserver_info_obj=adc_waf_bot_vserver_info()
				return cls.update_bulk_request(client,resource,adc_waf_bot_vserver_info_obj)
		except Exception as e :
			raise e

	'''
	delete virtual server info.
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
					adc_waf_bot_vserver_info_obj=adc_waf_bot_vserver_info()
					return cls.delete_bulk_request(client,resource,adc_waf_bot_vserver_info_obj)
		except Exception as e :
			raise e

	'''
	get virtual server info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_waf_bot_vserver_info_obj=adc_waf_bot_vserver_info()
				response = adc_waf_bot_vserver_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_waf_bot_vserver_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_waf_bot_vserver_info_obj = adc_waf_bot_vserver_info()
			option_ = options()
			option_._filter=filter_
			return adc_waf_bot_vserver_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_waf_bot_vserver_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_waf_bot_vserver_info_obj = adc_waf_bot_vserver_info()
			option_ = options()
			option_._count=True
			response = adc_waf_bot_vserver_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_waf_bot_vserver_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_waf_bot_vserver_info_obj = adc_waf_bot_vserver_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_waf_bot_vserver_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_waf_bot_vserver_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_waf_bot_vserver_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_waf_bot_vserver_info_responses, response, "adc_waf_bot_vserver_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_waf_bot_vserver_info_response_array
				i=0
				error = [adc_waf_bot_vserver_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_waf_bot_vserver_info_response_array
			i=0
			adc_waf_bot_vserver_info_objs = [adc_waf_bot_vserver_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_waf_bot_vserver_info'):
					for props in obj._adc_waf_bot_vserver_info:
						result = service.payload_formatter.string_to_bulk_resource(adc_waf_bot_vserver_info_response,self.__class__.__name__,props)
						adc_waf_bot_vserver_info_objs[i] = result.adc_waf_bot_vserver_info
						i=i+1
			return adc_waf_bot_vserver_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_waf_bot_vserver_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_waf_bot_vserver_info_response(base_response):
	def __init__(self,length=1) :
		self.adc_waf_bot_vserver_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_waf_bot_vserver_info= [ adc_waf_bot_vserver_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_waf_bot_vserver_info_responses(base_response):
	def __init__(self,length=1) :
		self.adc_waf_bot_vserver_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_waf_bot_vserver_info_response_array = [ adc_waf_bot_vserver_info() for _ in range(length)]
