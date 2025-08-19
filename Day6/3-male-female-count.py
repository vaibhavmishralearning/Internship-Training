print("\n_Male and Female Count____________")

data = ["MALE","FEMALE","MALE","FEMALE","MALE","MALE","FEMALE","MALE","MALE","FEMALE","MALE","MALE","MALE","MALE","FEMALE","FEMALE"]
print()

male_count = 0
female_count = 0

for item in data:
    if item == "MALE":
        male_count = male_count + 1
    elif item == "FEMALE":
        female_count = female_count + 1

print("Number Of Males : ",male_count)
print("Number Of Females : ",female_count)