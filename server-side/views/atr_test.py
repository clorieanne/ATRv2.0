import unittest
import json
import time
from atr import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.atr = Student()
        self.stud = '2012-6368'
        self.course = 1
        self.college = 1
        self.org_name = 'COMSOC'
        self.position = 'Auditor'
        self.acad_year = '2015-2016'
        self.acad_award = 'DOST'
        self.scholarship = 'DOST'
        self.dissertation = 'NA'
        self.special_project = 'NA'
        self.thesis_title = 'Hybrid'
        self.status = 'True'
        self.nameFirst = 'Lorie'
        self.nameMid = 'Millan'
        self.nameLast = 'Castillano'
        self.nickname = 'Sweet2x'
        self.gender = 'F'
        self.birthdate = '27'
        self.birthMonth = '12'
        self.birthYear = '1995'
        self.age = '20' 
        self.contactNum = '09501872378'
        self.homeAddress = 'Iligan City'
        self.father_nameFirst = 'Antonio'
        self.father_nameMiddle = 'Intong'
        self.father_nameLast = 'Castillano'
        self.mother_nameFirst = 'Leonora'  
        self.mother_nameMiddle = 'Tubio'
        self.mother_nameLast = 'Millan'
        self.guardian_nameFirst = 'NA'
        self.guardian_nameMiddle = 'NA'
        self.guardian_nameLast = 'NA'
        self.spouse_nameFirst = 'NA'  
        self.spouse_nameMiddle = 'NA'
        self.spouse_nameLast = 'NA'

    def test_add_personal_info(self):
        response = self.atr.add_personal_info(self.stud, self.nameFirst, 
                        self.nameMid, self.nameLast, self.nickname, 
                        self.gender, self.birthdate, self.birthMonth,
                        self.birthYear, self.age, self.contactNum, 
                        self.homeAddress, self.father_nameFirst, 
                        self.father_nameMiddle, self.father_nameLast, 
                        self.mother_nameFirst, self.mother_nameMiddle, 
                        self.mother_nameLast, self.guardian_nameFirst, 
                        self.guardian_nameMiddle, self.guardian_nameLast, 
                        self.spouse_nameFirst, self.spouse_nameMiddle, 
                        self.spouse_nameLast)

        self.assertEqual(response, self.stud)

    def test_add_application(self):
        response = self.atr.add_application(self.stud, self.course, 
                        self.college, self.org_name, self.position, 
                        self.acad_year, self.acad_award, self.scholarship,
                        self.dissertation, self.special_project, self.thesis_title,
                        self.status)
        self.assertEqual(response, 1)