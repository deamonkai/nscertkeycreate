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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Provides info about Gateway users resource
'''

class geo_user_info(base_resource):
	_total_apps= ""
	_username= ""
	_total_bytes= ""
	_total_users= ""
	_ctnsappname= ""
	_session_id= ""
	_total_countries= ""
	_country_name= ""
	_total_sessions= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/gateway/geo_user_info"
		except Exception as e :
			raise e

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
			return "geo_user_info"
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
			return "geo_user_infos"
		except Exception as e :
			raise e



	'''
	get Total Apps
	'''
	@property
	def total_apps(self) :
		try:
			return self._total_apps
		except Exception as e :
			raise e
	'''
	set Total Apps
	'''
	@total_apps.setter
	def total_apps(self,total_apps):
		try :
			if not isinstance(total_apps,str):
				raise TypeError("total_apps must be set to str value")
			self._total_apps = total_apps
		except Exception as e :
			raise e


	'''
	get Username
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Username
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
	get Total Bytes
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Total Bytes
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,str):
				raise TypeError("total_bytes must be set to str value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get Total Users
	'''
	@property
	def total_users(self) :
		try:
			return self._total_users
		except Exception as e :
			raise e
	'''
	set Total Users
	'''
	@total_users.setter
	def total_users(self,total_users):
		try :
			if not isinstance(total_users,str):
				raise TypeError("total_users must be set to str value")
			self._total_users = total_users
		except Exception as e :
			raise e


	'''
	get Application name
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set Application name
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Session Id
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set Session Id
	'''
	@session_id.setter
	def session_id(self,session_id):
		try :
			if not isinstance(session_id,str):
				raise TypeError("session_id must be set to str value")
			self._session_id = session_id
		except Exception as e :
			raise e


	'''
	get Total Countries
	'''
	@property
	def total_countries(self) :
		try:
			return self._total_countries
		except Exception as e :
			raise e
	'''
	set Total Countries
	'''
	@total_countries.setter
	def total_countries(self,total_countries):
		try :
			if not isinstance(total_countries,str):
				raise TypeError("total_countries must be set to str value")
			self._total_countries = total_countries
		except Exception as e :
			raise e


	'''
	get Country Name
	'''
	@property
	def country_name(self) :
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	set Country Name
	'''
	@country_name.setter
	def country_name(self,country_name):
		try :
			if not isinstance(country_name,str):
				raise TypeError("country_name must be set to str value")
			self._country_name = country_name
		except Exception as e :
			raise e


	'''
	get Total Sessions
	'''
	@property
	def total_sessions(self) :
		try:
			return self._total_sessions
		except Exception as e :
			raise e
	'''
	set Total Sessions
	'''
	@total_sessions.setter
	def total_sessions(self,total_sessions):
		try :
			if not isinstance(total_sessions,str):
				raise TypeError("total_sessions must be set to str value")
			self._total_sessions = total_sessions
		except Exception as e :
			raise e


	'''
	get Report Sample time (epoch time)
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time (epoch time)
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,str):
				raise TypeError("rpt_sample_time must be set to str value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Provides info about Gateway users.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				geo_user_info_obj=geo_user_info()
				response = geo_user_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of geo_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			geo_user_info_obj = geo_user_info()
			option_ = options()
			option_._filter=filter_
			return geo_user_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the geo_user_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			geo_user_info_obj = geo_user_info()
			option_ = options()
			option_._count=True
			response = geo_user_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of geo_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			geo_user_info_obj = geo_user_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = geo_user_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(geo_user_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.geo_user_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(geo_user_info_responses, response, "geo_user_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.geo_user_info_response_array
				i=0
				error = [geo_user_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.geo_user_info_response_array
			i=0
			geo_user_info_objs = [geo_user_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_geo_user_info'):
					for props in obj._geo_user_info:
						result = service.payload_formatter.string_to_bulk_resource(geo_user_info_response,self.__class__.__name__,props)
						geo_user_info_objs[i] = result.geo_user_info
						i=i+1
			return geo_user_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(geo_user_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class geo_user_info_response(base_response):
	def __init__(self,length=1) :
		self.geo_user_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.geo_user_info= [ geo_user_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class geo_user_info_responses(base_response):
	def __init__(self,length=1) :
		self.geo_user_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.geo_user_info_response_array = [ geo_user_info() for _ in range(length)]
