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
Configuration for AF Templates resource
'''

class af_templates(base_resource):
	_template_field_length= ""
	_observationPointId= ""
	_template_rx_time= ""
	_exporter_id= ""
	_template_field_name= ""
	_template_id= ""
	_template_field_id= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_templates"
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
			return "af_templatess"
		except Exception as e :
			raise e



	'''
	get Template Field Length
	'''
	@property
	def template_field_length(self) :
		try:
			return self._template_field_length
		except Exception as e :
			raise e
	'''
	set Template Field Length
	'''
	@template_field_length.setter
	def template_field_length(self,template_field_length):
		try :
			if not isinstance(template_field_length,int):
				raise TypeError("template_field_length must be set to int value")
			self._template_field_length = template_field_length
		except Exception as e :
			raise e


	'''
	get Observation Point ID
	'''
	@property
	def observationPointId(self) :
		try:
			return self._observationPointId
		except Exception as e :
			raise e
	'''
	set Observation Point ID
	'''
	@observationPointId.setter
	def observationPointId(self,observationPointId):
		try :
			if not isinstance(observationPointId,int):
				raise TypeError("observationPointId must be set to int value")
			self._observationPointId = observationPointId
		except Exception as e :
			raise e


	'''
	get Start Time
	'''
	@property
	def template_rx_time(self) :
		try:
			return self._template_rx_time
		except Exception as e :
			raise e
	'''
	set Start Time
	'''
	@template_rx_time.setter
	def template_rx_time(self,template_rx_time):
		try :
			if not isinstance(template_rx_time,long):
				raise TypeError("template_rx_time must be set to long value")
			self._template_rx_time = template_rx_time
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
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get Templates field names.
	'''
	@property
	def template_field_name(self) :
		try:
			return self._template_field_name
		except Exception as e :
			raise e
	'''
	set Templates field names.
	'''
	@template_field_name.setter
	def template_field_name(self,template_field_name):
		try :
			if not isinstance(template_field_name,str):
				raise TypeError("template_field_name must be set to str value")
			self._template_field_name = template_field_name
		except Exception as e :
			raise e


	'''
	get AF Template ID
	'''
	@property
	def template_id(self) :
		try:
			return self._template_id
		except Exception as e :
			raise e
	'''
	set AF Template ID
	'''
	@template_id.setter
	def template_id(self,template_id):
		try :
			if not isinstance(template_id,int):
				raise TypeError("template_id must be set to int value")
			self._template_id = template_id
		except Exception as e :
			raise e


	'''
	get Protocol
	'''
	@property
	def template_field_id(self) :
		try:
			return self._template_field_id
		except Exception as e :
			raise e
	'''
	set Protocol
	'''
	@template_field_id.setter
	def template_field_id(self,template_field_id):
		try :
			if not isinstance(template_field_id,int):
				raise TypeError("template_field_id must be set to int value")
			self._template_field_id = template_field_id
		except Exception as e :
			raise e

	'''
	Modify AF Templates..
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				af_templates_obj=af_templates()
				return cls.update_bulk_request(client,resource,af_templates_obj)
		except Exception as e :
			raise e

	'''
	Get all AF Templates being managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_templates_obj=af_templates()
				response = af_templates_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_templates resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_templates_obj = af_templates()
			option_ = options()
			option_._filter=filter_
			return af_templates_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_templates resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_templates_obj = af_templates()
			option_ = options()
			option_._count=True
			response = af_templates_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_templates resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_templates_obj = af_templates()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_templates_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_templates_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_templates
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_templates_responses, response, "af_templates_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_templates_response_array
				i=0
				error = [af_templates() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_templates_response_array
			i=0
			af_templates_objs = [af_templates() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_templates:
					result = service.payload_formatter.string_to_bulk_resource(af_templates_response,self.__class__.__name__,props)
					af_templates_objs[i] = result.af_templates
					i=i+1
			return af_templates_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_templates,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_templates_response(base_response):
	def __init__(self,length=1) :
		self.af_templates= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_templates= [ af_templates() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_templates_responses(base_response):
	def __init__(self,length=1) :
		self.af_templates_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_templates_response_array = [ af_templates() for _ in range(length)]
