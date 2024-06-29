package stu.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.util.Date;
import lombok.Data;

/**
 * 具体课表
 * @TableName course_schedule
 */
@TableName(value ="course_schedule")
@Data
public class CourseSchedule implements Serializable {
    /**
     * 课程编号，引用课程表的course_id
     */
    @TableId(value = "course_id")
    private String courseId;

    /**
     * 上课时间
     */
    @TableField(value = "class_time")
    private Date classTime;

    /**
     * 学生数量
     */
    @TableField(value = "number_of_students")
    private Integer numberOfStudents;

    /**
     * 教室编号，引用教室表的room_number
     */
    @TableField(value = "room_number")
    private String roomNumber;

    /**
     * 教师编号，引用教师表的teacher_id
     */
    @TableField(value = "teacher_id")
    private Integer teacherId;

    @TableField(exist = false)
    private static final long serialVersionUID = 1L;

    @Override
    public boolean equals(Object that) {
        if (this == that) {
            return true;
        }
        if (that == null) {
            return false;
        }
        if (getClass() != that.getClass()) {
            return false;
        }
        CourseSchedule other = (CourseSchedule) that;
        return (this.getCourseId() == null ? other.getCourseId() == null : this.getCourseId().equals(other.getCourseId()))
            && (this.getClassTime() == null ? other.getClassTime() == null : this.getClassTime().equals(other.getClassTime()))
            && (this.getNumberOfStudents() == null ? other.getNumberOfStudents() == null : this.getNumberOfStudents().equals(other.getNumberOfStudents()))
            && (this.getRoomNumber() == null ? other.getRoomNumber() == null : this.getRoomNumber().equals(other.getRoomNumber()))
            && (this.getTeacherId() == null ? other.getTeacherId() == null : this.getTeacherId().equals(other.getTeacherId()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getCourseId() == null) ? 0 : getCourseId().hashCode());
        result = prime * result + ((getClassTime() == null) ? 0 : getClassTime().hashCode());
        result = prime * result + ((getNumberOfStudents() == null) ? 0 : getNumberOfStudents().hashCode());
        result = prime * result + ((getRoomNumber() == null) ? 0 : getRoomNumber().hashCode());
        result = prime * result + ((getTeacherId() == null) ? 0 : getTeacherId().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", courseId=").append(courseId);
        sb.append(", classTime=").append(classTime);
        sb.append(", numberOfStudents=").append(numberOfStudents);
        sb.append(", roomNumber=").append(roomNumber);
        sb.append(", teacherId=").append(teacherId);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}