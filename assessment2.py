def calculate_classes(students):
    #max class size of 30 and min classes of 2
    max_class_size = 30
    min_classes = 2

    #classes needed
    classes = max(min_classes, (students + max_class_size - 1) // max_class_size)

    #average size of class
    average = students // classes

    #remainder of students that need to be distributed (modulo)
    remainder = students % classes

    allocation = {}

    #loop for classes to assign students
    for i in range(classes):
        #assign the average size to each class
        allocation[f"Class {i + 1}"] = average

        #add remaining students to classes
        if remainder > 0:
            allocation[f"Class {i + 1}"] += 1
            remainder -= 1

    print(f"Proposed Allocation: {classes} classes")
    print(allocation)


#example inputs
calculate_classes(31)
calculate_classes(59)
calculate_classes(87)