package stu.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.util.Date;
import lombok.Data;

/**
 * 考试时间表
 * @TableName exam_schedule
 */
@TableName(value ="exam_schedule")
@Data
public class ExamSchedule implements Serializable {
    /**
     * 课程编号，引用课程表的course_id
     */
    @TableId(value = "course_id")
    private String courseId;

    /**
     * 考试时间
     */
    @TableField(value = "exam_time")
    private Date examTime;

    /**
     * 教室编号，引用教室表的room_number
     */
    @TableField(value = "room_number")
    private String roomNumber;

    /**
     * 监考教师编号，引用教师表的teacher_id
     */
    @TableField(value = "invigilator_id")
    private Integer invigilatorId;

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
        ExamSchedule other = (ExamSchedule) that;
        return (this.getCourseId() == null ? other.getCourseId() == null : this.getCourseId().equals(other.getCourseId()))
            && (this.getExamTime() == null ? other.getExamTime() == null : this.getExamTime().equals(other.getExamTime()))
            && (this.getRoomNumber() == null ? other.getRoomNumber() == null : this.getRoomNumber().equals(other.getRoomNumber()))
            && (this.getInvigilatorId() == null ? other.getInvigilatorId() == null : this.getInvigilatorId().equals(other.getInvigilatorId()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getCourseId() == null) ? 0 : getCourseId().hashCode());
        result = prime * result + ((getExamTime() == null) ? 0 : getExamTime().hashCode());
        result = prime * result + ((getRoomNumber() == null) ? 0 : getRoomNumber().hashCode());
        result = prime * result + ((getInvigilatorId() == null) ? 0 : getInvigilatorId().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", courseId=").append(courseId);
        sb.append(", examTime=").append(examTime);
        sb.append(", roomNumber=").append(roomNumber);
        sb.append(", invigilatorId=").append(invigilatorId);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}