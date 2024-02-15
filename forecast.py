#!/usr/bin/env python3

import sys
import json
from pprint import pprint

import weather_gov

# Create connection
# Please set the email before proceeding
email = None
if not email:
    print("Please set the 'email' variable around line 15 to proceed")
    sys.exit(1)


client = weather_gov.Client(email=email)


# Most data must be retrieved via gridpoints, which are derived from LAT/LON.
# West Longitude is negative!
# This is "The Bean" in Chicago, IL
LAT = 41.8826
LON = -87.6233

# Get the "gridpoint" for the forcast; this will convert
# LAT/LON into a gridpoint for that forecast area.
Id, X, Y = client.points.fromLatLon(LAT, LON)

print(f"Lat/Lon ({LAT},{LON}) converts to Gridpoint : ({Id}, {X}, {Y})")

# Fetch the forecast based on this gridpoint
forecast = client.gridpoints.forecast(Id, X, Y)

# Now that we have the JSON output, show the forecast

for period in forecast["properties"]["periods"]:
    print(
        "{name:<15}:  {temp}{unit} {forecast}".format(
            name=period["name"],
            temp=period["temperature"],
            unit=period["temperatureUnit"],
            forecast=period["shortForecast"],
        )
    )
