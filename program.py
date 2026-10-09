# Patient Class
class patient:
  def __init__(self, name, patient_id, age, gender, diagnosis):
    self.name = name
    self.patient_id = patient_id
    self.age = age
    self.gender = gender
    self.diagnosis = diagnosis

    def display_info(self):
      print("\n ***** Patient Information *****")
      print(f"name: {self.name}")
      print(f"id: {self.patient_id}")
      print(f"age: {self.age}")
      print(f"gender: {self.gender}")
      print(f"diagnosis: {self.diagnosis}")

      # Hospital Class
      class Hospital:
        def __init__(self, hospital_name, location, capacity):
          self.hospital_name = hospital_name
          self.location = location
          self.capacity = capacity

          self.patients = []

          def add_patient(self, patient):
            self.patients.append(patient)
            print("patient added successfully")

            def display_patients(self):
              print("\n ***** Hospital Patients *****")
              print(f"\n ***** (self.hospital_name) *****")


              # Check if there are patients
              if len(self.patients) == 0:
                print ("No patients Records Found.")
              else:
                for patient in self.patients:
                  patient.display_info()


                  # Patient Objects
                  patient1 = patient("Salma", 101, 24, "Male", "Poverty")
                  patient2 = patient("Salam", 102, 24, "Male", "Fever")
                  patient3 = patient("Salmata", 103, 24, "Female", "Poverty")
                  patient4 = patient("Saidu", 104, 24, "Male", "Malaria")

                  # Hospital Objects
                  hospital = Hospital("Donald Clinic")


                  # Add patient to the hospital using the add_patient method in the hospital class
                  hospital.add_patient(patient1)
                  hospital.add_patient(patient2)
                  hospital.add_patient(patient3)
                  hospital.add_patient(patient4)

                  # Display all patients records in the hospital
                  hospital.display_patient()
                  

              
              
     