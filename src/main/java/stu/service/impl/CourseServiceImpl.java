package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Course;
import stu.service.CourseService;
import stu.mapper.CourseMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【course】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class CourseServiceImpl extends ServiceImpl<CourseMapper, Course>
    implements CourseService{

}




