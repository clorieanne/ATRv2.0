"""module for Student"""
from sqlconnect import spcall

class Student:
    """Student Class"""
    def add_personal_info(cls, stud_id, nameFirst, nameMid, nameLast,
                        nickname, gender, birthdate, birthMonth,
                        birthYear, age, contactNum, homeAddress,
                        father_nameFirst, father_nameMiddle,
                        father_nameLast, mother_nameFirst,
                        mother_nameMiddle, mother_nameLast,
                        guardian_nameFirst, guardian_nameMiddle,
                        guardian_nameLast, spouse_nameFirst,
                        spouse_nameMiddle, spouse_nameLast ):

        res = spcall('addpersonalinfo',(stud_id, nameFirst, nameMid, nameLast,
                        nickname, gender, birthdate, birthMonth,
                        birthYear, age, contactNum, homeAddress,
                        father_nameFirst, father_nameMiddle,
                        father_nameLast, mother_nameFirst,
                        mother_nameMiddle, mother_nameLast,
                        guardian_nameFirst, guardian_nameMiddle,
                        guardian_nameLast, spouse_nameFirst,
                        spouse_nameMiddle, spouse_nameLast), True)
        return str(res[0][0])

    def add_application(cls, stud_id, course, college, org_name,
                        position, acad_year, acad_award, scholarship,
                        dissertation, special_project, thesis_title,
                        status):

        res = spcall('apply',(stud_id, course, college, org_name,
                        position, acad_year, acad_award, scholarship,
                        dissertation, special_project, thesis_title,
                        status), True)
        return res[0][0]

