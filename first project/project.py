from os import name, system
import pickle
import re

# { student_id : { name: str, last_name: str, absense_dates: [str(#day/month(str))], marks:[float]} }
students_data = {}
student_id_int = 0

def loopbreaker():
      #checking for the countinuing the program
    temp_check = input("want to continue using the program? y/n \n")
    if temp_check == 'n':
         temp_check = input("Are you sure? y/n \n")
         if temp_check != 'y':
            return True
         else:
            return False 
    else:
        return True     

def screen_clear():
      # clear screen 
    system("pause")
    system("cls")
    return loopbreaker()
          
def show_menu():
      #program menu
    print("***********Menu***********\n")
    print("1.Add students' information \n")
    print("2.Show a student's GPA \n")
    print("3.Get student's last name \n'")
    print("4.Show a student's absence \n")
    print("5.Exit")
    command = int(input("Enter your choice: "))

    return command

def load_student_data():
    #loads student data from a pickle file
    global students_data, student_id_int
    temp_check= input("do you want to load past student information? y/n  ")
    if temp_check == 'y':
        with open('filename.pkl', 'rb') as handle:
            students_data = pickle.load(handle)

        student_id_int = students_data.keys()(len(students_data.key())-1)

        print("saved students' data loaded.")    

def save_student_data(final_student_data, final_student_number): 
    
    with open('studentnumber.pkl', 'wb') as handle:
        pickle.dump(final_student_number, handle)

def get_student_data(student_id_int):

    loop =True
    while loop:

        st_name = input("student name: ")
        st_last_name = input("last name: ")
        absence_dates = input("enter absence dates:")
        absence_dates = absence_dates.translate({ord(c): " " for c in "!@#$%^&*()[];:,-<>?|`~-=_+"}).split()
        mark_list = input("enter student's exam marks as fallow: (Mark, Mark, ...) \n marks: ")
        mark_list = mark_list.translate({ord(c): " " for c in "!@#$%^&*()[];:,-/<>?\|`~-=_+"}).split()
        marks = list(map(float,mark_list))
        students_data[student_id_int]={'name':st_name, 'last_name':st_last_name, 'absence_dates':absence_dates, 'marks':marks}
        print(str(student_id_int)+ ": "+ students_data[student_id_int]['name']+ " "+ students_data[student_id_int]['last_name']+ " has been saved.")
        student_id_int += 1
        save_student_data(students_data, student_id_int)

        loop = screen_clear()

def edit_student_data():
    pass        

def get_student_GPA():

    loop =True
    while loop:
        search_st_id= int(input("Please enter student's id on the list: "))

        if not search_st_id in students_data.keys():
            print(str(search_st_id)+ " isn't a student id currently in the lint :) ")
        else:    
            print(students_data[search_st_id]['last_name']+ "'s Gpa: "+ str(sum(students_data[search_st_id]["marks"])/len(students_data[search_st_id]["marks"])))
            
        loop = screen_clear()

def get_student_last_name():

    loop =True
    while loop:
        print("1:by student ID")
        print("2:by lowset GPA \n")
        menu_check= int(input("Choose: "))

        if menu_check==1:
            search_st_id= int(input("Please enter student's number on the list: "))
            if not search_st_id in students_data.keys():
                print(str(search_st_id)+ " isn't a student id currently in the lint :) ")
            else:    
                print(students_data[search_st_id]['last_name']+" is the last name. \n")
            
            loop = screen_clear() 

        elif menu_check==2:  
            search_Gpa= float(input("Enter the lowst GPA you are searching for: "))
            for id in students_data.keys():
                if search_Gpa < (sum(students_data[id]["marks"])/len(students_data[id]["marks"])):
                    print( students_data[id]["last_name"]+ " with Gpa:  ", end = "" )
                    print( sum(students_data[id]["marks"]) / len(students_data[id]["marks"]) ) 
       
            loop = screen_clear()
            
        else:
            print("you chooseed a wrong key :)")  
        
        loop = screen_clear() 

def get_student_absence_list():

    loop =True
    while loop:
        search_st_id= int(input("Enter student number you want the absence dates for: "))
        if not (search_st_id in students_data.keys()):
            print(str(search_st_id)+ " isn't a student id currently in the lint :) ")
        else: 
            for x in students_data[search_st_id]["absence_dates"]:
                print(x)     

        loop = screen_clear()


while True:
    student_id = 0
    loop = True
    load_student_data()
    command = show_menu()
    
    if(command == 1):
        get_student_data(student_id)
           
    elif(command == 2):
        get_student_GPA()

    elif(command == 3):
        get_student_last_name()

    elif(command == 4):
        get_student_absence_list()

    elif(command == 5):
        print("Thanks for using the app. \n")
        break
    else:
        print("you chooseed a wrong key, please try again.")
    
    loop = screen_clear()            

