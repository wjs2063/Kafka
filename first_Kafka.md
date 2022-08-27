
카프카의 폴더 : /Users/pn_jh/Desktop/kafka/kafka_2.13-3.2.0

## 실행준비 


### STEP 1
```  
 bin/zookeeper-server-start.sh config/zookeeper.properties   : Kafka 파일이 들어있는 폴더로 터미널 진입 후 지정 ( 상대경로이기때문) , 주키퍼실행
```
### STEP 2
``` 
bin/kafka-server-start.sh config/server.properties           : Kafka 서버 실행
```

- 이대로 진행하면 아마   1번오류가 뜰가능성이높다
``` 
 vi config/server.properties  로  i (insert 모드) 누르고 
 advertised.listeners=PLAINTEXT://your.host.name:9092 //  ip 주소 (ex: localhost) your.host.name 부분에 내 아이피를 적어준다
 그리고 esc 누르고 :wq 입력후 나온다
```

### STEP 3
```
 bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic first-kafka01
```

정상적으로 생성됐다.

### STEP 4
토픽이 잘 생성되었는지 판단하는 command
```
bin/kafka-topics.sh --describe --topic first-kafka01 --bootstrap-server localhost:9092
```

### STEP 5
프로듀서 생성
```
bin/kafka-console-producer.sh --topic first-kafka01 --bootstrap-server localhost:9092 
```
실행하면 메세지들 입력가능 
원하는대로 입력해본다 

### STEP 6

```
bin/kafka-console-consumer.sh --topic first-kafka01 --from-beginning --bootstrap-server localhost:9092
```
실행하면 내가보낸 메세지들이 잘 전송이되었다는것을 알수있다.





























### Error
1.
- WARN [Controller id=0, targetBrokerId=0] Connection to node 0 (/[내아이피주소]:9092) could not be established. 
