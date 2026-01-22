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
Configuration for Details about the adcaas application resource
'''

class adcaas_application(base_resource):
	_certificate= ""
	_job_id= ""
	_environment_id= ""
	_updated_at= ""
	_id= ""
	_deployed_at= ""
	_properties= ""
	_status= ""
	_name= ""
	_created_at= ""
	_model= ""
	_app_environment= ""
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
			return "adcaas_application"
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
			return "adcaas_applications"
		except Exception as e :
			raise e



	'''
	get Certificate
	'''
	@property
	def certificate(self) :
		try:
			return self._certificate
		except Exception as e :
			raise e
	'''
	set Certificate
	'''
	@certificate.setter
	def certificate(self,certificate):
		try :
			if not isinstance(certificate,str):
				raise TypeError("certificate must be set to str value")
			self._certificate = certificate
		except Exception as e :
			raise e


	'''
	get Job id
	'''
	@property
	def job_id(self) :
		try:
			return self._job_id
		except Exception as e :
			raise e
	'''
	set Job id
	'''
	@job_id.setter
	def job_id(self,job_id):
		try :
			if not isinstance(job_id,str):
				raise TypeError("job_id must be set to str value")
			self._job_id = job_id
		except Exception as e :
			raise e


	'''
	get Environment id
	'''
	@property
	def environment_id(self) :
		try:
			return self._environment_id
		except Exception as e :
			raise e
	'''
	set Environment id
	'''
	@environment_id.setter
	def environment_id(self,environment_id):
		try :
			if not isinstance(environment_id,str):
				raise TypeError("environment_id must be set to str value")
			self._environment_id = environment_id
		except Exception as e :
			raise e


	'''
	get Created_at timestamp
	'''
	@property
	def updated_at(self) :
		try:
			return self._updated_at
		except Exception as e :
			raise e
	'''
	set Created_at timestamp
	'''
	@updated_at.setter
	def updated_at(self,updated_at):
		try :
			if not isinstance(updated_at,str):
				raise TypeError("updated_at must be set to str value")
			self._updated_at = updated_at
		except Exception as e :
			raise e


	'''
	get Application ID
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Application ID
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
	get Deployed_at timestamp
	'''
	@property
	def deployed_at(self) :
		try:
			return self._deployed_at
		except Exception as e :
			raise e
	'''
	set Deployed_at timestamp
	'''
	@deployed_at.setter
	def deployed_at(self,deployed_at):
		try :
			if not isinstance(deployed_at,str):
				raise TypeError("deployed_at must be set to str value")
			self._deployed_at = deployed_at
		except Exception as e :
			raise e


	'''
	get Properties
	'''
	@property
	def properties(self) :
		try:
			return self._properties
		except Exception as e :
			raise e
	'''
	set Properties
	'''
	@properties.setter
	def properties(self,properties):
		try :
			if not isinstance(properties,str):
				raise TypeError("properties must be set to str value")
			self._properties = properties
		except Exception as e :
			raise e


	'''
	get Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Network function Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Network function Name
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
	get Created_at timestamp
	'''
	@property
	def created_at(self) :
		try:
			return self._created_at
		except Exception as e :
			raise e
	'''
	set Created_at timestamp
	'''
	@created_at.setter
	def created_at(self,created_at):
		try :
			if not isinstance(created_at,str):
				raise TypeError("created_at must be set to str value")
			self._created_at = created_at
		except Exception as e :
			raise e


	'''
	get Model
	'''
	@property
	def model(self) :
		try:
			return self._model
		except Exception as e :
			raise e
	'''
	set Model
	'''
	@model.setter
	def model(self,model):
		try :
			if not isinstance(model,str):
				raise TypeError("model must be set to str value")
			self._model = model
		except Exception as e :
			raise e


	'''
	get Environment name
	'''
	@property
	def app_environment(self) :
		try:
			return self._app_environment
		except Exception as e :
			raise e
	'''
	set Environment name
	'''
	@app_environment.setter
	def app_environment(self,app_environment):
		try :
			if not isinstance(app_environment,str):
				raise TypeError("app_environment must be set to str value")
			self._app_environment = app_environment
		except Exception as e :
			raise e

	'''
	Use this operation to get network function.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adcaas_application_obj=adcaas_application()
				response = adcaas_application_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adcaas_application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adcaas_application_obj = adcaas_application()
			option_ = options()
			option_._filter=filter_
			return adcaas_application_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adcaas_application resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adcaas_application_obj = adcaas_application()
			option_ = options()
			option_._count=True
			response = adcaas_application_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adcaas_application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adcaas_application_obj = adcaas_application()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adcaas_application_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adcaas_application_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adcaas_application
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adcaas_application_responses, response, "adcaas_application_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adcaas_application_response_array
				i=0
				error = [adcaas_application() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adcaas_application_response_array
			i=0
			adcaas_application_objs = [adcaas_application() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adcaas_application'):
					for props in obj._adcaas_application:
						result = service.payload_formatter.string_to_bulk_resource(adcaas_application_response,self.__class__.__name__,props)
						adcaas_application_objs[i] = result.adcaas_application
						i=i+1
			return adcaas_application_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adcaas_application,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adcaas_application_response(base_response):
	def __init__(self,length=1) :
		self.adcaas_application= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adcaas_application= [ adcaas_application() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adcaas_application_responses(base_response):
	def __init__(self,length=1) :
		self.adcaas_application_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adcaas_application_response_array = [ adcaas_application() for _ in range(length)]
