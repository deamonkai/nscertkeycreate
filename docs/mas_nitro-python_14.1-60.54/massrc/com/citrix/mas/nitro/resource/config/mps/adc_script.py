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
from massrc.com.citrix.mas.nitro.resource.config.mps.adc_script_output_file import adc_script_output_file
from massrc.com.citrix.mas.nitro.resource.config.mps.adc_script_stats import adc_script_stats


'''
Configuration for adc script running resource
'''

class adc_script(base_resource):
	_output_files=[]
	_adc_id= ""
	_status= ""
	_command= ""
	_exit_code= ""
	_filename= ""
	_timeout= ""
	_output_file_paths=[]
	_stats= ""
	_id= ""
	_report_id= ""
	_script_directory= ""
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
			return "adc_script"
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
			return "adc_scripts"
		except Exception as e :
			raise e


	'''
	Array of output files
	'''
	@property
	def output_files(self) :
		try:
			return self._output_files
		except Exception as e :
			raise e
	'''
	Array of output files
	'''
	@output_files.setter
	def output_files(self,output_files) :
		try :
			if not isinstance(output_files,list):
				raise TypeError("output_files must be set to array of adc_script_output_file value")
			for item in output_files :
				if not isinstance(item,adc_script_output_file):
					raise TypeError("item must be set to adc_script_output_file value")
			self._output_files = output_files
		except Exception as e :
			raise e

	'''
	adc id
	'''
	@property
	def adc_id(self):
		try:
			return self._adc_id
		except Exception as e :
			raise e
	'''
	adc id
	'''
	@adc_id.setter
	def adc_id(self,adc_id):
		try :
			if not isinstance(adc_id,str):
				raise TypeError("adc_id must be set to str value")
			self._adc_id = adc_id
		except Exception as e :
			raise e

	'''
	status of the current adc script
	'''
	@property
	def status(self):
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	status of the current adc script
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
	command
	'''
	@property
	def command(self):
		try:
			return self._command
		except Exception as e :
			raise e
	'''
	command
	'''
	@command.setter
	def command(self,command):
		try :
			if not isinstance(command,str):
				raise TypeError("command must be set to str value")
			self._command = command
		except Exception as e :
			raise e

	'''
	exit code
	'''
	@property
	def exit_code(self):
		try:
			return self._exit_code
		except Exception as e :
			raise e
	'''
	exit code
	'''
	@exit_code.setter
	def exit_code(self,exit_code):
		try :
			if not isinstance(exit_code,str):
				raise TypeError("exit_code must be set to str value")
			self._exit_code = exit_code
		except Exception as e :
			raise e

	'''
	file name
	'''
	@property
	def filename(self):
		try:
			return self._filename
		except Exception as e :
			raise e
	'''
	file name
	'''
	@filename.setter
	def filename(self,filename):
		try :
			if not isinstance(filename,str):
				raise TypeError("filename must be set to str value")
			self._filename = filename
		except Exception as e :
			raise e

	'''
	timeout
	'''
	@property
	def timeout(self):
		try:
			return self._timeout
		except Exception as e :
			raise e
	'''
	timeout
	'''
	@timeout.setter
	def timeout(self,timeout):
		try :
			if not isinstance(timeout,int):
				raise TypeError("timeout must be set to int value")
			self._timeout = timeout
		except Exception as e :
			raise e

	'''
	Array of output files
	'''
	@property
	def output_file_paths(self) :
		try:
			return self._output_file_paths
		except Exception as e :
			raise e
	'''
	Array of output files
	'''
	@output_file_paths.setter
	def output_file_paths(self,output_file_paths) :
		try :
			if not isinstance(output_file_paths,list):
				raise TypeError("output_file_paths must be set to array of str value")
			for item in output_file_paths :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._output_file_paths = output_file_paths
		except Exception as e :
			raise e

	'''
	Array of stats
	'''
	@property
	def stats(self):
		try:
			return self._stats
		except Exception as e :
			raise e
	'''
	Array of stats
	'''
	@stats.setter
	def stats(self,stats):
		try :
			if not isinstance(stats,adc_script_stats):
				raise TypeError("stats must be set to adc_script_stats value")
			self._stats = stats
		except Exception as e :
			raise e

	'''
	adc script id
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	adc script id
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
	report id
	'''
	@property
	def report_id(self):
		try:
			return self._report_id
		except Exception as e :
			raise e
	'''
	report id
	'''
	@report_id.setter
	def report_id(self,report_id):
		try :
			if not isinstance(report_id,str):
				raise TypeError("report_id must be set to str value")
			self._report_id = report_id
		except Exception as e :
			raise e

	'''
	script directory
	'''
	@property
	def script_directory(self):
		try:
			return self._script_directory
		except Exception as e :
			raise e
	'''
	script directory
	'''
	@script_directory.setter
	def script_directory(self,script_directory):
		try :
			if not isinstance(script_directory,str):
				raise TypeError("script_directory must be set to str value")
			self._script_directory = script_directory
		except Exception as e :
			raise e

	'''
	Use this operation to run the script.
	'''
	@classmethod
	def run(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"run")
				return res
			else : 
				adc_script_obj= adc_script()
				return cls.perform_operation_bulk_request(service,"run",resource,adc_script_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get managed devices.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_script_obj=adc_script()
				response = adc_script_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_script resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_script_obj = adc_script()
			option_ = options()
			option_._filter=filter_
			return adc_script_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_script resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_script_obj = adc_script()
			option_ = options()
			option_._count=True
			response = adc_script_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_script resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_script_obj = adc_script()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_script_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_script_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_script
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_script_responses, response, "adc_script_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_script_response_array
				i=0
				error = [adc_script() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_script_response_array
			i=0
			adc_script_objs = [adc_script() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_script'):
					for props in obj._adc_script:
						result = service.payload_formatter.string_to_bulk_resource(adc_script_response,self.__class__.__name__,props)
						adc_script_objs[i] = result.adc_script
						i=i+1
			return adc_script_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_script,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_script_response(base_response):
	def __init__(self,length=1) :
		self.adc_script= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_script= [ adc_script() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_script_responses(base_response):
	def __init__(self,length=1) :
		self.adc_script_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_script_response_array = [ adc_script() for _ in range(length)]
