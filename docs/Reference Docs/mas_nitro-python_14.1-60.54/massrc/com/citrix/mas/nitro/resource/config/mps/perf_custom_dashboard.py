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
Configuration for Custom Dashboard for Network reports resource
'''

class perf_custom_dashboard(base_resource):
	_reporting_category= ""
	_description= ""
	_id= ""
	_instances= ""
	_agg_level= ""
	_entities= ""
	_no_of_columns= ""
	_timestamp= ""
	_entity_type= ""
	_device_family= ""
	_name= ""
	_report_names= ""
	_coordinates= ""
	_coordinates_array=[]
	_report_names_array=[]
	_instances_array=[]
	_entities_array=[]
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
			return "perf_custom_dashboard"
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
			return "perf_custom_dashboards"
		except Exception as e :
			raise e



	'''
	get Reporting Category
	'''
	@property
	def reporting_category(self) :
		try:
			return self._reporting_category
		except Exception as e :
			raise e
	'''
	set Reporting Category
	'''
	@reporting_category.setter
	def reporting_category(self,reporting_category):
		try :
			if not isinstance(reporting_category,str):
				raise TypeError("reporting_category must be set to str value")
			self._reporting_category = reporting_category
		except Exception as e :
			raise e


	'''
	get Custom dashboard description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Custom dashboard description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the perf custom dashboard configuration 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the perf custom dashboard configuration 
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
	get Display Names of NetScaler instances
	'''
	@property
	def instances(self) :
		try:
			return self._instances
		except Exception as e :
			raise e


	'''
	get Aggregation Level
	'''
	@property
	def agg_level(self) :
		try:
			return self._agg_level
		except Exception as e :
			raise e
	'''
	set Aggregation Level
	'''
	@agg_level.setter
	def agg_level(self,agg_level):
		try :
			if not isinstance(agg_level,str):
				raise TypeError("agg_level must be set to str value")
			self._agg_level = agg_level
		except Exception as e :
			raise e


	'''
	get Entities(virtual servers or network interfaces) with instance display_names
	'''
	@property
	def entities(self) :
		try:
			return self._entities
		except Exception as e :
			raise e


	'''
	get No of columns in dashboard
	'''
	@property
	def no_of_columns(self) :
		try:
			return self._no_of_columns
		except Exception as e :
			raise e
	'''
	set No of columns in dashboard
	'''
	@no_of_columns.setter
	def no_of_columns(self,no_of_columns):
		try :
			if not isinstance(no_of_columns,int):
				raise TypeError("no_of_columns must be set to int value")
			self._no_of_columns = no_of_columns
		except Exception as e :
			raise e


	'''
	get timestamp in seconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in seconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get Entity Type
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	set Entity Type
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
	get Device Family of which this custom dashboard belongs to
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family of which this custom dashboard belongs to
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get Report Names
	'''
	@property
	def report_names(self) :
		try:
			return self._report_names
		except Exception as e :
			raise e


	'''
	get Co-ordinates
	'''
	@property
	def coordinates(self) :
		try:
			return self._coordinates
		except Exception as e :
			raise e

	'''
	Co-ordinates in array
	'''
	@property
	def coordinates_array(self) :
		try:
			return self._coordinates_array
		except Exception as e :
			raise e
	'''
	Co-ordinates in array
	'''
	@coordinates_array.setter
	def coordinates_array(self,coordinates_array) :
		try :
			if not isinstance(coordinates_array,list):
				raise TypeError("coordinates_array must be set to array of str value")
			for item in coordinates_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._coordinates_array = coordinates_array
		except Exception as e :
			raise e

	'''
	Report names in array
	'''
	@property
	def report_names_array(self) :
		try:
			return self._report_names_array
		except Exception as e :
			raise e
	'''
	Report names in array
	'''
	@report_names_array.setter
	def report_names_array(self,report_names_array) :
		try :
			if not isinstance(report_names_array,list):
				raise TypeError("report_names_array must be set to array of str value")
			for item in report_names_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._report_names_array = report_names_array
		except Exception as e :
			raise e

	'''
	Instances in array
	'''
	@property
	def instances_array(self) :
		try:
			return self._instances_array
		except Exception as e :
			raise e
	'''
	Instances in array
	'''
	@instances_array.setter
	def instances_array(self,instances_array) :
		try :
			if not isinstance(instances_array,list):
				raise TypeError("instances_array must be set to array of str value")
			for item in instances_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._instances_array = instances_array
		except Exception as e :
			raise e

	'''
	Entities (Virtual servers or Network Interfaces)
	'''
	@property
	def entities_array(self) :
		try:
			return self._entities_array
		except Exception as e :
			raise e
	'''
	Entities (Virtual servers or Network Interfaces)
	'''
	@entities_array.setter
	def entities_array(self,entities_array) :
		try :
			if not isinstance(entities_array,list):
				raise TypeError("entities_array must be set to array of str value")
			for item in entities_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._entities_array = entities_array
		except Exception as e :
			raise e

	'''
	add perf custom dashboard configurationn.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				perf_custom_dashboard_obj= perf_custom_dashboard()
				return cls.perform_operation_bulk_request(service,resource,perf_custom_dashboard_obj)
		except Exception as e :
			raise e

	'''
	get perf custom dashboard configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				perf_custom_dashboard_obj=perf_custom_dashboard()
				response = perf_custom_dashboard_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Delete perf custom dashboard configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					perf_custom_dashboard_obj=perf_custom_dashboard()
					return cls.delete_bulk_request(client,resource,perf_custom_dashboard_obj)
		except Exception as e :
			raise e

	'''
	modify perf custom dashboard configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				perf_custom_dashboard_obj=perf_custom_dashboard()
				return cls.update_bulk_request(client,resource,perf_custom_dashboard_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_custom_dashboard resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_custom_dashboard_obj = perf_custom_dashboard()
			option_ = options()
			option_._filter=filter_
			return perf_custom_dashboard_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_custom_dashboard resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_custom_dashboard_obj = perf_custom_dashboard()
			option_ = options()
			option_._count=True
			response = perf_custom_dashboard_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_custom_dashboard resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_custom_dashboard_obj = perf_custom_dashboard()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_custom_dashboard_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_custom_dashboard_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_custom_dashboard
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_custom_dashboard_responses, response, "perf_custom_dashboard_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_custom_dashboard_response_array
				i=0
				error = [perf_custom_dashboard() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_custom_dashboard_response_array
			i=0
			perf_custom_dashboard_objs = [perf_custom_dashboard() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_custom_dashboard'):
					for props in obj._perf_custom_dashboard:
						result = service.payload_formatter.string_to_bulk_resource(perf_custom_dashboard_response,self.__class__.__name__,props)
						perf_custom_dashboard_objs[i] = result.perf_custom_dashboard
						i=i+1
			return perf_custom_dashboard_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_custom_dashboard,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_custom_dashboard_response(base_response):
	def __init__(self,length=1) :
		self.perf_custom_dashboard= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_custom_dashboard= [ perf_custom_dashboard() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_custom_dashboard_responses(base_response):
	def __init__(self,length=1) :
		self.perf_custom_dashboard_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_custom_dashboard_response_array = [ perf_custom_dashboard() for _ in range(length)]
