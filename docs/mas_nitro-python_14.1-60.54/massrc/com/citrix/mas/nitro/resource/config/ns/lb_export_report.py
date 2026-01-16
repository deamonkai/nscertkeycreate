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
Configuration for Export or Schedule NetScaler Entities report resource
'''

class lb_export_report(base_resource):
	_enable_sslvpn= ""
	_recurrence_times_epoch= ""
	_enable_auth= ""
	_recurrence_type= ""
	_enable_cr= ""
	_export_now= ""
	_enable_gslb= ""
	_file_name= ""
	_mail_profile= ""
	_slack_profile= ""
	_enable_lb= ""
	_is_enabled= ""
	_enable_cs= ""
	_recurrence_options= ""
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
			return "lb_export_report"
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
			return "lb_export_reports"
		except Exception as e :
			raise e



	'''
	get Enable SSLVPN Report
	'''
	@property
	def enable_sslvpn(self) :
		try:
			return self._enable_sslvpn
		except Exception as e :
			raise e
	'''
	set Enable SSLVPN Report
	'''
	@enable_sslvpn.setter
	def enable_sslvpn(self,enable_sslvpn):
		try :
			if not isinstance(enable_sslvpn,bool):
				raise TypeError("enable_sslvpn must be set to bool value")
			self._enable_sslvpn = enable_sslvpn
		except Exception as e :
			raise e


	'''
	get Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def recurrence_times_epoch(self) :
		try:
			return self._recurrence_times_epoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch (string representation of 11 digit numbers).
	'''
	@recurrence_times_epoch.setter
	def recurrence_times_epoch(self,recurrence_times_epoch):
		try :
			if not isinstance(recurrence_times_epoch,str):
				raise TypeError("recurrence_times_epoch must be set to str value")
			self._recurrence_times_epoch = recurrence_times_epoch
		except Exception as e :
			raise e


	'''
	get Enable Auth Report
	'''
	@property
	def enable_auth(self) :
		try:
			return self._enable_auth
		except Exception as e :
			raise e
	'''
	set Enable Auth Report
	'''
	@enable_auth.setter
	def enable_auth(self,enable_auth):
		try :
			if not isinstance(enable_auth,bool):
				raise TypeError("enable_auth must be set to bool value")
			self._enable_auth = enable_auth
		except Exception as e :
			raise e


	'''
	get Tenant recurrence type
	'''
	@property
	def recurrence_type(self) :
		try:
			return self._recurrence_type
		except Exception as e :
			raise e
	'''
	set Tenant recurrence type
	'''
	@recurrence_type.setter
	def recurrence_type(self,recurrence_type):
		try :
			if not isinstance(recurrence_type,str):
				raise TypeError("recurrence_type must be set to str value")
			self._recurrence_type = recurrence_type
		except Exception as e :
			raise e


	'''
	get Enable CR Report
	'''
	@property
	def enable_cr(self) :
		try:
			return self._enable_cr
		except Exception as e :
			raise e
	'''
	set Enable CR Report
	'''
	@enable_cr.setter
	def enable_cr(self,enable_cr):
		try :
			if not isinstance(enable_cr,bool):
				raise TypeError("enable_cr must be set to bool value")
			self._enable_cr = enable_cr
		except Exception as e :
			raise e


	'''
	get Load Balancing Export Now
	'''
	@property
	def export_now(self) :
		try:
			return self._export_now
		except Exception as e :
			raise e
	'''
	set Load Balancing Export Now
	'''
	@export_now.setter
	def export_now(self,export_now):
		try :
			if not isinstance(export_now,bool):
				raise TypeError("export_now must be set to bool value")
			self._export_now = export_now
		except Exception as e :
			raise e


	'''
	get Enable GSLB Report
	'''
	@property
	def enable_gslb(self) :
		try:
			return self._enable_gslb
		except Exception as e :
			raise e
	'''
	set Enable GSLB Report
	'''
	@enable_gslb.setter
	def enable_gslb(self,enable_gslb):
		try :
			if not isinstance(enable_gslb,bool):
				raise TypeError("enable_gslb must be set to bool value")
			self._enable_gslb = enable_gslb
		except Exception as e :
			raise e


	'''
	get Export Report File name.
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Export Report File name.
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
	get Mail Profile
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail Profile
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
	get Slack Profile Name
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack Profile Name
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
	get Enable LB Report
	'''
	@property
	def enable_lb(self) :
		try:
			return self._enable_lb
		except Exception as e :
			raise e
	'''
	set Enable LB Report
	'''
	@enable_lb.setter
	def enable_lb(self,enable_lb):
		try :
			if not isinstance(enable_lb,bool):
				raise TypeError("enable_lb must be set to bool value")
			self._enable_lb = enable_lb
		except Exception as e :
			raise e


	'''
	get Enable Scheduled Report (default is enabled)
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set Enable Scheduled Report (default is enabled)
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get Enable CS Report
	'''
	@property
	def enable_cs(self) :
		try:
			return self._enable_cs
		except Exception as e :
			raise e
	'''
	set Enable CS Report
	'''
	@enable_cs.setter
	def enable_cs(self,enable_cs):
		try :
			if not isinstance(enable_cs,bool):
				raise TypeError("enable_cs must be set to bool value")
			self._enable_cs = enable_cs
		except Exception as e :
			raise e


	'''
	get Comma separated recurrence options of job that is scheduled
	'''
	@property
	def recurrence_options(self) :
		try:
			return self._recurrence_options
		except Exception as e :
			raise e
	'''
	set Comma separated recurrence options of job that is scheduled
	'''
	@recurrence_options.setter
	def recurrence_options(self,recurrence_options):
		try :
			if not isinstance(recurrence_options,str):
				raise TypeError("recurrence_options must be set to str value")
			self._recurrence_options = recurrence_options
		except Exception as e :
			raise e

	'''
	Use this operation to set the schedule config.
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
				lb_export_report_obj=lb_export_report()
				return cls.update_bulk_request(client,resource,lb_export_report_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to export report.
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
				lb_export_report_obj= lb_export_report()
				return cls.perform_operation_bulk_request(service,resource,lb_export_report_obj)
		except Exception as e :
			raise e

	'''
	get export schedule configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				lb_export_report_obj=lb_export_report()
				response = lb_export_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of lb_export_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			lb_export_report_obj = lb_export_report()
			option_ = options()
			option_._filter=filter_
			return lb_export_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the lb_export_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			lb_export_report_obj = lb_export_report()
			option_ = options()
			option_._count=True
			response = lb_export_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of lb_export_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			lb_export_report_obj = lb_export_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = lb_export_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(lb_export_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lb_export_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(lb_export_report_responses, response, "lb_export_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.lb_export_report_response_array
				i=0
				error = [lb_export_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.lb_export_report_response_array
			i=0
			lb_export_report_objs = [lb_export_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_lb_export_report'):
					for props in obj._lb_export_report:
						result = service.payload_formatter.string_to_bulk_resource(lb_export_report_response,self.__class__.__name__,props)
						lb_export_report_objs[i] = result.lb_export_report
						i=i+1
			return lb_export_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(lb_export_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class lb_export_report_response(base_response):
	def __init__(self,length=1) :
		self.lb_export_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.lb_export_report= [ lb_export_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class lb_export_report_responses(base_response):
	def __init__(self,length=1) :
		self.lb_export_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.lb_export_report_response_array = [ lb_export_report() for _ in range(length)]
