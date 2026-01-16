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
Configuration for Thresholds resource
'''

class threshold(base_resource):
	_region= ""
	_name= ""
	_sms_profile= ""
	_city= ""
	_pagerduty_profile= ""
	_stylebook_flag= ""
	_group_name= ""
	_rule= ""
	_duration= ""
	_feature= ""
	_exporter_id= ""
	_tenant_name= ""
	_servicenow_profile= ""
	_reference_key= ""
	_is_enabled= ""
	_resource_type= ""
	_ip_address= ""
	_country= ""
	_slack_profile= ""
	_mail_profile= ""
	_ctnsappname= ""
	_id= ""
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
			return "threshold"
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
			return "thresholds"
		except Exception as e :
			raise e



	'''
	get Region Code
	'''
	@property
	def region(self) :
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	set Region Code
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e


	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get City
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set City
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
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
	get Stylebook threshold configuration true or false
	'''
	@property
	def stylebook_flag(self) :
		try:
			return self._stylebook_flag
		except Exception as e :
			raise e
	'''
	set Stylebook threshold configuration true or false
	'''
	@stylebook_flag.setter
	def stylebook_flag(self,stylebook_flag):
		try :
			if not isinstance(stylebook_flag,bool):
				raise TypeError("stylebook_flag must be set to bool value")
			self._stylebook_flag = stylebook_flag
		except Exception as e :
			raise e


	'''
	get Group Name
	'''
	@property
	def group_name(self) :
		try:
			return self._group_name
		except Exception as e :
			raise e
	'''
	set Group Name
	'''
	@group_name.setter
	def group_name(self,group_name):
		try :
			if not isinstance(group_name,str):
				raise TypeError("group_name must be set to str value")
			self._group_name = group_name
		except Exception as e :
			raise e


	'''
	get Rule
	'''
	@property
	def rule(self) :
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	set Rule
	'''
	@rule.setter
	def rule(self,rule):
		try :
			if not isinstance(rule,str):
				raise TypeError("rule must be set to str value")
			self._rule = rule
		except Exception as e :
			raise e


	'''
	get duration of metric to be checked against threshold
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set duration of metric to be checked against threshold
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
	get feature
	'''
	@property
	def feature(self) :
		try:
			return self._feature
		except Exception as e :
			raise e
	'''
	set feature
	'''
	@feature.setter
	def feature(self,feature):
		try :
			if not isinstance(feature,str):
				raise TypeError("feature must be set to str value")
			self._feature = feature
		except Exception as e :
			raise e


	'''
	get Exporter Id
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter Id
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e


	'''
	get Servicenow Profile
	'''
	@property
	def servicenow_profile(self) :
		try:
			return self._servicenow_profile
		except Exception as e :
			raise e
	'''
	set Servicenow Profile
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
	get Reference Key
	'''
	@property
	def reference_key(self) :
		try:
			return self._reference_key
		except Exception as e :
			raise e
	'''
	set Reference Key
	'''
	@reference_key.setter
	def reference_key(self,reference_key):
		try :
			if not isinstance(reference_key,str):
				raise TypeError("reference_key must be set to str value")
			self._reference_key = reference_key
		except Exception as e :
			raise e


	'''
	get true or false
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set true or false
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,str):
				raise TypeError("is_enabled must be set to str value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get Resource Type
	'''
	@property
	def resource_type(self) :
		try:
			return self._resource_type
		except Exception as e :
			raise e
	'''
	set Resource Type
	'''
	@resource_type.setter
	def resource_type(self,resource_type):
		try :
			if not isinstance(resource_type,str):
				raise TypeError("resource_type must be set to str value")
			self._resource_type = resource_type
		except Exception as e :
			raise e


	'''
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
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
	get Country Code
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set Country Code
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
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
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the Thresholds configuration 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Thresholds configuration 
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
	get threshold configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				threshold_obj=threshold()
				response = threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	add threshold configuration.
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
				threshold_obj= threshold()
				return cls.perform_operation_bulk_request(service,resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	modify threshold configuraiton.
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
				threshold_obj=threshold()
				return cls.update_bulk_request(client,resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	Delete threshold configuration.
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
					threshold_obj=threshold()
					return cls.delete_bulk_request(client,resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._filter=filter_
			return threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._count=True
			response = threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_responses, response, "threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.threshold_response_array
				i=0
				error = [threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.threshold_response_array
			i=0
			threshold_objs = [threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_threshold'):
					for props in obj._threshold:
						result = service.payload_formatter.string_to_bulk_resource(threshold_response,self.__class__.__name__,props)
						threshold_objs[i] = result.threshold
						i=i+1
			return threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class threshold_response(base_response):
	def __init__(self,length=1) :
		self.threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.threshold= [ threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class threshold_responses(base_response):
	def __init__(self,length=1) :
		self.threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.threshold_response_array = [ threshold() for _ in range(length)]
