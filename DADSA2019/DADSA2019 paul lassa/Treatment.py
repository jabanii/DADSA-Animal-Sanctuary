#Author: Paul Jabani Lassa
#Created: 5th November 2019
#Revised: 20th November 2019
#Description:This class is the treatment class, objects in the csv file are loaded into this class

class Treatment:#attributes of the class treatment
    def __init__(self, sanctuary_id, surgery, surgery_date, medication, medication_start, medication_finish,
                 responsible_for_abuse, responsible_for_abandoning):
        self.sanctuary_id = sanctuary_id
        self.surgery = surgery
        self.surgery_date = surgery_date
        self.medication = medication
        self.medication_start = medication_start
        self.medication_finish = medication_finish
        self.responsible_for_abuse = responsible_for_abuse
        self.responsible_for_abandoning = responsible_for_abandoning

    def __str__(self):
        return_str = "Sanctuary: " + self.sanctuary_id + "||"
        return_str += "Surgery: " + self.surgery + "||"
        return_str += "Surgery Date: " + self.surgery_date + "||"
        return_str += "Medication: " + self.medication + "||"
        return_str += "Medication start date: " + self.medication_start + "||"
        return_str += "Medication end date: " + self.medication_finish + "||"
        return_str += "Reason for Abuse: " + self.responsible_for_abuse + "||"
        return_str += "Date of Abandoning: " + self.responsible_for_abandoning + "||"
        return return_str