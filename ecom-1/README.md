# eLearning Project

This project is an eLearning platform built using Django. It allows users to browse and enroll in various courses, and it includes a payment integration feature for processing transactions.

## Project Structure

```
ecom
├── ecom
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── payments
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates
│       └── payments
│           ├── payment_form.html
│           ├── payment_success.html
│           └── payment_failure.html
├── templates
│   ├── base.html
│   └── home.html
├── static
│   ├── css
│   ├── js
│   └── img
├── manage.py
└── README.md
```

## Features

- **Course Browsing**: Users can view a list of available courses.
- **Enrollment**: Users can enroll in courses of their choice.
- **Payment Integration**: The project includes a payment system to handle transactions securely.
- **User Authentication**: Users can create accounts and log in to manage their courses.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ecom
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Payment Integration

The payment integration is handled in the `payments` app. Users can enter their payment details in the payment form, and upon successful payment, they will be redirected to a success page. In case of failure, they will be redirected to a failure page.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.