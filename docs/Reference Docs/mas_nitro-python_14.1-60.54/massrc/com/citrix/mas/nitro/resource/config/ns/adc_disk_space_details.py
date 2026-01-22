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
Configuration for Check and clean disk space for NetScaler resource
'''

class adc_disk_space_details(base_resource):
	_disk0_perusage= ""
	_id= ""
	_disk1_used= ""
	_disk1_free= ""
	_disk1_total= ""
	_disk0_total= ""
	_disk0_used= ""
	_disk1_perusage= ""
	_disk0_free= ""
	_device= ""
	_folders=[]
	_files=[]
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
			return "adc_disk_space_details"
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
			return "adc_disk_space_detailss"
		except Exception as e :
			raise e



	'''
	get NetScaler Disk0 Utilization (%)
	'''
	@property
	def disk0_perusage(self) :
		try:
			return self._disk0_perusage
		except Exception as e :
			raise e


	'''
	get Id is Activity Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get Disk1 used space in percentage
	'''
	@property
	def disk1_used(self) :
		try:
			return self._disk1_used
		except Exception as e :
			raise e


	'''
	get Disk1 free space in MB
	'''
	@property
	def disk1_free(self) :
		try:
			return self._disk1_free
		except Exception as e :
			raise e


	'''
	get Disk1 total space in MB
	'''
	@property
	def disk1_total(self) :
		try:
			return self._disk1_total
		except Exception as e :
			raise e


	'''
	get Disk0 total space in MB
	'''
	@property
	def disk0_total(self) :
		try:
			return self._disk0_total
		except Exception as e :
			raise e


	'''
	get Disk0 used space in percentage
	'''
	@property
	def disk0_used(self) :
		try:
			return self._disk0_used
		except Exception as e :
			raise e


	'''
	get NetScaler Disk0 Utilization (%)
	'''
	@property
	def disk1_perusage(self) :
		try:
			return self._disk1_perusage
		except Exception as e :
			raise e


	'''
	get Disk0 Free space in MB
	'''
	@property
	def disk0_free(self) :
		try:
			return self._disk0_free
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address for space check and cleanup
	'''
	@property
	def device(self) :
		try:
			return self._device
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address for space check and cleanup
	'''
	@device.setter
	def device(self,device):
		try :
			if not isinstance(device,str):
				raise TypeError("device must be set to str value")
			self._device = device
		except Exception as e :
			raise e

	'''
	Folders to remove
	'''
	@property
	def folders(self) :
		try:
			return self._folders
		except Exception as e :
			raise e
	'''
	Folders to remove
	'''
	@folders.setter
	def folders(self,folders) :
		try :
			if not isinstance(folders,list):
				raise TypeError("folders must be set to array of str value")
			for item in folders :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._folders = folders
		except Exception as e :
			raise e

	'''
	Files to remove
	'''
	@property
	def files(self) :
		try:
			return self._files
		except Exception as e :
			raise e
	'''
	Files to remove
	'''
	@files.setter
	def files(self,files) :
		try :
			if not isinstance(files,list):
				raise TypeError("files must be set to array of str value")
			for item in files :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._files = files
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler disk space details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_disk_space_details_obj=adc_disk_space_details()
				response = adc_disk_space_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_disk_space_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_disk_space_details_obj = adc_disk_space_details()
			option_ = options()
			option_._filter=filter_
			return adc_disk_space_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_disk_space_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_disk_space_details_obj = adc_disk_space_details()
			option_ = options()
			option_._count=True
			response = adc_disk_space_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_disk_space_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_disk_space_details_obj = adc_disk_space_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_disk_space_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_disk_space_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_disk_space_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_disk_space_details_responses, response, "adc_disk_space_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_disk_space_details_response_array
				i=0
				error = [adc_disk_space_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_disk_space_details_response_array
			i=0
			adc_disk_space_details_objs = [adc_disk_space_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_disk_space_details'):
					for props in obj._adc_disk_space_details:
						result = service.payload_formatter.string_to_bulk_resource(adc_disk_space_details_response,self.__class__.__name__,props)
						adc_disk_space_details_objs[i] = result.adc_disk_space_details
						i=i+1
			return adc_disk_space_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_disk_space_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_disk_space_details_response(base_response):
	def __init__(self,length=1) :
		self.adc_disk_space_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_disk_space_details= [ adc_disk_space_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_disk_space_details_responses(base_response):
	def __init__(self,length=1) :
		self.adc_disk_space_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_disk_space_details_response_array = [ adc_disk_space_details() for _ in range(length)]
