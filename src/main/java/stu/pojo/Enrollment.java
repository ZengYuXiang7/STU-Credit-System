package stu.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import lombok.Data;

/**
 * 全部学生选课情况
 * @TableName enrollment
 */
@TableName(value ="enrollment")
@Data
public class Enrollment implements Serializable {
    /**
     * 选课编号
     */
    @TableId(value = "enrollment_id", type = IdType.AUTO)
    private Integer enrollmentId;

    /**
     * 学生编号，引用学生表的student_id
     */
    @TableField(value = "student_id")
    private Integer studentId;

    /**
     * 课程编号，引用课程表的course_id
     */
    @TableField(value = "course_id")
    private String courseId;

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
        Enrollment other = (Enrollment) that;
        return (this.getEnrollmentId() == null ? other.getEnrollmentId() == null : this.getEnrollmentId().equals(other.getEnrollmentId()))
            && (this.getStudentId() == null ? other.getStudentId() == null : this.getStudentId().equals(other.getStudentId()))
            && (this.getCourseId() == null ? other.getCourseId() == null : this.getCourseId().equals(other.getCourseId()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getEnrollmentId() == null) ? 0 : getEnrollmentId().hashCode());
        result = prime * result + ((getStudentId() == null) ? 0 : getStudentId().hashCode());
        result = prime * result + ((getCourseId() == null) ? 0 : getCourseId().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", enrollmentId=").append(enrollmentId);
        sb.append(", studentId=").append(studentId);
        sb.append(", courseId=").append(courseId);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}