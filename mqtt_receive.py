# -*- coding:utf-8 -*-
# !/usr/bin/python

import paho.mqtt.client as paho
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc) + '\n')
    client.subscribe("gpio")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload, encoding = 'utf-8') + '\n')



if __name__ == '__main__':
    client = paho.Client()
    client.username_pw_set("admin", "password")
    client.on_connect = on_connect
    client.on_message = on_message
    # client.connect_async(HOST, 61613, 60)
    client.connect("192.168.1.161", 1913, 60)

    client.loop_forever()
