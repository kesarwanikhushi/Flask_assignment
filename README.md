# Flask_assignment

# 📦 Flask + MongoDB Atlas Integration Project

This project is a simple Flask web application that performs two key functions:

1. **API Endpoint (`/api`)**: Returns JSON data read from a backend file.
2. **Frontend Form**: Submits user data (name and email) to a MongoDB Atlas database.

---

## 🔧 Technologies Used

- Python 3
- Flask
- MongoDB Atlas (Cloud-hosted NoSQL DB)
- HTML (for frontend forms)
- JSON (for data API)

---

## 📁 Project Structure

```
FlaskProject/
├── app.py               # Main Flask application
├── data.json            # JSON data served by /api
├── templates/
│   ├── form.html        # Frontend form
│   └── success.html     # Submission confirmation page
└── README.md            # Project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install flask pymongo certifi
```

### 3. Run the Flask Application

```bash
python app.py
```

The app will be live at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 MongoDB Atlas Setup

1. Create a cluster on MongoDB Atlas.
2. Create a database user.
3. Whitelist IP (0.0.0.0/0 for development).
4. Copy your connection string.
5. Update `app.py`:
   ```python
   from pymongo import MongoClient
   import certifi

   client = MongoClient("YOUR_CONNECTION_URI", tlsCAFile=certifi.where())
   db = client["flask_db"]
   collection = db["submissions"]
   ```

---

## 📬 Routes Overview

| Route       | Method | Description                                  |
|-------------|--------|----------------------------------------------|
| `/`         | GET    | Displays the form page                        |
| `/submit`   | POST   | Submits data to MongoDB                       |
| `/success`  | GET    | Shows confirmation message                    |
| `/api`      | GET    | Returns JSON data from `data.json` file      |

---

## ✅ Features

- Dynamic form submission with MongoDB integration
- Error handling on form submission
- API endpoint delivering JSON data
- Simple and clean codebase for educational use

---

## 📸 Screenshots

> Add screenshots of the form, success page, and MongoDB Atlas dashboard in your submission document.

---

## 📌 License

This project is for educational/demo purposes only.
