# Message Schedular App

## Description

Message Schedular App is a web application that allows users to set up reminders with custom messages. It provides a simple interface to schedule reminders and supports various methods of reminder delivery, such as SMS and Email.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vignxs/message-schedular-app.git
   cd message-schedular-app
   ```
2. **Install Dependencies**
   Make sure you have Python and pip installed on your system. Then, install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```
3. **Database Setup**
   Configure your database settings in `settings.py` and then run migrations to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Run the Development Server**
   Start the Django development server using the following command:

   ```bash
   python manage.py runserver
   ```

   The server should now be running locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Manual Testing

You can manually test the functionality of the application by accessing it through a web browser. Here are some steps you can follow:

1. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the home page.
2. Explore the different features of the application, such as setting up reminders, viewing existing reminders, and sending test reminders.
3. Make sure all the functionalities are working as expected and there are no errors.

## Deployment

To deploy the application to a production server, you'll need to configure additional settings such as database configuration, static files serving, and security settings. Refer to the Django documentation f
