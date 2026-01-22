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
Configuration for Af report for ICA Session hop detail resource
'''

class ica_session_hop_detail(af_generic_api):
	_hop_location= ""
	_ica_device_ip_address= ""
	_hop_count= ""
	_id= ""
	_ica_device_name= ""
	_rpt_sample_time= ""
	___count= ""
	_edt_type= ""
	_dc_latency= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_session_hop_detail"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_session_hop_detail,self).get_object_id()
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
			return "ica_session_hop_details"
		except Exception as e :
			raise e


	'''
	ica session hop location.
	'''
	@property
	def hop_location(self):
		try:
			return self._hop_location
		except Exception as e :
			raise e
	'''
	ica session hop location.
	'''
	@hop_location.setter
	def hop_location(self,hop_location):
		try :
			if not isinstance(hop_location,float):
				raise TypeError("hop_location must be set to float value")
			self._hop_location = hop_location
		except Exception as e :
			raise e

	'''
	ICA Device IP Address.
	'''
	@property
	def ica_device_ip_address(self):
		try:
			return self._ica_device_ip_address
		except Exception as e :
			raise e
	'''
	ICA Device IP Address.
	'''
	@ica_device_ip_address.setter
	def ica_device_ip_address(self,ica_device_ip_address):
		try :
			if not isinstance(ica_device_ip_address,str):
				raise TypeError("ica_device_ip_address must be set to str value")
			self._ica_device_ip_address = ica_device_ip_address
		except Exception as e :
			raise e

	'''
	ica session hop count.
	'''
	@property
	def hop_count(self):
		try:
			return self._hop_count
		except Exception as e :
			raise e
	'''
	ica session hop count.
	'''
	@hop_count.setter
	def hop_count(self,hop_count):
		try :
			if not isinstance(hop_count,float):
				raise TypeError("hop_count must be set to float value")
			self._hop_count = hop_count
		except Exception as e :
			raise e

	'''
	Id is ICA Session ID
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Session ID
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
	Name of ICA device
	'''
	@property
	def ica_device_name(self):
		try:
			return self._ica_device_name
		except Exception as e :
			raise e
	'''
	Name of ICA device
	'''
	@ica_device_name.setter
	def ica_device_name(self,ica_device_name):
		try :
			if not isinstance(ica_device_name,str):
				raise TypeError("ica_device_name must be set to str value")
			self._ica_device_name = ica_device_name
		except Exception as e :
			raise e

	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
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
	Number of records.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records.
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
	EDT type
	'''
	@property
	def edt_type(self):
		try:
			return self._edt_type
		except Exception as e :
			raise e
	'''
	EDT type
	'''
	@edt_type.setter
	def edt_type(self,edt_type):
		try :
			if not isinstance(edt_type,str):
				raise TypeError("edt_type must be set to str value")
			self._edt_type = edt_type
		except Exception as e :
			raise e

	'''
	ica session dc latency.
	'''
	@property
	def dc_latency(self):
		try:
			return self._dc_latency
		except Exception as e :
			raise e
	'''
	ica session dc latency.
	'''
	@dc_latency.setter
	def dc_latency(self,dc_latency):
		try :
			if not isinstance(dc_latency,float):
				raise TypeError("dc_latency must be set to float value")
			self._dc_latency = dc_latency
		except Exception as e :
			raise e

	'''
	Af Report for ICA Session hop details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_session_hop_detail_obj=ica_session_hop_detail()
				response = ica_session_hop_detail_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_session_hop_detail_obj = ica_session_hop_detail()
			option_ = options()
			option_._filter=filter_
			return ica_session_hop_detail_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_session_hop_detail resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_session_hop_detail_obj = ica_session_hop_detail()
			option_ = options()
			option_._count=True
			response = ica_session_hop_detail_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_session_hop_detail_obj = ica_session_hop_detail()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_session_hop_detail_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_session_hop_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_session_hop_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_session_hop_detail_responses, response, "ica_session_hop_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_session_hop_detail_response_array
				i=0
				error = [ica_session_hop_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_session_hop_detail_response_array
			i=0
			ica_session_hop_detail_objs = [ica_session_hop_detail() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_session_hop_detail:
					result = service.payload_formatter.string_to_bulk_resource(ica_session_hop_detail_response,self.__class__.__name__,props)
					ica_session_hop_detail_objs[i] = result.ica_session_hop_detail
					i=i+1
			return ica_session_hop_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_session_hop_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_session_hop_detail_response(base_response):
	def __init__(self,length=1) :
		self.ica_session_hop_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_session_hop_detail= [ ica_session_hop_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_session_hop_detail_responses(base_response):
	def __init__(self,length=1) :
		self.ica_session_hop_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_session_hop_detail_response_array = [ ica_session_hop_detail() for _ in range(length)]
