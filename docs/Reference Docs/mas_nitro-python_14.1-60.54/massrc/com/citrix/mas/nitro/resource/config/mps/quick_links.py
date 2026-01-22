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
Configuration for Quick links for unified experience resource
'''

class quick_links(base_resource):
	_link= ""
	_name= ""
	_description= ""
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
			return "quick_links"
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
			return "quick_linkss"
		except Exception as e :
			raise e



	'''
	get Link to the netscale console page
	'''
	@property
	def link(self) :
		try:
			return self._link
		except Exception as e :
			raise e
	'''
	set Link to the netscale console page
	'''
	@link.setter
	def link(self,link):
		try :
			if not isinstance(link,str):
				raise TypeError("link must be set to str value")
			self._link = link
		except Exception as e :
			raise e


	'''
	get Name of the quick link that will be shown to the user on citrix cloud UI
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the quick link that will be shown to the user on citrix cloud UI
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
	get Description of the quick link
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of the quick link
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e

	'''
	Use this operation to get applicable quick links.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				quick_links_obj=quick_links()
				response = quick_links_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of quick_links resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			quick_links_obj = quick_links()
			option_ = options()
			option_._filter=filter_
			return quick_links_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the quick_links resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			quick_links_obj = quick_links()
			option_ = options()
			option_._count=True
			response = quick_links_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of quick_links resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			quick_links_obj = quick_links()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = quick_links_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(quick_links_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.quick_links
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(quick_links_responses, response, "quick_links_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.quick_links_response_array
				i=0
				error = [quick_links() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.quick_links_response_array
			i=0
			quick_links_objs = [quick_links() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_quick_links'):
					for props in obj._quick_links:
						result = service.payload_formatter.string_to_bulk_resource(quick_links_response,self.__class__.__name__,props)
						quick_links_objs[i] = result.quick_links
						i=i+1
			return quick_links_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(quick_links,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class quick_links_response(base_response):
	def __init__(self,length=1) :
		self.quick_links= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.quick_links= [ quick_links() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class quick_links_responses(base_response):
	def __init__(self,length=1) :
		self.quick_links_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.quick_links_response_array = [ quick_links() for _ in range(length)]
