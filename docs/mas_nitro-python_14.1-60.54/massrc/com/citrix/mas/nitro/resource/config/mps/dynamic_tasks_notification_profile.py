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
Configuration for Dynamic Task Notification Profile resource
'''

class dynamic_tasks_notification_profile(base_resource):
	_sms=[]
	_slack=[]
	_email=[]
	_service_now=[]
	_pager_duty=[]
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
			return "dynamic_tasks_notification_profile"
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
			return "dynamic_tasks_notification_profiles"
		except Exception as e :
			raise e



	'''
	get sms Profile
	'''
	@property
	def sms(self) :
		try:
			return self._sms
		except Exception as e :
			raise e
	'''
	set sms Profile
	'''
	@sms.setter
	def sms(self,sms) :
		try :
			if not isinstance(sms,list):
				raise TypeError("sms must be set to array of str value")
			for item in sms :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._sms = sms
		except Exception as e :
			raise e


	'''
	get Slack Profile
	'''
	@property
	def slack(self) :
		try:
			return self._slack
		except Exception as e :
			raise e
	'''
	set Slack Profile
	'''
	@slack.setter
	def slack(self,slack) :
		try :
			if not isinstance(slack,list):
				raise TypeError("slack must be set to array of str value")
			for item in slack :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._slack = slack
		except Exception as e :
			raise e


	'''
	get Email Profile
	'''
	@property
	def email(self) :
		try:
			return self._email
		except Exception as e :
			raise e
	'''
	set Email Profile
	'''
	@email.setter
	def email(self,email) :
		try :
			if not isinstance(email,list):
				raise TypeError("email must be set to array of str value")
			for item in email :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._email = email
		except Exception as e :
			raise e


	'''
	get ServiceNow Profile
	'''
	@property
	def service_now(self) :
		try:
			return self._service_now
		except Exception as e :
			raise e
	'''
	set ServiceNow Profile
	'''
	@service_now.setter
	def service_now(self,service_now) :
		try :
			if not isinstance(service_now,list):
				raise TypeError("service_now must be set to array of str value")
			for item in service_now :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._service_now = service_now
		except Exception as e :
			raise e


	'''
	get pager_duty Profile
	'''
	@property
	def pager_duty(self) :
		try:
			return self._pager_duty
		except Exception as e :
			raise e
	'''
	set pager_duty Profile
	'''
	@pager_duty.setter
	def pager_duty(self,pager_duty) :
		try :
			if not isinstance(pager_duty,list):
				raise TypeError("pager_duty must be set to array of str value")
			for item in pager_duty :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._pager_duty = pager_duty
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dynamic_tasks_notification_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dynamic_tasks_notification_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dynamic_tasks_notification_profile_responses, response, "dynamic_tasks_notification_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dynamic_tasks_notification_profile_response_array
				i=0
				error = [dynamic_tasks_notification_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dynamic_tasks_notification_profile_response_array
			i=0
			dynamic_tasks_notification_profile_objs = [dynamic_tasks_notification_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_dynamic_tasks_notification_profile'):
					for props in obj._dynamic_tasks_notification_profile:
						result = service.payload_formatter.string_to_bulk_resource(dynamic_tasks_notification_profile_response,self.__class__.__name__,props)
						dynamic_tasks_notification_profile_objs[i] = result.dynamic_tasks_notification_profile
						i=i+1
			return dynamic_tasks_notification_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dynamic_tasks_notification_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dynamic_tasks_notification_profile_response(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks_notification_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dynamic_tasks_notification_profile= [ dynamic_tasks_notification_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dynamic_tasks_notification_profile_responses(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks_notification_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dynamic_tasks_notification_profile_response_array = [ dynamic_tasks_notification_profile() for _ in range(length)]
