#!/bin/python3

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

loc = result['iss_position']
lat = loc['latitude']
lon = loc['longitude']

print('Current ISS Position:')
print('Latitude: ', lat)
print('Longitude: ', lon)
print('')
  
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

#Home dot
latH = 51.643769
lonH = -2.685062
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lonH, latH)
location.dot(5)
location.hideturtle()

#show nest pass over time
passUrl = 'http://api.open-notify.org/iss-pass.json?lat=' + str(latH) + '&lon=' + str(lonH)
response = urllib.request.urlopen(passUrl)
result2 = json.loads(response.read())

passover = result2['response'][1]['risetime']
print('Current time is:')
print(time.ctime(time.time()))
print('Next passover time will be:')
print(time.ctime(passover))
passover2 = result2['response'][2]['risetime']

#display passover time on map
style = ('Arial', 6, 'bold')
location.write(time.ctime(passover), font=style)
nt = turtle.Turtle()
nt.penup()
nt.color('lawn green')
nt.goto (75, -60)
nt.write(time.ctime(passover2), font=style)
nt.hideturtle()

ttp = passover - time.time()

timeTillPass = int((ttp - (ttp % 3600)) / 3600)
timeTillPassMin = int((ttp - (timeTillPass * 3600)) / 60)
#time left
ct = turtle.Turtle()
ct.penup()
ct.color('lawn green')
ct.goto (-170, -70)
ct.write(str(timeTillPass) + ' hr, ' + str(timeTillPassMin) + ' min', font=style)
ct.hideturtle()
