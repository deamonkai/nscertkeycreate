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
Configuration for AF AppId to AppName mapping info resource
'''

class af_appid_mapping(base_resource):
	_appName= ""
	_exporter_id= ""
	_appNameAppId= ""
	_appNameIncarnationNumber= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_appid_mapping"
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
			return "af_appid_mappings"
		except Exception as e :
			raise e



	'''
	get AppName
	'''
	@property
	def appName(self) :
		try:
			return self._appName
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@appName.setter
	def appName(self,appName):
		try :
			if not isinstance(appName,str):
				raise TypeError("appName must be set to str value")
			self._appName = appName
		except Exception as e :
			raise e


	'''
	get The exporter ID mapping back to the af_exporter table
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set The exporter ID mapping back to the af_exporter table
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
	get AppName AppID
	'''
	@property
	def appNameAppId(self) :
		try:
			return self._appNameAppId
		except Exception as e :
			raise e
	'''
	set AppName AppID
	'''
	@appNameAppId.setter
	def appNameAppId(self,appNameAppId):
		try :
			if not isinstance(appNameAppId,float):
				raise TypeError("appNameAppId must be set to float value")
			self._appNameAppId = appNameAppId
		except Exception as e :
			raise e


	'''
	get Observation Point ID
	'''
	@property
	def appNameIncarnationNumber(self) :
		try:
			return self._appNameIncarnationNumber
		except Exception as e :
			raise e
	'''
	set Observation Point ID
	'''
	@appNameIncarnationNumber.setter
	def appNameIncarnationNumber(self,appNameIncarnationNumber):
		try :
			if not isinstance(appNameIncarnationNumber,float):
				raise TypeError("appNameIncarnationNumber must be set to float value")
			self._appNameIncarnationNumber = appNameIncarnationNumber
		except Exception as e :
			raise e

	'''
	Get all appid to appname mappings. Note this response would be a very CPU intensive..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_appid_mapping_obj=af_appid_mapping()
				response = af_appid_mapping_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_appid_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_appid_mapping_obj = af_appid_mapping()
			option_ = options()
			option_._filter=filter_
			return af_appid_mapping_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_appid_mapping resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_appid_mapping_obj = af_appid_mapping()
			option_ = options()
			option_._count=True
			response = af_appid_mapping_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_appid_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_appid_mapping_obj = af_appid_mapping()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_appid_mapping_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_appid_mapping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_appid_mapping
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_appid_mapping_responses, response, "af_appid_mapping_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_appid_mapping_response_array
				i=0
				error = [af_appid_mapping() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_appid_mapping_response_array
			i=0
			af_appid_mapping_objs = [af_appid_mapping() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_appid_mapping:
					result = service.payload_formatter.string_to_bulk_resource(af_appid_mapping_response,self.__class__.__name__,props)
					af_appid_mapping_objs[i] = result.af_appid_mapping
					i=i+1
			return af_appid_mapping_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_appid_mapping,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_appid_mapping_response(base_response):
	def __init__(self,length=1) :
		self.af_appid_mapping= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_appid_mapping= [ af_appid_mapping() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_appid_mapping_responses(base_response):
	def __init__(self,length=1) :
		self.af_appid_mapping_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_appid_mapping_response_array = [ af_appid_mapping() for _ in range(length)]
