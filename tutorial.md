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
