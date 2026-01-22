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
Configuration for Af report for VPN Error details resource
'''

class vpn_error_reports(af_generic_api):
	_vpn_fqdn= ""
	_exporter_id= ""
	_username= ""
	___count= ""
	_rpt_sample_time= ""
	_hits= ""
	_entity_type= ""
	_entity= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_error_reports"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_error_reports,self).get_object_id()
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
			return "vpn_error_reportss"
		except Exception as e :
			raise e


	'''
	VPN FQDN
	'''
	@property
	def vpn_fqdn(self):
		try:
			return self._vpn_fqdn
		except Exception as e :
			raise e
	'''
	VPN FQDN
	'''
	@vpn_fqdn.setter
	def vpn_fqdn(self,vpn_fqdn):
		try :
			if not isinstance(vpn_fqdn,str):
				raise TypeError("vpn_fqdn must be set to str value")
			self._vpn_fqdn = vpn_fqdn
		except Exception as e :
			raise e

	'''
	Exporter ID
	'''
	@property
	def exporter_id(self):
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	Exporter ID
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,float):
				raise TypeError("exporter_id must be set to float value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e

	'''
	VPN username
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	VPN username
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
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
	rpt_sample_time
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	rpt_sample_time
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
	Error Code
	'''
	@property
	def hits(self):
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	Error Code
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,float):
				raise TypeError("hits must be set to float value")
			self._hits = hits
		except Exception as e :
			raise e

	'''
	Entity Type
	'''
	@property
	def entity_type(self):
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	Entity Type
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e

	'''
	Entity
	'''
	@property
	def entity(self):
		try:
			return self._entity
		except Exception as e :
			raise e
	'''
	Entity
	'''
	@entity.setter
	def entity(self,entity):
		try :
			if not isinstance(entity,float):
				raise TypeError("entity must be set to float value")
			self._entity = entity
		except Exception as e :
			raise e

	'''
	Af Report for VPN Error Details ....
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_error_reports_obj=vpn_error_reports()
				response = vpn_error_reports_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_error_reports resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_error_reports_obj = vpn_error_reports()
			option_ = options()
			option_._filter=filter_
			return vpn_error_reports_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_error_reports resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_error_reports_obj = vpn_error_reports()
			option_ = options()
			option_._count=True
			response = vpn_error_reports_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_error_reports resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_error_reports_obj = vpn_error_reports()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_error_reports_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_error_reports_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_error_reports
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_error_reports_responses, response, "vpn_error_reports_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_error_reports_response_array
				i=0
				error = [vpn_error_reports() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_error_reports_response_array
			i=0
			vpn_error_reports_objs = [vpn_error_reports() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_error_reports:
					result = service.payload_formatter.string_to_bulk_resource(vpn_error_reports_response,self.__class__.__name__,props)
					vpn_error_reports_objs[i] = result.vpn_error_reports
					i=i+1
			return vpn_error_reports_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_error_reports,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_error_reports_response(base_response):
	def __init__(self,length=1) :
		self.vpn_error_reports= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_error_reports= [ vpn_error_reports() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_error_reports_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_error_reports_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_error_reports_response_array = [ vpn_error_reports() for _ in range(length)]
