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
Configuration for POST Cloud connected Console on-prem to talk to LAS via console service resource
'''

class cc_las_auto_activate(base_resource):
	_request_file= ""
	_output_file= ""
	_apiver= ""
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
			return "cc_las_auto_activate"
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
			return "cc_las_auto_activates"
		except Exception as e :
			raise e


	'''
	request_file
	'''
	@property
	def request_file(self):
		try:
			return self._request_file
		except Exception as e :
			raise e
	'''
	request_file
	'''
	@request_file.setter
	def request_file(self,request_file):
		try :
			if not isinstance(request_file,str):
				raise TypeError("request_file must be set to str value")
			self._request_file = request_file
		except Exception as e :
			raise e

	'''
	output_file
	'''
	@property
	def output_file(self):
		try:
			return self._output_file
		except Exception as e :
			raise e
	'''
	output_file
	'''
	@output_file.setter
	def output_file(self,output_file):
		try :
			if not isinstance(output_file,str):
				raise TypeError("output_file must be set to str value")
			self._output_file = output_file
		except Exception as e :
			raise e

	'''
	apiver
	'''
	@property
	def apiver(self):
		try:
			return self._apiver
		except Exception as e :
			raise e
	'''
	apiver
	'''
	@apiver.setter
	def apiver(self,apiver):
		try :
			if not isinstance(apiver,str):
				raise TypeError("apiver must be set to str value")
			self._apiver = apiver
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cc_las_auto_activate_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cc_las_auto_activate
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cc_las_auto_activate_responses, response, "cc_las_auto_activate_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cc_las_auto_activate_response_array
				i=0
				error = [cc_las_auto_activate() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cc_las_auto_activate_response_array
			i=0
			cc_las_auto_activate_objs = [cc_las_auto_activate() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cc_las_auto_activate'):
					for props in obj._cc_las_auto_activate:
						result = service.payload_formatter.string_to_bulk_resource(cc_las_auto_activate_response,self.__class__.__name__,props)
						cc_las_auto_activate_objs[i] = result.cc_las_auto_activate
						i=i+1
			return cc_las_auto_activate_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cc_las_auto_activate,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cc_las_auto_activate_response(base_response):
	def __init__(self,length=1) :
		self.cc_las_auto_activate= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cc_las_auto_activate= [ cc_las_auto_activate() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cc_las_auto_activate_responses(base_response):
	def __init__(self,length=1) :
		self.cc_las_auto_activate_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cc_las_auto_activate_response_array = [ cc_las_auto_activate() for _ in range(length)]
