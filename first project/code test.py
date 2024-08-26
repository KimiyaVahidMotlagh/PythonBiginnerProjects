
students_data ={1: {'name': 'MJ', 'last_name': 'A', 'absence_dates': ['1/July','30/Oct'], 'marks': [19, 17, 7, 16]}, 2: {'name': 'A', 'last_name': 'F', 'absence_dates': ['20/Oct'], 'marks': [18, 13, 9, 18]}, 3: {'name': 'K ', 'last_name': 'MJ', 'absence_dates': ['11/Jan', '30/Oct'], 'marks': [18, 7, 19, 15]}}


search_student_id= int(input("Enter student's id you want to make a change to: "))
if not search_student_id in students_data.keys():
    print(str(search_student_id)+(" isn't a student id currently in the list."))
else:
    print("what you want to do: \n 1:delete student \n 2:edit student's info.")
    command = int(input("your choice: "))
    if(command == 1):
        del students_data[search_student_id]
    elif(command == 2):
        pass

    else:
        print("you've choosed a wrong.")    

print(str(students_data))      