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
import operator
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.resource.config.mps.system_settings import system_settings
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class get_system_settings :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = get_system_settings()
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
        self.get_system_details(client,["svm_ns_comm","session_timeout","id"])

    def get_system_details(self, mas_client, details_to_fetch):

        try:
            simplelist = system_settings.get(mas_client)
            print "--------------"
            print "Response Came :"
            print "--------------"
            for detail in details_to_fetch:
                detail_value = (operator.attrgetter(detail)(simplelist[0]))
                print(detail + " : " + detail_value)
            print("get_system_details - Done")
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
            get_system_settings().main(get_system_settings(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



