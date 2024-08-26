
import pickle
students_data={}
studentnumber=0

with open('filename.pkl', 'wb') as handler:
    pickle.dump(students_data, handler)
