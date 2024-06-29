package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Teachers;
import stu.service.TeachersService;
import stu.mapper.TeachersMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【teachers(教师表)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class TeachersServiceImpl extends ServiceImpl<TeachersMapper, Teachers>
    implements TeachersService{

}




