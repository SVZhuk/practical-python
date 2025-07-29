#!/usr/bin/env python

import urllib.request
from xml.etree.ElementTree import parse

url = "http://www.ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"

# Let's first see what we're actually getting from the URL
try:
    u = urllib.request.urlopen(url)
    content = u.read()
    print("Response content (first 500 chars):")
    print(content[:500])
    print("\n" + "=" * 50 + "\n")

    # Reset the file-like object for parsing
    u = urllib.request.urlopen(url)
    doc = parse(u)
    print("XML parsed successfully!")
    
    
except Exception as e:
    print(f"Error parsing XML: {e}")
    print("The response might not be valid XML.")
