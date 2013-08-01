#__author__ = 'wattanai'

from fabric.api import *
import pexpect

def testUATdeploy(pwd, gitpp='asdfjkl;\''):

    env.user = 'BuilkTeamCity'
    env.password = pwd

    with cd('/home/BuilkTeamCity'):
        sudo('rm -r -f builkUAT/')
        run('virtualenv builkUAT')

    with cd('/home/BuilkTeamCity/builkUAT'):
        run('git clone git@github.com:Wattanai/testDeployPipeline.git')
        #child = pexpect.spawn('git clone git@github.com:Wattanai/testDeployPipeline.git')
        #child.expect('Enter passphrase for key \'/home/BuilkTeamCity/.ssh/id_rsa\':')
        #child.sendline(gitpp)
        #child.interact()


    with cd('/home/BuilkTeamCity/builkUAT'):
        run('source bin/activate')
            #with cd('/home/BuilkTeamCity/builkUAT/testDeployPipeline'):
        run('pip install -r testDeployPipeline/requirement.txt')
        sudo('nginx -s quit')
        sudo('rm /etc/nginx/nginx.conf')
        sudo('cp testDeployPipeline/nginx.conf /etc/nginx/nginx.conf')
        sudo('supervisorctl -c testDeployPipeline/supervisord.conf restart tornadoes:*')
                #sudo('supervisorctl reread')
                #sudo('supervisorctl update')
                #sudo('supervisorctl start tornadoes:*')
                #sudo('supervisorctl stop all')
                #sudo('supervisord -c supervisord.conf')
        sudo('nginx')
