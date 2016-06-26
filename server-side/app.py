from flask import Flask, request, jsonify
app = Flask(__name__)

from views.atr import Student
atr_student = Student()

@app.route("/")
def index():
    return "Hello World"

@app.route("/register", methods=['POST', 'GET'])
def register():
    post = request.get_json()
    stud = post.get('stud')
    course = post.get('course')
    college = post.get('college')
    org_name =post.get('org_name')
    position = post.get('position')
    acad_year = post.get('acad_year')
    acad_award = post.get('acad_award')
    scholarship = post.get('scholarship')
    dissertation = post.get('dissertation')
    special_project = post.get('special_project')
    thesis_title = post.get('thesis_title')
    status = post.get('status')
    nameFirst = post.get('nameFirst')
    nameMid = post.get('nameMid')
    nameLast = post.get('nameLast')
    nickname = post.get('nickname')
    gender = post.get('gender')
    birthdate = post.get('birthdate')
    birthMonth = post.get('birthMonth')
    birthYear = post.get('birthYear')
    age = post.get('age')
    contactNum = post.get('contactNum')
    homeAddress = post.get('homeAddress')
    father_nameFirst = post.get('father_nameFirst')
    father_nameMiddle = post.get('father_nameMiddle')
    father_nameLast = post.get('father_nameLast')
    mother_nameFirst = post.get('mother_nameFirst')
    mother_nameMiddle = post.get('mother_nameMiddle')
    mother_nameLast = post.get('mother_nameLast')
    guardian_nameFirst = post.get('guardian_nameFirst')
    guardian_nameMiddle = post.get('guardian_nameMiddle')
    guardian_nameLast = post.get('guardian_nameLast')
    spouse_nameFirst = post.get('spouse_nameFirst')
    spouse_nameMiddle = post.get('spouse_nameMiddle')
    spouse_nameLast = post.get('spouse_nameLast')

    response_personal = atr_student.add_personal_info(stud, nameFirst, nameMid, nameLast,
                        nickname, gender, birthdate, birthMonth,
                        birthYear, age, contactNum, homeAddress,
                        father_nameFirst, father_nameMiddle,
                        father_nameLast, mother_nameFirst,
                        mother_nameMiddle, mother_nameLast,
                        guardian_nameFirst, guardian_nameMiddle,
                        guardian_nameLast, spouse_nameFirst,
                        spouse_nameMiddle, spouse_nameLast )

    response_application = atr_student.add_application(stud, course, college, org_name,
                        position, acad_year, acad_award, scholarship,
                        dissertation, special_project, thesis_title,
                        status)

    return jsonify({'response_personal': response_personal, 'response_application': response_application})

    #return jsonify({'post' : post, 'stud': stud})


if __name__ == "__main__":
    app.run()