package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Enrollment;
import stu.service.EnrollmentService;
import stu.mapper.EnrollmentMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【enrollment(全部学生选课情况)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class EnrollmentServiceImpl extends ServiceImpl<EnrollmentMapper, Enrollment>
    implements EnrollmentService{

}




