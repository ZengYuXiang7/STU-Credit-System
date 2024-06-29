package stu.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author crc
 * @date 2024/6/29
 */
@Configuration
public class SwaggerConfig {
    @Bean
    public OpenAPI openApi() {
        return new OpenAPI()
                .info(new Info()
                        .title("文档标题")
                        .description("文档描述")
                        .contact(new Contact().name("crc").email("邮箱").url("crcbest.top"))
                        .version("v3.0"));
    }

}
