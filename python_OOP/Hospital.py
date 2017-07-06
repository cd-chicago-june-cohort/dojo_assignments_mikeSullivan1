class Patient(object):
    id_counter=1
    def __init__(self,name,allergies):
        self.id = Patient.id_counter
        Patient.id_counter+=1
        self.name=name
        self.allergies=allergies
        self.bed_num=0

    

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds=[]
        for i in range(0,capacity):
            self.beds.append(0)
        
    def admit(self,patient):
        #add id to self.patients
        for i in self.beds:
            if self.beds[i] == 0:
                patient.bed_num = i+1
                self.beds[i]=1
                self.patients.append(patient.id)
                return "{} is admitted to bed {}".format(patient.name,patient.bed_num)
        return "Sorry there are no beds. Good luck you fucking Prole."
    
    def discharge(self,patient):
        for x in range(0,len(patients)-1):
            if patient.id ==self.patients[x]:
                patients.pop(i)
        self.beds[patient.bed_num] =0
        patient.bed_num=0
        

        
patient0=Patient("George Washington", "Cherry Trees")

hospital1=Hospital("Washington General", 3)

print hospital1.admit(patient0)

