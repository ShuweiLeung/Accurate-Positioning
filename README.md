# Accurate-Positioning1

## Description

At work, I need to resolve a problem involving millions of IP addresses and do some meaningful things. Apparently, in order to obtain readable and geographical information corresponding to each IP address, it's unrealistic to search every IP address on special websites, so I write this automation script to deal with a batch of data.

Here are some instructions.

## Installation

To install the geoip2 module, type:

```
$ pip3 install geoip2
```

## Free GeoLite2 Databases

GeoLite2 databases are free IP geolocation databases comparable to, but less accurate than, MaxMind’s GeoIP2 databases. The GeoLite2 Country and City databases are updated on the first Tuesday of each month. The GeoLite2 ASN database is updated every Tuesday.

You can download them from [here](https://dev.maxmind.com/geoip/geoip2/geolite2/).

After that, unzip databases wherever you want. But, remember to change the database path in **Positioning.py**.

## Running Script
Run automation script in Python 3.x. Enjor yourself! :)
