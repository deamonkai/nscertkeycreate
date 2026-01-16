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
Configuration for Device Score Threshold Notification resource
'''

class instance_score_notification(base_resource):
	_mail_profile= ""
	_servicenow_profile= ""
	_sms_profile= ""
	_is_enabled= ""
	_pagerduty_profile= ""
	_id= ""
	_slack_profile= ""
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
			return "instance_score_notification"
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
			return "instance_score_notifications"
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
	get ServiceNow Profile
	'''
	@property
	def servicenow_profile(self) :
		try:
			return self._servicenow_profile
		except Exception as e :
			raise e
	'''
	set ServiceNow Profile
	'''
	@servicenow_profile.setter
	def servicenow_profile(self,servicenow_profile):
		try :
			if not isinstance(servicenow_profile,str):
				raise TypeError("servicenow_profile must be set to str value")
			self._servicenow_profile = servicenow_profile
		except Exception as e :
			raise e


	'''
	get SMS Profile
	'''
	@property
	def sms_profile(self) :
		try:
			return self._sms_profile
		except Exception as e :
			raise e
	'''
	set SMS Profile
	'''
	@sms_profile.setter
	def sms_profile(self,sms_profile):
		try :
			if not isinstance(sms_profile,str):
				raise TypeError("sms_profile must be set to str value")
			self._sms_profile = sms_profile
		except Exception as e :
			raise e


	'''
	get Notificaiton enabled or disabled
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set Notificaiton enabled or disabled
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
	get PagerDuty Profile
	'''
	@property
	def pagerduty_profile(self) :
		try:
			return self._pagerduty_profile
		except Exception as e :
			raise e
	'''
	set PagerDuty Profile
	'''
	@pagerduty_profile.setter
	def pagerduty_profile(self,pagerduty_profile):
		try :
			if not isinstance(pagerduty_profile,str):
				raise TypeError("pagerduty_profile must be set to str value")
			self._pagerduty_profile = pagerduty_profile
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the instance score thresholds notification
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the instance score thresholds notification
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
	get Slack Profile
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack Profile
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
	get instance score threshold notification.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				instance_score_notification_obj=instance_score_notification()
				response = instance_score_notification_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify instance score threshold notification.
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
				instance_score_notification_obj=instance_score_notification()
				return cls.update_bulk_request(client,resource,instance_score_notification_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of instance_score_notification resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			instance_score_notification_obj = instance_score_notification()
			option_ = options()
			option_._filter=filter_
			return instance_score_notification_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the instance_score_notification resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			instance_score_notification_obj = instance_score_notification()
			option_ = options()
			option_._count=True
			response = instance_score_notification_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of instance_score_notification resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			instance_score_notification_obj = instance_score_notification()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = instance_score_notification_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(instance_score_notification_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.instance_score_notification
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(instance_score_notification_responses, response, "instance_score_notification_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.instance_score_notification_response_array
				i=0
				error = [instance_score_notification() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.instance_score_notification_response_array
			i=0
			instance_score_notification_objs = [instance_score_notification() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_instance_score_notification'):
					for props in obj._instance_score_notification:
						result = service.payload_formatter.string_to_bulk_resource(instance_score_notification_response,self.__class__.__name__,props)
						instance_score_notification_objs[i] = result.instance_score_notification
						i=i+1
			return instance_score_notification_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(instance_score_notification,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class instance_score_notification_response(base_response):
	def __init__(self,length=1) :
		self.instance_score_notification= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.instance_score_notification= [ instance_score_notification() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class instance_score_notification_responses(base_response):
	def __init__(self,length=1) :
		self.instance_score_notification_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.instance_score_notification_response_array = [ instance_score_notification() for _ in range(length)]
