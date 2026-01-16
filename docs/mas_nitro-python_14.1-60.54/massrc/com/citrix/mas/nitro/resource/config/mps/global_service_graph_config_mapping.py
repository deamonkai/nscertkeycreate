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
Configuration for Config Data for Global Service Graph resource
'''

class global_service_graph_config_mapping(base_resource):
	_lbvserver_name= ""
	_k8s_pod_ip= ""
	_gslb_adc_ip= ""
	_k8s_service_name= ""
	_id= ""
	_k8s_pod_state= ""
	_gslbvserver_name= ""
	_ns_ip_address= ""
	_rpt_sample_time= ""
	_svc_name= ""
	_rec_type= ""
	_csvserver_name= ""
	_gslb_adc_display_name= ""
	_display_name= ""
	_k8s_labels= ""
	_servername= ""
	_k8s_pod_name= ""
	_k8s_cluster_name= ""
	_k8s_namespace= ""
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
			return "global_service_graph_config_mapping"
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
			return "global_service_graph_config_mappings"
		except Exception as e :
			raise e



	'''
	get LB VServer Name
	'''
	@property
	def lbvserver_name(self) :
		try:
			return self._lbvserver_name
		except Exception as e :
			raise e
	'''
	set LB VServer Name
	'''
	@lbvserver_name.setter
	def lbvserver_name(self,lbvserver_name):
		try :
			if not isinstance(lbvserver_name,str):
				raise TypeError("lbvserver_name must be set to str value")
			self._lbvserver_name = lbvserver_name
		except Exception as e :
			raise e


	'''
	get POD Ip
	'''
	@property
	def k8s_pod_ip(self) :
		try:
			return self._k8s_pod_ip
		except Exception as e :
			raise e
	'''
	set POD Ip
	'''
	@k8s_pod_ip.setter
	def k8s_pod_ip(self,k8s_pod_ip):
		try :
			if not isinstance(k8s_pod_ip,str):
				raise TypeError("k8s_pod_ip must be set to str value")
			self._k8s_pod_ip = k8s_pod_ip
		except Exception as e :
			raise e


	'''
	get GSLB NetScaler IP
	'''
	@property
	def gslb_adc_ip(self) :
		try:
			return self._gslb_adc_ip
		except Exception as e :
			raise e
	'''
	set GSLB NetScaler IP
	'''
	@gslb_adc_ip.setter
	def gslb_adc_ip(self,gslb_adc_ip):
		try :
			if not isinstance(gslb_adc_ip,str):
				raise TypeError("gslb_adc_ip must be set to str value")
			self._gslb_adc_ip = gslb_adc_ip
		except Exception as e :
			raise e


	'''
	get Service Name in Kubernetes
	'''
	@property
	def k8s_service_name(self) :
		try:
			return self._k8s_service_name
		except Exception as e :
			raise e
	'''
	set Service Name in Kubernetes
	'''
	@k8s_service_name.setter
	def k8s_service_name(self,k8s_service_name):
		try :
			if not isinstance(k8s_service_name,str):
				raise TypeError("k8s_service_name must be set to str value")
			self._k8s_service_name = k8s_service_name
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
	get Pod State in Kubernetes
	'''
	@property
	def k8s_pod_state(self) :
		try:
			return self._k8s_pod_state
		except Exception as e :
			raise e
	'''
	set Pod State in Kubernetes
	'''
	@k8s_pod_state.setter
	def k8s_pod_state(self,k8s_pod_state):
		try :
			if not isinstance(k8s_pod_state,str):
				raise TypeError("k8s_pod_state must be set to str value")
			self._k8s_pod_state = k8s_pod_state
		except Exception as e :
			raise e


	'''
	get GSLB VServer Name
	'''
	@property
	def gslbvserver_name(self) :
		try:
			return self._gslbvserver_name
		except Exception as e :
			raise e
	'''
	set GSLB VServer Name
	'''
	@gslbvserver_name.setter
	def gslbvserver_name(self,gslbvserver_name):
		try :
			if not isinstance(gslbvserver_name,str):
				raise TypeError("gslbvserver_name must be set to str value")
			self._gslbvserver_name = gslbvserver_name
		except Exception as e :
			raise e


	'''
	get Device IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
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
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def svc_name(self) :
		try:
			return self._svc_name
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@svc_name.setter
	def svc_name(self,svc_name):
		try :
			if not isinstance(svc_name,str):
				raise TypeError("svc_name must be set to str value")
			self._svc_name = svc_name
		except Exception as e :
			raise e


	'''
	get Record Identifier
	'''
	@property
	def rec_type(self) :
		try:
			return self._rec_type
		except Exception as e :
			raise e
	'''
	set Record Identifier
	'''
	@rec_type.setter
	def rec_type(self,rec_type):
		try :
			if not isinstance(rec_type,str):
				raise TypeError("rec_type must be set to str value")
			self._rec_type = rec_type
		except Exception as e :
			raise e


	'''
	get CS VServer Name
	'''
	@property
	def csvserver_name(self) :
		try:
			return self._csvserver_name
		except Exception as e :
			raise e
	'''
	set CS VServer Name
	'''
	@csvserver_name.setter
	def csvserver_name(self,csvserver_name):
		try :
			if not isinstance(csvserver_name,str):
				raise TypeError("csvserver_name must be set to str value")
			self._csvserver_name = csvserver_name
		except Exception as e :
			raise e


	'''
	get GSLB Device IP Address
	'''
	@property
	def gslb_adc_display_name(self) :
		try:
			return self._gslb_adc_display_name
		except Exception as e :
			raise e
	'''
	set GSLB Device IP Address
	'''
	@gslb_adc_display_name.setter
	def gslb_adc_display_name(self,gslb_adc_display_name):
		try :
			if not isinstance(gslb_adc_display_name,str):
				raise TypeError("gslb_adc_display_name must be set to str value")
			self._gslb_adc_display_name = gslb_adc_display_name
		except Exception as e :
			raise e


	'''
	get Device IP Address
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get Labels in Kubernetes
	'''
	@property
	def k8s_labels(self) :
		try:
			return self._k8s_labels
		except Exception as e :
			raise e
	'''
	set Labels in Kubernetes
	'''
	@k8s_labels.setter
	def k8s_labels(self,k8s_labels):
		try :
			if not isinstance(k8s_labels,str):
				raise TypeError("k8s_labels must be set to str value")
			self._k8s_labels = k8s_labels
		except Exception as e :
			raise e


	'''
	get Server Name
	'''
	@property
	def servername(self) :
		try:
			return self._servername
		except Exception as e :
			raise e
	'''
	set Server Name
	'''
	@servername.setter
	def servername(self,servername):
		try :
			if not isinstance(servername,str):
				raise TypeError("servername must be set to str value")
			self._servername = servername
		except Exception as e :
			raise e


	'''
	get Pod Name in Kubernetes
	'''
	@property
	def k8s_pod_name(self) :
		try:
			return self._k8s_pod_name
		except Exception as e :
			raise e
	'''
	set Pod Name in Kubernetes
	'''
	@k8s_pod_name.setter
	def k8s_pod_name(self,k8s_pod_name):
		try :
			if not isinstance(k8s_pod_name,str):
				raise TypeError("k8s_pod_name must be set to str value")
			self._k8s_pod_name = k8s_pod_name
		except Exception as e :
			raise e


	'''
	get Kubernetes cluster name
	'''
	@property
	def k8s_cluster_name(self) :
		try:
			return self._k8s_cluster_name
		except Exception as e :
			raise e
	'''
	set Kubernetes cluster name
	'''
	@k8s_cluster_name.setter
	def k8s_cluster_name(self,k8s_cluster_name):
		try :
			if not isinstance(k8s_cluster_name,str):
				raise TypeError("k8s_cluster_name must be set to str value")
			self._k8s_cluster_name = k8s_cluster_name
		except Exception as e :
			raise e


	'''
	get Namespace of service in Kubernetes
	'''
	@property
	def k8s_namespace(self) :
		try:
			return self._k8s_namespace
		except Exception as e :
			raise e
	'''
	set Namespace of service in Kubernetes
	'''
	@k8s_namespace.setter
	def k8s_namespace(self,k8s_namespace):
		try :
			if not isinstance(k8s_namespace,str):
				raise TypeError("k8s_namespace must be set to str value")
			self._k8s_namespace = k8s_namespace
		except Exception as e :
			raise e

	'''
	K8 cluster service details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				global_service_graph_config_mapping_obj=global_service_graph_config_mapping()
				response = global_service_graph_config_mapping_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of global_service_graph_config_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			global_service_graph_config_mapping_obj = global_service_graph_config_mapping()
			option_ = options()
			option_._filter=filter_
			return global_service_graph_config_mapping_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the global_service_graph_config_mapping resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			global_service_graph_config_mapping_obj = global_service_graph_config_mapping()
			option_ = options()
			option_._count=True
			response = global_service_graph_config_mapping_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of global_service_graph_config_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			global_service_graph_config_mapping_obj = global_service_graph_config_mapping()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = global_service_graph_config_mapping_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(global_service_graph_config_mapping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.global_service_graph_config_mapping
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(global_service_graph_config_mapping_responses, response, "global_service_graph_config_mapping_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.global_service_graph_config_mapping_response_array
				i=0
				error = [global_service_graph_config_mapping() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.global_service_graph_config_mapping_response_array
			i=0
			global_service_graph_config_mapping_objs = [global_service_graph_config_mapping() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_global_service_graph_config_mapping'):
					for props in obj._global_service_graph_config_mapping:
						result = service.payload_formatter.string_to_bulk_resource(global_service_graph_config_mapping_response,self.__class__.__name__,props)
						global_service_graph_config_mapping_objs[i] = result.global_service_graph_config_mapping
						i=i+1
			return global_service_graph_config_mapping_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(global_service_graph_config_mapping,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class global_service_graph_config_mapping_response(base_response):
	def __init__(self,length=1) :
		self.global_service_graph_config_mapping= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.global_service_graph_config_mapping= [ global_service_graph_config_mapping() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class global_service_graph_config_mapping_responses(base_response):
	def __init__(self,length=1) :
		self.global_service_graph_config_mapping_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.global_service_graph_config_mapping_response_array = [ global_service_graph_config_mapping() for _ in range(length)]
