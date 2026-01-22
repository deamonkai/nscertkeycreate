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
from massrc.com.citrix.mas.nitro.resource.config.mps.las_certchain import las_certchain
from massrc.com.citrix.mas.nitro.resource.config.mps.las_signeddata import las_signeddata


'''
Configuration for get-post las license init resource
'''

class las_lic_init(base_resource):
	_lpeid= ""
	_cn= ""
	_ns_profile= ""
	_nstype= ""
	_ver= ""
	_agent_id= ""
	_burnin_date= ""
	_lstoken= ""
	_hostid= ""
	_ent_token= ""
	_certchain= ""
	_signeddata= ""
	_nsip= ""
	_hostname= ""
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
			return "las_lic_init"
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
			return "las_lic_inits"
		except Exception as e :
			raise e


	'''
	NS Param: Input lpeId
	'''
	@property
	def lpeid(self):
		try:
			return self._lpeid
		except Exception as e :
			raise e
	'''
	NS Param: Input lpeId
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
	Common name to use to get the LAS public key
	'''
	@property
	def cn(self):
		try:
			return self._cn
		except Exception as e :
			raise e
	'''
	Common name to use to get the LAS public key
	'''
	@cn.setter
	def cn(self,cn):
		try :
			if not isinstance(cn,str):
				raise TypeError("cn must be set to str value")
			self._cn = cn
		except Exception as e :
			raise e

	'''
	NS Param: Profile information for NS
	'''
	@property
	def ns_profile(self):
		try:
			return self._ns_profile
		except Exception as e :
			raise e
	'''
	NS Param: Profile information for NS
	'''
	@ns_profile.setter
	def ns_profile(self,ns_profile):
		try :
			if not isinstance(ns_profile,str):
				raise TypeError("ns_profile must be set to str value")
			self._ns_profile = ns_profile
		except Exception as e :
			raise e

	'''
	NS PARAM: nstype
	'''
	@property
	def nstype(self):
		try:
			return self._nstype
		except Exception as e :
			raise e
	'''
	NS PARAM: nstype
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
	ADM Response: las sign response ver
	'''
	@property
	def ver(self):
		try:
			return self._ver
		except Exception as e :
			raise e
	'''
	ADM Response: las sign response ver
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
	ADM Response: agent id
	'''
	@property
	def agent_id(self):
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	ADM Response: agent id
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
	ADM Response: ls details token
	'''
	@property
	def lstoken(self):
		try:
			return self._lstoken
		except Exception as e :
			raise e
	'''
	ADM Response: ls details token
	'''
	@lstoken.setter
	def lstoken(self,lstoken):
		try :
			if not isinstance(lstoken,str):
				raise TypeError("lstoken must be set to str value")
			self._lstoken = lstoken
		except Exception as e :
			raise e

	'''
	 NS param: host ID
	'''
	@property
	def hostid(self):
		try:
			return self._hostid
		except Exception as e :
			raise e
	'''
	 NS param: host ID
	'''
	@hostid.setter
	def hostid(self,hostid):
		try :
			if not isinstance(hostid,str):
				raise TypeError("hostid must be set to str value")
			self._hostid = hostid
		except Exception as e :
			raise e

	'''
	ADM Response: Entitlement Token
	'''
	@property
	def ent_token(self):
		try:
			return self._ent_token
		except Exception as e :
			raise e
	'''
	ADM Response: Entitlement Token
	'''
	@ent_token.setter
	def ent_token(self,ent_token):
		try :
			if not isinstance(ent_token,str):
				raise TypeError("ent_token must be set to str value")
			self._ent_token = ent_token
		except Exception as e :
			raise e

	'''
	ADM Response: las certchain
	'''
	@property
	def certchain(self):
		try:
			return self._certchain
		except Exception as e :
			raise e
	'''
	ADM Response: las certchain
	'''
	@certchain.setter
	def certchain(self,certchain):
		try :
			if not isinstance(certchain,las_certchain):
				raise TypeError("certchain must be set to las_certchain value")
			self._certchain = certchain
		except Exception as e :
			raise e

	'''
	ADM Response: signeddata as a key value pair
	'''
	@property
	def signeddata(self):
		try:
			return self._signeddata
		except Exception as e :
			raise e
	'''
	ADM Response: signeddata as a key value pair
	'''
	@signeddata.setter
	def signeddata(self,signeddata):
		try :
			if not isinstance(signeddata,las_signeddata):
				raise TypeError("signeddata must be set to las_signeddata value")
			self._signeddata = signeddata
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
	NS param: host name
	'''
	@property
	def hostname(self):
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	NS param: host name
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_init_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_lic_init
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_init_responses, response, "las_lic_init_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_lic_init_response_array
				i=0
				error = [las_lic_init() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_lic_init_response_array
			i=0
			las_lic_init_objs = [las_lic_init() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_lic_init'):
					for props in obj._las_lic_init:
						result = service.payload_formatter.string_to_bulk_resource(las_lic_init_response,self.__class__.__name__,props)
						las_lic_init_objs[i] = result.las_lic_init
						i=i+1
			return las_lic_init_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_lic_init,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_lic_init_response(base_response):
	def __init__(self,length=1) :
		self.las_lic_init= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_lic_init= [ las_lic_init() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_lic_init_responses(base_response):
	def __init__(self,length=1) :
		self.las_lic_init_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_lic_init_response_array = [ las_lic_init() for _ in range(length)]
