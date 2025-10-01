# BattalWeb
The Battal Website is a simple and user-friendly web application built using Python and the Django framework. The project demonstrates how to create a basic website with essential web pages and navigation, making it a good starting point for beginners learning Django web development.

🔹 Features & Pages:

Home Page

Welcomes visitors with a clean interface.

Provides navigation links to other sections of the website.

About Us Page

Describes the purpose of the Battal Website.

Gives information about the team or organization behind it.

Contact Us Page

Includes a form for visitors to send queries (name, email, message).

Messages are stored in the Django database.

Can be extended with email notifications using Django’s email system.

Help Page

Provides guidance for using the website.

Contains frequently asked questions (FAQs) and support resources.

🔹 Tech Stack:

Frontend: HTML5, CSS3, Bootstrap (for styling)

Backend: Python, Django Framework

Database: SQLite (default, can be upgraded to MySQL/PostgreSQL)

🔹 Django Implementation:

Created a Django project called battal_project.

Created an app named main for handling web pages.

Defined views for home, about, contact, and help.

Used templates for rendering HTML pages dynamically.

Configured URLs to map requests to the respective views.

🔹 URL Structure Example:
/        → Home Page
/about   → About Us Page
/contact → Contact Us Page
/help    → Help Page

🔹 Purpose:

This project is designed for students and beginners who want to learn how to:

Set up a Django project.

Create multiple pages with templates.

Handle user input via forms.

Use basic database operations.
