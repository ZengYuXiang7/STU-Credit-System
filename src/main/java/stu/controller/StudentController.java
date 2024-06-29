package stu.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import stu.DTO.CourseScheduleDTO;
import stu.DTO.ExamScheduleDTO;
import stu.pojo.Course;
import stu.pojo.CourseSchedule;
import stu.pojo.Enrollment;
import stu.pojo.ExamSchedule;
import stu.service.CourseScheduleService;
import stu.service.CourseService;
import stu.service.EnrollmentService;
import stu.service.ExamScheduleService;

import java.util.List;
import java.util.stream.Collectors;

/**
 * @author crc
 * @date 2024/6/29
 */
@Tag(name = "学生功能")
@RestController()
@RequestMapping("/student")
public class StudentController {

    @Resource
    private EnrollmentService enrollmentService;
    @Resource
    private CourseService courseService;
    @Resource
    private CourseScheduleService courseScheduleService;
    @Resource
    private ExamScheduleService examScheduleService;


    @Operation(summary = "查询学生已经选的课程")
    @GetMapping("/course/list/{id}")
    public List<Course> getStudentCourse(@PathVariable("id") int studentId) {
        // 创建查询条件
        QueryWrapper<Enrollment> enrollmentQueryWrapper = new QueryWrapper<>();
        enrollmentQueryWrapper.eq("student_id", studentId);

        // 查询选课信息
        List<Enrollment> enrollments = enrollmentService.list(enrollmentQueryWrapper);

        // 根据选课信息查询课程详情
        List<Course> courses = enrollments.stream()
                .map(enrollment -> courseService.getById(enrollment.getCourseId()))
                .collect(Collectors.toList());

        return courses;
    }

    @Operation(summary = "查询个人课表")
    @GetMapping("/course/personal/{studentId}")
    public List<CourseScheduleDTO> getStudentSchedule(@PathVariable("studentId") int studentId) {
        // 创建查询条件
        QueryWrapper<Enrollment> enrollmentQueryWrapper = new QueryWrapper<>();
        enrollmentQueryWrapper.eq("student_id", studentId);

        // 查询选课信息
        List<Enrollment> enrollments = enrollmentService.list(enrollmentQueryWrapper);

        // 根据选课信息查询课程安排
        List<CourseScheduleDTO> courseSchedules = enrollments.stream().map(enrollment -> {
            // 创建查询条件
            QueryWrapper<CourseSchedule> courseScheduleQueryWrapper = new QueryWrapper<>();
            courseScheduleQueryWrapper.eq("course_id", enrollment.getCourseId());

            // 查询课程安排
            CourseSchedule courseSchedule = courseScheduleService.getOne(courseScheduleQueryWrapper);

            // 获取课程名称
            Course course = courseService.getById(courseSchedule.getCourseId());

            // 创建DTO
            CourseScheduleDTO courseScheduleDTO = new CourseScheduleDTO();
            courseScheduleDTO.setCourseId(courseSchedule.getCourseId());
            courseScheduleDTO.setCourseName(course.getCourseName());
            courseScheduleDTO.setClassTime(courseSchedule.getClassTime());
            courseScheduleDTO.setNumberOfStudents(courseSchedule.getNumberOfStudents());
            courseScheduleDTO.setRoomNumber(courseSchedule.getRoomNumber());
            courseScheduleDTO.setTeacherId(courseSchedule.getTeacherId());

            return courseScheduleDTO;
        }).collect(Collectors.toList());

        return courseSchedules;
    }

    @Operation(summary = "查询考试时间")
    @GetMapping("/exam/list/{studentId}")
    public List<ExamScheduleDTO> getStudentExamSchedule(@PathVariable("studentId") int studentId) {
        // 创建查询条件
        QueryWrapper<Enrollment> enrollmentQueryWrapper = new QueryWrapper<>();
        enrollmentQueryWrapper.eq("student_id", studentId);

        // 查询选课信息
        List<Enrollment> enrollments = enrollmentService.list(enrollmentQueryWrapper);

        // 根据选课信息查询考试安排
        List<ExamScheduleDTO> examSchedules = enrollments.stream().map(enrollment -> {
            // 创建查询条件
            QueryWrapper<ExamSchedule> examScheduleQueryWrapper = new QueryWrapper<>();
            examScheduleQueryWrapper.eq("course_id", enrollment.getCourseId());

            // 查询考试安排
            ExamSchedule examSchedule = examScheduleService.getOne(examScheduleQueryWrapper);

            // 获取课程名称
            Course course = courseService.getById(examSchedule.getCourseId());

            // 创建DTO
            ExamScheduleDTO examScheduleDTO = new ExamScheduleDTO();
            examScheduleDTO.setCourseId(examSchedule.getCourseId());
            examScheduleDTO.setCourseName(course.getCourseName());
            examScheduleDTO.setExamTime(examSchedule.getExamTime());
            examScheduleDTO.setRoomNumber(examSchedule.getRoomNumber());
            examScheduleDTO.setInvigilatorId(examSchedule.getInvigilatorId());

            return examScheduleDTO;
        }).collect(Collectors.toList());

        return examSchedules;
    }


    @Operation(summary = "查询考试成绩")
    @GetMapping("/grades/{studentId}")
    public List<Enrollment> getStudentGrades(@PathVariable("studentId") int studentId) {
        // 创建查询条件
        QueryWrapper<Enrollment> enrollmentQueryWrapper = new QueryWrapper<>();
        enrollmentQueryWrapper.eq("student_id", studentId);

        // 查询选课信息
        List<Enrollment> enrollments = enrollmentService.list(enrollmentQueryWrapper);

        // 返回带有成绩信息的选课记录
        return enrollments;
    }

}
