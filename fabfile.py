#__author__ = 'wattanai'

from fabric.api import *

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
        run('pip install -r testDeployPipeline/requirement.txt')
        sudo('nginx -s quit')
        sudo('rm /etc/nginx/nginx.conf')
        sudo('cp testDeployPipeline/nginx.conf /etc/nginx/nginx.conf')
        sudo('supervisorctl update')
        #sudo('supervisorctl stop torandoes:*')
        #sudo('supervisorctl -c testDeployPipeline/supervisord.conf start tornadoes:*')
        sudo('nginx')


def prepareUATdeployment(pwd):
    env.user = 'BuilkTeamCity'
    env.password = pwd

    with cd('/home/BuilkTeamCity'):
        sudo('rm -r -f builkUAT/')
        run('virtualenv builkUAT')

    with cd('/home/BuilkTeamCity/builkUAT'):
        run('git clone git@github.com:Wattanai/testDeployPipeline.git')
        run('source bin/activate && pip install -r testDeployPipeline/requirement.txt')

    with cd('/home/BuilkTeamCity'):
        run('rsync -arvh -e ssh builkUAT/ BuilkUAT@builkuat.cloudapp.net:/home/BuilkUAT/builkUAT/')

def deployUATserver(pwd):
    env.user = 'BuilkUAT'
    env.password = pwd

    sudo('supervisorctl restart tornadoes:*')

