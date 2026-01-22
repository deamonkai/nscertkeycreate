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

from massrc.com.citrix.mas.nitro.resource.config.mps.managed_device import managed_device

'''
Configuration for VM Device resource
'''

class vm_device(managed_device):
	_provision_request_id= ""
	_http_port= ""
	_domain_name= ""
	_vm_state= ""
	_throughput= ""
	_snmp_port= ""
	_image_name= ""
	_ssh_port= ""
	_number_of_cpu= ""
	_lb_role= ""
	_burst_priority= ""
	_host_ip_address= ""
	_routable= ""
	_https_port= ""
	_max_burst_throughput= ""
	_is_swg= ""
	_uuid= ""
	_vm_description= ""
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
			return "vm_device"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vm_device,self).get_object_id()
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
			return "vm_devices"
		except Exception as e :
			raise e



	'''
	get Value is set only if the instance was provisioned from NetScaler Console
	'''
	@property
	def provision_request_id(self) :
		try:
			return self._provision_request_id
		except Exception as e :
			raise e
	'''
	set Value is set only if the instance was provisioned from NetScaler Console
	'''
	@provision_request_id.setter
	def provision_request_id(self,provision_request_id):
		try :
			if not isinstance(provision_request_id,str):
				raise TypeError("provision_request_id must be set to str value")
			self._provision_request_id = provision_request_id
		except Exception as e :
			raise e


	'''
	get HTTP port of the container.
	'''
	@property
	def http_port(self) :
		try:
			return self._http_port
		except Exception as e :
			raise e
	'''
	set HTTP port of the container.
	'''
	@http_port.setter
	def http_port(self,http_port):
		try :
			if not isinstance(http_port,int):
				raise TypeError("http_port must be set to int value")
			self._http_port = http_port
		except Exception as e :
			raise e


	'''
	get Domain name of VM Device
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set Domain name of VM Device
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
		except Exception as e :
			raise e


	'''
	get State of Virtual Machine (Running | Halted)
	'''
	@property
	def vm_state(self) :
		try:
			return self._vm_state
		except Exception as e :
			raise e


	'''
	get Assign throughput in Mbps to VM Instance
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set Assign throughput in Mbps to VM Instance
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,float):
				raise TypeError("throughput must be set to float value")
			self._throughput = throughput
		except Exception as e :
			raise e


	'''
	get SNMP port of the container.
	'''
	@property
	def snmp_port(self) :
		try:
			return self._snmp_port
		except Exception as e :
			raise e
	'''
	set SNMP port of the container.
	'''
	@snmp_port.setter
	def snmp_port(self,snmp_port):
		try :
			if not isinstance(snmp_port,int):
				raise TypeError("snmp_port must be set to int value")
			self._snmp_port = snmp_port
		except Exception as e :
			raise e


	'''
	get Image Name, This parameter is used while provisioning VM Instance with XVA image, template_name is given priority if provided along with image_name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set Image Name, This parameter is used while provisioning VM Instance with XVA image, template_name is given priority if provided along with image_name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get SSH port of the container.
	'''
	@property
	def ssh_port(self) :
		try:
			return self._ssh_port
		except Exception as e :
			raise e
	'''
	set SSH port of the container.
	'''
	@ssh_port.setter
	def ssh_port(self,ssh_port):
		try :
			if not isinstance(ssh_port,int):
				raise TypeError("ssh_port must be set to int value")
			self._ssh_port = ssh_port
		except Exception as e :
			raise e


	'''
	get Number of CPU that is assigned to VM Instance
	'''
	@property
	def number_of_cpu(self) :
		try:
			return self._number_of_cpu
		except Exception as e :
			raise e


	'''
	get LB role performed by the device: North-South (Ingress or server), or East-West (client)
	'''
	@property
	def lb_role(self) :
		try:
			return self._lb_role
		except Exception as e :
			raise e
	'''
	set LB role performed by the device: North-South (Ingress or server), or East-West (client)
	'''
	@lb_role.setter
	def lb_role(self,lb_role):
		try :
			if not isinstance(lb_role,str):
				raise TypeError("lb_role must be set to str value")
			self._lb_role = lb_role
		except Exception as e :
			raise e


	'''
	get Burst Priority of the VM Instance between 1 and 4
	'''
	@property
	def burst_priority(self) :
		try:
			return self._burst_priority
		except Exception as e :
			raise e
	'''
	set Burst Priority of the VM Instance between 1 and 4
	'''
	@burst_priority.setter
	def burst_priority(self,burst_priority):
		try :
			if not isinstance(burst_priority,int):
				raise TypeError("burst_priority must be set to int value")
			self._burst_priority = burst_priority
		except Exception as e :
			raise e


	'''
	get Host IPAddress where VM is provisioned
	'''
	@property
	def host_ip_address(self) :
		try:
			return self._host_ip_address
		except Exception as e :
			raise e
	'''
	set Host IPAddress where VM is provisioned
	'''
	@host_ip_address.setter
	def host_ip_address(self,host_ip_address):
		try :
			if not isinstance(host_ip_address,str):
				raise TypeError("host_ip_address must be set to str value")
			self._host_ip_address = host_ip_address
		except Exception as e :
			raise e


	'''
	get Whether the device is reachable or not
	'''
	@property
	def routable(self) :
		try:
			return self._routable
		except Exception as e :
			raise e
	'''
	set Whether the device is reachable or not
	'''
	@routable.setter
	def routable(self,routable):
		try :
			if not isinstance(routable,bool):
				raise TypeError("routable must be set to bool value")
			self._routable = routable
		except Exception as e :
			raise e


	'''
	get HTTPS port of the container.
	'''
	@property
	def https_port(self) :
		try:
			return self._https_port
		except Exception as e :
			raise e
	'''
	set HTTPS port of the container.
	'''
	@https_port.setter
	def https_port(self,https_port):
		try :
			if not isinstance(https_port,int):
				raise TypeError("https_port must be set to int value")
			self._https_port = https_port
		except Exception as e :
			raise e


	'''
	get Maximum burst throughput in Mbps of VM Instance
	'''
	@property
	def max_burst_throughput(self) :
		try:
			return self._max_burst_throughput
		except Exception as e :
			raise e
	'''
	set Maximum burst throughput in Mbps of VM Instance
	'''
	@max_burst_throughput.setter
	def max_burst_throughput(self,max_burst_throughput):
		try :
			if not isinstance(max_burst_throughput,float):
				raise TypeError("max_burst_throughput must be set to float value")
			self._max_burst_throughput = max_burst_throughput
		except Exception as e :
			raise e


	'''
	get Boolean to indicate whether a VM is SWG
	'''
	@property
	def is_swg(self) :
		try:
			return self._is_swg
		except Exception as e :
			raise e


	'''
	get UUID of VM Instance generated by Hypervisor
	'''
	@property
	def uuid(self) :
		try:
			return self._uuid
		except Exception as e :
			raise e


	'''
	get Description of the VM instance
	'''
	@property
	def vm_description(self) :
		try:
			return self._vm_description
		except Exception as e :
			raise e

	'''
	Use this operation to get VM Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				vm_device_obj=vm_device()
				response = vm_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vm_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._filter=filter_
			return vm_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vm_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._count=True
			response = vm_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vm_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vm_device_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vm_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vm_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vm_device_responses, response, "vm_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vm_device_response_array
				i=0
				error = [vm_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vm_device_response_array
			i=0
			vm_device_objs = [vm_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vm_device'):
					for props in obj._vm_device:
						result = service.payload_formatter.string_to_bulk_resource(vm_device_response,self.__class__.__name__,props)
						vm_device_objs[i] = result.vm_device
						i=i+1
			return vm_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vm_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vm_device_response(base_response):
	def __init__(self,length=1) :
		self.vm_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vm_device= [ vm_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vm_device_responses(base_response):
	def __init__(self,length=1) :
		self.vm_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vm_device_response_array = [ vm_device() for _ in range(length)]
