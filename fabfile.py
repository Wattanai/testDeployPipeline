#__author__ = 'wattanai'

from fabric.api import *
from fexpect import expect

def testUATdeploy(pwd, gitpp):

    env.user = 'BuilkTeamCity'
    env.password = pwd

    with cd('/home/BuilkTeamCity'):
        sudo('rm -r -f builkUAT/')
        run('virtualenv builkUAT')

    with cd('/home/BuilkTeamCity/builkUAT'):
        run('git clone git@github.com:Wattanai/testDeployPipeline.git')
        passpharseExpectation = expect("Enter passphrase for key '/home/BuilkTeamCity/.ssh/id_rsa':", gitpp)

    with cd('/home/BuilkTeamCity/builkUAT/bin'):
        run('source activate')
        run('pip install -r ../requirement.txt')
        sudo('rm /etc/nginx/nginx.conf')
        sudo('cp ../nginx.conf /etc/nginx/nginx.conf')
        sudo('nginx -s quit')
        sudo('supervisorctl stop all')
        sudo('supervisord -c ../supervisord.conf')
        sudo('nginx')
