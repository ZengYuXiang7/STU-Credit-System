package stu.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import stu.pojo.Program;
import stu.service.ProgramService;
import stu.mapper.ProgramMapper;
import org.springframework.stereotype.Service;

/**
* @author SmdxLa
* @description 针对表【program(培养方案)】的数据库操作Service实现
* @createDate 2024-06-29 17:16:47
*/
@Service
public class ProgramServiceImpl extends ServiceImpl<ProgramMapper, Program>
    implements ProgramService{

}




