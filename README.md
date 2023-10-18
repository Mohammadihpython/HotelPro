# Hotel Management System Pro
This is a Hotel Management System built using Django and Django Rest Framework. The system includes features such as OTP authentication and Celery for task management.


## Installation

1. Clone the repository to your local machine.
   ```
   git clone ttps://github.com/Mohammadihpython/HotelPro.git
   ```
2. Create a virtual environment and activate it.
3. Install the dependencies using 
   ```
   pip install -r requirements.txt
   ```
4. Run the migrations using  
    ```
   python manage.py migrate
    ```
7. Create a superuser using 
   ```
   python manage.py createsuperuser
   ```
8. Start the development server using
   ```
   python manage.py runserver
   ``` 

## database desgin 
![database degine image](<docs/images/Screenshot from 2023-09-16 21-34-28.png> )
### Authentication

The system uses OTP authentication for user login. When a user attempts to login, an OTP is sent to their registered mobile number. The user must enter the OTP to complete the login process.

### User Management

The system includes user management features such as creating new users, updating user details, and deleting users.

### Room Management

The system allows users to view available rooms, book rooms, and cancel room bookings.

### Task Management

The system uses Celery for task management. Tasks such as sending OTPs and sending booking confirmation emails are handled asynchronously.

## API Endpoints

The following API endpoints are available:

- /account/register/ - GET, POST
- /account/login/ - POST
- /rooms/suggestion/ - POST
- /api/bookings/ - GET, POST
- /api/bookings/<int:pk>/ - GET, PUT, DELETE
