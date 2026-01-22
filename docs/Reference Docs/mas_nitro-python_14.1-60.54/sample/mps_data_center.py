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
from massrc.com.citrix.mas.nitro.resource.config.mps.mps_datacenter import mps_datacenter
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class mps_data_center :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = mps_data_center()
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
        self.add_datacenter(client)
        self.delete_datacenter(client)

    def add_datacenter(self,client) :
        try:
            my_datacenter = mps_datacenter()
            my_datacenter.name = "new_dc"
            my_datacenter.latitude = float(12.9716)
            my_datacenter.longitude = float(77.5946)
            simplelist = mps_datacenter.add(client,my_datacenter)         
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("name of the datacenter added: " + simplelist[0].name)
            my_datacenter = mps_datacenter()
            filter_value = "name:new_dc"
            simplelist = mps_datacenter.get_filtered(client,filter_value)
            print("id of the datacenter added: " + simplelist[0].id)
            print("add_datacenter - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message
        except Exception as e:
            raise e


    def delete_datacenter(self,client) :
        try:
            my_datacenter = mps_datacenter()
            filter_value = "name:new_dc"
            simplelist = mps_datacenter.get_filtered(client,filter_value)
            my_datacenter = mps_datacenter()
            my_datacenter.id= str(simplelist[0].id)
            simplelist = mps_datacenter.delete(client,my_datacenter)         
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("id of the datacenter deleted: " + simplelist[0].id)
            print("delete_datacenter - Done")
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
            mps_data_center().main(mps_data_center(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



