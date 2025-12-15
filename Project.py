import csv
import numpy as np
# Question 1.Read exam_score and perform basic statistical operation using numpy
math = []
with open("Exam_Score_Prediction.csv","r") as file:
    reader = csv.DictReader(file)
    for i in reader:
      print(i["exam_score"])
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
with open("Exam_Score_Prediction.csv","r") as file:
   reader = csv.DictReader(file)
   for value in reader:
      class_attendance.append(float(value["class_attendance"]))

attendance = np.array(class_attendance)
floor = np.floor(attendance)

status = np.where(floor >= 70, "Allowed","Not Allowed")
not_allowed = floor[status == "Not Allowed"]
print("Not Allowed",not_allowed)

# Question 3.Read SLeep_hours from csv file and check which student sleep between 6 to 8 hours
sleep = []
with open("Exam_Score_Prediction.csv","r") as f:
   reader = csv.DictReader(f)
   for x in reader:
      sleep.append(float(x["sleep_hours"]))

hours = np.array(sleep)      
floor = np.floor(hours)

y = np.where((floor >= 6) & (floor <= 8))
count = len(y[0])

print("student sleeps between 6 to 8 hours:",count)

# Question 4.Read gender from csv file and print the count of male,female,others
gender = []
with open("Exam_Score_Prediction.csv","r") as f:
   reader = csv.DictReader(f)
   for y in reader:
      gender.append(y["gender"])

Gender = np.array(gender)

male_count = len(np.where(Gender == "male")[0])
female_count = len(np.where(Gender == "female")[0])
other_count = len(np.where(Gender == "other")[0])

print("Male:",male_count)
print("Female:",female_count)
print("Other:",other_count)