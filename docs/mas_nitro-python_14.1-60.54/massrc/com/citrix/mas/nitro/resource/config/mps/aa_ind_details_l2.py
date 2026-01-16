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
Configuration for Indicator Alert Details resource
'''

class aa_ind_details_l2(base_resource):
	_ind_value= ""
	_violation_count= ""
	_ind_detection_msg= ""
	_svcname= ""
	_appname= ""
	_confidence= ""
	_window_start_time= ""
	_violation_ratio= ""
	_window_end_time= ""
	_ip_address= ""
	_severity= ""
	_ind_detection_time= ""
	_ctnsappname= ""
	_rpt_sample_time= ""
	_ind_id= ""
	_ind_name_desc= ""
	_ind_weight_desc= ""
	_ind_category_desc= ""
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
			return "aa_ind_details_l2"
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
			return "aa_ind_details_l2s"
		except Exception as e :
			raise e



	'''
	get Indicator Value
	'''
	@property
	def ind_value(self) :
		try:
			return self._ind_value
		except Exception as e :
			raise e
	'''
	set Indicator Value
	'''
	@ind_value.setter
	def ind_value(self,ind_value):
		try :
			if not isinstance(ind_value,int):
				raise TypeError("ind_value must be set to int value")
			self._ind_value = ind_value
		except Exception as e :
			raise e


	'''
	get violation_count
	'''
	@property
	def violation_count(self) :
		try:
			return self._violation_count
		except Exception as e :
			raise e
	'''
	set violation_count
	'''
	@violation_count.setter
	def violation_count(self,violation_count):
		try :
			if not isinstance(violation_count,long):
				raise TypeError("violation_count must be set to long value")
			self._violation_count = violation_count
		except Exception as e :
			raise e


	'''
	get Indicator Detection Message
	'''
	@property
	def ind_detection_msg(self) :
		try:
			return self._ind_detection_msg
		except Exception as e :
			raise e
	'''
	set Indicator Detection Message
	'''
	@ind_detection_msg.setter
	def ind_detection_msg(self,ind_detection_msg):
		try :
			if not isinstance(ind_detection_msg,str):
				raise TypeError("ind_detection_msg must be set to str value")
			self._ind_detection_msg = ind_detection_msg
		except Exception as e :
			raise e


	'''
	get svcname
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set svcname
	'''
	@svcname.setter
	def svcname(self,svcname):
		try :
			if not isinstance(svcname,str):
				raise TypeError("svcname must be set to str value")
			self._svcname = svcname
		except Exception as e :
			raise e


	'''
	get ApplicationName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set ApplicationName
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get confidence
	'''
	@property
	def confidence(self) :
		try:
			return self._confidence
		except Exception as e :
			raise e
	'''
	set confidence
	'''
	@confidence.setter
	def confidence(self,confidence):
		try :
			if not isinstance(confidence,float):
				raise TypeError("confidence must be set to float value")
			self._confidence = confidence
		except Exception as e :
			raise e


	'''
	get Window start time.
	'''
	@property
	def window_start_time(self) :
		try:
			return self._window_start_time
		except Exception as e :
			raise e
	'''
	set Window start time.
	'''
	@window_start_time.setter
	def window_start_time(self,window_start_time):
		try :
			if not isinstance(window_start_time,long):
				raise TypeError("window_start_time must be set to long value")
			self._window_start_time = window_start_time
		except Exception as e :
			raise e


	'''
	get violation_ratio
	'''
	@property
	def violation_ratio(self) :
		try:
			return self._violation_ratio
		except Exception as e :
			raise e
	'''
	set violation_ratio
	'''
	@violation_ratio.setter
	def violation_ratio(self,violation_ratio):
		try :
			if not isinstance(violation_ratio,float):
				raise TypeError("violation_ratio must be set to float value")
			self._violation_ratio = violation_ratio
		except Exception as e :
			raise e


	'''
	get Window End time.
	'''
	@property
	def window_end_time(self) :
		try:
			return self._window_end_time
		except Exception as e :
			raise e
	'''
	set Window End time.
	'''
	@window_end_time.setter
	def window_end_time(self,window_end_time):
		try :
			if not isinstance(window_end_time,long):
				raise TypeError("window_end_time must be set to long value")
			self._window_end_time = window_end_time
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
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
	get Severity of the alert [ CRITICAL/MEDIUM/LOW ]
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity of the alert [ CRITICAL/MEDIUM/LOW ]
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,int):
				raise TypeError("severity must be set to int value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Report Sample time.
	'''
	@property
	def ind_detection_time(self) :
		try:
			return self._ind_detection_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@ind_detection_time.setter
	def ind_detection_time(self,ind_detection_time):
		try :
			if not isinstance(ind_detection_time,long):
				raise TypeError("ind_detection_time must be set to long value")
			self._ind_detection_time = ind_detection_time
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
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Indicator Rule Id
	'''
	@property
	def ind_id(self) :
		try:
			return self._ind_id
		except Exception as e :
			raise e
	'''
	set Indicator Rule Id
	'''
	@ind_id.setter
	def ind_id(self,ind_id):
		try :
			if not isinstance(ind_id,int):
				raise TypeError("ind_id must be set to int value")
			self._ind_id = ind_id
		except Exception as e :
			raise e

	'''
	Indicator name description
	'''
	@property
	def ind_name_desc(self):
		try:
			return self._ind_name_desc
		except Exception as e :
			raise e
	'''
	Indicator name description
	'''
	@ind_name_desc.setter
	def ind_name_desc(self,ind_name_desc):
		try :
			if not isinstance(ind_name_desc,str):
				raise TypeError("ind_name_desc must be set to str value")
			self._ind_name_desc = ind_name_desc
		except Exception as e :
			raise e

	'''
	Indicator weight description
	'''
	@property
	def ind_weight_desc(self):
		try:
			return self._ind_weight_desc
		except Exception as e :
			raise e
	'''
	Indicator weight description
	'''
	@ind_weight_desc.setter
	def ind_weight_desc(self,ind_weight_desc):
		try :
			if not isinstance(ind_weight_desc,int):
				raise TypeError("ind_weight_desc must be set to int value")
			self._ind_weight_desc = ind_weight_desc
		except Exception as e :
			raise e

	'''
	Indicator category description
	'''
	@property
	def ind_category_desc(self):
		try:
			return self._ind_category_desc
		except Exception as e :
			raise e
	'''
	Indicator category description
	'''
	@ind_category_desc.setter
	def ind_category_desc(self,ind_category_desc):
		try :
			if not isinstance(ind_category_desc,str):
				raise TypeError("ind_category_desc must be set to str value")
			self._ind_category_desc = ind_category_desc
		except Exception as e :
			raise e

	'''
	Use this operation to get AAA server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				aa_ind_details_l2_obj=aa_ind_details_l2()
				response = aa_ind_details_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_ind_details_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_ind_details_l2_obj = aa_ind_details_l2()
			option_ = options()
			option_._filter=filter_
			return aa_ind_details_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_ind_details_l2 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_ind_details_l2_obj = aa_ind_details_l2()
			option_ = options()
			option_._count=True
			response = aa_ind_details_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_ind_details_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_ind_details_l2_obj = aa_ind_details_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_ind_details_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_ind_details_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_ind_details_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_ind_details_l2_responses, response, "aa_ind_details_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_ind_details_l2_response_array
				i=0
				error = [aa_ind_details_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_ind_details_l2_response_array
			i=0
			aa_ind_details_l2_objs = [aa_ind_details_l2() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_aa_ind_details_l2'):
					for props in obj._aa_ind_details_l2:
						result = service.payload_formatter.string_to_bulk_resource(aa_ind_details_l2_response,self.__class__.__name__,props)
						aa_ind_details_l2_objs[i] = result.aa_ind_details_l2
						i=i+1
			return aa_ind_details_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_ind_details_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_ind_details_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_ind_details_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_ind_details_l2= [ aa_ind_details_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_ind_details_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_ind_details_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_ind_details_l2_response_array = [ aa_ind_details_l2() for _ in range(length)]
