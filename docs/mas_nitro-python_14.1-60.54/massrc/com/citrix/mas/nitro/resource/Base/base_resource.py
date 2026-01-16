'''
* Copyright (c) 2008-2025 Citrix Systems, Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
'''
from abc import ABCMeta, abstractmethod, abstractproperty
import json
import requests
import sys,os,re
import logging
from logging import handlers, Formatter


from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.util.nitro_util import nitro_util
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception

class base_resource:
    __metaclass__ = ABCMeta
    _headers = {}
    #request params is declared ,are filtered params from resource object which forms nitro request payload
    _request_params={}
    #response params is declared ,are filtered params from response nitro payload . These only params are
    #initiated for returning response object.
    _response_params={}
    _logger=None
    _url_filter=None


    #In case op primary key is different than objecttype
    _op_by_primary_key_name=""

    @abstractmethod
    def get_nitro_response(self, service, string):
        pass

    @abstractmethod
    def get_nitro_bulk_response(self, service, string):
        pass

    @abstractmethod
    def get_object_type(self):
        pass

    @abstractmethod
    def validate(self,operationType=""):
        pass

    @staticmethod
    def get_plural_object_name():
        return None

    def get_resource_url(self):
        return None

    #Basepath for url prefixed before say nitro/v1/config
    #example stylebook for http:<ip>/stylebook/nitro/v1/config
    def get_api_basepath(self):
        return ""

    # url is built with multiple objects say
    # <object_type1>/<object_value1>/<object_type2>/<object value2>...the
    # example stylebooks/<namespace/version/name>/configpacks/<configpack_id>
    def get_namespace_url(self):
        return ""

    #For async apis following function is defined to wait for finish of job
    def wait_for_job(self):
        return None

    def get_resource_id(self):
        return None

    '''
    Gets the headers.
    @return headers.
    '''
    @property
    def headers(self):
        try:
            return self._headers
        except Exception as e:
            raise e

    '''
    sets the headers
    '''

    @headers.setter
    def headers(self, headers ):
        try :
            if not isinstance(headers,dict):
                raise TypeError("headers must be set to dict value")
            self._headers = headers
        except Exception as e:
            raise e

    '''
    * Gets the resource type.
    '''
    @classmethod
    def get_object_type(cls):
        return cls.__name__

    '''
    Use this method to perform a filtered get operation on netscaler resource.
    @param service nitro_service object.
    @param option_ options class object.
    @return Array of nitro resources of given resource type.
    @throws Exception Nitro exception is thrown.
    '''

    def getfiltered(self, service, option_):
        try:
            if (not service.isLogin()):
                service.login()
            response = self.__get(service, option_)
            return response
        except Exception as e:
            raise e


    '''
    * Converts resource to Json string.
    * @param service nitro_service object.
    * @param id sessionId.
    * @param option_ Options object.
    * @return  string in Json format.
    '''

    def get_unprocessed_url(self):
        return ""

    def resource_to_string(self,service,option_):
        try:
            onerror = service.onerror
            return service.payload_formatter.resource_to_string(self,option_,onerror)

        except Exception as e:
            raise e

    def is_body_property(self, property_name):
        return not self.is_url_property(property_name)

    def is_url_property(self, property_name):
        property_name = "{%s}" % property_name

        if (property_name in self.get_unprocessed_url()):
            return True
        return False

    def process_url(self, url):

        m = re.findall('\{.*\}', url)
        for group in m:
            url = url.replace(group, self.__dict__["_" + group[1:-1]])
        return url

    '''
    * forms a String for unset operation on a resource.
    * @param service nitro_service object.
    * @param id session id.
    * @param option_ Options object.
    * @param args Array of args that are to be unset.
    * @return  string in Json format.
    * @throws Exception if invalid input is given.
    '''
    def unset_string(self, service, args):
        try:
            result = "{\"" + self.__class__.get_object_type() + "\":"
            result = result + service.payload_formatter.unset_string(self, args) + "}"
            return result
        except Exception as e:
            raise e

    def update_headers(self, headers):
        if headers:
            self.headers.update(headers)

    '''
    used to call get_request function

    '''
    def get_resources(self,nitro_service,option_=None):
        try :

            if not nitro_service.isLogin():
                nitro_service.login()
            response = self.__get(nitro_service,option_)

            if type(response) is list:
                return response
            else :
                return response[0]

        except Exception as e:
            raise e


    def get_resource(self, service, option_=""):
        try:
            if (not service.isLogin()):
                service.login()
            response = self.__get(service, option_)
            if type(response) is list:
                return response
            else :
                return response[0]
            return None
        except Exception as e:
            raise e



    '''
    get_request
    '''
    def __get(self,service,option_):

        try :
            urlstr = ""
            object_type = self.get_object_type()
            ipaddress = service.ipaddress
            sessionid = service.sessionid
            version = service.version
            protocol = service.protocol
            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)
            timeout = service.timeout
            verify = service.certverify
            url = self.get_resource_url()

            api_basepath = self.get_api_basepath()
            if api_basepath:
                api_basepath = "/"+api_basepath.strip('/')

            namespace_url = self.get_namespace_url().strip('/')

            if namespace_url:
                urlstr = protocol + "://" + ipaddress + api_basepath + "/nitro/" + version + "/config/" + namespace_url
            else:
                if not url:
                    urlstr = protocol + "://" + ipaddress + api_basepath+"/nitro/" + version + "/config/" + object_type
                else:
                    urlstr = protocol + "://" + ipaddress + url

                name = self.get_object_id()
                if name:
                    name=name.strip('/')

                if name and len(name)>0:
                    urlstr = urlstr + "/" + nitro_util.encode(nitro_util.encode(name))

            response_received =""

            if option_:
                optionstr = option_.to_string()
                if len(optionstr)>0 :
                    urlstr = urlstr + "?" + optionstr

            headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid }
            if service.isCloud == True:
                    headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid , 'isCloud': 'true', 'allow_redirects':'true'}
            self.update_headers(headers)
            response = ''
            if service._logger:
                service._logger.debug("GET urlstr:"+urlstr)

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})

            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                response = requests.get(urlstr, headers=headers, timeout=timeout, cookies=cookie_h, verify=verify)
            else:
                response = requests.get(urlstr, headers=headers, timeout=timeout)

            if service._logger:
                service._logger.debug("GET Response:"+str(response.text))
            if not response.ok:
                response = json.loads(response.text)
                errorcode,message,severity = base_resource.get_error_details_from_response(response)
                raise nitro_exception(errorcode, str(message), str(severity))
            else:
                response = self.get_nitro_response(service, response.text)
            return response


        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e


    '''
    perform operation
    '''
    def perform_operation(self,service, action="", option_=""):

        try:
            if not option_ and not action:
                return self.post_request(service, None)
            elif not option_ :
                option_ = options()
                option_.action=action
                option_.version=service.version
                return self.post_request(service,option_)

        except Exception as e:
            raise e

    '''

    '''

    def post_request(self,service,option_):
        try :
            return self.add_resource(service,option_)
        except Exception as e:
            raise e



    '''
    performs bulk operation
    '''
    @classmethod
    def perform_operation_bulk_request(cls,service,action,resources,objtype):
        try:
            if (not service.isLogin()):
                service.login()
            option_ = options()
            option_.action=action
            option_.version=service.version
            onerror = service.onerror
            request = service.payload_formatter.resource_to_string_bulk(resources,option_,onerror)
            return cls.post_bulk_data(service,request,objtype,option_)
        except Exception as e:
            raise e

    '''
    performs bulk operation
    '''
    @classmethod
    def perform_operation_bulk_request(cls,service,resources,objtype):
        try:
            if (not service.isLogin()):
                service.login()
            onerror = service.onerror
            request = service.payload_formatter.resource_to_string_bulk(resources,None,onerror)
            return cls.post_bulk_data(service,request,objtype,None)
        except Exception as e:
            raise e

    '''
    post_bulk_data
    '''
    @classmethod
    def post_bulk_data(cls,service,request,objtype,option_=""):
        try:

            response = cls.__post(cls,service,request,option_,objtype)
            return response
        except Exception as e:
            raise e



    '''
    add resource
    '''

    def add_resource(self,nitro_service,option_):

        try:
            request = self.resource_to_string(nitro_service,option_)
            response = self.__post(self,nitro_service,request,option_)

            return response
        except Exception as e:
            raise e

    '''
    post operation
    '''
    @staticmethod
    def get_error_details_from_response(response):
        if "errorcode" in response:
            errorcode = response["errorcode"]
        else:
            errorcode = ""

        if "message" in response:
            message = response["message"]
        else:
            message = ""

        if "severity" in response:
            severity = response["severity"]
        else:
            severity = ""

        return errorcode,message,severity

    '''
    post operation
    '''
    @staticmethod
    def __post(resourcetype,service,request,option,objtype=""):

        try :

            urlstr=""
            object_type =""
            if objtype :
                object_type = objtype.get_object_type()
            else :
                object_type = resourcetype.get_object_type()
            if (object_type is not "login" and not service.isLogin()):
                service.login()
            username = service.username
            password = service.password
            ipaddress = service.ipaddress
            sessionid = service.sessionid
            version = service.version
            protocol = service.protocol
            timeout = service.timeout
            verify = service.certverify
            headers =""
            content_type = ""
            object_type_str = object_type

            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)

            if objtype :
                api_basepath = objtype.get_api_basepath()
                url = objtype.get_resource_url()
                namespace_url = objtype.get_namespace_url().strip('/')
            else:
                api_basepath = resourcetype.get_api_basepath()
                url = resourcetype.get_resource_url()
                namespace_url = resourcetype.get_namespace_url().strip('/')

            if api_basepath:
                api_basepath = "/"+api_basepath.strip('/')

            url_filter=resourcetype._url_filter

            # url is built with multiple objects say
            # <object_type1>/<object_value1>/<object_type2>/<object value2>...the
            if namespace_url:
                urlstr = protocol + "://" + ipaddress + api_basepath + "/nitro/" + version + "/config/" + namespace_url
            else:
                if not url:
                    urlstr = protocol + "://" + ipaddress + api_basepath+"/nitro/" + version + "/config/"+object_type
                else:
                    urlstr = protocol + "://" + ipaddress + url

            if url_filter:
                urlstr = urlstr + "?" + url_filter
            if option :
                option.onerror=service.onerror
                option.detailview=False
                optionstr = option.to_string()
                if len(optionstr)>0 :
                    if url_filter:
                        urlstr = urlstr + "&" + optionstr
                    else:
                        urlstr = urlstr + "?" + optionstr

            content_type =  "Application/vnd.com.citrix.mas."+object_type + "+" + "json"
            if url or namespace_url :
                content_type = "application/json"

            if(sessionid != None and object_type is not "login") :
                headers = {'Content-type': content_type ,'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid }
                if service.isCloud == True:
                    headers = {'Content-type': content_type ,'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid, 'isCloud': 'true', 'allow_redirects':'true'}
            elif (object_type is "login"):
                headers = {'Content-type': content_type,'Connection': 'keep-alive','X-NITRO-USER':username,'X-NITRO-PASS':password}
                if service.isCloud == True:
                    username=service.ID
                    password=service.Secret
                    headers = {'Content-type': content_type,'Connection': 'keep-alive', 'isCloud': 'true','X-NITRO-USER':username,'X-NITRO-PASS':password, 'allow_redirects':'true'}

            if service._logger:
                service._logger.debug("POST urlstr:"+urlstr)
                service._logger.debug("POST Request Payload:"+str(request))

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})

            response = ''
            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                if object_type is  not"login":
                    cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                    response = requests.post(urlstr, data=request, headers=headers, cookies=cookie_h, timeout=timeout, verify=verify)
                else:
                    response = requests.post(urlstr, data=request, headers=headers, timeout=timeout, verify=verify)

            else:
                response = requests.post(urlstr, data=request, headers=headers, timeout=timeout)

            if service._logger:
                service._logger.debug("POST Response Payload:"+str(response)+str(response.text))


            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            else:
                if (object_type is "login"):
                    try:
                        cookie = response.headers['set-cookie']
                        service.sessionid = cookie[cookie.find("=")+1:cookie.find(";")]
                        response = json.loads(response.text)
                        return response
                    except:
                         response = json.loads(response.text)
                         raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))


                if objtype :
                    response = objtype.get_nitro_bulk_response(service, response.text)
                else :
                    response = resourcetype.get_nitro_response(service, response.text)

            return response

        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e


    '''
    delete_resource
    '''
    def delete_resource(self,nitro_service):

        try:
            if not nitro_service.isLogin() :
                nitro_service.login()
            args = nitro_util.object_to_string_withoutquotes(self)
            return self.__delete_request(nitro_service, args)

        except Exception as e:
            raise e


    '''
    update_resource
    '''
    def update_resource(self,service):

        try :
            if not service.isLogin():
                service.login()
            option_ = options()
            option_.version=service.version
            request = self.resource_to_string(service,option_)
            return self.put_data(service, request,option_)

        except Exception as e:
            raise e


    '''
    put_data
    '''

    def put_data(self, nitro_service, request,option_):
        try:
            response = self._put(self, nitro_service, request,option_)
            return response
        except Exception as e:
            raise e
    '''
    put operation
    '''
    @staticmethod
    def _put(resource_type, service, request,option, objtype=""):

        try :
            urlstr=""
            ipaddress = service.ipaddress
            sessionid = service.sessionid
            version = service.version
            protocol = service.protocol
            timeout = service.timeout
            verify = service.certverify

            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)

            content_type = ""
            object_type=""
            if objtype :
                object_type = objtype.get_object_type()
            else :
                object_type = resource_type.get_object_type()


            if objtype:
                url = objtype.get_resource_url()
                api_basepath = objtype.get_api_basepath()
                namespace_url = objtype.get_namespace_url().strip('/')
            else:
                url = resource_type.get_resource_url()
                api_basepath = resource_type.get_api_basepath()
                namespace_url = resource_type.get_namespace_url().strip('/')

            if api_basepath:
                api_basepath = "/"+api_basepath.strip('/')

            url_filter=resource_type._url_filter

            if namespace_url:
                urlstr = protocol + "://" + ipaddress + api_basepath + "/nitro/" + version + "/config/" + namespace_url
            else:
                if not url:
                    urlstr = protocol + "://" + ipaddress + api_basepath + "/nitro/" + version + "/config/"  + object_type
                else:
                    urlstr = protocol + "://" + ipaddress + url
                    if objtype:
                        resource_id = objtype.get_resource_id()
                    else:
                        resource_id = resource_type.get_resource_id()
                    if resource_id:
                        urlstr = urlstr + "/" + resource_id

            if url_filter:
                urlstr = urlstr + "?" + url_filter
            if option :
                option.onerror=service.onerror
                option.detailview=False
                optionstr = option.to_string()
                if len(optionstr)>0 :
                    if url_filter:
                        urlstr = urlstr + "&" + optionstr
                    else:
                        urlstr = urlstr + "?" + optionstr

            content_type =  "Application/vnd.com.citrix.mas."+object_type + "+" + "json"

            if namespace_url:
                content_type = "application/json"

            if(sessionid != None) :
                headers = {'Content-type': content_type ,'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid }
                if service.isCloud == True:
                    headers = {'Content-type': content_type ,'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid, 'isCloud': 'true', 'allow_redirects':'true'}
            else :
                raise Exception("Session doesn't exist")

            if service._logger:
                service._logger.debug("PUT urlstr:"+urlstr)
                service._logger.debug("PUT Request Payload:"+request)

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})

            response = ''
            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                response = requests.put(urlstr, data=request, headers=headers, cookies=cookie_h, timeout=timeout, verify=verify)
            else:
                response = requests.put(urlstr, data=request, headers=headers,timeout=timeout)

            if service._logger:
                service._logger.debug("PUT Response Payload:"+str(response.text))


            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            else:

                if objtype :
                    response = objtype.get_nitro_bulk_response(service, response.text)
                else :
                    response = resource_type.get_nitro_response(service, response.text)

            return response


        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e


    '''
    * Use this method to perform a download file of MPS resource.
    * @param service nitro_service object
    * @throws Exception API exception is thrown.
    '''
    @classmethod
    def download_resources(cls,service,resource):
        try:
            if not service.isLogin() :
                service.login()
            return cls._download(service,resource)

        except Exception as e:
            raise e

    '''
    * Use this method to perform a upload file of MPS resource.
    * @param service nitro_service object
    * @throws Exception API exception is thrown.
    '''
    @classmethod
    def upload_resources(cls,service,resource):
        try:
            if not service.isLogin() :
                service.login()
            return cls._upload(service,resource)

        except Exception as e:
            raise e


    '''
    download operation
    '''

    @classmethod
    def _download(cls,service,resource) :
        try:
            urlstr=""
            ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            protocol = service.protocol
            object_type = resource.get_object_type()
            path =""
            path = resource.file_location_path
            path = path + "/"
            filename =""
            filename = resource.file_name
            timeout = service.timeout
            verify = service.certverify

            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)

            #Assuming the filename is the "id" of the resource

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/download/" + object_type

            if filename is "" :
                raise Exception("File name not specified")
            if path is "":
                raise Exception("Local path not specified")
            if (filename is not None and len(filename) > 0) :
                urlstr = urlstr + "/" + filename

            '''
            Checking if the file to be download'ed already exists in
            destination folder
            '''
            if (not os.path.isdir(path)) :
                raise Exception("Directory Does not exists")


            if (os.path.exists(path+filename)) :
                raise Exception("File already exists")

            if(sessionid is not None) :
                headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid}
                if service.isCloud == True:
                    headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid, 'isCloud': 'true'}
            else:
                raise Exception(" Session doesn't Exist")

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})

            response = ''
            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                response = requests.get(urlstr, headers=headers, cookies=cookie_h, timeout=timeout, verify=verify)
            else:
                response = requests.get(urlstr, headers=headers, timeout=timeout)

            with open(path + filename, "wb") as writer:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        writer.write(chunk)
                        writer.flush()

            #we have to make a dummy response
            if not response.ok:


                if str(response.status_code) == '404' :
                    os.remove(path+filename)
                    temp='{ "errorcode": 404, "message": "File Not Found On Remote Machine", "severity": "ERROR" }'
                    response = resource.get_nitro_response(service, temp)
            else :

                temp='{ "errorcode": 0, "message": "Done", "'+object_type+'": [ {}] }'
                response = resource.get_nitro_response(service, temp)

            return response

        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e


    '''
    upload operation
    for uploading files
    '''

    @classmethod
    def _upload(cls,service,resource) :
        try:
            urlstr=""
            ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            protocol = service.protocol
            object_type = resource.get_object_type()
            path =""
            path = resource.file_location_path
            path = path + "/"
            filename =""
            filename = resource.file_name
            file_component_name = resource.file_component_value
            timeout = service.timeout
            verify = service.certverify

            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)

            #Checking if file to be uploaded exists on client system
            if (not os.path.exists(path+filename)) :
                raise Exception("File doesn't exist in the specified directory")

            if(sessionid is None) :
                raise Exception(" Session doesn't Exist")

            length = os.path.getsize(path+filename)
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/upload/" + object_type

            headers = {'Cookie':'NITRO_AUTH_TOKEN=' +  sessionid, 'Content-Length': str(length),
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip,deflate,sdch', 'Cache-Control': 'no-cache', 'Connection': 'Keep-Alive'
                       }

            if service.isCloud == True:
                headers = {'Cookie':'NITRO_AUTH_TOKEN=' + sessionid, 'Content-Length': str(length),
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip,deflate,sdch', 'Cache-Control': 'no-cache',
                           'Connection': 'Keep-Alive', 'isCloud':'true', 'allow_redirects':'true'
                           }
            files = {file_component_name: (filename, open(os.path.join(path, filename), 'rb'), 'multipart/form-data', {
                'Content-Disposition': 'form-data; name=' + file_component_name + '; filename=' + filename})}

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})
                
            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                response = requests.post(urlstr, files=files, headers=headers, cookies=cookie_h, timeout=timeout, verify=verify)
            else:
                response = requests.post(urlstr, files=files, headers=headers, timeout=timeout)

            response = resource.get_nitro_response(service, response.text)
            return response

        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e



    '''
    delete operation
    '''
    def __delete_request(self,service,args):
        try :

            urlstr=""
            ipaddress = service.ipaddress
            sessionid = service.sessionid
            version = service.version
            protocol = service.protocol
            timeout = service.timeout
            object_type = self.get_object_type()
            verify = service.certverify
            port = service.port
            if port != 80 and port !=443:
                ipaddress = ipaddress+':'+str(port)
            url = self.get_resource_url()

            url_filter=self._url_filter

            api_basepath = self.get_api_basepath()
            if api_basepath:
                api_basepath = "/"+api_basepath.strip('/')

            namespace_url = self.get_namespace_url().strip('/')
            if namespace_url:
                urlstr = protocol + "://" + ipaddress + api_basepath + "/nitro/" + version + "/config/" + namespace_url
            else:
                if not url:
                    urlstr = protocol + "://" + ipaddress + api_basepath+"/nitro/" + version + "/config/" + object_type
                else:
                    urlstr = protocol + "://" + ipaddress + url

                name = self.get_object_id();
                if name:
                    name = name.strip('/')
                if name is not None  and len(name) > 0:
                    urlstr = urlstr + "/" + nitro_util.encode(nitro_util.encode(name))
                else:
                    resource_id = self.get_resource_id()
                    if resource_id:
                        urlstr = urlstr + "/" + resource_id

            '''
            if args is not None :
                urlstr = urlstr + "/" + args
            '''
            if url_filter:
                urlstr = urlstr + "?" + url_filter

            headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid }
            if service.isCloud == True:
                headers = {'Connection': 'keep-alive', 'Cookie':'NITRO_AUTH_TOKEN=' + sessionid, 'isCloud': 'true', 'allow_redirects':'true'}
            self.update_headers(headers)

            if service.ads_service_type:
                headers.update({'ADS_SERVICE_TYPE':service.ads_service_type})

            response = ''

            if service._logger:
                service._logger.debug("DELETE urlstr:"+urlstr)

            if protocol == 'https':
                if service.certverify == True:
                    verify = service.certbundlepath
                cookie_h = {'NITRO_AUTH_TOKEN':sessionid}
                response = requests.delete(urlstr, headers=headers, cookies=cookie_h, timeout=timeout, verify=verify)
            else:
                response = requests.delete(urlstr, headers=headers, timeout=timeout)

            if service._logger:
                service._logger.debug("DELETE Response Payload:"+str(response.text))


            if not response.ok:
                response = json.loads(response.text)
                errorcode,message,severity = base_resource.get_error_details_from_response(response)
                if (errorcode == 444):
                    service.clear_session(self)
                raise nitro_exception(errorcode, str(message), str(severity))
            else:
                if response and hasattr(response,"text"):
                    response = self.get_nitro_response(service, response.text)
            return response

        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error")
        except requests.exceptions.Timeout:
            raise Exception("Request Timed Out")
        except Exception as e:
            raise e

    '''
    put_bulk_data request
    '''
    @classmethod
    def put_bulk_data(cls,service,request,objtype,option_):
        try:
            if not service.isLogin() :
                service.login()
            return cls._put(cls, service, request, option_, objtype)
        except Exception as e:
            raise e




    '''
    update bulk request
    '''
    @classmethod
    def update_bulk_request(cls,service,resources,objtype):
        try:
            if not service.isLogin() :
                service.login()
            option_=options()
            option_.version=service.version
            onerror = service.onerror
            request = service.payload_formatter.resource_to_string_bulk(resources, option_, onerror)
            return cls.put_bulk_data(service,request,objtype, option_)

        except Exception as e:
            raise e



    '''
    delete bulk request
    '''
    @classmethod
    def delete_bulk_request(cls,service,resources,objtype):
        try:
            if not service.isLogin() :
                service.login()
            option_=options()
            option_.action="delete"
            option_.version=service.version
            onerror = service.onerror
            request = service.payload_formatter.resource_to_string_bulk(resources, option_, onerror)
            return cls.post_bulk_data(service,request,objtype,option_)


        except Exception as e:
            raise e


