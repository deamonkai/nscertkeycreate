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
Configuration for LAS CC poll interval resource
'''

class cc_las_poll_interval(base_resource):
	_id= ""
	_console_las_refresh= ""
	_console_ns_refresh= ""
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
			return "cc_las_poll_interval"
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
			return "cc_las_poll_intervals"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for all the VM Instances
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the VM Instances
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
	get LAS blob refresh interval between console and LAS
	'''
	@property
	def console_las_refresh(self) :
		try:
			return self._console_las_refresh
		except Exception as e :
			raise e
	'''
	set LAS blob refresh interval between console and LAS
	'''
	@console_las_refresh.setter
	def console_las_refresh(self,console_las_refresh):
		try :
			if not isinstance(console_las_refresh,int):
				raise TypeError("console_las_refresh must be set to int value")
			self._console_las_refresh = console_las_refresh
		except Exception as e :
			raise e


	'''
	get LAS blob refresh interval between console and NS
	'''
	@property
	def console_ns_refresh(self) :
		try:
			return self._console_ns_refresh
		except Exception as e :
			raise e
	'''
	set LAS blob refresh interval between console and NS
	'''
	@console_ns_refresh.setter
	def console_ns_refresh(self,console_ns_refresh):
		try :
			if not isinstance(console_ns_refresh,int):
				raise TypeError("console_ns_refresh must be set to int value")
			self._console_ns_refresh = console_ns_refresh
		except Exception as e :
			raise e

	'''
	Use this operation to get LAS signed identity.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				cc_las_poll_interval_obj=cc_las_poll_interval()
				response = cc_las_poll_interval_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cc_las_poll_interval resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cc_las_poll_interval_obj = cc_las_poll_interval()
			option_ = options()
			option_._filter=filter_
			return cc_las_poll_interval_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cc_las_poll_interval resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cc_las_poll_interval_obj = cc_las_poll_interval()
			option_ = options()
			option_._count=True
			response = cc_las_poll_interval_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cc_las_poll_interval resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cc_las_poll_interval_obj = cc_las_poll_interval()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cc_las_poll_interval_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cc_las_poll_interval_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cc_las_poll_interval
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cc_las_poll_interval_responses, response, "cc_las_poll_interval_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cc_las_poll_interval_response_array
				i=0
				error = [cc_las_poll_interval() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cc_las_poll_interval_response_array
			i=0
			cc_las_poll_interval_objs = [cc_las_poll_interval() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cc_las_poll_interval'):
					for props in obj._cc_las_poll_interval:
						result = service.payload_formatter.string_to_bulk_resource(cc_las_poll_interval_response,self.__class__.__name__,props)
						cc_las_poll_interval_objs[i] = result.cc_las_poll_interval
						i=i+1
			return cc_las_poll_interval_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cc_las_poll_interval,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cc_las_poll_interval_response(base_response):
	def __init__(self,length=1) :
		self.cc_las_poll_interval= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cc_las_poll_interval= [ cc_las_poll_interval() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cc_las_poll_interval_responses(base_response):
	def __init__(self,length=1) :
		self.cc_las_poll_interval_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cc_las_poll_interval_response_array = [ cc_las_poll_interval() for _ in range(length)]
