import csv
import numpy as np
# Question 1.Read exam_score and perform basic statistical operation using numpy
math = []
with open("Exam_Score_Prediction.csv","r") as file:
    reader = csv.DictReader(file)
    for i in reader:
#      print(i["exam_score"])
      math.append(float(i["exam_score"]))

arr = np.array(math)
# Mean
print(np.mean(arr))

# Median
print(np.median(arr))

# Cumsum
print(np.cumsum(arr))

# Cumprod
print(np.cumprod(arr))

# minimum
print(np.min(arr))

# maximum
print(np.max(arr))

# standard
print(np.std(arr))

# var
print(np.var(arr))


# Question 2.Read class_attendance from csv file and check which student is allowed or not alowed based on 70%
class_attendance = []
with open("Exam_Score_Prediction.csv","r") as f:
   reader = csv.DictReader(f)
   for i in reader:
      class_attendance.append(float(i["class_attendance"]))

arr = np.array(class_attendance)
x =(np.where(arr >= 70,"Allowed","Not allowed"))
print("list of allowed and not_allowed students:",x)
count = 0
for i in x:
   if i == "Not allowed":
      count += 1
print("not allowed:",count)      



# Question 3.Read SLeep_hours from csv file and check which student sleep between 6 to 8 hours
Sleep_hours = []
with open("Exam_Score_Prediction.csv","r") as f:
   reader = csv.DictReader(f)
   for i in reader:
      Sleep_hours.append((i["sleep_hours"]))
arr = np.array(Sleep_hours,dtype=float)
count = 0
len = 0
for x in arr:
  if x >= 6 and x <= 8:
     count += 1
print("sleep hours:",count) 

for y in arr:
   len += 1       
print("students who slept between 6 to 8 hours:",len)     



# Question 4.Read gender from csv file and print the count of male,female,others
Gender = []
with open("Exam_Score_Prediction.csv","r") as f:
   reader = csv.DictReader(f)
   for i in reader:
      Gender.append((i["gender"]))
Male = 0
Female = 0
Other = 0      
for i in Gender:
   if i == "male":
      Male += 1
   elif i == "female":
      Female += 1
   else:
      Other += 1   
print("male_count:",Male)
print("female_count:",Female)
print("other_count:",Other)          
