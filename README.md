# Hospital Management System

A comprehensive web-based Hospital Management System built with Django that streamlines hospital operations including patient management, doctor management, appointment scheduling, and billing.

## 🏥 Features

### Admin Dashboard
- **Doctor Management**
  - Add, update, and remove doctors
  - Approve/reject doctor registrations
  - View doctor specializations and departments
  - Track doctor performance and patient assignments

- **Patient Management**
  - Add, update, and remove patients
  - Approve/reject patient registrations
  - Assign patients to doctors
  - Track patient admission and discharge

- **Appointment Management**
  - Create and manage appointments
  - Approve/reject appointment requests
  - View appointment history and status

- **Billing & Discharge**
  - Generate patient discharge summaries
  - Calculate bills (room charges, doctor fees, medicine costs)
  - Download bills as PDF
  - Track payment history

### Doctor Dashboard
- View assigned patients
- Manage appointments
- Search patients by name or symptoms
- View patient discharge history
- Delete appointments

### Patient Dashboard
- View assigned doctor details
- Book appointments with available doctors
- Search doctors by name or department
- View appointment status
- Access discharge summary and bills

### Additional Features
- **User Authentication**: Secure login/signup for Admin, Doctor, and Patient roles
- **Email Notifications**: Contact form with email integration
- **AI Chatbot**: Gemini AI-powered chatbot for patient assistance
- **Responsive Design**: Mobile-friendly interface
- **Profile Management**: Upload and manage profile pictures

## 🛠️ Technology Stack

- **Backend**: Django 3.0.5
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **PDF Generation**: xhtml2pdf
- **Email**: SMTP (Gmail)
- **AI Integration**: Google Gemini API
- **Additional Libraries**: 
  - django-widget-tweaks (form styling)

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Git

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Sarvanpilli/Hospital-Management-Website-using-Django.git
cd Hospital-Management-Website-using-Django/hospitalmanagement-master
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
pip install google-generativeai
```

### 4. Configure Email Settings (Optional)
Edit `hospitalmanagement/settings.py` and update the email configuration:
```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
EMAIL_RECEIVING_USER = ['recipient@gmail.com']
```

**Note**: For Gmail, you need to:
1. Enable 2-Factor Authentication
2. Generate an App Password
3. Use the App Password in settings

### 5. Configure Gemini AI (Optional)
Update the Gemini API key in `hospitalmanagement/settings.py`:
```python
GEMINI_API_KEY = 'your-gemini-api-key'
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 8. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
hospitalmanagement-master/
├── hospital/                    # Main application
│   ├── migrations/             # Database migrations
│   ├── admin.py               # Admin panel configuration
│   ├── forms.py               # Form definitions
│   ├── models.py              # Database models
│   ├── urls.py                # URL routing
│   ├── views.py               # View functions
│   └── views_chatbot.py       # AI chatbot views
├── hospitalmanagement/         # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── static/                     # Static files
│   ├── images/                # Image assets
│   ├── profile_pic/           # User profile pictures
│   └── style.css              # Stylesheets
├── templates/                  # HTML templates
│   └── hospital/              # App-specific templates
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
└── .gitignore                 # Git ignore rules
```

## 🗃️ Database Models

### Doctor
- User (OneToOne with Django User)
- Profile Picture
- Address, Mobile
- Department (Cardiologist, Dermatologist, Emergency Medicine, etc.)
- Status (Approved/Pending)

### Patient
- User (OneToOne with Django User)
- Profile Picture
- Address, Mobile
- Symptoms
- Assigned Doctor
- Admission Date
- Status (Approved/Pending)

### Appointment
- Patient ID, Doctor ID
- Patient Name, Doctor Name
- Appointment Date
- Description
- Status (Approved/Pending)

### PatientDischargeDetails
- Patient Information
- Assigned Doctor
- Admission & Release Dates
- Days Spent
- Charges (Room, Medicine, Doctor Fee, Other)
- Total Bill

## 👥 User Roles & Access

### Admin
- Full system access
- Manage doctors and patients
- Approve registrations
- Generate bills and discharge patients

### Doctor
- View assigned patients
- Manage appointments
- Search patient records
- Cannot approve registrations

### Patient
- View assigned doctor
- Book appointments
- View bills and discharge summary
- Cannot access other patients' data

## 🔐 Default Login Credentials

After creating a superuser, you can access the admin panel at:
- URL: `http://127.0.0.1:8000/admin/`
- Username: (your superuser username)
- Password: (your superuser password)

For Doctor and Patient accounts, they must be created through the signup forms and approved by an admin.

## 📧 Contact Form Setup

To enable the contact form functionality:

1. Use a Gmail account with 2FA enabled
2. Generate an App Password from Google Account settings
3. Update `settings.py` with your credentials
4. The contact form will send emails to the configured recipient

## 🤖 AI Chatbot

The system includes an AI-powered chatbot using Google's Gemini API. To enable:

1. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Update `GEMINI_API_KEY` in `settings.py`
3. The chatbot will be available to patients for health-related queries

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset database
python manage.py flush
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Port Already in Use
```bash
python manage.py runserver 8080
```

## 📝 Usage Guide

### For Admins
1. Login at `/adminlogin`
2. Approve pending doctor/patient registrations
3. Manage appointments
4. Generate bills and discharge patients

### For Doctors
1. Signup at `/doctorsignup`
2. Wait for admin approval
3. Login at `/doctorlogin`
4. View and manage assigned patients

### For Patients
1. Signup at `/patientsignup`
2. Wait for admin approval
3. Login at `/patientlogin`
4. Book appointments and view medical records

## 🔒 Security Notes

⚠️ **Important**: This is a development setup. For production:

1. Change `DEBUG = False` in settings.py
2. Update `SECRET_KEY` with a secure random key
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL/MySQL)
5. Set up HTTPS
6. Use environment variables for sensitive data
7. Implement proper backup strategies

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Developer

Original Developer: Sumit Kumar
- Facebook: fb.com/sumit.luv
- YouTube: youtube.com/lazycoders

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- Google Gemini AI
- xhtml2pdf Library

## 📞 Support

For issues and questions:
- Create an issue in the GitHub repository
- Use the contact form in the application

---

**Note**: This system is designed for educational and demonstration purposes. Ensure compliance with healthcare regulations (HIPAA, etc.) before using in a production environment.
