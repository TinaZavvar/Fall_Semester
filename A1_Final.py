### Tina
class Admin:
    def __init__(self):
        pass

    def add(self,n1, concept):
        if concept=="course":
            self.n1=n1
            course_name.append(n1)
            n1={"student_names":[], "grades":[]}
            course1.append(n1)
            return course1, course_name
        elif concept=="student":
            self.n1=n1
            name1.append(n1)
            print("Student added to the list")
            return name1

    def check_amount(self,num,concept):

        self.num=num
        concept=="student" 
        if num>=0 and num<=100:
            print("The grade is acceptable!")
        else:
            print("wrong number for the grade!")
            num=int(input(print("Enter the grade:(0-100) ")))
    
    def check_name(self,num,concept):
        self.num=num
        if concept=="course":
            for i in range(len(course1)):
                if num in course1:
                    print("It is already exist!")
            else:
                user.add(num, concept)
                
        if concept=="student":
                if num is False:
                    nn=int(input("The student is not in the list of the institution! Add=1"))
                    if nn==1 :
                        user.add(std,concept)
                        print("Student added to the list")
                    else:
                        print("Error! You can't continue")

    def delete(self,subject,concept):
        self.subject=subject
        if concept=="student":
            if subject in name1:
                i5=name1.index(subject)
                print("{} deleted".format(name1[i5]))
                name1.remove(name1[i5])
            else:
                print("It is not a correct name")
        
        elif concept=="course":
            if subject in course1:
                i5=course1.index(subject)
                print("{} deleted".format(course1[i5]))
                course1.remove(course1[i5])
            else:
                print("It is not a correct course")

    def update(self,name,concept):
        self.name=name
        if concept=="student":
            if name in name1:
                i5=name1.index(name)
                i4=input(print("What is the new name? "))
                name1[i5]=i4
                print("Updated student is: {}".format(name1[i5]))
            else:
                print("It is not a correct name")
                
        elif concept=="course":    
            if name in course_name:
                i5=course_name.index(name)
                new_course1=input(print("What is the new name? "))
                course_name[i5]=new_course1
                print("The new course is {}.".format(course_name[i5]))
            else:
                print("It is not a correct course")



    
    
class Student(Admin):
    concept="student"

def print_out(course_name,course1):
    print("Final result is:")
    for v in course_name:
        print("Course:{}".format(v))
        id_course=course_name.index(v)
        dic_students=course1[id_course]
        print("Enrolled student(s) with respective grade:{}\n".format(dic_students))



i=0
name1=[]
grade1=[]
course1=[]
units1=[]
concept=""
course_name=[]

i1=1
while i is 0:
    user0=int(input("Who is the user? Admin=1, Student=2"))
    #if user0 !=1 and user0 !=2:
    #    print("Incorrect user")
    #    user0=int(input("Who is the user? Admin=1, Student=2"))
    while i1 is 1:
        if user0==1:
            user=Admin()
            con=int(input("To which concept do you want the access? Students=1, Courses=2"))        
            if con==1:
                concept="student"
                cate=int(input("To which category do you want the access?\
    Enrol/Unrol_Students in a Course= 1/2 \
    or submit grade for a studnt= 3 \
    or Adding/Modifying/Deleting Students to Institution list= 4/5/6 "))
                std=str(input("Who?"))
                xx=std in name1

                if cate<4:
                    course=input(" To/From/For which course?")
                    if course in course_name:
                        id_course=course_name.index(course)
                        dic_students=course1[id_course]
                        if cate==1:
                            user.check_name(xx,concept)
                            dic_students["student_names"].append(std)
                            dic_students["grades"].append("N/A")
                        elif cate==2:
                            if std in dic_students["student_names"]:
                                indx=dic_students["student_names"].index(std)
                                dic_students["student_names"].remove(std)
                                grd=dic_students["grades"][indx]
                                dic_students["grades"].remove(grd)
                            else:
                                print("The student is not in the list of this course!")
                        else:
                            grd=int(input("Enter the grade:(0-100) "))
                            user.check_amount(grd,concept)
                            indx=dic_students["student_names"].index(std)
                            dic_students["grades"][indx]= grd
                    else:
                        print("This course does not exist!")
                elif cate==4:
                    user.add(std,concept)
                elif cate==5:
                    user.check_name(xx,concept)
                    user.update(std,concept)
                elif cate==6:
                    user.check_name(xx,concept)
                    user.delete(std,concept)
                else:
                    print("This category doesn't exist.")
                    
            else:
                concept="course"
                cate=int(input("To which category do you want the access?\
    Adding/Modifying/Deleting courses=1/2/3 "))
                if cate==1:
                    crs=str(input("Enter the course name:  "))
                    user.check_name(crs,concept)
                elif cate==2:
                     name=input("Enter the course name: ")
                     user.update(name,concept)
                elif cate==3:
                     name=input("Enter the course name: ")
                     user.delete(name,concept)
                
        
        elif user0==2:
            user=Student()
            print("As a student you can just enroll/unroll to/from a course!")
            nm=str(input("What is your name?"))
#             xx=nm in name1
#             user.check_name(xx,concept)
            
            ctgry=int(input("What do you want to do? Enroll/unroll to a course= 1/2"))
            crs=str(input("Choose your course?"))
            if crs in course_name:
                id_course=course_name.index(crs)
                dic_students=course1[id_course]
            else:
                print("Your chosen course doesn't exist! Start again.")
                break
                
            if ctgry==1:
                dic_students["student_names"].append(nm)
                dic_students["grades"].append("N/A")
            elif ctgry==2:
                if nm in dic_students["student_names"]:
                    indx=dic_students["student_names"].index(nm)
                    dic_students["student_names"].remove(nm)
                    grd=dic_students["grades"][indx]
                    dic_students["grades"].remove(grd)
                else:
                    print("The student is not in the list of this course!")            
            else:
                print("Your entered number is wrong! Start again.")
        i1=int(input("Do you want to continue? yes=1, no=2"))
    i=int(input("Do you want to change the user type? yes=0, no=1"))
    if i==0:
        i1=1

            
                    
print_out(course_name,course1)




