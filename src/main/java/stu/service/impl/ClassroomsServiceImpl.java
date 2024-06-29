package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Classrooms;
import stu.service.ClassroomsService;
import stu.mapper.ClassroomsMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【classrooms(教室表)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class ClassroomsServiceImpl extends ServiceImpl<ClassroomsMapper, Classrooms>
    implements ClassroomsService{

}




