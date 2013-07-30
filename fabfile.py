#__author__ = 'wattanai'

from fabric.api import *

def testUATdeploy():

    env.user = 'BuilkTeamCity'
    env.password = 'tmhctr@1008'

    with cd('/var'):
        sudo('mkdir www2')
        sudo('cp /home/BuilkTeamCity/TeamCity/buildAgent/work/a01bcce3ff90c57d/* /var/www2/')