#!/usr/bin/env python
# coding=utf-8

import sys
import io
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

#f = io.open('tvp.xml', 'w')
#f.write(etree.tounicode(dom, pretty_print=True))
#f.close()

locations = dom.xpath('//target:Location', namespaces={'target': 'http://xml.fmi.fi/namespace/om/atmosphericfeatures/0.95'})
gmlnames = [l.findall('./{http://www.opengis.net/gml/3.2}name') for l in locations]
print [n.text for n in gmlnames[0]]
measurementTVPs = dom.xpath('//wml2:point/wml2:MeasurementTVP', namespaces={'wml2': 'http://www.opengis.net/waterml/2.0'})
temps = [(m.getchildren()[0].text, m.getchildren()[1].text) for m in measurementTVPs]

for t in temps:
    print t[0] + ', ' + t[1]
