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

from massrc.com.citrix.mas.nitro.resource.config.mps.af_generic_api import af_generic_api

'''
Configuration for Af report for ICA User resource
'''

class vpn_error_details_timeline(af_generic_api):
	_rpt_sample_time= ""
	___count= ""
	_id= ""
	_error_counts= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_error_details_timeline"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_error_details_timeline,self).get_object_id()
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
			return "vpn_error_details_timelines"
		except Exception as e :
			raise e


	'''
	Report Sample Time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample Time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	Id is not dicided yet
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is not dicided yet
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
	Failure counts.
	'''
	@property
	def error_counts(self):
		try:
			return self._error_counts
		except Exception as e :
			raise e
	'''
	Failure counts.
	'''
	@error_counts.setter
	def error_counts(self,error_counts):
		try :
			if not isinstance(error_counts,float):
				raise TypeError("error_counts must be set to float value")
			self._error_counts = error_counts
		except Exception as e :
			raise e

	'''
	Af Report for Error Counts ....
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_error_details_timeline_obj=vpn_error_details_timeline()
				response = vpn_error_details_timeline_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_error_details_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_error_details_timeline_obj = vpn_error_details_timeline()
			option_ = options()
			option_._filter=filter_
			return vpn_error_details_timeline_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_error_details_timeline resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_error_details_timeline_obj = vpn_error_details_timeline()
			option_ = options()
			option_._count=True
			response = vpn_error_details_timeline_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_error_details_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_error_details_timeline_obj = vpn_error_details_timeline()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_error_details_timeline_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_error_details_timeline_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_error_details_timeline
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_error_details_timeline_responses, response, "vpn_error_details_timeline_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_error_details_timeline_response_array
				i=0
				error = [vpn_error_details_timeline() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_error_details_timeline_response_array
			i=0
			vpn_error_details_timeline_objs = [vpn_error_details_timeline() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_error_details_timeline:
					result = service.payload_formatter.string_to_bulk_resource(vpn_error_details_timeline_response,self.__class__.__name__,props)
					vpn_error_details_timeline_objs[i] = result.vpn_error_details_timeline
					i=i+1
			return vpn_error_details_timeline_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_error_details_timeline,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_error_details_timeline_response(base_response):
	def __init__(self,length=1) :
		self.vpn_error_details_timeline= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_error_details_timeline= [ vpn_error_details_timeline() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_error_details_timeline_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_error_details_timeline_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_error_details_timeline_response_array = [ vpn_error_details_timeline() for _ in range(length)]
