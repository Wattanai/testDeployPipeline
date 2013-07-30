#__author__ = 'wattanai'

from fabric.api import *

def testUATdeploy():
    cd('/var')
    sudo('mkdir www2')
    sudo('cp /home/BuilkTeamCity/TeamCity/builkAgent/work/a01bcce3ff90c57d/* /var/www2/')