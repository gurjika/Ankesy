# Ankesy

**Ankesy** is a scam reporting platform designed to help users identify and track scams by submitting detailed reports about potential fraudulent activities. The platform supports automated email notifications to inform parents or guardians about revealed information and categorized scam types. Devleloped for 2 day Medialab hackathon.

## Features

- **Report Scams:**  
  Users can submit detailed scam reports with various information types (credit card, email, phone number, etc.).
  
- **Scam Type Categorization:**  
  Scams are categorized into types like Phishing, Prize Scams, Investment Fraud, etc.

- **Parent Notifications via Email:**  
  Parents or guardians are notified via email with details of revealed information for flagged reports. Emails are customized with HTML templates.

- **Celery for Asynchronous Tasks:**  
  Background tasks like sending emails are handled efficiently using Celery.

- **Redis for Task Queue Management:**  
  Redis serves as the message broker for Celery, ensuring smooth task execution.

- **Nginx as Reverse Proxy:**  
  Static and media files are served through Nginx, which also acts as a reverse proxy.

- **Deployed on Digital Ocean:**  
  The app is hosted on Digital Ocean for a reliable and scalable infrastructure.

---

## Tech Stack

- **Backend Framework:** Django Rest Framework
- **Database:** Mysql  
- **Task Queue:** Celery with Redis  
- **Web Server:** Nginx  
- **Deployment:** Docker, Digital Ocean  
- **Email Service:** Django Email System with HTML templates  

---

## Setup and Installation

Follow the steps below to set up and run the project on your local machine.

### Installation

1. Clone the repository:

   ```bash
   git clone -b dev https://github.com/gurjika/Ankesy.git
   cd ankesy


2. Create a `.env` file and specify the required environment variables:
    ```env
    DB_PASSWORD=your_db_password
    SECRET_KEY=your_secret_key
    EMAIL_HOST_PASSWORD=email_app_password
    ```

3. Run the application using Docker Compose:
    ```sh
    docker-compose up -d
    ```

4. Run the database migrations:
    ```sh
    docker-compose run django python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    docker-compose run django python manage.py createsuperuser
    ```