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
from massrc.com.citrix.mas.nitro.resource.config.mps.variable_values import variable_values
from massrc.com.citrix.mas.nitro.resource.config.mps.config_variable import config_variable
from massrc.com.citrix.mas.nitro.resource.config.mps.configuration_template import configuration_template
from massrc.com.citrix.mas.nitro.resource.config.mps.config_command import config_command


'''
Configuration for Configuration Template Temporary file resource
'''

class config_template_temp(base_resource):
	_device_family= ""
	_variable_vals=[]
	_name= ""
	_ip_address= ""
	_variables=[]
	_duration= ""
	_template_info= ""
	_id= ""
	_commands=[]
	_description= ""
	_end_time= ""
	_commands_str= ""
	_templates=[]
	_file_location_path= ""
	_file_name= ""
	_template_file= ""
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
			return "config_template_temp"
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
			return "config_template_temp"
		except Exception as e :
			raise e



	'''
	get Family (ns/sdx) of Devices for which config template is defined.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family (ns/sdx) of Devices for which config template is defined.
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Values of Variables used in commands of the configuration template
	'''
	@property
	def variable_vals(self) :
		try:
			return self._variable_vals
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the configuration template
	'''
	@variable_vals.setter
	def variable_vals(self,variable_vals) :
		try :
			if not isinstance(variable_vals,list):
				raise TypeError("variable_vals must be set to array of variable_values value")
			for item in variable_vals :
				if not isinstance(item,variable_values):
					raise TypeError("item must be set to variable_values value")
			self._variable_vals = variable_vals
		except Exception as e :
			raise e


	'''
	get Name of config template based on action
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of config template based on action
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get IP Address for which configuration temaplte generated/requested
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for which configuration temaplte generated/requested
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Array of variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Array of variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of config_variable value")
			for item in variables :
				if not isinstance(item,config_variable):
					raise TypeError("item must be set to config_variable value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get Duration today/last_1_day/last_1_week/current_month/last_1_month of Interval for which configuration changes are recorded
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Duration today/last_1_day/last_1_week/current_month/last_1_month of Interval for which configuration changes are recorded
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Configuration Template to be executed/scheduled
	'''
	@property
	def template_info(self) :
		try:
			return self._template_info
		except Exception as e :
			raise e
	'''
	set Configuration Template to be executed/scheduled
	'''
	@template_info.setter
	def template_info(self,template_info):
		try :
			if not isinstance(template_info,configuration_template):
				raise TypeError("template_info must be set to configuration_template value")
			self._template_info = template_info
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the configuration templates
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the configuration templates
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
	get Array of commands part of the configuration template
	'''
	@property
	def commands(self) :
		try:
			return self._commands
		except Exception as e :
			raise e
	'''
	set Array of commands part of the configuration template
	'''
	@commands.setter
	def commands(self,commands) :
		try :
			if not isinstance(commands,list):
				raise TypeError("commands must be set to array of config_command value")
			for item in commands :
				if not isinstance(item,config_command):
					raise TypeError("item must be set to config_command value")
			self._commands = commands
		except Exception as e :
			raise e


	'''
	get Description of config template
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of config template
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
	get End Time of Interval for which configuration changes are recorded
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set End Time of Interval for which configuration changes are recorded
	'''
	@end_time.setter
	def end_time(self,end_time):
		try :
			if not isinstance(end_time,float):
				raise TypeError("end_time must be set to float value")
			self._end_time = end_time
		except Exception as e :
			raise e


	'''
	get Configuration Template Commands separated by new line character
	'''
	@property
	def commands_str(self) :
		try:
			return self._commands_str
		except Exception as e :
			raise e
	'''
	set Configuration Template Commands separated by new line character
	'''
	@commands_str.setter
	def commands_str(self,commands_str):
		try :
			if not isinstance(commands_str,str):
				raise TypeError("commands_str must be set to str value")
			self._commands_str = commands_str
		except Exception as e :
			raise e

	'''
	Templates List that are to be imported
	'''
	@property
	def templates(self) :
		try:
			return self._templates
		except Exception as e :
			raise e
	'''
	Templates List that are to be imported
	'''
	@templates.setter
	def templates(self,templates) :
		try :
			if not isinstance(templates,list):
				raise TypeError("templates must be set to array of str value")
			for item in templates :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._templates = templates
		except Exception as e :
			raise e

	'''
	File Location on Client for upload/download
	'''
	@property
	def file_location_path(self):
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e

	'''
	File Name
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	Template File that is to be imported
	'''
	@property
	def template_file(self):
		try:
			return self._template_file
		except Exception as e :
			raise e
	'''
	Template File that is to be imported
	'''
	@template_file.setter
	def template_file(self,template_file):
		try :
			if not isinstance(template_file,str):
				raise TypeError("template_file must be set to str value")
			self._template_file = template_file
		except Exception as e :
			raise e

	'''
	Use this operation to upload pre upgrade script file.
	'''

	'''
	Use this operation to upload pre upgrade script file.
	'''
	@classmethod
	def import_pre_upgrade_script_file(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"import_pre_upgrade_script_file")
			else : 
				config_template_temp_obj= config_template_temp()
				return cls.perform_operation_bulk_request(service,"import_pre_upgrade_script_file", resource,config_template_temp_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload config file.
	'''

	'''
	Use this operation to upload config file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to add configuration template.
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
				config_template_temp_obj= config_template_temp()
				return cls.perform_operation_bulk_request(service,resource,config_template_temp_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete config file.
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
					config_template_temp_obj=config_template_temp()
					return cls.delete_bulk_request(client,resource,config_template_temp_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download config file.
	'''

	'''
	Use this operation to download config file.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to upload post upgrade script file.
	'''

	'''
	Use this operation to upload post upgrade script file.
	'''
	@classmethod
	def import_post_upgrade_script_file(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"import_post_upgrade_script_file")
			else : 
				config_template_temp_obj= config_template_temp()
				return cls.perform_operation_bulk_request(service,"import_post_upgrade_script_file", resource,config_template_temp_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get configuration templates.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				config_template_temp_obj=config_template_temp()
				response = config_template_temp_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to upload post upgrade pre failover script file.
	'''

	'''
	Use this operation to upload post upgrade pre failover script file.
	'''
	@classmethod
	def import_post_upgrade_pre_failover_script_file(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"import_post_upgrade_pre_failover_script_file")
			else : 
				config_template_temp_obj= config_template_temp()
				return cls.perform_operation_bulk_request(service,"import_post_upgrade_pre_failover_script_file", resource,config_template_temp_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of config_template_temp resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			config_template_temp_obj = config_template_temp()
			option_ = options()
			option_._filter=filter_
			return config_template_temp_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the config_template_temp resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			config_template_temp_obj = config_template_temp()
			option_ = options()
			option_._count=True
			response = config_template_temp_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of config_template_temp resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			config_template_temp_obj = config_template_temp()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = config_template_temp_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(config_template_temp_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_template_temp
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_template_temp_responses, response, "config_template_temp_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_template_temp_response_array
				i=0
				error = [config_template_temp() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_template_temp_response_array
			i=0
			config_template_temp_objs = [config_template_temp() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_template_temp'):
					for props in obj._config_template_temp:
						result = service.payload_formatter.string_to_bulk_resource(config_template_temp_response,self.__class__.__name__,props)
						config_template_temp_objs[i] = result.config_template_temp
						i=i+1
			return config_template_temp_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_template_temp,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_template_temp_response(base_response):
	def __init__(self,length=1) :
		self.config_template_temp= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_template_temp= [ config_template_temp() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_template_temp_responses(base_response):
	def __init__(self,length=1) :
		self.config_template_temp_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_template_temp_response_array = [ config_template_temp() for _ in range(length)]
