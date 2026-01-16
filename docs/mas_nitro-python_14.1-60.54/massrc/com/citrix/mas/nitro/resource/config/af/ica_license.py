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
Configuration for Af report for ica_license resource
'''

class ica_license(base_resource):
	_rpt_sample_time= ""
	___count= ""
	_total_license= ""
	_license_in_use= ""
	_ip_address= ""
	_threshold= ""
	_id= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_license"
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
			return "ica_licenses"
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
	total_license.
	'''
	@property
	def total_license(self):
		try:
			return self._total_license
		except Exception as e :
			raise e
	'''
	total_license.
	'''
	@total_license.setter
	def total_license(self,total_license):
		try :
			if not isinstance(total_license,float):
				raise TypeError("total_license must be set to float value")
			self._total_license = total_license
		except Exception as e :
			raise e

	'''
	license_in_use.
	'''
	@property
	def license_in_use(self):
		try:
			return self._license_in_use
		except Exception as e :
			raise e
	'''
	license_in_use.
	'''
	@license_in_use.setter
	def license_in_use(self,license_in_use):
		try :
			if not isinstance(license_in_use,float):
				raise TypeError("license_in_use must be set to float value")
			self._license_in_use = license_in_use
		except Exception as e :
			raise e

	'''
	Ip Address.
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	Ip Address.
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
	threshold.
	'''
	@property
	def threshold(self):
		try:
			return self._threshold
		except Exception as e :
			raise e
	'''
	threshold.
	'''
	@threshold.setter
	def threshold(self,threshold):
		try :
			if not isinstance(threshold,float):
				raise TypeError("threshold must be set to float value")
			self._threshold = threshold
		except Exception as e :
			raise e

	'''
	Id IP Address
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id IP Address
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
	Af Report for ICA license..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_license_obj=ica_license()
				response = ica_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_license_obj = ica_license()
			option_ = options()
			option_._filter=filter_
			return ica_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_license resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_license_obj = ica_license()
			option_ = options()
			option_._count=True
			response = ica_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_license_obj = ica_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_license_responses, response, "ica_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_license_response_array
				i=0
				error = [ica_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_license_response_array
			i=0
			ica_license_objs = [ica_license() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_license:
					result = service.payload_formatter.string_to_bulk_resource(ica_license_response,self.__class__.__name__,props)
					ica_license_objs[i] = result.ica_license
					i=i+1
			return ica_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_license_response(base_response):
	def __init__(self,length=1) :
		self.ica_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_license= [ ica_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_license_responses(base_response):
	def __init__(self,length=1) :
		self.ica_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_license_response_array = [ ica_license() for _ in range(length)]
