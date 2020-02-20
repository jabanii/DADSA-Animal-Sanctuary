#Author: Paul Jabani Lassa
#Created: 5th November 2019
#Revised: 20th November 2019
#Description:This class is the wild animal class, objects in the csv file are loaded into this class
class WildAnimal:#attributes of the class wild animal
    def __init__(self, sanctuary_id, animal_type, vaccinated,
                 admission_reason, arrival_date, departure_date, destination, destination_address):
        self.sanctuary_id = sanctuary_id
        self.animal_type = animal_type
        self.vaccinated = vaccinated
        self.admission_reason = admission_reason
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.destination = destination
        self.destination_address = destination_address

    def __str__(self):
        return_str = "Sanctuary Identification: " + self.sanctuary_id + "||"
        return_str += "Animal Type: " + self.animal_type + "||"
        return_str += "Vaccinated: " + self.vaccinated + "||"
        return_str += "Reason for Admission: " + self.admission_reason + "||"
        return_str += "Date of Arrival: " + self.arrival_date + "||"
        return_str += "Date of Depature: " + self.departure_date + "||"
        return_str += "Destination: " + self.destination + "||"
        return_str += "Destination Address: " + self.destination_address + "||"
        return return_str

