package stu.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import stu.pojo.*;
import stu.service.*;

import java.util.List;

/**
 * @author crc
 * @date 2024/6/29
 */
@Tag(name = "管理员功能")
@RestController()
@RequestMapping("/manager")
public class ManagerController {

    @Resource
    CourseService courseService;
   @Resource
    TeachersService teachersService;
   @Resource
    StudentsService studentsService;
   @Resource
    ClassroomsService classroomsService;
   @Resource
   CourseScheduleService courseScheduleService;
   @Resource
   EnrollmentService enrollmentService;
   @Resource
   ExamScheduleService examScheduleService;
   @Resource
   TextbooksService textbooksService;
   @Resource
   TeacherAssignmentService teacherAssignmentService;
    @Resource
    ProgramService  programService;

    @Operation(summary  = "查询全部教师")
    @GetMapping("/teacher/list")
    public List<Teachers> getAllTeacher(){
        return teachersService.list();
    }

    @Operation(summary  = "查询全部学生")
    @GetMapping("/student/list")
    public List<Students> getAllStudent(){
        return studentsService.list();
    }

    @Operation(summary  = "查询全部课程")
    @GetMapping("/course/list")
    public List<Course> getAllCourse(){
        return courseService.list();
    }

    @Operation(summary  = "查询全部教室")
    @GetMapping("/classroom/list")
    public List<Classrooms> getAllClassroom(){
        return classroomsService.list();
    }

    @Operation(summary  = "查询全部课程表")
    @GetMapping("/courseSchedule/list")
    public List<CourseSchedule> getAllCourseSchedule(){
        return courseScheduleService.list();
    }

    @Operation(summary  = "查询全部选课")
    @GetMapping("/enrollment/list")
    public List<Enrollment> getAllEnrollment(){
        return enrollmentService.list();
    }

    @Operation(summary  = "查询全部考试安排")
    @GetMapping("/examSchedule/list")
    public List<ExamSchedule> getAllExamSchedule(){
        return examScheduleService.list();
    }

    @Operation(summary  = "查询全部教材")
    @GetMapping("/textbooks/list")
    public List<Textbooks> getAllTextbooks(){
        return textbooksService.list();
    }

    @Operation(summary  = "查询全部教师分配")
    @GetMapping("/teacherAssignment/list")
    public List<TeacherAssignment> getAllTeacherAssignment(){
        return teacherAssignmentService.list();
    }

    @Operation(summary  = "查询全部项目")
    @GetMapping("/program/list")
    public List<Program> getAllProgram(){
        return programService.list();
    }

}
