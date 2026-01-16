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
Configuration for Virtual server appflow info on NetScaler resource
'''

class adc_vserver_appflow_info(base_resource):
	_name= ""
	_appflow_policy_rule= ""
	_transaction_log_effective= ""
	_es4nslog= ""
	_transport_mode= ""
	_client_header= ""
	_type= ""
	_netprofile= ""
	_ns_ip_address= ""
	_httpxforwardedfor= ""
	_export_option=[]
	_partition_name= ""
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
			return "adc_vserver_appflow_info"
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
			return "adc_vserver_appflow_infos"
		except Exception as e :
			raise e


	'''
	Virtual server name
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Virtual server name
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
	Appflow policy rule
	'''
	@property
	def appflow_policy_rule(self):
		try:
			return self._appflow_policy_rule
		except Exception as e :
			raise e
	'''
	Appflow policy rule
	'''
	@appflow_policy_rule.setter
	def appflow_policy_rule(self,appflow_policy_rule):
		try :
			if not isinstance(appflow_policy_rule,str):
				raise TypeError("appflow_policy_rule must be set to str value")
			self._appflow_policy_rule = appflow_policy_rule
		except Exception as e :
			raise e

	'''
	Transaction Log Enabled/Disabled
	'''
	@property
	def transaction_log_effective(self):
		try:
			return self._transaction_log_effective
		except Exception as e :
			raise e
	'''
	Transaction Log Enabled/Disabled
	'''
	@transaction_log_effective.setter
	def transaction_log_effective(self,transaction_log_effective):
		try :
			if not isinstance(transaction_log_effective,str):
				raise TypeError("transaction_log_effective must be set to str value")
			self._transaction_log_effective = transaction_log_effective
		except Exception as e :
			raise e

	'''
	ESNS enable
	'''
	@property
	def es4nslog(self):
		try:
			return self._es4nslog
		except Exception as e :
			raise e
	'''
	ESNS enable
	'''
	@es4nslog.setter
	def es4nslog(self,es4nslog):
		try :
			if not isinstance(es4nslog,str):
				raise TypeError("es4nslog must be set to str value")
			self._es4nslog = es4nslog
		except Exception as e :
			raise e

	'''
	Transport Mode [ Logstream/Appflow ]
	'''
	@property
	def transport_mode(self):
		try:
			return self._transport_mode
		except Exception as e :
			raise e
	'''
	Transport Mode [ Logstream/Appflow ]
	'''
	@transport_mode.setter
	def transport_mode(self,transport_mode):
		try :
			if not isinstance(transport_mode,str):
				raise TypeError("transport_mode must be set to str value")
			self._transport_mode = transport_mode
		except Exception as e :
			raise e

	'''
	Custom Client Header to Export
	'''
	@property
	def client_header(self):
		try:
			return self._client_header
		except Exception as e :
			raise e
	'''
	Custom Client Header to Export
	'''
	@client_header.setter
	def client_header(self,client_header):
		try :
			if not isinstance(client_header,str):
				raise TypeError("client_header must be set to str value")
			self._client_header = client_header
		except Exception as e :
			raise e

	'''
	Tells whether virtual server type
	'''
	@property
	def type(self):
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	Tells whether virtual server type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e

	'''
	Net Proile
	'''
	@property
	def netprofile(self):
		try:
			return self._netprofile
		except Exception as e :
			raise e
	'''
	Net Proile
	'''
	@netprofile.setter
	def netprofile(self,netprofile):
		try :
			if not isinstance(netprofile,str):
				raise TypeError("netprofile must be set to str value")
			self._netprofile = netprofile
		except Exception as e :
			raise e

	'''
	NetScaler IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
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
	X-Forwarded-For Header Export status
	'''
	@property
	def httpxforwardedfor(self):
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	X-Forwarded-For Header Export status
	'''
	@httpxforwardedfor.setter
	def httpxforwardedfor(self,httpxforwardedfor):
		try :
			if not isinstance(httpxforwardedfor,str):
				raise TypeError("httpxforwardedfor must be set to str value")
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e :
			raise e

	'''
	Export Options: TCP, ICA
	'''
	@property
	def export_option(self) :
		try:
			return self._export_option
		except Exception as e :
			raise e
	'''
	Export Options: TCP, ICA
	'''
	@export_option.setter
	def export_option(self,export_option) :
		try :
			if not isinstance(export_option,list):
				raise TypeError("export_option must be set to array of str value")
			for item in export_option :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._export_option = export_option
		except Exception as e :
			raise e

	'''
	Partition Name
	'''
	@property
	def partition_name(self):
		try:
			return self._partition_name
		except Exception as e :
			raise e

	'''
	delete virtual server policy.
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
					adc_vserver_appflow_info_obj=adc_vserver_appflow_info()
					return cls.delete_bulk_request(client,resource,adc_vserver_appflow_info_obj)
		except Exception as e :
			raise e

	'''
	get NA virtual server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_vserver_appflow_info_obj=adc_vserver_appflow_info()
				response = adc_vserver_appflow_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Add virtual server policy.
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
				adc_vserver_appflow_info_obj= adc_vserver_appflow_info()
				return cls.perform_operation_bulk_request(service,resource,adc_vserver_appflow_info_obj)
		except Exception as e :
			raise e

	'''
	modify virtual server policy.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				adc_vserver_appflow_info_obj=adc_vserver_appflow_info()
				return cls.update_bulk_request(client,resource,adc_vserver_appflow_info_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_vserver_appflow_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_vserver_appflow_info_obj = adc_vserver_appflow_info()
			option_ = options()
			option_._filter=filter_
			return adc_vserver_appflow_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_vserver_appflow_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_vserver_appflow_info_obj = adc_vserver_appflow_info()
			option_ = options()
			option_._count=True
			response = adc_vserver_appflow_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_vserver_appflow_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_vserver_appflow_info_obj = adc_vserver_appflow_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_vserver_appflow_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_vserver_appflow_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_vserver_appflow_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_vserver_appflow_info_responses, response, "adc_vserver_appflow_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_vserver_appflow_info_response_array
				i=0
				error = [adc_vserver_appflow_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_vserver_appflow_info_response_array
			i=0
			adc_vserver_appflow_info_objs = [adc_vserver_appflow_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_vserver_appflow_info'):
					for props in obj._adc_vserver_appflow_info:
						result = service.payload_formatter.string_to_bulk_resource(adc_vserver_appflow_info_response,self.__class__.__name__,props)
						adc_vserver_appflow_info_objs[i] = result.adc_vserver_appflow_info
						i=i+1
			return adc_vserver_appflow_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_vserver_appflow_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_vserver_appflow_info_response(base_response):
	def __init__(self,length=1) :
		self.adc_vserver_appflow_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_vserver_appflow_info= [ adc_vserver_appflow_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_vserver_appflow_info_responses(base_response):
	def __init__(self,length=1) :
		self.adc_vserver_appflow_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_vserver_appflow_info_response_array = [ adc_vserver_appflow_info() for _ in range(length)]
