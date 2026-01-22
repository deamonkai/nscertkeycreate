import sys
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.resource.config.mps.config_job import config_job
from massrc.com.citrix.mas.nitro.resource.config.mps.configuration_template import configuration_template
from massrc.com.citrix.mas.nitro.resource.config.mps.config_command import config_command
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class add_config_job :
    def __init__(self):
        ipaddress=""
        username=""
        password=""

    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = add_config_job()
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
        self.create_configjob(client)

    def create_configjob(self,client) :
        try:
            device_list=[]
            device_list.append('10.102.201.86-p1')

            config_commandObj=config_command()
            config_commandObj.protocol='SSH'
            config_commandObj.command='show ns config'

            command_list=[]
            command_list.append(config_commandObj)

            config_temp=configuration_template()
            config_temp.commands=command_list

            config_job_obj= config_job()
            config_job_obj.name='test2'
            config_job_obj.devices=device_list
            config_job_obj.device_family='ns'
            config_job_obj.scheduleTimesEpoch='1481997540'
            config_job_obj.tz_offset=19800
            config_job_obj.on_error="CONTINUE"
            config_job_obj.template_info=config_temp
            simplelist = config_job.add(client, config_job_obj)
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("name : "+simplelist[0].name)
            print("status : "+simplelist[0].status)
            print("create_configjob - Done")

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
            add_config_job().main(add_config_job(),sys.argv)

    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")

