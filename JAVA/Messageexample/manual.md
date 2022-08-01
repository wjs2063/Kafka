

## Producer, Consumer 간의 메시지 교환 예제



# USAGE

### Zookeeper 실행
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Kafka server 실행
```
bin/kafka-server-start.sh config/server.properties
```


### TOPIC 생성
```
in/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic first-kafka01
```

```

```

```
