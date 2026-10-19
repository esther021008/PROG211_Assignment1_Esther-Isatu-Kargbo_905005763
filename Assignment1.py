# Complaint class
class Complaint:
    #class attribute
    government_name = "Citizen Services Department"

    def __init__(self, complaint_id, category, description):
        self.complaint_id = complaint_id
        self.category = category
        self.description = description
        self.status = "Pending"

    # update status function
    def update_status(self, new_status):
        self.status = new_status

    #display complaint
    def display_complaint(self):
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")

    #class method to acces the class attribute
    @classmethod
    def display_department(cls):
        print(f"Department: {cls.government_name}")

#citizen class
class Citizen:
    def __init__(self, citizen_id, name, community):
        self.citizen_id = citizen_id
        self.name = name
        self.community = community
        self.complaint = None

    def submit_complaint(self, complaint):
        self.complaint = complaint

    #display citizen information
    def display_info(self):
        print(f"****** CITIZEN INFORMATION *******")
        print(f"Citizen ID: {self.citizen_id}")
        print("Name:", self.name)
        print("Community:", self.community)

        if self.complaint:
            print(" ******** COMPLAINT ********")
            self.complaint.display_complaint()

# add function
def add_complaint(complaints, complaint):
    complaints.append(complaint)
    print("Complaint added successfully.")


def display_complaints(complaints):
    for complaint in complaints:
        complaint.display_complaint()




complaints = []

citizen1 = Citizen(
    "C001",
    "Esther",
    "Grafton"
)

complaint1 = Complaint(
    "CP001",
    "Electricity",
    "Damaged transformer"
)

citizen2 = Citizen(
    "C002",
    "Clifford",
    "Waterloo"
)

complaint2 = Complaint(
    "CP001",
    "water",
    "Blocked drainages"
)

complaint1.update_status("Resolved")
complaint2.update_status("Pending")

citizen1.submit_complaint(complaint1)
citizen2.submit_complaint(complaint2)

add_complaint(complaints, complaint1)
add_complaint(complaints,complaint2)

Complaint.display_department()

citizen1.display_info()
print(f" \n ******Second Citizen******")
citizen2.display_info()