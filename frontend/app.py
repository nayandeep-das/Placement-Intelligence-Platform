import streamlit as st

from api import (
    predict_student,
    recommend_student,
    guidance_student
)


st.set_page_config(

    page_title="Placement Intelligence Platform",

    page_icon="🎓",

    layout="wide",

    initial_sidebar_state="expanded"

)

st.title(
    "🎓 Placement Intelligence Platform"
)

st.markdown(
    "### AI-Powered Placement Prediction and Career Recommendation System"
)

st.divider()

with st.sidebar:

    st.header("About")

    st.write(
        """
        This application uses Machine Learning to predict placement chances,
        recommend suitable career roles, and provide personalized guidance
        based on a student's profile.
        """
    )

    st.divider()

    st.info(
        "Developed using FastAPI, Streamlit, Scikit-Learn, and MySQL."
    )

st.header(
    "👤 Student Information"
)

col1, col2 = st.columns(2)

with col1:

    branch_name = st.selectbox(

        "Branch",

        [

            "Computer Science and Engineering",

            "Information Technology",

            "Electronics and Communication Engineering",

            "Electrical Engineering",

            "Mechanical Engineering",

            "Civil Engineering",

            "Chemical Engineering",

            "Metallurgical Engineering"

        ]

    )

    preferred_role = st.selectbox(

    "Preferred Role",

    [

        "Software Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Machine Learning Engineer",
        "Data Scientist",
        "AI Engineer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Database Engineer",
        "QA Engineer",
        "Data Analyst",
        "Business Analyst",
        "BI Analyst",
        "Embedded Engineer",
        "Firmware Engineer",
        "VLSI Engineer",
        "Hardware Engineer",
        "Mechanical Engineer",
        "Electrical Engineer",
        "Civil Engineer",
        "Chemical Engineer",
        "Metallurgical Engineer",
        "Production Engineer",
        "Process Engineer",
        "Project Engineer",
        "Design Engineer",
        "Research Associate",
        "Research Engineer",
        "Technology Consultant",
        "Consultant",
        "Risk Analyst",
        "Quant Analyst",
        "Network Engineer",
        "Cybersecurity Engineer",
        "Management Trainee"

        ]

    )

    cgpa = st.number_input(

        "CGPA",

        min_value=0.0,

        max_value=10.0,

        value=8.0,

        step=0.1

    )

    coding_score = st.number_input(

        "Coding Score",

        min_value=0,

        max_value=100,

        value=70

    )

    dsa_solved = st.number_input(

        "DSA Problems Solved",

        min_value=0,

        value=200

    )

with col2:

    projects = st.number_input(

        "Projects",

        min_value=0,

        value=2

    )

    internships = st.number_input(

        "Internships",

        min_value=0,

        value=1

    )

    communication_score = st.number_input(

        "Communication Score",

        min_value=0,

        max_value=100,

        value=75

    )

    aptitude_score = st.number_input(

        "Aptitude Score",

        min_value=0,

        max_value=100,

        value=75

    )

SKILLS_BY_CATEGORY = {

    "Programming": {
        "Python": 1,
        "Java": 2,
        "C": 3,
        "C++": 4,
        "JavaScript": 5,
        "Git": 7,
        "GitHub": 8,
        "Object Oriented Programming": 9,
        "Data Structures & Algorithms": 10
    },

    "Web Development": {
        "HTML": 11,
        "CSS": 12,
        "Bootstrap": 13,
        "React": 14,
        "Node.js": 15,
        "Express.js": 16,
        "REST APIs": 17
    },

    "Database": {
        "SQL": 6,
        "MySQL": 18,
        "MongoDB": 19,
        "Database Design": 20,
        "SQL Optimization": 21
    },

    "Data Science": {
        "Pandas": 22,
        "NumPy": 23,
        "Scikit-Learn": 24,
        "TensorFlow": 25,
        "PyTorch": 26,
        "Machine Learning": 27,
        "Deep Learning": 28,
        "Natural Language Processing": 29,
        "Computer Vision": 30,
        "Data Visualization": 31,
        "Feature Engineering": 32,
        "Model Evaluation": 33
    },

    "Cloud": {
        "AWS": 34,
        "Azure": 35,
        "Google Cloud": 36,
        "Docker": 37,
        "Kubernetes": 38,
        "Linux": 39,
        "CI/CD": 40
    },

    "Networking": {
        "Computer Networks": 41,
        "Cyber Security": 42,
        "Network Security": 43,
        "Ethical Hacking": 44,
        "Cryptography": 45
    },

    "Electronics": {
        "Embedded Systems": 46,
        "Microcontrollers": 47,
        "PCB Design": 48,
        "Digital Electronics": 49,
        "Analog Electronics": 50,
        "VLSI": 51,
        "Verilog": 52,
        "FPGA": 53,
        "Signal Processing": 54
    },

    "Electrical": {
        "Power Systems": 55,
        "Control Systems": 56,
        "Electrical Machines": 57,
        "MATLAB": 58,
        "PLC": 59
    },

    "Mechanical": {
        "CAD": 60,
        "SolidWorks": 61,
        "AutoCAD": 62,
        "CATIA": 63,
        "ANSYS": 64,
        "GD&T": 65,
        "Thermodynamics": 66,
        "Manufacturing Processes": 67
    },

    "Civil": {
        "Structural Design": 68,
        "Surveying": 69,
        "STAAD Pro": 70,
        "ETABS": 71,
        "Construction Management": 72
    },

    "Chemical": {
        "Process Design": 73,
        "Process Simulation": 74,
        "Heat Transfer": 75,
        "Mass Transfer": 76,
        "Chemical Reaction Engineering": 77
    },

    "Metallurgy": {
        "Material Science": 78,
        "Heat Treatment": 79,
        "Failure Analysis": 80
    },

    "Biotechnology": {
        "PCR": 81,
        "Cell Culture": 82,
        "Bioinformatics": 83,
        "Genetics": 84,
        "Molecular Biology": 85
    },

    "Soft Skills": {
        "Communication": 86,
        "Leadership": 87,
        "Teamwork": 88,
        "Problem Solving": 89,
        "Critical Thinking": 90,
        "Presentation Skills": 91,
        "Time Management": 92
    }

}

st.subheader("🛠 Technical Skills")

selected_skills = []

for category, skills in SKILLS_BY_CATEGORY.items():

    st.markdown(f"#### {category}")

    selected = st.multiselect(

        f"Select {category} Skills",

        list(skills.keys()),

        key=category

    )

    selected_skills.extend(selected)

student_skill_ids = []

for skill in selected_skills:

    for skills in SKILLS_BY_CATEGORY.values():

        if skill in skills:

            student_skill_ids.append(skills[skill])

            break

skill_count = len(student_skill_ids)

analyze = st.button(

    "🚀 Analyze Placement Profile",

    use_container_width=True,

    type="primary"

)

if analyze:

    student_data = {

    "branch_name": branch_name,

    "preferred_role": preferred_role,

    "cgpa": cgpa,

    "coding_score": coding_score,

    "dsa_solved": dsa_solved,

    "projects": projects,

    "internships": internships,

    "communication_score": communication_score,

    "aptitude_score": aptitude_score,

    "skill_count": skill_count,

    "skills": student_skill_ids

    }

    
    
    prediction = predict_student(
        student_data
    )

    recommendation = recommend_student(
        student_data
    )

    guidance = guidance_student(
        student_data
    )

    st.divider()

    st.header(
    "📊 Analysis Results"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader(
        "🎯 Prediction"
    )

        st.metric(

        "Placement Probability",

        f"{prediction['PlacementProbability']}%"

    )   
        
        st.progress(

            prediction["PlacementProbability"] / 100

    )

        st.metric(

        "Placement Status",

        prediction["PlacementPrediction"]

    )

        st.metric(

        "Readiness",

        prediction["PlacementReadiness"]

    )

        readiness = prediction["PlacementReadiness"]

        if readiness == "High":
            st.success("🟢 High Placement Readiness")

        elif readiness == "Moderate":
            st.info("🔵 Moderate Placement Readiness")

        elif readiness == "Developing":
            st.warning("🟡 Developing Placement Readiness")

        else:
            st.error("🔴 Needs Improvement")

    with col2:

        st.subheader(
        "💼 Recommendation"
    )

        st.metric(

        "Recommended Role",

        recommendation["RecommendedRole"]

    )

        st.metric(

        "Recommendation Score",

        f"{recommendation['RecommendationScore']}%"

    )
        st.progress(
        
        recommendation["RecommendationScore"] / 100
    )
        
    with col3:

        st.subheader("🏢 Recommended Companies")

        for company in recommendation["RecommendedCompanies"]:

            st.success(company)

    st.divider()

    st.header("💡 Personalized Guidance")

    for advice in guidance["Guidance"]:
        st.info(advice)




