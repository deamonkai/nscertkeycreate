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
Configuration for Bandwidth info of VPX on SDX resource
'''

class vpx_info(base_resource):
	_ip_address= ""
	_name= ""
	_license_edition= ""
	_id= ""
	_throughput= ""
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
			return "vpx_info"
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
			return "vpx_infos"
		except Exception as e :
			raise e



	'''
	get IP Address of the VPX on SDX
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address of the VPX on SDX
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
	get Vpx name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Vpx name
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
	get Type of License Edition
	'''
	@property
	def license_edition(self) :
		try:
			return self._license_edition
		except Exception as e :
			raise e
	'''
	set Type of License Edition
	'''
	@license_edition.setter
	def license_edition(self,license_edition):
		try :
			if not isinstance(license_edition,str):
				raise TypeError("license_edition must be set to str value")
			self._license_edition = license_edition
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get Throughput in Mbps
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e

	'''
	Use this operation to get info of vpx on sdx.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				vpx_info_obj=vpx_info()
				response = vpx_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpx_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpx_info_obj = vpx_info()
			option_ = options()
			option_._filter=filter_
			return vpx_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpx_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpx_info_obj = vpx_info()
			option_ = options()
			option_._count=True
			response = vpx_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpx_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpx_info_obj = vpx_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpx_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vpx_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpx_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpx_info_responses, response, "vpx_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpx_info_response_array
				i=0
				error = [vpx_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpx_info_response_array
			i=0
			vpx_info_objs = [vpx_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vpx_info'):
					for props in obj._vpx_info:
						result = service.payload_formatter.string_to_bulk_resource(vpx_info_response,self.__class__.__name__,props)
						vpx_info_objs[i] = result.vpx_info
						i=i+1
			return vpx_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpx_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpx_info_response(base_response):
	def __init__(self,length=1) :
		self.vpx_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpx_info= [ vpx_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpx_info_responses(base_response):
	def __init__(self,length=1) :
		self.vpx_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpx_info_response_array = [ vpx_info() for _ in range(length)]
