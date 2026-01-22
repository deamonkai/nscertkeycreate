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
Configuration for get-post las_lic_activate resource
'''

class las_lic_activate(base_resource):
	_action= ""
	_std_capacity= ""
	_nsip= ""
	_instance= ""
	_hostname= ""
	_lsactivationblobtoken= ""
	_nstype= ""
	_plt_capacity= ""
	_ent_capacity= ""
	_lpeid= ""
	_agent_id= ""
	_burnin_date= ""
	_ver= ""
	_requestutc= ""
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
			return "las_lic_activate"
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
			return "las_lic_activates"
		except Exception as e :
			raise e


	'''
	type of call: initial, push, refresh
	'''
	@property
	def action(self):
		try:
			return self._action
		except Exception as e :
			raise e
	'''
	type of call: initial, push, refresh
	'''
	@action.setter
	def action(self,action):
		try :
			if not isinstance(action,str):
				raise TypeError("action must be set to str value")
			self._action = action
		except Exception as e :
			raise e

	'''
	NS Param: std_capacity
	'''
	@property
	def std_capacity(self):
		try:
			return self._std_capacity
		except Exception as e :
			raise e

	'''
	NS Param: nsip
	'''
	@property
	def nsip(self):
		try:
			return self._nsip
		except Exception as e :
			raise e

	'''
	NS Param: instance
	'''
	@property
	def instance(self):
		try:
			return self._instance
		except Exception as e :
			raise e
	'''
	NS Param: instance
	'''
	@instance.setter
	def instance(self,instance):
		try :
			if not isinstance(instance,int):
				raise TypeError("instance must be set to int value")
			self._instance = instance
		except Exception as e :
			raise e

	'''
	NS Param: host name
	'''
	@property
	def hostname(self):
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	NS Param: host name
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e

	'''
	ADM Param: adm_signed_token
	'''
	@property
	def lsactivationblobtoken(self):
		try:
			return self._lsactivationblobtoken
		except Exception as e :
			raise e
	'''
	ADM Param: adm_signed_token
	'''
	@lsactivationblobtoken.setter
	def lsactivationblobtoken(self,lsactivationblobtoken):
		try :
			if not isinstance(lsactivationblobtoken,str):
				raise TypeError("lsactivationblobtoken must be set to str value")
			self._lsactivationblobtoken = lsactivationblobtoken
		except Exception as e :
			raise e

	'''
	NS Param: Netscaler Form Factor
	'''
	@property
	def nstype(self):
		try:
			return self._nstype
		except Exception as e :
			raise e
	'''
	NS Param: Netscaler Form Factor
	'''
	@nstype.setter
	def nstype(self,nstype):
		try :
			if not isinstance(nstype,str):
				raise TypeError("nstype must be set to str value")
			self._nstype = nstype
		except Exception as e :
			raise e

	'''
	NS Param: plt_capacity
	'''
	@property
	def plt_capacity(self):
		try:
			return self._plt_capacity
		except Exception as e :
			raise e

	'''
	NS Param: ent_capacity
	'''
	@property
	def ent_capacity(self):
		try:
			return self._ent_capacity
		except Exception as e :
			raise e

	'''
	NS Param: lpeId
	'''
	@property
	def lpeid(self):
		try:
			return self._lpeid
		except Exception as e :
			raise e
	'''
	NS Param: lpeId
	'''
	@lpeid.setter
	def lpeid(self,lpeid):
		try :
			if not isinstance(lpeid,str):
				raise TypeError("lpeid must be set to str value")
			self._lpeid = lpeid
		except Exception as e :
			raise e

	'''
	ADM Param: agent_id
	'''
	@property
	def agent_id(self):
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	ADM Param: agent_id
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e

	'''
	NS Param: ns burnin date
	'''
	@property
	def burnin_date(self):
		try:
			return self._burnin_date
		except Exception as e :
			raise e
	'''
	NS Param: ns burnin date
	'''
	@burnin_date.setter
	def burnin_date(self,burnin_date):
		try :
			if not isinstance(burnin_date,str):
				raise TypeError("burnin_date must be set to str value")
			self._burnin_date = burnin_date
		except Exception as e :
			raise e

	'''
	NS Param: version
	'''
	@property
	def ver(self):
		try:
			return self._ver
		except Exception as e :
			raise e
	'''
	NS Param: version
	'''
	@ver.setter
	def ver(self,ver):
		try :
			if not isinstance(ver,str):
				raise TypeError("ver must be set to str value")
			self._ver = ver
		except Exception as e :
			raise e

	'''
	NS Param: request UTC
	'''
	@property
	def requestutc(self):
		try:
			return self._requestutc
		except Exception as e :
			raise e
	'''
	NS Param: request UTC
	'''
	@requestutc.setter
	def requestutc(self,requestutc):
		try :
			if not isinstance(requestutc,long):
				raise TypeError("requestutc must be set to long value")
			self._requestutc = requestutc
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_activate_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_lic_activate
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_activate_responses, response, "las_lic_activate_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_lic_activate_response_array
				i=0
				error = [las_lic_activate() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_lic_activate_response_array
			i=0
			las_lic_activate_objs = [las_lic_activate() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_lic_activate'):
					for props in obj._las_lic_activate:
						result = service.payload_formatter.string_to_bulk_resource(las_lic_activate_response,self.__class__.__name__,props)
						las_lic_activate_objs[i] = result.las_lic_activate
						i=i+1
			return las_lic_activate_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_lic_activate,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_lic_activate_response(base_response):
	def __init__(self,length=1) :
		self.las_lic_activate= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_lic_activate= [ las_lic_activate() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_lic_activate_responses(base_response):
	def __init__(self,length=1) :
		self.las_lic_activate_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_lic_activate_response_array = [ las_lic_activate() for _ in range(length)]
