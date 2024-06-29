package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Students;
import stu.service.StudentsService;
import stu.mapper.StudentsMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【students(学生表)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class StudentsServiceImpl extends ServiceImpl<StudentsMapper, Students>
    implements StudentsService{

}




