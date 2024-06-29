package stu.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import lombok.Data;

/**
 * 教师任课表
 * @TableName teacher_assignment
 */
@TableName(value ="teacher_assignment")
@Data
public class TeacherAssignment implements Serializable {
    /**
     * 任课编号
     */
    @TableId(value = "assignment_id", type = IdType.AUTO)
    private Integer assignmentId;

    /**
     * 课程编号，引用课程表的course_id
     */
    @TableField(value = "course_id")
    private String courseId;

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
        TeacherAssignment other = (TeacherAssignment) that;
        return (this.getAssignmentId() == null ? other.getAssignmentId() == null : this.getAssignmentId().equals(other.getAssignmentId()))
            && (this.getCourseId() == null ? other.getCourseId() == null : this.getCourseId().equals(other.getCourseId()))
            && (this.getTeacherId() == null ? other.getTeacherId() == null : this.getTeacherId().equals(other.getTeacherId()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getAssignmentId() == null) ? 0 : getAssignmentId().hashCode());
        result = prime * result + ((getCourseId() == null) ? 0 : getCourseId().hashCode());
        result = prime * result + ((getTeacherId() == null) ? 0 : getTeacherId().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", assignmentId=").append(assignmentId);
        sb.append(", courseId=").append(courseId);
        sb.append(", teacherId=").append(teacherId);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}