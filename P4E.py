import os
import platform
student_records = []
def Student_System():
    student_record = {}
    print("""
            |==================================================================|
            |==================================================================|
            |==================================================================|
            |======== Welcome To Lenguini Management System Of FCI MU =========|
            |==================================================================|
            |==================================================================|
            |==================================================================|

            ==================
            = System Options =
            ==================
            ===========================
            = 1- Add new student -> 1 =
            ===========================
            = 2- Search Student  -> 2 =
            ===========================
            = 3- All Students    -> 3 =
            ===========================
            = 4- Remove Student  -> 4 =
            ===========================
            """)

    # Validation for Input
    try:
        user = int(input("Enter Num of Option: ")) #Input User
    except ValueError:
        exit("It's not Num please prompt valid num")#Error Msg
    # Add New User To System
    if user == 1:
        student_name = str(input("Student Name: "))
        student_id = int(input("Student ID: "))
        for std_id in student_records:
            std_ID = std_id.get('id')
            if student_id == std_ID:
                print('This User Is Already Existed\n')
                runAgain()
        student_age = int(input("Student Age: "))
        student_level = int(input("Student Level: "))
        student_subjects = input("Subjects: ").split()
        student_degree_of_subject = []
        for x in student_subjects: # Iteration over subjects to add score to it's subject
            degree_of_subject = int(input(f"Enter {x}'s degree: "))
            student_degree_of_subject.append(degree_of_subject) # Add new score to student_degree_of_subject
        # Made a Dictionary with Input data as mentioned above
        student_record.update({'name': student_name, 'age': student_age , 'level': student_level,
                               'subjects': student_subjects, 'degrees': student_degree_of_subject,
                               'id': student_id})
        # Add the dictionary with data as record in List
        student_records.append(student_record)
    # Search for a student in Lenguini management system
    elif user == 2:
        search = int(input("Enter Student's ID: ")) # Search with unique ID
        for student in student_records: # Iteration over Parent container - student_records -
            ID = student.get('id') # Get Student's ID to make matching
            if search == ID:
                print(f"""                             
                                              |*************|
                                ===============*   Name    *========================
                                *              *************                       *
                                ==>> {student.get('name')}                         =
                                *              **************                      *
                                ===============*    Age    *========================
                                *              *************                       *
                                ==>> {student.get('age')}                          =
                                *              *************                       * 
                                ===============*   Level   *========================
                                *              *************                       *
                                ==>> {student.get('level')}                        =
                                *              *************                       *
                                ===============* Subjects  *========================
                                *              *************                       *
                                ==>> {student.get('subjects')}                     =
                                *              *************                       * 
                                ===============*  Degrees  *========================
                                *              *************                       *
                                ==>> {student.get('degrees')}                      =
                                *              *************                       *
                                ===============*    ID     *========================
                                *              *************                       *
                                ==>> {student.get('id')}                           =
                                ====================================================
                                """)
                break
            else:
                print('Not Found please Add him/her')
    # Show All DataBase
    elif user == 3:
        for record in student_records:  # Iteration over Parent container - student_records -
            print(f"""                        
                                              |*************|
                                ===============*   Name    *========================
                                *              *************                       *
                                ==>> {record.get('name')}                          =
                                *              **************                      *
                                ===============*    Age    *========================
                                *              *************                       *
                                ==>> {record.get('age')}                           =
                                *              *************                       * 
                                ===============*   Level   *========================
                                *              *************                       *
                                ==>> {record.get('level')}                         =
                                *              *************                       *
                                ===============* Subjects  *========================
                                *              *************                       *
                                ==>> {record.get('subjects')}                      =
                                *              *************                       * 
                                ===============*  Degrees  *========================
                                *              *************                       *
                                ==>> {record.get('degrees')}                       =
                                *              *************                       *
                                ===============*    ID     *========================
                                *              *************                       *
                                ==>> {record.get('id')}                            =
                                ====================================================
            """)
    elif user == 4:
        dele = int(input('Enter Student\'s ID: '))
        for del_st in student_records: # Iteration over Parent container - student_records -
            id = del_st.get('id')  # Get Student's ID to make matching
            if dele == id:
                student_records.remove(del_st)
                break


Student_System()
def runAgain():
    # To clear window
    runagn = input("\nwant To Run Again Y/n: ")
    if runagn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Student_System()
        runAgain()


runAgain()












