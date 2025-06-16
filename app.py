from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

# Disable automatic .env loading to prevent encoding errors
os.environ['FLASK_SKIP_DOTENV'] = '1'

app = Flask(__name__)
CORS(app)

# Karib Shams Portfolio Data
PORTFOLIO_DATA = {
    "personal_info": {
        "name": "Karib Shams",
        "title": "AI/ML Researcher & Graduate Teaching Assistant",
        "email": "shams321karib@gmail.com",
        "phone": "+8801797470717",
        "whatsapp": "https://wa.me/8801797470717",
        "location": "Dhaka, Bangladesh",
        "bio": "Passionate about solving complex problems through technology, with hands-on experience in computer vision, NLP, knowledge graphs, and explainable AI. Currently pursuing MSc in CSE and working with state-of-the-art LLMs. I am a Graduate Teaching Assistant at East West University with strong foundation in AI, machine learning, and deep learning.",
        "social_links": {
            "github": "https://github.com/karibshams",
            "linkedin": "https://www.linkedin.com/in/karib-shams-007975305/",
            "scholar": "https://scholar.google.com/citations?hl=en&user=C26dtwMAAAAJ",
            "kaggle": "https://www.kaggle.com/shamskarib",
            "whatsapp": "https://wa.me/8801797470717"
        }
    },
    "education": [
        {
            "degree": "MSc in Computer Science & Engineering",
            "institution": "East West University, Dhaka",
            "duration": "February 2025 – January 2026 (Expected)",
            "status": "Current Semester Running",
            "cgpa": "Yet to be finalized"
        },
        {
            "degree": "B.Sc. in Computer Science & Engineering",
            "institution": "East West University, Dhaka",
            "duration": "2020 - 2024",
            "cgpa": "3.58"
        },
        {
            "degree": "Higher Secondary Certificate (HSC)",
            "institution": "National Ideal College",
            "duration": "2017 - 2019",
            "gpa": "4.67"
        },
        {
            "degree": "Secondary School Certificate (SSC)",
            "institution": "Motijheel Model School and College",
            "duration": "2016 - 2017",
            "gpa": "5.00"
        }
    ],
    "skills": {
        "programming_languages": ["Python", "Java", "C", "C++", "R", "SQL"],
        "web_technologies": ["HTML5", "CSS3", "JavaScript", "Django"],
        "ai_ml_specializations": ["Computer Vision", "NLP", "Deep Learning", "Knowledge Graphs", "Explainable AI", "LLMs"],
        "tools_technologies": ["Jupyter Notebook", "Google Colab", "Linux", "Visual Studio", "Roboflow", "Kaggle", "Oracle Apex", "Microsoft Office", "Cisco PT", "OpenSSL", "Windows PowerShell", "Code Blocks", "NetBeans"]
    },
    "experience": [
        {
            "position": "Graduate Teaching Assistant (GTA)",
            "company": "East West University",
            "duration": "20 October 2024 – Current",
            "courses": ["Statistics for Data Science", "Artificial Intelligence", "Machine Learning"],
            "description": "Teaching graduate and undergraduate courses in AI/ML domain, assisting students with complex concepts and research methodologies."
        },
        {
            "position": "Undergraduate Teaching Assistant (UTA)",
            "company": "East West University",
            "duration": "10 June 2024 - 19 October 2024",
            "courses": ["Algorithms", "Statistics for Data Science", "Artificial Intelligence", "Machine Learning"],
            "description": "Assisted in teaching core computer science courses, mentored students in programming and algorithmic thinking."
        }
    ],
    "publications": [
        {
            "title": "Histopathology Images-Based Deep Learning Prediction of Prognosis and Therapeutic Response in Small Cell Lung Cancer",
            "type": "Research Paper",
            "description": "Published research focusing on using deep learning techniques for medical diagnosis and prognosis prediction in lung cancer treatment."
        },
        {
            "title": "Tuberculosis Diagnosis from Chest X-Ray Image Using Deep Learning Techniques",
            "type": "Research Paper",
            "description": "Research on automated tuberculosis diagnosis using computer vision and deep learning methodologies for medical imaging analysis."
        },
        {
            "title": "An Image Dataset for Traffic Flow and Pedestrian Movement Analysis on Bangladeshi Urban Roads",
            "type": "Dataset Paper",
            "description": "Dataset contribution for traffic analysis and urban planning research specifically focused on Bangladeshi road conditions and traffic patterns."
        },
        {
            "title": "Bangladeshi Traffic Flow Dataset",
            "type": "Dataset",
            "description": "Contributor to the dataset published on Mendeley Data",
            "doi": "10.17632/h8bfgtdp2r.6",
            "platform": "Mendeley Data"
        }
    ],
    "research_projects": [
        {
            "title": "Emotion Detection from Text Using Configurable Transformer-Based Models",
            "description": "Developing advanced NLP models for emotion detection from textual data using state-of-the-art transformer architectures.",
            "technologies": ["Python", "Transformers", "NLP", "Deep Learning", "PyTorch"],
            "category": "Research"
        },
        {
            "title": "Integrated Text Intelligence: Constructing Knowledge Graphs and Performing Sentiment Analysis",
            "description": "Building comprehensive text analysis systems combining knowledge graph construction with sentiment analysis using NLP and deep learning.",
            "technologies": ["Knowledge Graphs", "Sentiment Analysis", "NLP", "Deep Learning", "Graph Neural Networks"],
            "category": "Research"
        },
        {
            "title": "Bangladesh E-commerce Reviews Dataset",
            "description": "Creating a comprehensive dataset for sentiment and emotion classification from Bangladesh e-commerce reviews for NLP research.",
            "technologies": ["Dataset Creation", "Sentiment Analysis", "Bengali NLP", "Data Mining"],
            "category": "Research"
        },
        {
            "title": "TFP-BD: Traffic Flow and Pedestrian Dataset",
            "description": "An image dataset for Traffic Flow and Pedestrian movement analysis on Bangladeshi urban roads for computer vision research.",
            "technologies": ["Computer Vision", "Traffic Analysis", "Dataset Creation", "Image Processing"],
            "category": "Research"
        },
        {
            "title": "Enhancing Retail Store Inventory Management Using Machine Learning and Explainable AI",
            "description": "Developing intelligent inventory management systems with explainable AI for better business decision making.",
            "technologies": ["Machine Learning", "Explainable AI", "Business Intelligence", "Predictive Analytics"],
            "category": "Research"
        }
    ],
    "academic_projects": [
        {
            "title": "Online E-ticketing System",
            "description": "Full-stack web application for online ticket booking and management system developed as part of Software Engineering course.",
            "technologies": ["Web Development", "Database Design", "Software Engineering", "System Architecture"],
            "course": "Software Engineering"
        },
        {
            "title": "Online Food Delivery Website",
            "description": "Complete food delivery platform with user management, order processing, and delivery tracking features.",
            "technologies": ["Web Development", "Database Management", "User Interface Design", "System Integration"],
            "course": "Software Engineering"
        },
        {
            "title": "Securing Networked System with Public Key Infrastructure",
            "description": "Implementation of secure communication protocols and transport layer security in networked systems.",
            "technologies": ["Cybersecurity", "PKI", "Network Security", "Cryptography"],
            "course": "Cyber Security"
        },
        {
            "title": "Full-fledged Network for Organization",
            "description": "Designed and implemented complete network infrastructure with multiple subnets for organizational use.",
            "technologies": ["Network Design", "Subnetting", "Network Administration", "Infrastructure Planning"],
            "course": "Computer Networks"
        }
    ],
    "references": [
        {
            "name": "Dr. Mohammad Rifat Ahmmad Rashid",
            "title": "Associate Professor",
            "department": "Department of Computer Science & Engineering",
            "institution": "East West University",
            "email": "rifat.rashid@ewubd.edu"
        },
        {
            "name": "Dr. Md Sawkat Ali",
            "title": "Associate Professor",
            "department": "Department of Computer Science & Engineering",
            "institution": "East West University",
            "email": "alim@ewubd.edu"
        },
        {
            "name": "Musharrat Khan",
            "title": "Senior Lecturer",
            "department": "Department of Computer Science & Engineering",
            "institution": "East West University",
            "email": "musharrat.khan@ewubd.edu"
        }
    ],
    "languages": ["Bangla", "English"],
    "hobbies": ["Engaging in data science and analytics", "Traveling", "AI Research", "Technology Innovation"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/portfolio')
def get_portfolio_data():
    return jsonify(PORTFOLIO_DATA)

@app.route('/api/personal-info')
def get_personal_info():
    return jsonify(PORTFOLIO_DATA['personal_info'])

@app.route('/api/education')
def get_education():
    return jsonify(PORTFOLIO_DATA['education'])

@app.route('/api/skills')
def get_skills():
    return jsonify(PORTFOLIO_DATA['skills'])

@app.route('/api/experience')
def get_experience():
    return jsonify(PORTFOLIO_DATA['experience'])

@app.route('/api/publications')
def get_publications():
    return jsonify(PORTFOLIO_DATA['publications'])

@app.route('/api/research-projects')
def get_research_projects():
    return jsonify(PORTFOLIO_DATA['research_projects'])

@app.route('/api/academic-projects')
def get_academic_projects():
    return jsonify(PORTFOLIO_DATA['academic_projects'])

@app.route('/api/references')
def get_references():
    return jsonify(PORTFOLIO_DATA['references'])

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    
    # In a real application, you would save this to a database
    # or send an email notification
    contact_info = {
        "name": data.get('name'),
        "email": data.get('email'),
        "subject": data.get('subject'),
        "message": data.get('message'),
        "timestamp": datetime.now().isoformat()
    }
    
    # Log the contact submission (in production, save to database)
    print(f"New contact submission: {contact_info}")
    
    return jsonify({
        "status": "success",
        "message": "Thank you for your message! I'll get back to you soon."
    })

@app.route('/api/research-project/<int:project_id>')
def get_research_project(project_id):
    if 0 <= project_id < len(PORTFOLIO_DATA['research_projects']):
        project = PORTFOLIO_DATA['research_projects'][project_id]
        project['id'] = project_id
        return jsonify(project)
    return jsonify({"error": "Research project not found"}), 404

@app.route('/api/academic-project/<int:project_id>')
def get_academic_project(project_id):
    if 0 <= project_id < len(PORTFOLIO_DATA['academic_projects']):
        project = PORTFOLIO_DATA['academic_projects'][project_id]
        project['id'] = project_id
        return jsonify(project)
    return jsonify({"error": "Academic project not found"}), 404

@app.route('/api/publication/<int:pub_id>')
def get_publication(pub_id):
    if 0 <= pub_id < len(PORTFOLIO_DATA['publications']):
        publication = PORTFOLIO_DATA['publications'][pub_id]
        publication['id'] = pub_id
        return jsonify(publication)
    return jsonify({"error": "Publication not found"}), 404

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Karib Shams Portfolio API"
    })

# Statistics endpoint
@app.route('/api/stats')
def get_stats():
    return jsonify({
        "total_publications": len(PORTFOLIO_DATA['publications']),
        "total_research_projects": len(PORTFOLIO_DATA['research_projects']),
        "total_academic_projects": len(PORTFOLIO_DATA['academic_projects']),
        "years_of_experience": "2024-Current",
        "current_position": "Graduate Teaching Assistant",
        "education_level": "MSc in CSE (Ongoing)"
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)