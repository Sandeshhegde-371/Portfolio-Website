from pathlib import Path
import streamlit as st 

from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assests" / "Resume.pdf"
profile_pic = current_dir / "assests" / "Profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sandesh Shrikant Hegde"
PAGE_ICON = ":wave:"
NAME = "Sandesh Shrikant Hegde"

DESCRIPTION = """
I'm an AI/ML undergraduate at The National Institute of Engineering, Mysuru, with a deep passion for building intelligent, data-driven systems. I love working on real-world problems involving NLP, computer vision, and scalable MLOps pipelines. I’ve built end-to-end projects from data wrangling to model deployment, and I’m always eager to learn and contribute to impactful AI applications.
"""
EMAIL = "sandesh.hegde3715@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    
}
ACCOMPLISHMENTS = {
    "🥈 Runner-Up: Innovista Minor Project Expo 2024": "Football Player Analysis",
    "🥉 2nd Runner-Up: Tech Spark State Expo 2025": "Football Player Analysis",
    "🧠 FOSSHACK 2025 -National Level Hackathon": " NLP-Based Text Summarization",
}
CERTIFICATES = {
    "Core Employability Skills": "Wadhwani Foundation",
    "Artificial Intelligence Fundamentals": "IBM",
    "Data Analytics Essentials": " IBM",
    "Data Visualization & Dashboard Essentials": " IBM",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=330)
    # --- SOCIAL LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA)+2)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index+1].write(f"[{platform}]({link})")
    st.write("📫", EMAIL)

with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.header("Experience")
st.write("---")
st.subheader("🧠 Machine Learning Intern – Plasmid Innovations Ltd (May–July 2024)")
st.write(
    """
- Location: Bengaluru, India
- Duration: May – July 2024
- Role: Machine Learning Intern (NLP + Data Analytics)

- ► Built and optimized an NLP-based spam news classifier using TensorFlow and Scikit-learn, improving accuracy to 90% through TF-IDF, word embeddings, and hyperparameter tuning
- ► Designed dynamic Power BI dashboards from SQL/Excel sources to support quarterly planning and resource allocation across departments
- ► Collaborated with cross-functional teams to integrate data pipelines and enhance model traceability, reproducibility, and production-readiness using Git and DVC
"""
)


# --- SKILLS ---
st.write('\n')
st.header("Technical Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python, C, C++, R
- 📊 Data Visulization: PowerBi, MS Excel, Tableau
- 📈 AI/Machine Learning: Scikit-learn, TensorFlow, Keras, Pandas, NumPy
- 📚 Modeling: Classification Models, Regression Models
- 🗄️ Databases: MongoDB, MySQL
- 🛠️ Tools: Git, Jupyter Notebook, VS Code, Anaconda, MLFlow, AWS

"""
)


# --- Projects ---
st.write('\n')
st.write('\n')
st.header("Projects")
st.write("---")

# --- JOB 1
st.subheader("🚧 Spam News Detection System (End-to-End ML Pipeline)")
st.write(
    """
- Tech Stack: Python, Pandas, TensorFlow, Scikit-learn, DVC, AWS S3, Git
- Role: Full-stack ML Developer | Individual Project
- Duration: 1 Month

- Overview : This project involved developing a production-ready machine learning pipeline for detecting spam or fake news articles using NLP techniques and multiple classification algorithms. The system was designed with full traceability, version control, and deployment capabilities.

- Key Features:
- ► Collected and cleaned a labeled dataset of news headlines and bodies.
- ► Used advanced preprocessing (stop-word removal, stemming, vectorization with TF-IDF).
- ► Trained and compared various ML models: SVC, Random Forest, Naive Bayes, XGBoost.
- ► Achieved 97%+ accuracy using SVC, with detailed precision-recall analysis.
- ► Integrated DVC (Data Version Control) for managing dataset and model versions.
- ► Deployed trained model artifacts to AWS S3, using structured logging and exception handling to ensure deployment stability.
"""
)

# --- JOB 2
st.write('\n')
st.write('\n')
st.subheader("🚧 Football Player Analysis using Computer Vision & AI")
st.write(
    """
- Tech Stack: Python, YOLOv8, OpenCV, OCR, MongoDB, FastAPI, Gemini 2.0 Chatbot
- Role: AI Engineer & Full-stack Integrator
- Duration: 2 Months

- Overview : An innovative system to analyze football player performance by processing broadcast match videos. The application leverages YOLOv8 object detection and OCR techniques to track player positions, ball movement, and infer key game events.

- Key Features:
- ► Real-time player detection and tracking using YOLOv8 and OpenCV.
- ► Ball detection, trajectory estimation, and event classification (passes, goals, tackles).
- ► Extracted player stats such as distance covered, time on screen, and zone occupancy.
- ► Built a FastAPI backend to serve detections to the frontend and chatbot engine.
- ► Integrated Gemini 2.0 chatbot for providing summarized coaching insights based on visual stats.
- ► Stored structured player analytics in MongoDB for querying and dashboarding.
"""
)

# --- JOB 3
st.write('\n')
st.write('\n')
st.subheader("🚧 Online Voting System")
st.write(
    """
- Tech Stack: Python, Django, HTML, CSS, MySQL
- Role: SQL Query Optimizer & Backend Developer
- Duration: 3 Weeks

- Overview : A secure, full-stack online voting platform built using Django, designed to streamline election processes with robust access control and real-time vote tracking. Emphasis was placed on backend performance and database efficiency, ensuring the system could scale while maintaining data integrity.

- Key Features:
- ► Developed complex SQL queries for retrieving and aggregating real-time voting data while minimizing latency and ensuring optimal performance.
- ► Refactored inefficient database queries and implemented indexing strategies to improve load times for admin dashboards and result summaries by over 40%.
- ► Prevented double voting using unique vote-tracking logic and user-IP verification.
- ► Delivered a fully functional voting solution with emphasis on database security, efficiency, and real-world scalability.
"""
)

# --- Certifications ---
st.write('\n')
st.header("Certifications")
st.write("---")
for hackathon, project in CERTIFICATES.items():
    st.write(f"{hackathon} : {project}")
    
    
# --- Accomplishments ---
st.write('\n')
st.header("Accomplishments")
st.write("---")
for hackathon, project in ACCOMPLISHMENTS.items():
    st.write(f"{hackathon} : {project}")