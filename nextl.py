def lambda_handler(event, context):
    # TODO implement
    import urllib2
    import xml.etree.ElementTree as ET

    nextLTime = ""
    nextLURL="http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=L%7C3601";
    nextL_debug = False

    response = urllib2.urlopen(nextLURL, timeout = 5)
    content = response.read()
    tree = ET.fromstring(content)

    if nextL_debug is True:
    	print "**********************"
    	print content
    	print "**********************"

    flag = False
    for child in tree.iter():
	if child.tag == 'predictions':
		print 'Stop = ' + child.attrib['stopTitle']
	if child.tag == 'direction':
		if child.attrib['title'] == 'Inbound to Embarcadero Station':
			print 'Direct = ' + child.attrib['title']
			flag = True
	if (flag is True and child.tag == 'prediction'):
        	if nextL_debug is True:
			print child.tag, child.attrib
		depart_min = child.attrib['minutes']
		depart_sec = child.attrib['seconds']
		print 'Departure min = ' + depart_min
		nextLTime = depart_min
		break
    return nextLTime

lambda_handler("","")
