# Karib Shams - AI/ML Portfolio (Flask Web App)

This is a **personal portfolio web application** built using **Flask**, serving structured data through REST APIs and rendering a frontend via HTML templates. It showcases academic background, skills, research, and professional experiences of **Karib Shams**, an AI/ML researcher and teaching assistant.

---

## 🔧 Technologies Used

- **Python + Flask**
- **HTML + Jinja2**
- **JavaScript (for frontend API integration)**
- **Flask-CORS** (for enabling frontend-backend API requests)
- **Bootstrap / Custom CSS** (optional styling)
- **RESTful API** endpoints

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/karibshams/protfolio_v1.git
cd protfolio_v1
````

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/macOS

pip install flask flask-cors
```

### 3. Run the Flask Server

```bash
python app.py
```

Visit the app at: [http://localhost:5000](http://localhost:5000)

---

## 📡 Available API Endpoints

| Endpoint                 | Description                 |
| ------------------------ | --------------------------- |
| `/api/portfolio`         | Full portfolio JSON data    |
| `/api/personal-info`     | Personal info               |
| `/api/education`         | Education details           |
| `/api/skills`            | Skills and technologies     |
| `/api/experience`        | Work experience             |
| `/api/publications`      | Research publications       |
| `/api/research-projects` | Research project list       |
| `/api/academic-projects` | Academic project list       |
| `/api/references`        | Academic references         |
| `/api/contact`           | Contact form (POST request) |
| `/api/stats`             | Summary stats               |
| `/health`                | Health check endpoint       |

---

## 📂 Folder Structure

```
├── app.py
├── static/
├── templates/
├── .env
├── venv/
└── README.md
```

---

## 📬 Contact

📧 **Email:** [shams321karib@gmail.com](mailto:shams321karib@gmail.com)
📍 **Location:** Dhaka, Bangladesh
🔗 [LinkedIn](https://www.linkedin.com/in/karib-shams-007975305/) | [GitHub](https://github.com/karibshams)

---

## 📄 License

This project is open-source for learning and demonstration purposes.


