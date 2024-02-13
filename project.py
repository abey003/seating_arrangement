import os
import csv

j = 0
k = 0
data=[]

def seating_result(seating_data,students_per_class):
    count = 0
    with open('Seating.csv', 'w') as file:
        writer = csv.writer(file)
        print("\n")
        print("First Class")
        print("\n")
        for i in range(0,len(seating_data),2):
            print(seating_data[i],seating_data[i+1])
            writer.writerow([seating_data[i],seating_data[i+1]])
            print("\n")
            count = count + 2
            if count == students_per_class:
                total_student = "Total Seats:"+str(count)
                print("Total Seats :", count)
                print("\n")
                print("Next Class")
                print("\n")
                writer.writerow([total_student,"---"])
                writer.writerow(["Next Class","---"])
                count = 0
        total_student = "Total Seats:"+str(count)
        print("Total Seats :", count)
        writer.writerow([total_student,"---"])

def seat_sorting_1_subject(all_data,students_per_class):
    for i in range(len(all_data)):
        element = all_data[i]
        for j in range(0,len(element),1):
            extracted_data = element[i]
            data.append(extracted_data[0])
    count = 0
    with open('Seating.csv', 'w') as file:
        writer = csv.writer(file)
        print("\n")
        print("First Class")
        print("\n")
        for i in range(0,len(data),2):
            print(data[i],"---")
            writer.writerow([data[i],"---"])
            print("\n")
            count = count + 1
            if count == students_per_class:
                total_student = "Total Seats:"+str(count)
                print("Total Seats :", count)
                print("\n")
                print("Next Class")
                print("\n")
                writer.writerow([total_student,"---"])
                writer.writerow(["Next Class","---"])
                count = 0
        total_student = "Total Seats:"+str(count)
        print("Total Seats :", count)
        writer.writerow([total_student,"---"])

def seat_sorting_2_subjects(all_data):
    j = 0
    a = 0 
    element_1 = all_data[0]
    element_2 = all_data[1]
    for i in range(0,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        j = j+1 
        a = a+1
    a = 0
    element_1 = all_data[1]
    for i in range(j,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = "---"
        data.append(extracted_data_1[0])
        data.append(extracted_data_2)
    return data

def seat_sorting_3_subjects(all_data):
    j = 0
    data = []
    a = 0 
    element_1 = all_data[0]
    element_2 = all_data[1]
    for i in range(0,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        j = j+1
        a = a+1
    a = 0
    element_1 = all_data[1]
    element_2 = all_data[2]
    for i in range(j,len(element_1),1):
        extracted_data_1 = element_1[i]
        while(a<len(element_2)):
            extracted_data_2 = element_2[a]
            data.append(extracted_data_1[0])
            data.append(extracted_data_2[0])
            a = a+1
        extracted_data_2 = "---"
        data.append(extracted_data_1[0])
        data.append(extracted_data_2)
    return data

def seat_sorting_4_subjects(all_data):
    j = 0
    k = 0
    data = []
    a = 0 
    element_1 = all_data[0]
    element_2 = all_data[1]
    for i in range(0,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        j = j+1 
        a = a+1
    a = 0
    element_1 = all_data[1]
    element_2 = all_data[2]
    for i in range(j,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        k = k+1 
        a = a+1
    a = 0
    element_1 = all_data[2]
    element_2 = all_data[3]
    for i in range(k,len(element_1),1):
        extracted_data_1 = element_1[i]
        while(a<len(element_2)):
            extracted_data_2 = element_2[a]
            data.append(extracted_data_1[0])
            data.append(extracted_data_2[0])
            a = a+1
        extracted_data_2 = "---"
        data.append(extracted_data_1[0])
        data.append(extracted_data_2)
    return data

def seat_sorting_5_subjects(all_data):
    j = 0
    k = 0
    data = []
    a = 0
    element_1 = all_data[0]
    element_2 = all_data[1]
    for i in range(0,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        j = j+1 
        a = a+1
    a = 0
    element_1 = all_data[1]
    element_2 = all_data[2]

    for i in range(j,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        k = k+1  
        a = a+1
    j = 0
    a = 0
    element_1 = all_data[2]
    element_2 = all_data[3]

    for i in range(k,len(element_1),1):
        extracted_data_1 = element_1[i]
        extracted_data_2 = element_2[a]
        data.append(extracted_data_1[0])
        data.append(extracted_data_2[0])
        j = j+1 
        a = a+1
    a = 0
    element_1 = all_data[3]
    element_2 = all_data[4]

    for i in range(j,len(element_1),1):
        extracted_data_1 = element_1[i]
        while(a<len(element_2)):
            extracted_data_2 = element_2[a]
            data.append(extracted_data_1[0])
            data.append(extracted_data_2[0])
            a = a+1
        extracted_data_2 = "---"
        data.append(extracted_data_1[0])
        data.append(extracted_data_2)
    return data

def read_csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def main():
    seating_data = []
    students_per_class = int(input("Enter the number of students per class:"))
    folder_path = 'Data'
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    all_data = []
    for file_name in csv_files:
        file_path = os.path.join(folder_path, file_name)
        file_data = read_csv_to_list(file_path)
        all_data.append(file_data)
    print(all_data)
    length = len(all_data)
    if length == 1:
        seat_sorting_1_subject(all_data,students_per_class)
        exit(0)
    elif length == 2:
        seating_data = seat_sorting_2_subjects(all_data)
    elif length == 3:
        seating_data = seat_sorting_3_subjects(all_data)
    elif length == 4:
        seating_data = seat_sorting_4_subjects(all_data)
    elif length == 5:
        seating_data = seat_sorting_5_subjects(all_data)
    else:
        pass
    seating_result(seating_data,students_per_class)

if __name__ == "__main__":
    main()
