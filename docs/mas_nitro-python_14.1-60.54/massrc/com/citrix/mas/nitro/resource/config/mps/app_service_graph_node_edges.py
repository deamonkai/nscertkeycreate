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
Configuration for API used to report the global service graph for per app. resource
'''

class app_service_graph_node_edges(base_resource):
	_tot_svr_ttfb_transactions= ""
	_tot_svr_busy_err= ""
	_ctnsappname= ""
	_destination= ""
	_destination_type= ""
	_tot_bytes= ""
	_tot_svr_ttfb= ""
	_source= ""
	_response_time= ""
	_tot_requests= ""
	_id= ""
	_svcname= ""
	_appname= ""
	_tot_respbytes= ""
	_source_type= ""
	_type= ""
	_tot_reqbytes= ""
	_vservername= ""
	_ip_address= ""
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
			return "app_service_graph_node_edges"
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
			return "app_service_graph_node_edgess"
		except Exception as e :
			raise e



	'''
	get Number of Transactions
	'''
	@property
	def tot_svr_ttfb_transactions(self) :
		try:
			return self._tot_svr_ttfb_transactions
		except Exception as e :
			raise e
	'''
	set Number of Transactions
	'''
	@tot_svr_ttfb_transactions.setter
	def tot_svr_ttfb_transactions(self,tot_svr_ttfb_transactions):
		try :
			if not isinstance(tot_svr_ttfb_transactions,long):
				raise TypeError("tot_svr_ttfb_transactions must be set to long value")
			self._tot_svr_ttfb_transactions = tot_svr_ttfb_transactions
		except Exception as e :
			raise e


	'''
	get Total Server Errors
	'''
	@property
	def tot_svr_busy_err(self) :
		try:
			return self._tot_svr_busy_err
		except Exception as e :
			raise e
	'''
	set Total Server Errors
	'''
	@tot_svr_busy_err.setter
	def tot_svr_busy_err(self,tot_svr_busy_err):
		try :
			if not isinstance(tot_svr_busy_err,long):
				raise TypeError("tot_svr_busy_err must be set to long value")
			self._tot_svr_busy_err = tot_svr_busy_err
		except Exception as e :
			raise e


	'''
	get Vserver Name
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set Vserver Name
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
	get CS VServer Name
	'''
	@property
	def destination(self) :
		try:
			return self._destination
		except Exception as e :
			raise e
	'''
	set CS VServer Name
	'''
	@destination.setter
	def destination(self,destination):
		try :
			if not isinstance(destination,str):
				raise TypeError("destination must be set to str value")
			self._destination = destination
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def destination_type(self) :
		try:
			return self._destination_type
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@destination_type.setter
	def destination_type(self,destination_type):
		try :
			if not isinstance(destination_type,str):
				raise TypeError("destination_type must be set to str value")
			self._destination_type = destination_type
		except Exception as e :
			raise e


	'''
	get Total Bytes(Data Volume)
	'''
	@property
	def tot_bytes(self) :
		try:
			return self._tot_bytes
		except Exception as e :
			raise e
	'''
	set Total Bytes(Data Volume)
	'''
	@tot_bytes.setter
	def tot_bytes(self,tot_bytes):
		try :
			if not isinstance(tot_bytes,long):
				raise TypeError("tot_bytes must be set to long value")
			self._tot_bytes = tot_bytes
		except Exception as e :
			raise e


	'''
	get Service Resp Rate
	'''
	@property
	def tot_svr_ttfb(self) :
		try:
			return self._tot_svr_ttfb
		except Exception as e :
			raise e
	'''
	set Service Resp Rate
	'''
	@tot_svr_ttfb.setter
	def tot_svr_ttfb(self,tot_svr_ttfb):
		try :
			if not isinstance(tot_svr_ttfb,long):
				raise TypeError("tot_svr_ttfb must be set to long value")
			self._tot_svr_ttfb = tot_svr_ttfb
		except Exception as e :
			raise e


	'''
	get Source Node
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source Node
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e


	'''
	get Response Time
	'''
	@property
	def response_time(self) :
		try:
			return self._response_time
		except Exception as e :
			raise e
	'''
	set Response Time
	'''
	@response_time.setter
	def response_time(self,response_time):
		try :
			if not isinstance(response_time,float):
				raise TypeError("response_time must be set to float value")
			self._response_time = response_time
		except Exception as e :
			raise e


	'''
	get Total Requests
	'''
	@property
	def tot_requests(self) :
		try:
			return self._tot_requests
		except Exception as e :
			raise e
	'''
	set Total Requests
	'''
	@tot_requests.setter
	def tot_requests(self,tot_requests):
		try :
			if not isinstance(tot_requests,long):
				raise TypeError("tot_requests must be set to long value")
			self._tot_requests = tot_requests
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
	get Service Name
	'''
	@property
	def svcname(self) :
		try:
			return self._svcname
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@svcname.setter
	def svcname(self,svcname):
		try :
			if not isinstance(svcname,str):
				raise TypeError("svcname must be set to str value")
			self._svcname = svcname
		except Exception as e :
			raise e


	'''
	get App name
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set App name
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get Total Response Bytes
	'''
	@property
	def tot_respbytes(self) :
		try:
			return self._tot_respbytes
		except Exception as e :
			raise e
	'''
	set Total Response Bytes
	'''
	@tot_respbytes.setter
	def tot_respbytes(self,tot_respbytes):
		try :
			if not isinstance(tot_respbytes,long):
				raise TypeError("tot_respbytes must be set to long value")
			self._tot_respbytes = tot_respbytes
		except Exception as e :
			raise e


	'''
	get LB VServer Name
	'''
	@property
	def source_type(self) :
		try:
			return self._source_type
		except Exception as e :
			raise e
	'''
	set LB VServer Name
	'''
	@source_type.setter
	def source_type(self,source_type):
		try :
			if not isinstance(source_type,str):
				raise TypeError("source_type must be set to str value")
			self._source_type = source_type
		except Exception as e :
			raise e


	'''
	get Vserver Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Vserver Type
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
	get Total Request Bytes
	'''
	@property
	def tot_reqbytes(self) :
		try:
			return self._tot_reqbytes
		except Exception as e :
			raise e
	'''
	set Total Request Bytes
	'''
	@tot_reqbytes.setter
	def tot_reqbytes(self,tot_reqbytes):
		try :
			if not isinstance(tot_reqbytes,long):
				raise TypeError("tot_reqbytes must be set to long value")
			self._tot_reqbytes = tot_reqbytes
		except Exception as e :
			raise e


	'''
	get Vserver Name
	'''
	@property
	def vservername(self) :
		try:
			return self._vservername
		except Exception as e :
			raise e
	'''
	set Vserver Name
	'''
	@vservername.setter
	def vservername(self,vservername):
		try :
			if not isinstance(vservername,str):
				raise TypeError("vservername must be set to str value")
			self._vservername = vservername
		except Exception as e :
			raise e


	'''
	get NS IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set NS IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Reports the global service graph for multi apps.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				app_service_graph_node_edges_obj=app_service_graph_node_edges()
				response = app_service_graph_node_edges_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_service_graph_node_edges resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_service_graph_node_edges_obj = app_service_graph_node_edges()
			option_ = options()
			option_._filter=filter_
			return app_service_graph_node_edges_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_service_graph_node_edges resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_service_graph_node_edges_obj = app_service_graph_node_edges()
			option_ = options()
			option_._count=True
			response = app_service_graph_node_edges_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_service_graph_node_edges resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_service_graph_node_edges_obj = app_service_graph_node_edges()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_service_graph_node_edges_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(app_service_graph_node_edges_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_service_graph_node_edges
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_service_graph_node_edges_responses, response, "app_service_graph_node_edges_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_service_graph_node_edges_response_array
				i=0
				error = [app_service_graph_node_edges() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_service_graph_node_edges_response_array
			i=0
			app_service_graph_node_edges_objs = [app_service_graph_node_edges() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_service_graph_node_edges'):
					for props in obj._app_service_graph_node_edges:
						result = service.payload_formatter.string_to_bulk_resource(app_service_graph_node_edges_response,self.__class__.__name__,props)
						app_service_graph_node_edges_objs[i] = result.app_service_graph_node_edges
						i=i+1
			return app_service_graph_node_edges_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_service_graph_node_edges,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_service_graph_node_edges_response(base_response):
	def __init__(self,length=1) :
		self.app_service_graph_node_edges= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_service_graph_node_edges= [ app_service_graph_node_edges() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_service_graph_node_edges_responses(base_response):
	def __init__(self,length=1) :
		self.app_service_graph_node_edges_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_service_graph_node_edges_response_array = [ app_service_graph_node_edges() for _ in range(length)]
