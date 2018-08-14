#!/bin/python3

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

loc = result['iss_position']
lat = loc['latitude']
lon = loc['longitude']

print('Latitude: ', lat)
print('Longitude: ', lon)
  
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss2.png')
iss = turtle.Turtle()
iss.shape('iss2.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)
