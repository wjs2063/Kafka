#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:09:58 2022

@author: pn_jh
"""

#!pip3 install kafka-python
#!pip3 install msgpack

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import KafkaClient
from kafka import TopicPartition

import json
import msgpack

#First bin/zookeeper-server-start.sh config/zookeeper.properties

#Second bin/kafka-server-start.sh config/server.properties

# bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic first-kafka01


# Zookeeper,Kafka 서버, Topic 생성먼저해야함

zookeeper_servers = ["localhost:2181"]
bootstrap_servers = ["localhost:9092"]

client = KafkaClient(bootstrap_servers=bootstrap_servers,)

client_info=list(client.cluster.brokers())[0]
# client_info[0] 에는 node_Id 가 들어가있음
print(client.connected(client_info[0]))
#client.connected(client_info[0])

# broker의 metadata들 
metadata = client.cluster.broker_metadata(client_info[0])

print(metadata.nodeId)
print(metadata.host)
print(metadata.port)


metadata2 = client.cluster.partitions_for_broker(client_info[0])
print(metadata2)


metadata3 = client.cluster.topics()
print(metadata3)

# Broker 에 메세지를 보낼때에는 byte 형이나 json 형태의 직렬화가능한경우만 가능 
# INT,STRING 불가능


producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


for i in range(10) :
    producer.send("topic-first_kafka01-byte", b'byte-msg-%d'%i)


consumer_byte = KafkaConsumer("topic-first_kafka01-byte",
                              bootstrap_servers=bootstrap_servers, 
                              group_id = None,
                              enable_auto_commit=True,
                              auto_offset_reset='earliest',
                              consumer_timeout_ms = 5000
                             )
try : 
    for msg in consumer_byte :
        print(msg.value.decode("utf-8"))
        print(msg.topic, msg.partition, msg.offset, msg.key)
        print("")
    
except :
    consumer_byte.close()
    print("finished --- 1")
    
finally :
    consumer_byte.close()
    print("finished --- 2")