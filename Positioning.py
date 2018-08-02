#Premise: suppose data is stored in JSON file.

import json
import geoip2.database

class Geo:
    def obtainGeo(self, path):
    """
    :param path the file path of your JSON file
    :return:
    """
    input = open(path, "r")
    for line in input:
   	obj = json.loads(line)
        ip = obj["ip"]
				
	#load external database to obtain geographical info
				
	#This creates a Reader object. You should use the same object across multiple requests as creation of it is expensive.
	reader = geoip2.database.Reader('your path to GeoLite2-City.mmdb')
				
	#Replace "city" with the method corresponding to the database that you are using, e.g., "country".
        geo = reader.city(ip)

        country_iso_code = geo.country.iso_code  #'US'
        country = geo.country.name  #United States
        country_Chinese = geo.country.names['zh-CN']  #u'美国'
        state = geo.subdivisions.most_specific.name  #'Minnesota'
        state_iso_code = geo.subdivisions.most_specific.iso_code  #'MN'
        city = geo.city.name  #'Minneapolis'
        postcode = geo.postal.code  #'55455'
        latitude = geo.location.latitude  #'44.9733'
        longitude = geo.location.longitude  #'-93.2323'

        reader.close()
    
    input.close()
