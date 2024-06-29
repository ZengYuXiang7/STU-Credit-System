package stu.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import lombok.Data;

/**
 * 培养方案
 * @TableName program
 */
@TableName(value ="program")
@Data
public class Program implements Serializable {
    /**
     * 培养方案编号
     */
    @TableId(value = "program_id", type = IdType.AUTO)
    private Integer programId;

    /**
     * 系别
     */
    @TableField(value = "department")
    private String department;

    /**
     * 必修学分
     */
    @TableField(value = "compulsory_credits")
    private Integer compulsoryCredits;

    /**
     * 选修学分
     */
    @TableField(value = "elective_credits")
    private Integer electiveCredits;

    /**
     * 外语学分
     */
    @TableField(value = "foreign_language_credits")
    private Integer foreignLanguageCredits;

    /**
     * 总学分
     */
    @TableField(value = "total_credits")
    private Integer totalCredits;

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
        Program other = (Program) that;
        return (this.getProgramId() == null ? other.getProgramId() == null : this.getProgramId().equals(other.getProgramId()))
            && (this.getDepartment() == null ? other.getDepartment() == null : this.getDepartment().equals(other.getDepartment()))
            && (this.getCompulsoryCredits() == null ? other.getCompulsoryCredits() == null : this.getCompulsoryCredits().equals(other.getCompulsoryCredits()))
            && (this.getElectiveCredits() == null ? other.getElectiveCredits() == null : this.getElectiveCredits().equals(other.getElectiveCredits()))
            && (this.getForeignLanguageCredits() == null ? other.getForeignLanguageCredits() == null : this.getForeignLanguageCredits().equals(other.getForeignLanguageCredits()))
            && (this.getTotalCredits() == null ? other.getTotalCredits() == null : this.getTotalCredits().equals(other.getTotalCredits()));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((getProgramId() == null) ? 0 : getProgramId().hashCode());
        result = prime * result + ((getDepartment() == null) ? 0 : getDepartment().hashCode());
        result = prime * result + ((getCompulsoryCredits() == null) ? 0 : getCompulsoryCredits().hashCode());
        result = prime * result + ((getElectiveCredits() == null) ? 0 : getElectiveCredits().hashCode());
        result = prime * result + ((getForeignLanguageCredits() == null) ? 0 : getForeignLanguageCredits().hashCode());
        result = prime * result + ((getTotalCredits() == null) ? 0 : getTotalCredits().hashCode());
        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(getClass().getSimpleName());
        sb.append(" [");
        sb.append("Hash = ").append(hashCode());
        sb.append(", programId=").append(programId);
        sb.append(", department=").append(department);
        sb.append(", compulsoryCredits=").append(compulsoryCredits);
        sb.append(", electiveCredits=").append(electiveCredits);
        sb.append(", foreignLanguageCredits=").append(foreignLanguageCredits);
        sb.append(", totalCredits=").append(totalCredits);
        sb.append(", serialVersionUID=").append(serialVersionUID);
        sb.append("]");
        return sb.toString();
    }
}