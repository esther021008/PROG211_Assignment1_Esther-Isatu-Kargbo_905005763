Citizen Complaint Management System

1. Project Overview

The Citizen Complaint Management System is a simple Python project developed to demonstrate Object-Oriented Programming (OOP). It helps organize citizens’ information and record complaints about problems affecting their communities.

Examples of complaints include damaged roads, water supply problems, and other community issues.

2. Problem Statement

Citizens may experience difficulties reporting and organizing community problems. This project demonstrates how a simple computer program can help record complaints, store their details, and track their status.

3. Project Objectives

* To record citizens’ information.
* To create and manage citizen complaints.
* To organize complaints using a Python list.
* To display complaint information.
* To update the status of a complaint.
* To demonstrate the use of Object-Oriented Programming in Python.

4. Technologies Used

* Programming Language: Python
* Code Editor: Visual Studio Code
* Version Control: Git and GitHub

5. Main Features

* Register citizen information in the program.
* Record complaint IDs, categories, and descriptions.
* Assign a default status of Pending to each complaint.
* Update complaint status.
* Store multiple complaints in a Python list.
* Display citizen and complaint information.

6. Classes Used

Complaint Class

The Complaint class stores information about a complaint. Its attributes include:

* complaint_id — the unique identification number of a complaint.
* category — the type of problem reported.
* description — details about the problem.
* status — the current status of the complaint.

Its methods include update_status() and display_complaint(). It also has a class method called display_department().

Citizen Class

The Citizen class stores information about a citizen, including:

* citizen_id — the citizen’s identification number.
* name — the citizen’s name.
* community — the citizen’s community.
* complaint — the complaint associated with the citizen.

Its methods include submit_complaint() and display_info().

7. Object-Oriented Programming Concepts

This project demonstrates the following OOP concepts:

* Classes: Blueprints used to create objects.
* Objects: Instances created from the Citizen and Complaint classes.
* Attributes: Variables that store information about citizens and complaints.
* Instance methods: Methods that perform operations on objects.
* Class method: The display_department() method displays the department name.
* Object interaction: A citizen object can submit a complaint object.

8. Data Structure

The project uses a Python list called complaints to store complaint objects. The add_complaint() function adds complaints to the list, while display_complaints() displays the stored complaints.

9. How to Run the Program

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Save the Python code in a file named main.py.
4. Open the terminal in Visual Studio Code.
5. Run the following command:

python main.py

If your system uses the python3 command, run:

python3 main.py

10. Example Output

Complaint added successfully.
Department: Citizen Services Department
===== CITIZEN INFORMATION =====
Citizen ID: C001
Name: Esther
Community: Grafton
===== COMPLAINT =====
Complaint ID: CP001
Category: Electricity
Description: Damaged Transformer
Status: Resolved

11. Sustainable Development Goal (SDG)

This project relates to SDG 16: Peace, Justice and Strong Institutions.

SDG 16 promotes effective, accountable, and transparent institutions. 
The project demonstrates how technology can help organize citizen complaints and support communication about community problems.

Official link: https://sdgs.un.org/goals/goal16

12. Digital Public Goods Principles

The project considers principles associated with Digital Public Goods (DPGs), including:

* Open-source potential: The code can be shared and improved by others.
* Inclusiveness: The idea focuses on helping citizens report community problems.
* Privacy awareness: Real citizen information should be protected if the system is developed further.
* Reusability: The classes can be adapted for other complaint-management projects.

This is an educational project and has not been certified as an official Digital Public Good.

13. Limitations

The current program is a basic demonstration. It does not save complaint records permanently after the program closes, 
and it does not connect directly to a government department or online database.

14. Future Improvements

Future versions could include:

* A database for permanent record storage.
* A graphical user interface.
* A search feature for finding complaints.
* A more complete citizen registration system.
* User authentication and improved data protection.

15. Conclusion

The Citizen Complaint Management System demonstrates how Python and Object-Oriented Programming can be used to organize citizen information and community complaints.
It provides a foundation for developing a more advanced system to support the reporting and tracking of community problems.



United Nations. (n.d.). Goal 16: Peace, justice and strong institutions. https://sdgs.un.org/goals/goal16

Digital Public Goods Alliance. (n.d.). Digital Public Goods Standard. https://www.digitalpublicgoods.net/standard
