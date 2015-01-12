#!/usr/bin/env python
# coding=utf-8
import sys
import urllib2
from lxml import etree

place = sys.argv[1]
starttime = sys.argv[2]
endtime = sys.argv[3]
apikey = sys.argv[4]

url = 'http://data.fmi.fi/fmi-apikey/{}/wfs' \
      '?request=getFeature' \
      '&storedquery_id=fmi::observations::weather::daily::timevaluepair' \
      '&parameters=tday' \
      '&place={}' \
      '&starttime={}' \
      '&endtime={}' \
      '&'.format(apikey, place, starttime, endtime)

xmlurl = urllib2.urlopen(url)

dom = etree.parse(xmlurl)

measurementTVPs = dom.xpath('//wml2:point/wml2:MeasurementTVP', namespaces={'wml2': 'http://www.opengis.net/waterml/2.0'})
temps = [(m.getchildren()[0].text, m.getchildren()[1].text) for m in measurementTVPs]

for t in temps:
    print t[0] + ', ' + t[1]
