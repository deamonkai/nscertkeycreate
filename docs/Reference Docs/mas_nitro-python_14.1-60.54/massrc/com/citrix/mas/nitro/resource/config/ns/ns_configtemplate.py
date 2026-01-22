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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_configtemplate_scheduler import ns_configtemplate_scheduler
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_command import ns_command


'''
Configuration for NetScaler configuration template resource
'''

class ns_configtemplate(base_resource):
	_name= ""
	_send_report_only_when_diff= ""
	_variable_vals=[]
	_mail_profile= ""
	_id= ""
	_last_updated_time= ""
	_variables=[]
	_isDefaultSchedule= ""
	_slack_profile= ""
	_ns_configtemplate_create_user= ""
	_scheduleDetail= ""
	_mail_export= ""
	_device_groups_db= ""
	_slack_export= ""
	_description= ""
	_tenant_id= ""
	_scheduleInfo= ""
	_to_be_exported= ""
	_template_create_user= ""
	_commands=[]
	_ignoresysuserpassword= ""
	_template_file= ""
	_device_groups=[]
	_devices=[]
	_preview_commands=[]
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
			return "ns_configtemplate"
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
			return "ns_configtemplates"
		except Exception as e :
			raise e



	'''
	get Name of the configuration template
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the configuration template
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
	get Send notification report only when there is a diff
	'''
	@property
	def send_report_only_when_diff(self) :
		try:
			return self._send_report_only_when_diff
		except Exception as e :
			raise e
	'''
	set Send notification report only when there is a diff
	'''
	@send_report_only_when_diff.setter
	def send_report_only_when_diff(self,send_report_only_when_diff):
		try :
			if not isinstance(send_report_only_when_diff,bool):
				raise TypeError("send_report_only_when_diff must be set to bool value")
			self._send_report_only_when_diff = send_report_only_when_diff
		except Exception as e :
			raise e


	'''
	get Values of Variables used in commands of the audit template
	'''
	@property
	def variable_vals(self) :
		try:
			return self._variable_vals
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the audit template
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
	get Mail profile name to send notification mail.
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail profile name to send notification mail.
	'''
	@mail_profile.setter
	def mail_profile(self,mail_profile):
		try :
			if not isinstance(mail_profile,str):
				raise TypeError("mail_profile must be set to str value")
			self._mail_profile = mail_profile
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system users
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system users
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
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
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
	get Scheduled specification for template or default polling interval
	'''
	@property
	def isDefaultSchedule(self) :
		try:
			return self._isDefaultSchedule
		except Exception as e :
			raise e
	'''
	set Scheduled specification for template or default polling interval
	'''
	@isDefaultSchedule.setter
	def isDefaultSchedule(self,isDefaultSchedule):
		try :
			if not isinstance(isDefaultSchedule,bool):
				raise TypeError("isDefaultSchedule must be set to bool value")
			self._isDefaultSchedule = isDefaultSchedule
		except Exception as e :
			raise e


	'''
	get Slack profile name to send slack notification.
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack profile name to send slack notification.
	'''
	@slack_profile.setter
	def slack_profile(self,slack_profile):
		try :
			if not isinstance(slack_profile,str):
				raise TypeError("slack_profile must be set to str value")
			self._slack_profile = slack_profile
		except Exception as e :
			raise e


	'''
	get User who created the template
	'''
	@property
	def ns_configtemplate_create_user(self) :
		try:
			return self._ns_configtemplate_create_user
		except Exception as e :
			raise e


	'''
	get Schedule Detail
	'''
	@property
	def scheduleDetail(self) :
		try:
			return self._scheduleDetail
		except Exception as e :
			raise e


	'''
	get Setting for enabling/disabling config audit diff report for mail export
	'''
	@property
	def mail_export(self) :
		try:
			return self._mail_export
		except Exception as e :
			raise e
	'''
	set Setting for enabling/disabling config audit diff report for mail export
	'''
	@mail_export.setter
	def mail_export(self,mail_export):
		try :
			if not isinstance(mail_export,bool):
				raise TypeError("mail_export must be set to bool value")
			self._mail_export = mail_export
		except Exception as e :
			raise e


	'''
	get Device Groups List Comma separated to store in DB
	'''
	@property
	def device_groups_db(self) :
		try:
			return self._device_groups_db
		except Exception as e :
			raise e
	'''
	set Device Groups List Comma separated to store in DB
	'''
	@device_groups_db.setter
	def device_groups_db(self,device_groups_db):
		try :
			if not isinstance(device_groups_db,str):
				raise TypeError("device_groups_db must be set to str value")
			self._device_groups_db = device_groups_db
		except Exception as e :
			raise e


	'''
	get Setting for enabling/disabling config audit diff report for slack export
	'''
	@property
	def slack_export(self) :
		try:
			return self._slack_export
		except Exception as e :
			raise e
	'''
	set Setting for enabling/disabling config audit diff report for slack export
	'''
	@slack_export.setter
	def slack_export(self,slack_export):
		try :
			if not isinstance(slack_export,bool):
				raise TypeError("slack_export must be set to bool value")
			self._slack_export = slack_export
		except Exception as e :
			raise e


	'''
	get Template Description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Template Description
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
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Scheduling information for audit template
	'''
	@property
	def scheduleInfo(self) :
		try:
			return self._scheduleInfo
		except Exception as e :
			raise e
	'''
	set Scheduling information for audit template
	'''
	@scheduleInfo.setter
	def scheduleInfo(self,scheduleInfo):
		try :
			if not isinstance(scheduleInfo,ns_configtemplate_scheduler):
				raise TypeError("scheduleInfo must be set to ns_configtemplate_scheduler value")
			self._scheduleInfo = scheduleInfo
		except Exception as e :
			raise e


	'''
	get Setting for enabling/disabling config audit diff report
	'''
	@property
	def to_be_exported(self) :
		try:
			return self._to_be_exported
		except Exception as e :
			raise e
	'''
	set Setting for enabling/disabling config audit diff report
	'''
	@to_be_exported.setter
	def to_be_exported(self,to_be_exported):
		try :
			if not isinstance(to_be_exported,bool):
				raise TypeError("to_be_exported must be set to bool value")
			self._to_be_exported = to_be_exported
		except Exception as e :
			raise e


	'''
	get User who created the template
	'''
	@property
	def template_create_user(self) :
		try:
			return self._template_create_user
		except Exception as e :
			raise e


	'''
	get NetScaler Configuration Commands
	'''
	@property
	def commands(self) :
		try:
			return self._commands
		except Exception as e :
			raise e
	'''
	set NetScaler Configuration Commands
	'''
	@commands.setter
	def commands(self,commands) :
		try :
			if not isinstance(commands,list):
				raise TypeError("commands must be set to array of ns_command value")
			for item in commands :
				if not isinstance(item,ns_command):
					raise TypeError("item must be set to ns_command value")
			self._commands = commands
		except Exception as e :
			raise e


	'''
	get When set to true, ignores password difference in diff command output
	'''
	@property
	def ignoresysuserpassword(self) :
		try:
			return self._ignoresysuserpassword
		except Exception as e :
			raise e
	'''
	set When set to true, ignores password difference in diff command output
	'''
	@ignoresysuserpassword.setter
	def ignoresysuserpassword(self,ignoresysuserpassword):
		try :
			if not isinstance(ignoresysuserpassword,bool):
				raise TypeError("ignoresysuserpassword must be set to bool value")
			self._ignoresysuserpassword = ignoresysuserpassword
		except Exception as e :
			raise e


	'''
	get CSV file for importing variables
	'''
	@property
	def template_file(self) :
		try:
			return self._template_file
		except Exception as e :
			raise e
	'''
	set CSV file for importing variables
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
	Device Group Array for which audit template is added
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	Device Group Array for which audit template is added
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e

	'''
	List of NetScaler IP Address
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	List of NetScaler IP Address
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e

	'''
	Preview of list of commands
	'''
	@property
	def preview_commands(self) :
		try:
			return self._preview_commands
		except Exception as e :
			raise e
	'''
	Preview of list of commands
	'''
	@preview_commands.setter
	def preview_commands(self,preview_commands) :
		try :
			if not isinstance(preview_commands,list):
				raise TypeError("preview_commands must be set to array of str value")
			for item in preview_commands :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._preview_commands = preview_commands
		except Exception as e :
			raise e

	'''
	Use this operation to preview.
	'''
	@classmethod
	def preview(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"preview")
				return res
			else : 
				ns_configtemplate_obj= ns_configtemplate()
				return cls.perform_operation_bulk_request(service,"preview",resource,ns_configtemplate_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to import variables file.
	'''
	@classmethod
	def import_variables_file(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"import_variables_file")
				return res
			else : 
				ns_configtemplate_obj= ns_configtemplate()
				return cls.perform_operation_bulk_request(service,"import_variables_file",resource,ns_configtemplate_obj)
		except Exception as e :
			raise e

	'''
	Get NetScaler configuration templates.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_configtemplate_obj=ns_configtemplate()
				response = ns_configtemplate_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add NetScaler configuration template.
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
				ns_configtemplate_obj= ns_configtemplate()
				return cls.perform_operation_bulk_request(service,resource,ns_configtemplate_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler configuration template.
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
				ns_configtemplate_obj=ns_configtemplate()
				return cls.update_bulk_request(client,resource,ns_configtemplate_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete NetScaler configuration template.
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
					ns_configtemplate_obj=ns_configtemplate()
					return cls.delete_bulk_request(client,resource,ns_configtemplate_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_configtemplate resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_configtemplate_obj = ns_configtemplate()
			option_ = options()
			option_._filter=filter_
			return ns_configtemplate_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_configtemplate resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_configtemplate_obj = ns_configtemplate()
			option_ = options()
			option_._count=True
			response = ns_configtemplate_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_configtemplate resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_configtemplate_obj = ns_configtemplate()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_configtemplate_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_configtemplate_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_configtemplate
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_configtemplate_responses, response, "ns_configtemplate_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_configtemplate_response_array
				i=0
				error = [ns_configtemplate() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_configtemplate_response_array
			i=0
			ns_configtemplate_objs = [ns_configtemplate() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_configtemplate'):
					for props in obj._ns_configtemplate:
						result = service.payload_formatter.string_to_bulk_resource(ns_configtemplate_response,self.__class__.__name__,props)
						ns_configtemplate_objs[i] = result.ns_configtemplate
						i=i+1
			return ns_configtemplate_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_configtemplate,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_configtemplate_response(base_response):
	def __init__(self,length=1) :
		self.ns_configtemplate= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_configtemplate= [ ns_configtemplate() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_configtemplate_responses(base_response):
	def __init__(self,length=1) :
		self.ns_configtemplate_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_configtemplate_response_array = [ ns_configtemplate() for _ in range(length)]
