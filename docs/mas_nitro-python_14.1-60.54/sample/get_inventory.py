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
from massrc.com.citrix.mas.nitro.resource.config.mps.inventory import inventory
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class get_inventory :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = get_inventory()
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
        self.inventory_check(client,"10.106.101.112")

    def inventory_check(self,client,device_ip,partition = None) :
        '''
        This function emulates the 'rediscover' option for a device added to the NetScaler Console.
        Args:
            mas_client: [mandatory] The nitro service object using which the operation will be performed
            device_ip: [mandatory] [str] The IP of the device that needs to be rediscovered
            partition: [optional] [str] The name of the partition in the device that needs to be rediscovered
        Returns:
            act_id: [str] The activity ID of the rediscovery process
        '''
        try:
            inventory_obj = inventory()
            if partition:
                device_ip = device_ip + "-" + partition
            inventory_obj._device_ipaddress = device_ip
            simplelist = inventory.get(client)
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("activity id from inventory check: "+simplelist[0].act_id)
            print("inventory_check - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message
        except Exception as e:
            print "here"

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
            get_inventory().main(get_inventory(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



