#Author: Paul Jabani Lassa
#Created: 5th November 2019
#Revised: 20th November 2019
#Description:

from pet import Pet
from WildAnimal import WildAnimal
from Treatment import Treatment
import csv

#class arrays stored in lists
list_pet = []
list_wildAnimal = []
list_treatment = []

#lists used to store array
abandon_list = []
abuse_list = []

#putting csv files into variables to make them easy to call
pet_file = "DADSA 2019-20 CWK A DATA PETS(1).csv"
wildAnimal_file = "DADSA 2019-20 CWK A WILD ANIMALS.csv"
treatment_file = "DADSA 2019-20 CWK A TREATMENT.csv"

#Function: load_petData
#description: loads pet data from the csv file to populate the class pet
#Parameters: nil
#Warning: nil
def load_petData():
    with open(pet_file, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        #skip first row because of labels
        first = True
        for row in reader:
            if first:
                first = False
            else:
                list_pet.append(Pet(row[0], row[1], row[2], row[3], row[4], row[5],
                                    row[6], row[7], row[8],row[9], row[10]))

#Function: load_Wildanimal
#Description: loads wild animal data from the csv file to populate the class WildAnimal
#Parameters: nil
#Warning: nil
def load_Wildanimal():
    with open(wildAnimal_file, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        # skip first row because of labels
        first = True
        for row in reader:
            if first:
                first = False
            else:
                list_wildAnimal.append(WildAnimal(row[0], row[1], row[2], row[3],
                                           row[4], row[5], row[6], row[7]))

#Function: load_treatment
#Description:cloads Treatment data from the csv file to populate the class Treatment
#Parameters: nil
#warning: nil
def load_treatment():
    with open(treatment_file, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        #skip first row because of labels
        first = True
        for row in reader:
            if first:
                first = False
            else:
                list_treatment.append(Treatment(row[0], row[1], row[2], row[3], row[4], row[5],
                                    row[6], row[7]))

def restart_method(method):
    restart = input('1. would you like to add another animal? \n2. Go back to main')
    if restart == 1:
        method
    else:
        menue()

#Function: write_new_pet
#Description: this function writes a new pet to the last row in the pet csv file
#Parameters: nil
#warning: nil
def write_new_pet():
    #request for inputs for the info to be added to certain colums in the csv
    print('Please fill in details accordingly')
    sanctuary_id = input('Enter Sanctuary ID: ')
    animal_type = input('Enter Animal Type: ')
    breed = input('Enter Animal Breed: ')
    vaccinated = input('Enter vaccination status: ')
    neutered = input('Enter Neutered status: ')
    microchip_num = input('Enter Microchip Number: ')
    admission_reason = input('What is the reason for admission: ')
    arrival_date = input('Enter arival date: ')
    departure_date = input('Enter Departure date: ')
    destination = input('Enter Destination: ')
    destination_address = input('Enter Destination Address: ')
    #adds all inputs to the variable row
    row = [sanctuary_id, animal_type, breed, vaccinated, neutered, microchip_num,
           admission_reason,arrival_date,departure_date, destination, destination_address]
    #writes to the csv
    with open(pet_file, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row)
    csvfile.close()
    print('Pet has been added!')
    #request to loop back and add another pet
    restart = input('would you like to add another pet? y/n')
    if restart=='y':
        write_new_pet()
    elif restart =='n':
        menue()
    else:
        exit()

#Function: Write_new_wildAnimal
#Description:writes to the Wild Animal csv file
#parameters: nil
#warning: nil
def write_new_wildAnimal():
    print('Please fill in details accordingly')
    sanctuary_id = input('Enter Sanctuary ID: ')
    animal_type = input('Enter Animal Type: ')
    vaccinated = input('Enter vaccination status: ')
    admission_reason = input('What is the reason for admission: ')
    arrival_date = input('Enter arival date: ')
    departure_date = input('Enter Departure date: ')
    destination = input('Enter Destination: ')
    destination_address = input('Enter Destination Address: ')

    row = [sanctuary_id, animal_type, vaccinated, admission_reason,
           arrival_date, departure_date, destination, destination_address]
    with open(wildAnimal_file, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row)
        csvfile.close()
        print('Wild animal has been added!')
        restart = input('would you like to add another Wild animal? y/n')
        if restart == 'y':
            write_new_wildAnimal()
        else:
            exit()
    restart = input('would you like to add another wild animal? y/n')
    if restart == 'y':
        write_new_wildAnimal()
    elif restart == 'n':
        menue()
    else:
        exit()

#Function:write_new_treatment
#Description: this function, when called, addes a new treatment to the treatment csv file
#parameters: nil
#warning: nil
def write_new_treatment():
    print('Please fill in details accordingly')
    sanctuary_id = input('Enter Sanctuary ID: ')
    surgery = input('Enter surgery type: ')
    surgery_date = input('Enter surgery date: ')
    medication = input('Enter medication: ')
    medication_start = input('Enter medication start date: ')
    medication_finish = input('Enter medication end date: ')
    responsible_for_abuse = input('Name of individual that abused the animal: ')
    responsible_for_abandoning = input('name of individual that abandoned the animal: ')

    row = [sanctuary_id, surgery, surgery_date, medication, medication_start,
           medication_finish, responsible_for_abuse, responsible_for_abandoning]

    with open(treatment_file, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row)
        csvfile.close()
        print('Treatment has been added!')
        restart = input('Would you like to add another Treatment? y/n')
        if restart == 'y':
            write_new_treatment()
        else:
            exit()
    restart = input('would you like to add another treatment? y/n')
    if restart == 'y':
        write_new_treatment()
    elif restart == 'n':
        menue()
    else:
        exit()


#Function: ready_for_adoption
#Description: gets and print all animals ready for adoption
#parameters: pet_type
#warning: nil
def ready_for_adoption(pet_type):
    adoptionStatus = []
    print("this is the lisf of " + pet_type + " ready to be adopted")
    for i in list_pet:
        if i.animal_type == pet_type:
            if i.vaccinated != "":
                if i.neutered != "":
                    if i.microchip_num != "":
                        adoptionStatus.append(i.sanctuary_id)
    print(adoptionStatus)
    w = input('would you like to make another search? y/n\n')
    if w == 'y':
        menue()
    else:
        quit()

#Function:Sort_alphabetical
#Description: sort list in alphabetical order using bubble sort
#Parameters: array
#nwarning: nil
def sort_alphabetical(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            # loop through the array from beginning to last element
            # swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j+1], array[j]

#Function:BinarySearch
#Description: this is the implementaition of the binary sory algorithm
#Parameters: lys and val
#warning: nil
def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1

    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid].sanctuary_id == val:
            index = mid
            return lys[index]
        else:
            if val < lys[mid].sanctuary_id :
                last = mid - 1
            else:
                first = mid + 1

    if index == -1:
        return index

#Function:return_pet_id_binary
#Description: this is the implementaition of the binary sory algorithm to the pet data
#Parameters: return_pet
#warning: nil
def return_pet_id_binary(return_pet):
    return BinarySearch(list_pet, return_pet)

#Function:return_wild_id_binary
#Description: this is the implementaition of the binary sory algorithm to the wild animal data
#Parameters: return_wild
#warning: nil
def return_wild_id_binary(return_wild):
    return BinarySearch(list_wildAnimal, return_wild)

#Function:return_trestment_id_binary
#Description: this is the implementaition of the binary sory algorithm to the treatment data
#Parameters: return_treatment
#warning: nil
def return_treatment_id_binary(return_treatment):
    return BinarySearch(list_treatment, return_treatment )


def merge_sort(array):
    n= len(array)
    if n <= 1:
        return array
        midpoint=int(len(array)/2)
        left, right= merge_sort(array[:midpoint], merge_sort(array[midpoint:]))
        return merge(left, right)

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer +=1
        else:

            result.append(right[right_pointer])
            right_pointer +=1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer])

    return result

#Function:ready_to_return
#Description: this function, when called, print list of animals ready to be returned to owner
#Parameters: nil
#warning: nil
def ready_to_return():
    pet_status = []
    wildAnimal_status = []
    return_list=[]
    print('\nAnimals ready to be returened to owner (in accending order): ')
    for i in list_pet:
        if  i.destination == "":
            return_list.append(i.sanctuary_id)

    print('\nlist of wild animals ready to be returned: ')
    for i in list_wildAnimal:
        if  i.destination == "":
            return_list.append(i.sanctuary_id)

    sort_alphabetical(return_list)
   # merge_sort(return_list)
    print(return_list)

#Function: find_with_id
#Description: this function, when called, finds animal in the sanctuary using the id
#Parameters: animal_id
#warning: nil
def find_with_id(animal_id):
    isPetID = False
    isWildID = False
    #isTreatID = False

    for i in list_pet:
        if i.sanctuary_id == animal_id:
            isPetID = True
            print('this is the pet you searched: ')
            print(i)

    if isPetID == False:
        for i in list_wildAnimal:
            if i.sanctuary_id == animal_id:
                isWildID = True
                print('This is the wild animal you searched: ')
                print(i)

    if isWildID==False:
        print('ID not found')

    for i in list_treatment:
        if i.sanctuary_id == animal_id:
            #isTreatID = True
            print('This is the treatment for the id you searched: ')
            print(i)

    w = input('would you like to make another search? y/n\n')
    if w == 'y':
        menue()
    else:
        quit()


#Function:find_abandoned
#Description: produces the list of abandoned animals
#parameters:nil
#warning: nil
def find_abandoned():
    print('this is the list of people who have abandoned their animals: ')
    for i in list_treatment:
        if i.responsible_for_abandoning != "" and i.responsible_for_abandoning not in abandon_list:
            abandon_list.append(i.responsible_for_abandoning)
    sort_alphabetical(abandon_list)
    #merge_sort(abandon_list)
    print(abandon_list)
    w = input('would you like to make another search? y/n\n')
    if w == 'y':
        menue()
    else:
        quit()

#Function find_abused
#Description:produces the list of abandoned animals
#parameters:nil
#warning: nil
def find_abused():
    print('This is the list of people who have abusef their animals: ')
    for i in list_treatment:
        if i.responsible_for_abuse != "" and i.responsible_for_abuse not in abuse_list:
            abuse_list.append(i.responsible_for_abuse)
    sort_alphabetical(abuse_list)
    #merge_sort(abuse_list)
    print(abuse_list)
    w = input('would you like to make another search? y/n\n')
    if w == 'y':
        menue()
    else:
        quit()

#Function: return_pet_id
#Description: validates and returns the id of the pet inputed
#parameters:return_pet
#warning: nil
def return_pet_id(return_pet):
    foundID = False
    for i in list_pet:
        if i.sanctuary_id == return_pet:
            foundID == True
            return i
        else:
            foundID == False

    if foundID == False:
        print('ID was not found, please enter another ID: ')
        edit_menu_pet()


#Function: return_Wild_id
#Description: validates and returns the id of the wild animal inputed
#parameters:return_wild
#warning: nil
def return_Wild_id(return_wild):
    foundID = False
    for i in list_wildAnimal:
        if i.sanctuary_id == return_wild:
            foundID ==True
            return i
        else:
            foundID ==False
    if foundID==False:
        print('ID not found please input another ID: ')
        edit_menu_wild()

#Function: return_treatment_id
#Description: validates and returns the id of the wild treatment inputed
#parameters:nil
#warning: nil
def return_treatment_id(return_treat):
    foundID=False
    for i in list_treatment:
        if i.sanctuary_id == return_treat:
            foundID ==True
            return i
        else:
            foundID == False

    if foundID==False:
        print('ID not found, please input another ID: ')
        edit_menu_treat()

#Function: edit_pet
#Description: locates the row/colums and edits details into Pet csv
#parameters: pet_id_to_edit
#warning: nil
def edit_pet(pet_id_to_edit):
    c = csv.reader(open(pet_file))
    lines = list(c)

    for row in lines:
        if row[0] == pet_id_to_edit.sanctuary_id:
            row[1] = pet_id_to_edit.animal_type
            row[2] = pet_id_to_edit.breed
            row[3] = pet_id_to_edit.vaccinated
            row[4] = pet_id_to_edit.neutered
            row[5] = pet_id_to_edit.microchip_num
            row[6] = pet_id_to_edit.admission_reason
            row[7] = pet_id_to_edit.arrival_date
            row[8] = pet_id_to_edit.departure_date
            row[9] = pet_id_to_edit.destination
            row[10] = pet_id_to_edit.destination_address

    writer = csv.writer(open(pet_file, 'w', newline=""))
    writer.writerows(lines)
    print(pet_id_to_edit)

#Function:edit_wild
#Description: locates the row/colums and edits details into wild animal csv
#parameters: wild_id_to_edit
#warning: nil
def edit_wild(wild_id_to_edit):
    c = csv.reader(open(wildAnimal_file))
    lines = list(c)

    for row in lines:
        if row[0] == wild_id_to_edit.sanctuary_id:
            row[1] = wild_id_to_edit.animal_type
            row[2] = wild_id_to_edit.vaccinated
            row[3] = wild_id_to_edit.admission_reason
            row[4] = wild_id_to_edit.arrival_date
            row[5] = wild_id_to_edit.departure_date
            row[6] = wild_id_to_edit.destination
            row[7] = wild_id_to_edit.destination_address

    writer = csv.writer(open(wildAnimal_file, 'w', newline=""))
    writer.writerows(lines)
    print(wild_id_to_edit)

#Function:
#Description: locates the row/colums and edits details into treatment csv
#parameters:treat_id_to_edit
#warning: nil
def edit_treatment(treat_id_to_edit):
    c = csv.reader(open(treatment_file))
    lines = list(c)

    for row in lines:
        if row[0] == treat_id_to_edit.sanctuary_id:
            row[1] = treat_id_to_edit.surgery
            row[2] = treat_id_to_edit.surgery_date
            row[3] = treat_id_to_edit.medication
            row[4] = treat_id_to_edit.medication_start
            row[5] = treat_id_to_edit.medication_finish
            row[6] = treat_id_to_edit.responsible_for_abuse
            row[7] = treat_id_to_edit.responsible_for_abandoning


    writer = csv.writer(open(treatment_file, 'w', newline=""))
    writer.writerows(lines)
    print(treat_id_to_edit)

#Function:edit_menu_pet
#Description:this function is the entry point menue to edit the details associated with pets
#parameters:nil
#warning: nil
def edit_menu_pet():
    pet_to_edit = input("Enter Pet ID: ")
    #pet = return_pet_id(pet_to_edit)
    pet = return_pet_id_binary(pet_to_edit)
    print(pet)
    print("\n")

    print("What would your like to edit? ")
    print("1. Pet type: ")
    print("2. Breed: ")
    print("3. Vaccination: ")
    print("4. Neutered: ")
    print("5. Microchip Number: ")
    print("6. Admission Reason: ")
    print("7. Arrival Date: ")
    print("8. Departure Date: ")
    print("9. Destination: ")
    print("10. Destination Address: ")

    optionChosen = False

    while not optionChosen:
        n = int(input("\n Please choose an option: "))

        if n == 1:
            optionChosen = True
            print("Add your new detail here: ")
            animal_type = input().title()
            pet.animal_type = animal_type
            edit_pet(pet)

        elif n == 2:
            optionChosen = True
            print("Add your new detail here: ")
            breed = input().title()
            pet.breed = breed
            edit_pet(pet)

        elif n == 3:
            optionChosen = True
            print("Add your new detail here: ")
            vaccinated = input().title()
            pet.vaccinated = vaccinated
            edit_pet(pet)

        elif n == 4:
            optionChosen = True
            print("Add your new detail here: ")
            neutered = input().title()
            pet.neutered = neutered
            edit_pet(pet)

        elif n == 5:
            optionChosen = True
            print("Add your new detail here: ")
            microchip_num = input().title()
            pet.microchip_num = microchip_num
            edit_pet(pet)

        elif n == 6:
            optionChosen = True
            print("Add your new detail here: ")
            admission_reason = input().title()
            pet.admission_reason = admission_reason
            edit_pet(pet)

        elif n == 7:
            optionChosen = True
            print("Add your new detail here: ")
            arrival_date = input().title()
            pet.arrival_date = arrival_date
            edit_pet(pet)

        elif n == 8:
            optionChosen = True
            print("Add your new detail here: ")
            departure_date = input().title()
            pet.departure_date = departure_date
            edit_pet(pet)

        elif n == 9:
            optionChosen = True
            print("Add your new detail here: ")
            destination = input().title()
            pet.destination = destination
            edit_pet(pet)

        elif n == 10:
            optionChosen = True
            print("Add your new detail here: ")
            destination_address = input().title()
            pet.destination_address = destination_address
            edit_pet(pet)
        else:
            print('invalid input')
            edit_menu_pet()

#Function: edit_menu_wild
#Description:this function is the entry point menue to edit the details associated with wild animals
#parameters:nil
#warning: nil
def edit_menu_wild():
    wild_to_edit = input("Enter Animal ID: ")
    #wild = return_Wild_id(wild_to_edit)
    wild = return_wild_id_binary(wild_to_edit)
    print(wild)
    print("\n")

    print("What would your like to edit? ")
    print("1. Animal Type: ")
    print("2. Vaccination status: ")
    print("3. Reason For Admission: ")
    print("4. Arrival Date: ")
    print("5. Departure Date: ")
    print("6. Destination: ")
    print("7. Destination Address: ")

    optionChosen = False

    while not optionChosen:
        n = int(input("\n Please choose an option: "))

        if n == 1:
            optionChosen = True
            print("What is the animals type: ")
            type = input().title()
            wild.animal_type = type
            edit_wild(wild)

        elif n == 2:
            optionChosen = True
            print("Has the animal been Vaccinated?(yes/no): ")
            vaccinated = input().title()
            wild.vaccinated = vaccinated
            edit_wild(wild)

        elif n == 3:
            optionChosen = True
            print("What is it's reason for admission: ")
            reason = input().title()
            wild.admission_reason = reason
            edit_wild(wild)


        elif n == 4:
            optionChosen = True
            print("What is the date of arrival: ")
            arrival = input().title()
            wild.arrival_date = arrival
            edit_wild(wild)

        elif n == 5:
            optionChosen = True
            print("What is the date of departure: ")
            departure = input().title()
            wild.departure_date = departure
            edit_wild(wild)

        elif n == 6:
            optionChosen = True
            print("What is the animals final destination: ")
            destination = input().title()
            wild.destination = destination
            edit_wild(wild)

        elif n == 7:
            optionChosen = True
            print("what is the animals destination address: ")
            destination_address = input().title()
            wild.destination_address = destination_address
            edit_wild(wild)
        else:
            print('invalid input')
            edit_menu_wild()

#Function: edit_menu_treat
#Description:this function is the entry point menue to edit the details associated with treatment
#parameters:nil
#warning: nil
def edit_menu_treat():
    treat_to_edit = input("Enter Pet ID: ")
    #treatment= return_treatment_id(treat_to_edit)
    treatment = return_treatment_id_binary(treat_to_edit)
    print(treatment)
    print("\n")

    print("What would your like to edit? ")
    print("1. Surgery: ")
    print("2. Surgery date: ")
    print("3. Medication: ")
    print("4. Medication start: ")
    print("5. Medication finish: ")
    print("6. Responsible for abuse: ")
    print("7. Responsible for abandoning: ")

    optionChosen = False

    while not optionChosen:
        n = int(input("\n Please choose an option: "))

        if n == 1:
            optionChosen = True
            print("Add your new detail here: ")
            animal_surgery = input().title()
            treatment.surgery= animal_surgery
            edit_treatment(treatment)

        elif n == 2:
            optionChosen = True
            print("Add your new detail here: ")
            surgery_date= input().title()
            treatment.surgery_date = surgery_date
            edit_treatment(treatment)

        elif n == 3:
            optionChosen = True
            print("Add your new detail here: ")
            medication = input().title()
            treatment.medication = medication
            edit_treatment(treatment)

        elif n == 4:
            optionChosen = True
            print("Add your new detail here: ")
            medication_start = input().title()
            treatment.medication_start = medication_start
            edit_treatment(treatment)

        elif n == 5:
            optionChosen = True
            print("Add your new detail here: ")
            medication_finish = input().title()
            treatment.medication_finish = medication_finish
            edit_treatment(treatment)

        elif n == 6:
            optionChosen = True
            print("Add your new detail here: ")
            abuser = input().title()
            treatment.responsible_for_abuse = abuser
            edit_treatment(treatment)

        elif n == 7:
            optionChosen = True
            print("Add your new detail here: ")
            abandon = input().title()
            treatment.responsible_for_abandoning = abandon
            edit_treatment(treatment)
        else:
            print('invalid input')
            edit_menu_treat()

#Function:
#Description: this function is the main menue, the entry point yo all the code
#parameters:nil
#warning: nil
def menue():
    print('WHAT WOULD YOU LIKE TO DO TODAY?')
    print('1. Create a new entry  for new arrival') #functional
    print('2. Find the full data of an animal using its ID') #functional
    print('3. Produce list of identified people that have abused animals')#functional
    print('4. Produce list of people that have abandoned their animals')#functional
    print('5. Produce list of cats ready for adoption')#functional
    print('6. Produce list of dogs ready for adoption')#functional
    print('7. Produce list of animals that are ready to be returned to their owners')#functional
    print('8. Edit stored data\n')

    #user makes a selection and the various entry points are determined
    selection = int(input('\nEnter a selection: '))

    if (selection == 1): #Create a new entry for new arrival
        print('What type of entry would you like to make?')
        print('1. Pet')
        print('2. wild animal')
        print('3. Treatment')


        choice = int(input('\nEnter a selection: \n'))
        if(choice==1):
            write_new_pet()

        elif(choice==2):
            write_new_wildAnimal()

        elif(choice==3):
            write_new_treatment()
        else:
            print('invalid input')
            menue()



    elif (selection == 2):
        #Find the full data of an animal using its ID
        animal_id = input('what is the ID of the animal you would like to look up: ')
        find_with_id(animal_id)


    elif (selection == 3):
        print('list of identified people that have abused animals')
        find_abused()


    elif (selection == 4):
        print('list of people that have abandoned their animals')

        find_abandoned()

    elif (selection == 5): #Produce list of cats ready for adoption
        print('list of cats ready for adoption')

        ready_for_adoption("Cat")

    elif (selection == 6): #Produce list of dogs ready for adoption1
        print('list of dogs ready for adoption')

        ready_for_adoption("Dog")

    elif (selection == 7):
        print('list of animals that are ready to be returned to their owners')

        ready_to_return()

    elif (selection == 8):
        print('Edit stored data')
        print(("1. edit pet\n"
                "2. edit wild animal\n"
                "3. edit treatment\n"))

        response = int(input("?: "))
        print(response)

        if response == 1:

            edit_menu_pet()

        elif response ==2:
            edit_menu_wild()

        elif response ==3:
            edit_menu_treat()

        else:
            print('your response ' + response +' is an invalid selection')
            w = input('would you like to restart? y/n\n')
            if w  == 'y':
                menue()
            else:
                quit()



load_Wildanimal()
load_treatment()
load_petData()
menue()