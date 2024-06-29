package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Textbooks;
import stu.service.TextbooksService;
import stu.mapper.TextbooksMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【textbooks(教材表)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class TextbooksServiceImpl extends ServiceImpl<TextbooksMapper, Textbooks>
    implements TextbooksService{

}




