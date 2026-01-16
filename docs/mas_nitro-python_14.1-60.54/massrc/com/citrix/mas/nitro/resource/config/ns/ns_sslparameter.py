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
Configuration for NetScaler SSL Parameter resource
'''

class ns_sslparameter(base_resource):
	_sendclosenotify= ""
	_poll_time= ""
	_quantumsize= ""
	_defaultprofile= ""
	_denysslreneg= ""
	_encrypttriggerpktcount= ""
	_ns_ip_address= ""
	_snihttphostmatch= ""
	_pushenctriggertimeout= ""
	_insertionencoding= ""
	_pushflag= ""
	_dropreqwithnohostheader= ""
	_ssltriggertimeout= ""
	_partition_name= ""
	_display_name= ""
	_strictcachecks= ""
	_id= ""
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
			return "ns_sslparameter"
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
			return "ns_sslparameters"
		except Exception as e :
			raise e



	'''
	get sendclosenotify
	'''
	@property
	def sendclosenotify(self) :
		try:
			return self._sendclosenotify
		except Exception as e :
			raise e
	'''
	set sendclosenotify
	'''
	@sendclosenotify.setter
	def sendclosenotify(self,sendclosenotify):
		try :
			if not isinstance(sendclosenotify,str):
				raise TypeError("sendclosenotify must be set to str value")
			self._sendclosenotify = sendclosenotify
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get quantumsize
	'''
	@property
	def quantumsize(self) :
		try:
			return self._quantumsize
		except Exception as e :
			raise e
	'''
	set quantumsize
	'''
	@quantumsize.setter
	def quantumsize(self,quantumsize):
		try :
			if not isinstance(quantumsize,int):
				raise TypeError("quantumsize must be set to int value")
			self._quantumsize = quantumsize
		except Exception as e :
			raise e


	'''
	get defaultprofile
	'''
	@property
	def defaultprofile(self) :
		try:
			return self._defaultprofile
		except Exception as e :
			raise e
	'''
	set defaultprofile
	'''
	@defaultprofile.setter
	def defaultprofile(self,defaultprofile):
		try :
			if not isinstance(defaultprofile,bool):
				raise TypeError("defaultprofile must be set to bool value")
			self._defaultprofile = defaultprofile
		except Exception as e :
			raise e


	'''
	get denysslreneg
	'''
	@property
	def denysslreneg(self) :
		try:
			return self._denysslreneg
		except Exception as e :
			raise e
	'''
	set denysslreneg
	'''
	@denysslreneg.setter
	def denysslreneg(self,denysslreneg):
		try :
			if not isinstance(denysslreneg,str):
				raise TypeError("denysslreneg must be set to str value")
			self._denysslreneg = denysslreneg
		except Exception as e :
			raise e


	'''
	get encrypttriggerpktcount
	'''
	@property
	def encrypttriggerpktcount(self) :
		try:
			return self._encrypttriggerpktcount
		except Exception as e :
			raise e
	'''
	set encrypttriggerpktcount
	'''
	@encrypttriggerpktcount.setter
	def encrypttriggerpktcount(self,encrypttriggerpktcount):
		try :
			if not isinstance(encrypttriggerpktcount,int):
				raise TypeError("encrypttriggerpktcount must be set to int value")
			self._encrypttriggerpktcount = encrypttriggerpktcount
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get snihttphostmatch
	'''
	@property
	def snihttphostmatch(self) :
		try:
			return self._snihttphostmatch
		except Exception as e :
			raise e
	'''
	set snihttphostmatch
	'''
	@snihttphostmatch.setter
	def snihttphostmatch(self,snihttphostmatch):
		try :
			if not isinstance(snihttphostmatch,str):
				raise TypeError("snihttphostmatch must be set to str value")
			self._snihttphostmatch = snihttphostmatch
		except Exception as e :
			raise e


	'''
	get pushenctriggertimeout
	'''
	@property
	def pushenctriggertimeout(self) :
		try:
			return self._pushenctriggertimeout
		except Exception as e :
			raise e
	'''
	set pushenctriggertimeout
	'''
	@pushenctriggertimeout.setter
	def pushenctriggertimeout(self,pushenctriggertimeout):
		try :
			if not isinstance(pushenctriggertimeout,int):
				raise TypeError("pushenctriggertimeout must be set to int value")
			self._pushenctriggertimeout = pushenctriggertimeout
		except Exception as e :
			raise e


	'''
	get insertionencoding
	'''
	@property
	def insertionencoding(self) :
		try:
			return self._insertionencoding
		except Exception as e :
			raise e
	'''
	set insertionencoding
	'''
	@insertionencoding.setter
	def insertionencoding(self,insertionencoding):
		try :
			if not isinstance(insertionencoding,str):
				raise TypeError("insertionencoding must be set to str value")
			self._insertionencoding = insertionencoding
		except Exception as e :
			raise e


	'''
	get pushflag
	'''
	@property
	def pushflag(self) :
		try:
			return self._pushflag
		except Exception as e :
			raise e
	'''
	set pushflag
	'''
	@pushflag.setter
	def pushflag(self,pushflag):
		try :
			if not isinstance(pushflag,int):
				raise TypeError("pushflag must be set to int value")
			self._pushflag = pushflag
		except Exception as e :
			raise e


	'''
	get dropreqwithnohostheader
	'''
	@property
	def dropreqwithnohostheader(self) :
		try:
			return self._dropreqwithnohostheader
		except Exception as e :
			raise e
	'''
	set dropreqwithnohostheader
	'''
	@dropreqwithnohostheader.setter
	def dropreqwithnohostheader(self,dropreqwithnohostheader):
		try :
			if not isinstance(dropreqwithnohostheader,str):
				raise TypeError("dropreqwithnohostheader must be set to str value")
			self._dropreqwithnohostheader = dropreqwithnohostheader
		except Exception as e :
			raise e


	'''
	get ssltriggertimeout
	'''
	@property
	def ssltriggertimeout(self) :
		try:
			return self._ssltriggertimeout
		except Exception as e :
			raise e
	'''
	set ssltriggertimeout
	'''
	@ssltriggertimeout.setter
	def ssltriggertimeout(self,ssltriggertimeout):
		try :
			if not isinstance(ssltriggertimeout,int):
				raise TypeError("ssltriggertimeout must be set to int value")
			self._ssltriggertimeout = ssltriggertimeout
		except Exception as e :
			raise e


	'''
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get strictcachecks
	'''
	@property
	def strictcachecks(self) :
		try:
			return self._strictcachecks
		except Exception as e :
			raise e
	'''
	set strictcachecks
	'''
	@strictcachecks.setter
	def strictcachecks(self,strictcachecks):
		try :
			if not isinstance(strictcachecks,str):
				raise TypeError("strictcachecks must be set to str value")
			self._strictcachecks = strictcachecks
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	Use this operation to get SSL Parameter Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_sslparameter_obj=ns_sslparameter()
				response = ns_sslparameter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_sslparameter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_sslparameter_obj = ns_sslparameter()
			option_ = options()
			option_._filter=filter_
			return ns_sslparameter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_sslparameter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_sslparameter_obj = ns_sslparameter()
			option_ = options()
			option_._count=True
			response = ns_sslparameter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_sslparameter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_sslparameter_obj = ns_sslparameter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_sslparameter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_sslparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sslparameter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sslparameter_responses, response, "ns_sslparameter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sslparameter_response_array
				i=0
				error = [ns_sslparameter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sslparameter_response_array
			i=0
			ns_sslparameter_objs = [ns_sslparameter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sslparameter'):
					for props in obj._ns_sslparameter:
						result = service.payload_formatter.string_to_bulk_resource(ns_sslparameter_response,self.__class__.__name__,props)
						ns_sslparameter_objs[i] = result.ns_sslparameter
						i=i+1
			return ns_sslparameter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sslparameter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sslparameter_response(base_response):
	def __init__(self,length=1) :
		self.ns_sslparameter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sslparameter= [ ns_sslparameter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sslparameter_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sslparameter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sslparameter_response_array = [ ns_sslparameter() for _ in range(length)]
