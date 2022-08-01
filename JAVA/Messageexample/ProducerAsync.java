package org.example;
import java.util.Properties;
import java.util.Scanner;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.commons.lang3.StringUtils;
public class ProducerAsync {
    private static final String FIN_MESSAGE = "exit";
    private static final String TOPIC_NAME = "first-kafka01";

    public static void main(String[] args) {
        Properties props = new Properties(); //Properties 오브젝트를 시작
        props.put("bootstrap.servers", "localhost:9092"); //브로커 리스트를 정의합니다. 실제 서버는없고 local에서 진행
        props.put("key.serializer",
                "org.apache.kafka.common.serialization.StringSerializer"); //메시지 키와 벨류에 문자열을 지정하므로 내장된 StringSerializer를 지정
        props.put("value.serializer",
                "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<>(props); //Properties 오브젝트를 전달해 새 프로듀서를 생성

        while(true) {
            Scanner sc = new Scanner(System.in);
            System.out.print("Input > ");
            String message = sc.nextLine();

            ProducerRecord<String, String> record = new ProducerRecord<>(TOPIC_NAME, message);
            try {
                producer.send(record, (metadata, exception) -> {
                    if (exception != null) {
                        // some exception
                    }
                });

            } catch (Exception e) {
                // exception
            } finally {
                producer.flush();
            }

            if (StringUtils.equals(message, FIN_MESSAGE)) {
                producer.close();
                break;
            }
        }
    }
}
