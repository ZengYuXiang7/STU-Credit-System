package stu;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author crc
 * @date 2024/6/29
 */
@MapperScan("stu.mapper")
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
    SpringApplication.run(Application.class,args);
    }
}
