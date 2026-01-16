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
Configuration for MPS Agent diag information resource
'''

class mps_agent_diag(base_resource):
	_cas= ""
	_id= ""
	_geo= ""
	_download= ""
	_dns= ""
	_s3= ""
	_grp= ""
	_agent= ""
	_trust= ""
	_pop= ""
	_endtime= ""
	_proxy= ""
	_adm= ""
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
			return "mps_agent_diag"
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
			return "mps_agent_diags"
		except Exception as e :
			raise e



	'''
	get Agent diag cas endpoint state
	'''
	@property
	def cas(self) :
		try:
			return self._cas
		except Exception as e :
			raise e
	'''
	set Agent diag cas endpoint state
	'''
	@cas.setter
	def cas(self,cas):
		try :
			if not isinstance(cas,int):
				raise TypeError("cas must be set to int value")
			self._cas = cas
		except Exception as e :
			raise e


	'''
	get Id is the agent id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is the agent id
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
	get agent pop geo information
	'''
	@property
	def geo(self) :
		try:
			return self._geo
		except Exception as e :
			raise e
	'''
	set agent pop geo information
	'''
	@geo.setter
	def geo(self,geo):
		try :
			if not isinstance(geo,str):
				raise TypeError("geo must be set to str value")
			self._geo = geo
		except Exception as e :
			raise e


	'''
	get Agent diag download.citrixnetworkapi.net state
	'''
	@property
	def download(self) :
		try:
			return self._download
		except Exception as e :
			raise e
	'''
	set Agent diag download.citrixnetworkapi.net state
	'''
	@download.setter
	def download(self,download):
		try :
			if not isinstance(download,int):
				raise TypeError("download must be set to int value")
			self._download = download
		except Exception as e :
			raise e


	'''
	get Agent diag DNS state
	'''
	@property
	def dns(self) :
		try:
			return self._dns
		except Exception as e :
			raise e
	'''
	set Agent diag DNS state
	'''
	@dns.setter
	def dns(self,dns):
		try :
			if not isinstance(dns,int):
				raise TypeError("dns must be set to int value")
			self._dns = dns
		except Exception as e :
			raise e


	'''
	get Agent diag s3 endpoint state
	'''
	@property
	def s3(self) :
		try:
			return self._s3
		except Exception as e :
			raise e
	'''
	set Agent diag s3 endpoint state
	'''
	@s3.setter
	def s3(self,s3):
		try :
			if not isinstance(s3,int):
				raise TypeError("s3 must be set to int value")
			self._s3 = s3
		except Exception as e :
			raise e


	'''
	get Agent diag adm.cloud.com state
	'''
	@property
	def grp(self) :
		try:
			return self._grp
		except Exception as e :
			raise e
	'''
	set Agent diag adm.cloud.com state
	'''
	@grp.setter
	def grp(self,grp):
		try :
			if not isinstance(grp,int):
				raise TypeError("grp must be set to int value")
			self._grp = grp
		except Exception as e :
			raise e


	'''
	get Agent diag adm.cloud.com state
	'''
	@property
	def agent(self) :
		try:
			return self._agent
		except Exception as e :
			raise e
	'''
	set Agent diag adm.cloud.com state
	'''
	@agent.setter
	def agent(self,agent):
		try :
			if not isinstance(agent,int):
				raise TypeError("agent must be set to int value")
			self._agent = agent
		except Exception as e :
			raise e


	'''
	get Agent diag trust.citrixnetworkapi.net state
	'''
	@property
	def trust(self) :
		try:
			return self._trust
		except Exception as e :
			raise e
	'''
	set Agent diag trust.citrixnetworkapi.net state
	'''
	@trust.setter
	def trust(self,trust):
		try :
			if not isinstance(trust,int):
				raise TypeError("trust must be set to int value")
			self._trust = trust
		except Exception as e :
			raise e


	'''
	get agent pop information
	'''
	@property
	def pop(self) :
		try:
			return self._pop
		except Exception as e :
			raise e
	'''
	set agent pop information
	'''
	@pop.setter
	def pop(self,pop):
		try :
			if not isinstance(pop,str):
				raise TypeError("pop must be set to str value")
			self._pop = pop
		except Exception as e :
			raise e


	'''
	get endtime of the agent diag
	'''
	@property
	def endtime(self) :
		try:
			return self._endtime
		except Exception as e :
			raise e
	'''
	set endtime of the agent diag
	'''
	@endtime.setter
	def endtime(self,endtime):
		try :
			if not isinstance(endtime,str):
				raise TypeError("endtime must be set to str value")
			self._endtime = endtime
		except Exception as e :
			raise e


	'''
	get Agent diag proxy configured or not
	'''
	@property
	def proxy(self) :
		try:
			return self._proxy
		except Exception as e :
			raise e
	'''
	set Agent diag proxy configured or not
	'''
	@proxy.setter
	def proxy(self,proxy):
		try :
			if not isinstance(proxy,int):
				raise TypeError("proxy must be set to int value")
			self._proxy = proxy
		except Exception as e :
			raise e


	'''
	get Agent diag adm.cloud.com state
	'''
	@property
	def adm(self) :
		try:
			return self._adm
		except Exception as e :
			raise e
	'''
	set Agent diag adm.cloud.com state
	'''
	@adm.setter
	def adm(self,adm):
		try :
			if not isinstance(adm,int):
				raise TypeError("adm must be set to int value")
			self._adm = adm
		except Exception as e :
			raise e

	'''
	Use this operation to delete Agent diag information.
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
					mps_agent_diag_obj=mps_agent_diag()
					return cls.delete_bulk_request(client,resource,mps_agent_diag_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent diag information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_agent_diag_obj=mps_agent_diag()
				response = mps_agent_diag_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add Agent diag information.
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
				mps_agent_diag_obj= mps_agent_diag()
				return cls.perform_operation_bulk_request(service,resource,mps_agent_diag_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_agent_diag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_agent_diag_obj = mps_agent_diag()
			option_ = options()
			option_._filter=filter_
			return mps_agent_diag_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_agent_diag resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_agent_diag_obj = mps_agent_diag()
			option_ = options()
			option_._count=True
			response = mps_agent_diag_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_agent_diag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_agent_diag_obj = mps_agent_diag()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_agent_diag_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_agent_diag_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_agent_diag
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_agent_diag_responses, response, "mps_agent_diag_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_agent_diag_response_array
				i=0
				error = [mps_agent_diag() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_agent_diag_response_array
			i=0
			mps_agent_diag_objs = [mps_agent_diag() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_agent_diag'):
					for props in obj._mps_agent_diag:
						result = service.payload_formatter.string_to_bulk_resource(mps_agent_diag_response,self.__class__.__name__,props)
						mps_agent_diag_objs[i] = result.mps_agent_diag
						i=i+1
			return mps_agent_diag_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_agent_diag,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_agent_diag_response(base_response):
	def __init__(self,length=1) :
		self.mps_agent_diag= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_agent_diag= [ mps_agent_diag() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_agent_diag_responses(base_response):
	def __init__(self,length=1) :
		self.mps_agent_diag_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_agent_diag_response_array = [ mps_agent_diag() for _ in range(length)]
