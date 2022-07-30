## Kafka - JAVA

### IntelliJ

- 파일 -> 프로젝트 구조 -> 모듈 -> 디펜던시 -> + 누르고 kafka폴더의 lib 의 jar 파일 넣어준다 
- 파일 -> Invalidate Caches / Restart 를 해본다
- view -> Tool windows -> Gradle -> Refresh Gradle dependencies 


```
bin/kafka-topics.sh --bootstrap-server first-kafka01:9092 --create --topic peter-basic01 --partitions 1 --replication-factor 1
```




