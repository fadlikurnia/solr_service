#!/bin/sh
# Author: Parama Faldi Kurnia

# shutdown solr service
./opt/hsolr/bin/shutdown.sh

# delete all file with pattern *.log at tomcat server
rm -f /opt/hsolr/tc/logs/*.log

# delete all file with pattern *.txt at tomcat server
rm -f /opt/hsolr/tc/logs/*.txt

# delete all file with pattern solr.log.* at tomcat server
rm -f /opt/hsolr/logs/solr.log.*

# init solr.log with empty content
echo "" > /opt/hsolr/logs/solr.log

# init catalina.out with empty content
echo "" > /opt/hsolr/tc/logs/catalina.out

# start solr service on port 8983
./opt/hsolr/bin/startup.sh -Djetty.port=8983
