#!/usr/bin/env python
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
import sys
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.resource.config.mps.managed_device import managed_device
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service

class add_get_delete_managed_device :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = add_get_delete_managed_device()
        config.ip = args_[1]
        config.username = args_[2]
        config.password = args_[3]


        try :
            client = nitro_service(config.ip,"http")
            #client.isCloud = True          #uncomment this line for NetScaler Console       
            client.set_credential(config.username,config.password) #For Service, username and password are treated as ID and secret
            client.timeout = 1800
            client.login()
            config.run_sample(client)
            client.logout()
        except nitro_exception as  e:
            print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::message="+str(e.args))
        return



    def run_sample(self, client) :
        self.add_managed_device(client)  #Adding managed_device by uploading csv file
        self.get_device_id_list(client,{"attrs" : "ip_address,id"})
        self.delete_managed_device(client,"5ea1b39d-58b2-41cc-9eb8-65eb9d8ec5f5") #deleting managed_device by its id. Provide valid id here by getting the list of ids first.


    def uploadCSV_file(self,client):
        obj=managed_device()
        obj.file_name="Sample.csv"
        obj.file_location_path="C:/Users/Suraj/Desktop/Desktop"
        managed_device.upload(client,obj)

    def add_managed_device(self,client) :
        try:
            self.uploadCSV_file(client)
            obj=managed_device()
            obj.file_name="Sample.csv"
            obj.profile_name="ns_nsroot_profile"
            managed_device.add_device(client,obj)
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("add_managed_device - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message

        except Exception as e:
            raise e

    def delete_device(self, client, device_id):
        '''
        This function deletes a device from the NetScaler Console.
        Args:
            client: [mandatory] The nitro service object using which the operation will be performed
            device_id: [mandatory] [str] The ID of the device to be deleted
        Returns:
            True/False: True if delete is successful, False otherwise
        '''
        try:
            device_obj = managed_device()
            device_obj.id = str(device_id)
            simplelist = managed_device.delete(mas_client,device_obj)
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("delete_managed_device - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message
        except Exception as e:
            raise e

    def get_device_id_list(self,client,options):
        try:
            device_obj = managed_device()
            # options = urlencode(options)
            # simplelist = managed_device.get(mas_client,None,options)
            simplelist = managed_device.get(mas_client)
            print "--------------"
            print "Response Came :"
            print "--------------"
            for item in simplelist:
                print("ip_address: %s",item["ip_address"])
                print("id: %s",item["id"])
                print("--------------")
            print("get_device_id_list - Done\n")
            

        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message
        except Exception as e:
            raise e

#
# Main thread of execution
#

if __name__ == '__main__':
    try:
        print len(sys.argv)
        if len(sys.argv) < 3:
            sys.exit()
        else:
            ipaddress=sys.argv[1]
            username=sys.argv[2]
            password=sys.argv[3]
            add_get_delete_managed_device().main(add_get_delete_managed_device(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



