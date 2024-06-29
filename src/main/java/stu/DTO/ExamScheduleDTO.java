package stu.DTO;

import java.util.Date;

/**
 * @author crc
 * @date 2024/6/29
 */
public class ExamScheduleDTO {
    private String courseId;
    private String courseName;
    private Date examTime;
    private String roomNumber;
    private int invigilatorId;

    // Getters and setters
    public String getCourseId() {
        return courseId;
    }

    public void setCourseId(String courseId) {
        this.courseId = courseId;
    }

    public String getCourseName() {
        return courseName;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }

    public Date getExamTime() {
        return examTime;
    }

    public void setExamTime(Date examTime) {
        this.examTime = examTime;
    }

    public String getRoomNumber() {
        return roomNumber;
    }

    public void setRoomNumber(String roomNumber) {
        this.roomNumber = roomNumber;
    }

    public int getInvigilatorId() {
        return invigilatorId;
    }

    public void setInvigilatorId(int invigilatorId) {
        this.invigilatorId = invigilatorId;
    }
}