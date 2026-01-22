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
Configuration for adc script stats resource
'''

class adc_script_stats(base_resource):
	_time= ""
	_mem= ""
	_cpu= ""
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
			return "adc_script_stats"
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
			return "adc_script_statss"
		except Exception as e :
			raise e


	'''
	time
	'''
	@property
	def time(self):
		try:
			return self._time
		except Exception as e :
			raise e
	'''
	time
	'''
	@time.setter
	def time(self,time):
		try :
			if not isinstance(time,str):
				raise TypeError("time must be set to str value")
			self._time = time
		except Exception as e :
			raise e

	'''
	mem
	'''
	@property
	def mem(self):
		try:
			return self._mem
		except Exception as e :
			raise e
	'''
	mem
	'''
	@mem.setter
	def mem(self,mem):
		try :
			if not isinstance(mem,str):
				raise TypeError("mem must be set to str value")
			self._mem = mem
		except Exception as e :
			raise e

	'''
	cpu
	'''
	@property
	def cpu(self):
		try:
			return self._cpu
		except Exception as e :
			raise e
	'''
	cpu
	'''
	@cpu.setter
	def cpu(self,cpu):
		try :
			if not isinstance(cpu,str):
				raise TypeError("cpu must be set to str value")
			self._cpu = cpu
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_script_stats_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_script_stats
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_script_stats_responses, response, "adc_script_stats_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_script_stats_response_array
				i=0
				error = [adc_script_stats() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_script_stats_response_array
			i=0
			adc_script_stats_objs = [adc_script_stats() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_script_stats'):
					for props in obj._adc_script_stats:
						result = service.payload_formatter.string_to_bulk_resource(adc_script_stats_response,self.__class__.__name__,props)
						adc_script_stats_objs[i] = result.adc_script_stats
						i=i+1
			return adc_script_stats_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_script_stats,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_script_stats_response(base_response):
	def __init__(self,length=1) :
		self.adc_script_stats= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_script_stats= [ adc_script_stats() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_script_stats_responses(base_response):
	def __init__(self,length=1) :
		self.adc_script_stats_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_script_stats_response_array = [ adc_script_stats() for _ in range(length)]
