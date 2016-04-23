#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$Apr 23, 2016 3:36:55 PM$"

from subprocess import call

# shutdown solr service
call("bash /opt/hsolr/bin/shutdown.sh", shell=True)

# delete all file with pattern *.log at tomcat server
call("rm -f /opt/hsolr/tc/logs/*.log", shell=True)

# delete all file with pattern *.txt at tomcat server
call("rm -f /opt/hsolr/tc/logs/*.txt", shell=True)

# delete all file with pattern solr.log.* at tomcat server
call("rm -f /opt/hsolr/logs/solr.log.*", shell=True)

# init solr.log with empty content
call("echo "" > /opt/hsolr/logs/solr.log", shell=True)

# init catalina.out with empty content
call("echo "" > /opt/hsolr/tc/logs/catalina.out", shell=True)

# start solr service on port 8983
call("bash /opt/hsolr/bin/startup.sh -Djetty.port=8983 -Xms4096m -Xmx4096m", shell=True)
print "FINISHED"
