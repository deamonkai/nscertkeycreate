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
Configuration for Cluster node information resource
'''

class ns_clusternode(base_resource):
	_spotted_config_supported= ""
	_clip= ""
	_act_id= ""
	_iscco= ""
	_clusterid= ""
	_node_group= ""
	_nodeid= ""
	_password= ""
	_clmasterstate= ""
	_clnodeip= ""
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
			return "ns_clusternode"
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
			return "ns_clusternodes"
		except Exception as e :
			raise e



	'''
	get is spotted config supported
	'''
	@property
	def spotted_config_supported(self) :
		try:
			return self._spotted_config_supported
		except Exception as e :
			raise e
	'''
	set is spotted config supported
	'''
	@spotted_config_supported.setter
	def spotted_config_supported(self,spotted_config_supported):
		try :
			if not isinstance(spotted_config_supported,bool):
				raise TypeError("spotted_config_supported must be set to bool value")
			self._spotted_config_supported = spotted_config_supported
		except Exception as e :
			raise e


	'''
	get Cluster IP
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IP
	'''
	@clip.setter
	def clip(self,clip):
		try :
			if not isinstance(clip,str):
				raise TypeError("clip must be set to str value")
			self._clip = clip
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get Is CCO
	'''
	@property
	def iscco(self) :
		try:
			return self._iscco
		except Exception as e :
			raise e
	'''
	set Is CCO
	'''
	@iscco.setter
	def iscco(self,iscco):
		try :
			if not isinstance(iscco,bool):
				raise TypeError("iscco must be set to bool value")
			self._iscco = iscco
		except Exception as e :
			raise e


	'''
	get Cluster Instance ID
	'''
	@property
	def clusterid(self) :
		try:
			return self._clusterid
		except Exception as e :
			raise e
	'''
	set Cluster Instance ID
	'''
	@clusterid.setter
	def clusterid(self,clusterid):
		try :
			if not isinstance(clusterid,int):
				raise TypeError("clusterid must be set to int value")
			self._clusterid = clusterid
		except Exception as e :
			raise e


	'''
	get Node Group where the node belongs in L3 Cluster
	'''
	@property
	def node_group(self) :
		try:
			return self._node_group
		except Exception as e :
			raise e
	'''
	set Node Group where the node belongs in L3 Cluster
	'''
	@node_group.setter
	def node_group(self,node_group):
		try :
			if not isinstance(node_group,str):
				raise TypeError("node_group must be set to str value")
			self._node_group = node_group
		except Exception as e :
			raise e


	'''
	get Cluster Node ID
	'''
	@property
	def nodeid(self) :
		try:
			return self._nodeid
		except Exception as e :
			raise e
	'''
	set Cluster Node ID
	'''
	@nodeid.setter
	def nodeid(self,nodeid):
		try :
			if not isinstance(nodeid,int):
				raise TypeError("nodeid must be set to int value")
			self._nodeid = nodeid
		except Exception as e :
			raise e


	'''
	get Password of the CCO node(CLIP)
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password of the CCO node(CLIP)
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Cluster Master State
	'''
	@property
	def clmasterstate(self) :
		try:
			return self._clmasterstate
		except Exception as e :
			raise e


	'''
	get Cluster Node IP
	'''
	@property
	def clnodeip(self) :
		try:
			return self._clnodeip
		except Exception as e :
			raise e
	'''
	set Cluster Node IP
	'''
	@clnodeip.setter
	def clnodeip(self,clnodeip):
		try :
			if not isinstance(clnodeip,str):
				raise TypeError("clnodeip must be set to str value")
			self._clnodeip = clnodeip
		except Exception as e :
			raise e

	'''
	Use this operation to get clusternode stats.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_clusternode_obj=ns_clusternode()
				response = ns_clusternode_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to remove node from cluster.
	'''
	@classmethod
	def remove_node(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"remove_node")
				return res
			else : 
				ns_clusternode_obj= ns_clusternode()
				return cls.perform_operation_bulk_request(service,"remove_node",resource,ns_clusternode_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_clusternode resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_clusternode_obj = ns_clusternode()
			option_ = options()
			option_._filter=filter_
			return ns_clusternode_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_clusternode resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_clusternode_obj = ns_clusternode()
			option_ = options()
			option_._count=True
			response = ns_clusternode_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_clusternode resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_clusternode_obj = ns_clusternode()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_clusternode_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_clusternode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_clusternode
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_clusternode_responses, response, "ns_clusternode_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_clusternode_response_array
				i=0
				error = [ns_clusternode() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_clusternode_response_array
			i=0
			ns_clusternode_objs = [ns_clusternode() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_clusternode'):
					for props in obj._ns_clusternode:
						result = service.payload_formatter.string_to_bulk_resource(ns_clusternode_response,self.__class__.__name__,props)
						ns_clusternode_objs[i] = result.ns_clusternode
						i=i+1
			return ns_clusternode_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_clusternode,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_clusternode_response(base_response):
	def __init__(self,length=1) :
		self.ns_clusternode= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_clusternode= [ ns_clusternode() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_clusternode_responses(base_response):
	def __init__(self,length=1) :
		self.ns_clusternode_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_clusternode_response_array = [ ns_clusternode() for _ in range(length)]
