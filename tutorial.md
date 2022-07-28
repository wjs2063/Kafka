## 실행환경

- OS: mac os



### 설치

- https://www.apache.org/dyn/closer.cgi?path=/kafka/3.2.0/kafka_2.12-3.2.0.tgz 
- terminal 에서 다운로드 받은 파일 경로로 들어간후 ```bin/zookeeper-server-start.sh config/zookeeper.properties ``` (상대경로) : 주키퍼 서버실행 
- ```INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)  ``` 문구가 보이면 성공 
- ```bin/kafka-server-start.sh config/server.properties ``` 새로운터미널 추가후에 명령어 실행  : kafka 서버 실행
