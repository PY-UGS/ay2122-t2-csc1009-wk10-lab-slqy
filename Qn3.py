# Week 01 Question 2b
module = "CSC1009"

switcher = {
    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "Object-Oriented Programming",
    "CSC1010": "Computer Networks"
}

# display the correct module name
print(switcher.get(module), "\n")


# Week 01 Question 2c
for x in range(102, 65, -1):
    if x % 2 == 1:
        # print the odd number in descending order starting from 102 and ending with 66
        print("Value of x:", x)
