{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f06de6eb-525a-46d7-bc2c-01d4f8d28657",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: kafka-python in ./opt/anaconda3/envs/kafka/lib/python3.7/site-packages (2.0.2)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['/Users/pn_jh',\n",
       " '/Users/pn_jh/opt/anaconda3/envs/kafka/lib/python37.zip',\n",
       " '/Users/pn_jh/opt/anaconda3/envs/kafka/lib/python3.7',\n",
       " '/Users/pn_jh/opt/anaconda3/envs/kafka/lib/python3.7/lib-dynload',\n",
       " '',\n",
       " '/Users/pn_jh/opt/anaconda3/envs/kafka/lib/python3.7/site-packages',\n",
       " '/Users/pn_jh/opt/anaconda3/envs/kafka/lib/python3.7/site-packages/IPython/extensions',\n",
       " '/Users/pn_jh/.ipython']"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "!pip3 install kafka-python\n",
    "#!pip install msgpack\n",
    "#!pip uninstall kafka -y\n",
    "import sys\n",
    "sys.path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "14e7b0e5-450b-4223-b222-d15cdeb5ffa6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/pn_jh'"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "74334265-466a-4145-9f64-52629ded1825",
   "metadata": {},
   "outputs": [],
   "source": [
    "from kafka import KafkaProducer\n",
    "from kafka import KafkaConsumer\n",
    "from kafka import KafkaClient\n",
    "from kafka import TopicPartition\n",
    "import random\n",
    "import traceback\n",
    "import json\n",
    "from kafka import KafkaProducer\n",
    "\n",
    "import json\n",
    "import msgpack"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "63b78da8-09b1-414f-8970-7608c9c8cffa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Local 환경이므로 아래와같이 설정\n",
    "# Cloud 환경이라면 서버 들의 ip와 포트적어주면 됨\n",
    "\n",
    "zookeeper_servers = [\"localhost:2181\"]\n",
    "bootstrap_servers = [\"localhost:9092\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3237a8e5-046c-4ed7-ab68-871a123c6bc4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{BrokerMetadata(nodeId='bootstrap-0', host='localhost', port=9092, rack=None)}"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "client = KafkaClient(bootstrap_servers=bootstrap_servers)\n",
    "client.cluster.brokers()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "7f94d7fc-7f6e-481e-929d-8a23430f1fe1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Broker의 nodeID 를 아래 에 입력해줌\n",
    "client.connected('bootstrap-0')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fda562e4-1f93-4a5c-9063-dc53cc4d4c2d",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a349fe3c-11b5-4523-a148-6c899db04072",
   "metadata": {},
   "outputs": [],
   "source": [
    "metadata = client.cluster.broker_metadata('bootstrap-0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "73acad31-91e1-4286-b350-494b77fea6fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bootstrap-0\n",
      "localhost\n",
      "9092\n"
     ]
    }
   ],
   "source": [
    "print(metadata.nodeId)\n",
    "print(metadata.host)\n",
    "print(metadata.port)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "3545a8ce-7385-40fe-8928-2d4aa95ddb7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "## 브로커 아이디 입력\n",
    "metadata2 = client.cluster.partitions_for_broker('bootstrap-0')\n",
    "metadata2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "367a3030-4bb4-4ec4-8506-242b844a955c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "78092f50-d285-4a7f-94a5-b2da46e8672c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "metadata3 = client.cluster.topics()\n",
    "metadata3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "820f983d-8489-4db9-be8b-75a09f0df000",
   "metadata": {},
   "outputs": [],
   "source": [
    "producer = KafkaProducer(bootstrap_servers=bootstrap_servers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "5a45b08c-d80b-4fb7-8b68-b764e9f096e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(4) :\n",
    "    producer.send(\"topic-180818-byte\", b'byte-msg-%d'%i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "5091b462-bffe-4ee1-b4d8-690b96f45327",
   "metadata": {},
   "outputs": [],
   "source": [
    "for c in \"5678\" :\n",
    "    producer.send(\"topic-180818-1\", json.dumps(\"msg-{}\".format(c)).encode('utf-8'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b7b3bfa-8e8b-434e-8f33-894f6ab70c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "producer = KafkaProducer(bootstrap_servers=bootstrap_servers, \n",
    "                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41317382-a8ec-4e2b-ba5b-8386f3cfc368",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
