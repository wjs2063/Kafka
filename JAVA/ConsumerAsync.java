package org.example;
import java.util.Properties;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.commons.lang3.StringUtils;
import java.util.Arrays;

public class ConsumerAsync{
    private static final String FIN_MESSAGE = "exit";
    private static final String TOPIC_NAME = "first-kafka01";
    public static void main(String[] args) {
        Properties props = new Properties(); //Properties 오브젝트를 시작합니다.
        props.put("bootstrap.servers", "localhost:9092"); //브로커 리스트를 정의합니다.
        props.put("group.id", "kafka-consumer01"); //컨슈머 그룹 아이디 정의합니다.
        props.put("enable.auto.commit", "false"); //자동 커밋을 사용하지 않습니다.
        props.put("auto.offset.reset", "latest"); //컨슈머 오프셋을 찾지 못하는 경우 latest로 초기화 합니다. 가장 최근부터 메시지를 가져오게 됩니다.
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer"); //문자열을 사용했으므로 StringDeserializer 지정합니다.
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props); //Properties 오브젝트를 전달하여 새 컨슈머를 생성합니다.
        consumer.subscribe(Arrays.asList("first-kafka01")); //구독할 토픽을 지정합니다.

        String message = null;
        try {
            do {
                ConsumerRecords<String, String> records = consumer.poll(1000);

                for (ConsumerRecord<String, String> record : records) {
                    message = record.value();
                    System.out.println(message);
                }
            } while (!StringUtils.equals(message, FIN_MESSAGE));
        } catch(Exception e) {
            // exception
        } finally {
            consumer.close();
        }
    }
}
