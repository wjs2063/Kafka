## 실행환경

- OS: mac os



### 설치

- https://www.apache.org/dyn/closer.cgi?path=/kafka/3.2.0/kafka_2.12-3.2.0.tgz 
- terminal 에서 다운로드 받은 파일 경로로 들어간후 ```bin/zookeeper-server-start.sh config/zookeeper.properties ``` (상대경로) : 주키퍼 서버실행 
- ```INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)  ``` 문구가 보이면 성공 
- ```bin/kafka-server-start.sh config/server.properties ``` 새로운터미널 추가후에 명령어 실행  : kafka 서버 실행





## Kafka 기본개념

1. 구성요소 

- Zookeeper           : Kafka 메타데이터 관리 및 브로커의 Health check (정상상태) 담당. AWS의 로드밸런서랑 느낌이 비슷한?거같다 
- Kafka cluster       : 여러대의 브로커를 구성한 클러스터  
- Broker              : Kafka 애플리케이션이 설치된 서버 or 노드  
- Producer            : Kafka 로 메세지를 보내는역할을하는 모든 Clients 
- Consumer            : Kafka 에서 메세지를 꺼내가는 역할을 하는 모든 Clients 
- Topic               : 메시지 피드들을 토픽으로 구분하고 각 토픽은 Kafka 내에서 고유함 (비유를들자면 토픽은 디렉토리 이고 디렉토리안의 파일들은 이벤트들임 )
- Partition           : 병렬 처리 및 고성능을 얻기위해 하나의 토픽을 여러개로 나눈것  
- Segment             :  프로듀서가 전송한 실제메시지가 브로커의 로컬디스크에 저장되는 파일  
- Message             :  프로듀서가 브로커로 전송하거나 컨슈머가 읽어가는 데이터 조각 


- Replication : 각 메세지들을 여러개로 복제하여 Kafka 클러스터내의 브로커들에 분산시키는 동작  ( 다른 브로커가 종료되더라도 안정성 유지가능 )
- Partition  : 하나의 토픽이 한번에 처리할수있는 한계를 높이기위해 토픽하나를 여러개로 나눠 병렬처리가 가능하게만든 것 

2. Kafka 의 핵심 개념 

``` 
1. 분산시스템 : 일부 서버에 장애가 발생할떄 다른 서버가 대신 처리하므로 장애대응에 유연함. 시스템확장 용이 ,
2. Page cache :  OS 의 page cache 를 활용하는 방식
3. Batch 전송 : Batch 단위로 전송하므로 효율적 
4. 압축전송 : 네트워크 대역폭 or 회선 비용등을 줄일수있음 
5. 토픽,파티션, 오프셋 : 파티션의 메세지가 저장되는곳= 오프셋 (64비트정수형태, 오름차순)
6. 고가용성 : 리플리케이션 제공 - 토픽의 파티션 복제  ex 리플리케이션 팩터 4로 설정하면 리더 1 팔로워 3  즉  n개면 1 : n-1 비율  일반적으로 팩터 3으로 권장 
7. 주키퍼 의존성 : 
```
