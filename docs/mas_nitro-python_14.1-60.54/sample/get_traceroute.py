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
from massrc.com.citrix.mas.nitro.resource.config.mps.traceroute import traceroute
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class get_traceroute :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = get_traceroute()
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
        self.perform_traceroute(client,"10.106.101.112")

    def perform_traceroute(self,client, device_ip, partition = None) :
        '''
        This function emulates the traceroute function for a device associated with the NetScaler Console.
        Args:
            client: [mandatory] The nitro service object using which the operation will be performed
            device_ip: [mandatory] [str] The IP of the device that needs to be tracerouted
            partition: [optional] [str] The name of the partition in the device that needs to be tracerouted
        Returns:
            traceroute_status: [str] A string containing the status of the traceroute operation
        '''
        try:
            traceroute_obj = traceroute()
            if partition:
                device_ip = device_ip + "-" + partition
            traceroute_obj.device_ipaddress = device_ip
            simplelist = traceroute.get(client, traceroute_obj)
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("traceroute status: "+simplelist[0].traceroute_status)
            print("device ip address: "+simplelist[0].device_ipaddress)
            print("perform_traceroute - Done")
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
            get_traceroute().main(get_traceroute(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



