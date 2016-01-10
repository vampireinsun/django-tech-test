#### The Task

Build a Django app for borrowers to register and request a loan. You will need to collect the following information:

* The borrower's name, email, and telephone number.
* The borrower's business' name, address, registered company number (8 digit number), and business sector (pick from Retail, Professional Services, Food & Drink, or Entertainment).
* The amount the borrower wishes to borrow in GBP (between £10000 and £100000), for how long (number of days), and a reason for the loan (text description).
* This information should be stored in the database via appropriate models, and accessible to an admin in the standard Django Admin tool.

#### Notes for implementation
* No third part auth package involved with, django own auth framwork is used
* The database db.sqlite3 contains some sample data 
   - users:  neily:neily,  ymao:ymao, admin:admin
   - Only the user admin has the right to access the admin site
   - The main entry page is : http://127.0.0.1:8000/index/
   - I use django's own server to run this implementation.

