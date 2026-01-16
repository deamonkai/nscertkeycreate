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
from massrc.com.citrix.mas.nitro.resource.config.mps.entity_map import entity_map


'''
Configuration for Site resource
'''

class mps_datacenter(base_resource):
	_itm_radar_rum= ""
	_itm_radar_region= ""
	_itm_radar_url= ""
	_tenant_id= ""
	_type= ""
	_country= ""
	_region= ""
	_name= ""
	_cloud_region= ""
	_cloud_provider= ""
	_city= ""
	_cloud_vpc= ""
	_latitude= ""
	_longitude= ""
	_id= ""
	_location= ""
	_zipcode= ""
	_itm_radar_instance_id= ""
	_count_map=[]
	_total_major_events= ""
	_device_ip= ""
	_total_number_of_devices= ""
	_application_name= ""
	_total_critical_events= ""
	_total_events= ""
	_total_number_of_agents= ""
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
			return "mps_datacenter"
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
			return "mps_datacenters"
		except Exception as e :
			raise e



	'''
	get ITM Radar RUM enumeration to enable or not
	'''
	@property
	def itm_radar_rum(self) :
		try:
			return self._itm_radar_rum
		except Exception as e :
			raise e
	'''
	set ITM Radar RUM enumeration to enable or not
	'''
	@itm_radar_rum.setter
	def itm_radar_rum(self,itm_radar_rum):
		try :
			if not isinstance(itm_radar_rum,str):
				raise TypeError("itm_radar_rum must be set to str value")
			self._itm_radar_rum = itm_radar_rum
		except Exception as e :
			raise e


	'''
	get The public cloud region value for ITM Radat
	'''
	@property
	def itm_radar_region(self) :
		try:
			return self._itm_radar_region
		except Exception as e :
			raise e
	'''
	set The public cloud region value for ITM Radat
	'''
	@itm_radar_region.setter
	def itm_radar_region(self,itm_radar_region):
		try :
			if not isinstance(itm_radar_region,str):
				raise TypeError("itm_radar_region must be set to str value")
			self._itm_radar_region = itm_radar_region
		except Exception as e :
			raise e


	'''
	get ITM Radar endpoint for an ADM site
	'''
	@property
	def itm_radar_url(self) :
		try:
			return self._itm_radar_url
		except Exception as e :
			raise e
	'''
	set ITM Radar endpoint for an ADM site
	'''
	@itm_radar_url.setter
	def itm_radar_url(self,itm_radar_url):
		try :
			if not isinstance(itm_radar_url,str):
				raise TypeError("itm_radar_url must be set to str value")
			self._itm_radar_url = itm_radar_url
		except Exception as e :
			raise e


	'''
	get Tenant ID
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant ID
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Datacenter type: Site/Datacenter
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Datacenter type: Site/Datacenter
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,int):
				raise TypeError("type must be set to int value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Name of the country
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set Name of the country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e


	'''
	get Name of the region
	'''
	@property
	def region(self) :
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	set Name of the region
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e


	'''
	get Datacentre Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Datacentre Name
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
	get cloud_region
	'''
	@property
	def cloud_region(self) :
		try:
			return self._cloud_region
		except Exception as e :
			raise e
	'''
	set cloud_region
	'''
	@cloud_region.setter
	def cloud_region(self,cloud_region):
		try :
			if not isinstance(cloud_region,str):
				raise TypeError("cloud_region must be set to str value")
			self._cloud_region = cloud_region
		except Exception as e :
			raise e


	'''
	get Cloud Provide
	'''
	@property
	def cloud_provider(self) :
		try:
			return self._cloud_provider
		except Exception as e :
			raise e
	'''
	set Cloud Provide
	'''
	@cloud_provider.setter
	def cloud_provider(self,cloud_provider):
		try :
			if not isinstance(cloud_provider,str):
				raise TypeError("cloud_provider must be set to str value")
			self._cloud_provider = cloud_provider
		except Exception as e :
			raise e


	'''
	get Name of the city
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set Name of the city
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e


	'''
	get cloud_vpc
	'''
	@property
	def cloud_vpc(self) :
		try:
			return self._cloud_vpc
		except Exception as e :
			raise e
	'''
	set cloud_vpc
	'''
	@cloud_vpc.setter
	def cloud_vpc(self,cloud_vpc):
		try :
			if not isinstance(cloud_vpc,str):
				raise TypeError("cloud_vpc must be set to str value")
			self._cloud_vpc = cloud_vpc
		except Exception as e :
			raise e


	'''
	get latitude of the city
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude of the city
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e


	'''
	get longitude of the city
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude of the city
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system users
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system users
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
	get Location Name
	'''
	@property
	def location(self) :
		try:
			return self._location
		except Exception as e :
			raise e
	'''
	set Location Name
	'''
	@location.setter
	def location(self,location):
		try :
			if not isinstance(location,str):
				raise TypeError("location must be set to str value")
			self._location = location
		except Exception as e :
			raise e


	'''
	get Zipcode of location
	'''
	@property
	def zipcode(self) :
		try:
			return self._zipcode
		except Exception as e :
			raise e
	'''
	set Zipcode of location
	'''
	@zipcode.setter
	def zipcode(self,zipcode):
		try :
			if not isinstance(zipcode,str):
				raise TypeError("zipcode must be set to str value")
			self._zipcode = zipcode
		except Exception as e :
			raise e


	'''
	get The Instance id of the target Netscaler in which the radar object will be deployed
	'''
	@property
	def itm_radar_instance_id(self) :
		try:
			return self._itm_radar_instance_id
		except Exception as e :
			raise e
	'''
	set The Instance id of the target Netscaler in which the radar object will be deployed
	'''
	@itm_radar_instance_id.setter
	def itm_radar_instance_id(self,itm_radar_instance_id):
		try :
			if not isinstance(itm_radar_instance_id,str):
				raise TypeError("itm_radar_instance_id must be set to str value")
			self._itm_radar_instance_id = itm_radar_instance_id
		except Exception as e :
			raise e

	'''
	Count Map
	'''
	@property
	def count_map(self) :
		try:
			return self._count_map
		except Exception as e :
			raise e
	'''
	Count Map
	'''
	@count_map.setter
	def count_map(self,count_map) :
		try :
			if not isinstance(count_map,list):
				raise TypeError("count_map must be set to array of entity_map value")
			for item in count_map :
				if not isinstance(item,entity_map):
					raise TypeError("item must be set to entity_map value")
			self._count_map = count_map
		except Exception as e :
			raise e

	'''
	Total major events.
	'''
	@property
	def total_major_events(self):
		try:
			return self._total_major_events
		except Exception as e :
			raise e

	'''
	Device Ip
	'''
	@property
	def device_ip(self):
		try:
			return self._device_ip
		except Exception as e :
			raise e
	'''
	Device Ip
	'''
	@device_ip.setter
	def device_ip(self,device_ip):
		try :
			if not isinstance(device_ip,str):
				raise TypeError("device_ip must be set to str value")
			self._device_ip = device_ip
		except Exception as e :
			raise e

	'''
	Total number of devices deployed city wise..
	'''
	@property
	def total_number_of_devices(self):
		try:
			return self._total_number_of_devices
		except Exception as e :
			raise e

	'''
	Application Name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e

	'''
	Total Critical events city wise.
	'''
	@property
	def total_critical_events(self):
		try:
			return self._total_critical_events
		except Exception as e :
			raise e

	'''
	Total events city wise.
	'''
	@property
	def total_events(self):
		try:
			return self._total_events
		except Exception as e :
			raise e

	'''
	Total number of agents deployed city wise.
	'''
	@property
	def total_number_of_agents(self):
		try:
			return self._total_number_of_agents
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_datacenter_obj=mps_datacenter()
				response = mps_datacenter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add Agent information.
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
				mps_datacenter_obj= mps_datacenter()
				return cls.perform_operation_bulk_request(service,resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify Agent information.
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
				mps_datacenter_obj=mps_datacenter()
				return cls.update_bulk_request(client,resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Agent information.
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
					mps_datacenter_obj=mps_datacenter()
					return cls.delete_bulk_request(client,resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_datacenter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._filter=filter_
			return mps_datacenter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_datacenter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._count=True
			response = mps_datacenter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_datacenter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_datacenter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_datacenter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_datacenter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_datacenter_responses, response, "mps_datacenter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_datacenter_response_array
				i=0
				error = [mps_datacenter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_datacenter_response_array
			i=0
			mps_datacenter_objs = [mps_datacenter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_datacenter'):
					for props in obj._mps_datacenter:
						result = service.payload_formatter.string_to_bulk_resource(mps_datacenter_response,self.__class__.__name__,props)
						mps_datacenter_objs[i] = result.mps_datacenter
						i=i+1
			return mps_datacenter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_datacenter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_datacenter_response(base_response):
	def __init__(self,length=1) :
		self.mps_datacenter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_datacenter= [ mps_datacenter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_datacenter_responses(base_response):
	def __init__(self,length=1) :
		self.mps_datacenter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_datacenter_response_array = [ mps_datacenter() for _ in range(length)]
