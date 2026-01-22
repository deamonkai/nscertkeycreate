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
Configuration for Notify Service resource
'''

class notify_service(base_resource):
	_tenant_name= ""
	_id= ""
	_notification_type= ""
	_severity= ""
	_profile_name= ""
	_email_msg_body= ""
	_pagerduty_msg_body= ""
	_slack_msg_body= ""
	_servicenow_msg_body= ""
	_template_name= ""
	_email_subject= ""
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
			return "notify_service"
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
			return "notify_services"
		except Exception as e :
			raise e



	'''
	get Tenant name for which notification to be sent.
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant name for which notification to be sent.
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	get Notification type - email/slack/service-now/pager-duty
	'''
	@property
	def notification_type(self) :
		try:
			return self._notification_type
		except Exception as e :
			raise e
	'''
	set Notification type - email/slack/service-now/pager-duty
	'''
	@notification_type.setter
	def notification_type(self,notification_type):
		try :
			if not isinstance(notification_type,str):
				raise TypeError("notification_type must be set to str value")
			self._notification_type = notification_type
		except Exception as e :
			raise e


	'''
	get EVENT_SEV_CRITICAL_HEX = #cf3434,EVENT_SEV_MAJOR_HEX = #ff9e47,EVENT_SEV_MINOR_HEX = #b2af45,EVENT_SEV_WARNING_HEX = #ffd71c,EVENT_SEV_CLEAR_HEX = #49bf62,EVENT_SEV_INFORMATION_HEX = #21a9ef,EVENT_SEV_ALERT_HEX= #ffd71c,EVENT_SEV_NOTICE_HEX= #ffd71c,EVENT_SEV_EMERG_HEX = #cf3434,EVENT_SEV_UNKNOWN_HEX = #999999,EVENT_SEV_ERROR_HEX = #cf3434
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set EVENT_SEV_CRITICAL_HEX = #cf3434,EVENT_SEV_MAJOR_HEX = #ff9e47,EVENT_SEV_MINOR_HEX = #b2af45,EVENT_SEV_WARNING_HEX = #ffd71c,EVENT_SEV_CLEAR_HEX = #49bf62,EVENT_SEV_INFORMATION_HEX = #21a9ef,EVENT_SEV_ALERT_HEX= #ffd71c,EVENT_SEV_NOTICE_HEX= #ffd71c,EVENT_SEV_EMERG_HEX = #cf3434,EVENT_SEV_UNKNOWN_HEX = #999999,EVENT_SEV_ERROR_HEX = #cf3434
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,str):
				raise TypeError("severity must be set to str value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Profile name through which notifications will be sent.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name through which notifications will be sent.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get Email notification body
	'''
	@property
	def email_msg_body(self) :
		try:
			return self._email_msg_body
		except Exception as e :
			raise e
	'''
	set Email notification body
	'''
	@email_msg_body.setter
	def email_msg_body(self,email_msg_body):
		try :
			if not isinstance(email_msg_body,str):
				raise TypeError("email_msg_body must be set to str value")
			self._email_msg_body = email_msg_body
		except Exception as e :
			raise e


	'''
	get Pager Duty Message Body
	'''
	@property
	def pagerduty_msg_body(self) :
		try:
			return self._pagerduty_msg_body
		except Exception as e :
			raise e
	'''
	set Pager Duty Message Body
	'''
	@pagerduty_msg_body.setter
	def pagerduty_msg_body(self,pagerduty_msg_body):
		try :
			if not isinstance(pagerduty_msg_body,str):
				raise TypeError("pagerduty_msg_body must be set to str value")
			self._pagerduty_msg_body = pagerduty_msg_body
		except Exception as e :
			raise e


	'''
	get Slack message body
	'''
	@property
	def slack_msg_body(self) :
		try:
			return self._slack_msg_body
		except Exception as e :
			raise e
	'''
	set Slack message body
	'''
	@slack_msg_body.setter
	def slack_msg_body(self,slack_msg_body):
		try :
			if not isinstance(slack_msg_body,str):
				raise TypeError("slack_msg_body must be set to str value")
			self._slack_msg_body = slack_msg_body
		except Exception as e :
			raise e


	'''
	get Service now message body
	'''
	@property
	def servicenow_msg_body(self) :
		try:
			return self._servicenow_msg_body
		except Exception as e :
			raise e
	'''
	set Service now message body
	'''
	@servicenow_msg_body.setter
	def servicenow_msg_body(self,servicenow_msg_body):
		try :
			if not isinstance(servicenow_msg_body,str):
				raise TypeError("servicenow_msg_body must be set to str value")
			self._servicenow_msg_body = servicenow_msg_body
		except Exception as e :
			raise e


	'''
	get Notification template name for different services.
	'''
	@property
	def template_name(self) :
		try:
			return self._template_name
		except Exception as e :
			raise e
	'''
	set Notification template name for different services.
	'''
	@template_name.setter
	def template_name(self,template_name):
		try :
			if not isinstance(template_name,str):
				raise TypeError("template_name must be set to str value")
			self._template_name = template_name
		except Exception as e :
			raise e


	'''
	get Email Subject
	'''
	@property
	def email_subject(self) :
		try:
			return self._email_subject
		except Exception as e :
			raise e
	'''
	set Email Subject
	'''
	@email_subject.setter
	def email_subject(self,email_subject):
		try :
			if not isinstance(email_subject,str):
				raise TypeError("email_subject must be set to str value")
			self._email_subject = email_subject
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(notify_service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.notify_service
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(notify_service_responses, response, "notify_service_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.notify_service_response_array
				i=0
				error = [notify_service() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.notify_service_response_array
			i=0
			notify_service_objs = [notify_service() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_notify_service'):
					for props in obj._notify_service:
						result = service.payload_formatter.string_to_bulk_resource(notify_service_response,self.__class__.__name__,props)
						notify_service_objs[i] = result.notify_service
						i=i+1
			return notify_service_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(notify_service,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class notify_service_response(base_response):
	def __init__(self,length=1) :
		self.notify_service= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.notify_service= [ notify_service() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class notify_service_responses(base_response):
	def __init__(self,length=1) :
		self.notify_service_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.notify_service_response_array = [ notify_service() for _ in range(length)]
