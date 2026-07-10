import streamlit as st
import pdfplumber


# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Resume Job Matching System",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Resume Job Matching System")
st.write("Upload a resume and compare it with a job description.")


# ----------------------------------
# Function to Extract PDF Text
# ----------------------------------

def extract_resume_text(pdf_file):

    text = ""

    if pdf_file is not None:

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    return text



# ----------------------------------
# Function to Extract Skills
# ----------------------------------

def extract_skills(text):

    skills_database = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",

        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",

        "TensorFlow",
        "Keras",
        "Scikit-learn",

        "Pandas",
        "NumPy",

        "Matplotlib",
        "Seaborn",

        "OpenCV",
        "YOLO",
        "YOLOv8",

        "Power BI",
        "DAX",

        "MLflow",
        "Optuna",

        "Git",
        "GitHub",

        "Flask",
        "Streamlit",

        "Roboflow",

        "NLP",
        "Computer Vision"

    ]


    found = []


    for skill in skills_database:

        if skill.lower() in text.lower():

            found.append(skill)


    return list(set(found))



# ----------------------------------
# Upload Resume
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)



# ----------------------------------
# Job Description
# ----------------------------------

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the Job Description Here",
    height=250
)



# ----------------------------------
# Resume Processing
# ----------------------------------

resume_text = ""

resume_skills = []


if uploaded_file is not None:

    resume_text = extract_resume_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")


    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )


    resume_skills = extract_skills(resume_text)



# ----------------------------------
# Skill Matching
# ----------------------------------

job_skills = extract_skills(job_description)



matching_skills = list(
    set(resume_skills).intersection(job_skills)
)


missing_skills = list(
    set(job_skills) - set(resume_skills)
)



# ----------------------------------
# Display Skills
# ----------------------------------

if uploaded_file is not None:


    st.subheader("✅ Resume Skills")

    st.write(resume_skills)


    st.subheader("💼 Job Skills")

    st.write(job_skills)


    st.subheader("🎯 Matching Skills")

    st.success(matching_skills)


    st.subheader("❌ Missing Skills")

    st.warning(missing_skills)



    # ----------------------------------
    # Skill Match Percentage
    # ----------------------------------

    if len(job_skills) > 0:

        skill_match = (
            len(matching_skills) /
            len(job_skills)
        ) * 100

    else:

        skill_match = 0



    st.subheader("📊 Skill Match Percentage")


    st.progress(
        skill_match / 100
    )


    st.success(
        f"{skill_match:.2f}% Skills Matched"
    )



    # ----------------------------------
    # Candidate Evaluation
    # ----------------------------------

    st.subheader("🤖 Candidate Evaluation")


    if skill_match >= 85:

        st.success(
            "⭐⭐⭐⭐⭐ Excellent Match"
        )

        st.write(
            "The candidate is highly suitable for this job."
        )


    elif skill_match >= 70:

        st.info(
            "⭐⭐⭐⭐ Good Match"
        )

        st.write(
            "The candidate meets most required skills."
        )


    elif skill_match >= 50:

        st.warning(
            "⭐⭐⭐ Average Match"
        )

        st.write(
            "The candidate partially satisfies requirements."
        )


    else:

        st.error(
            "⭐ Poor Match"
        )

        st.write(
            "Candidate needs additional skills."
        )



    # ----------------------------------
    # Recruiter Dashboard
    # ----------------------------------

    st.subheader("📊 Recruiter Dashboard")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Resume Skills",
            len(resume_skills)
        )


    with col2:

        st.metric(
            "Matched Skills",
            len(matching_skills)
        )


    with col3:

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )



    # ----------------------------------
    # Download Report
    # ----------------------------------

    report = f"""

Resume Screening Report


Resume Skills:
{', '.join(resume_skills)}


Job Skills:
{', '.join(job_skills)}


Matching Skills:
{', '.join(matching_skills)}


Missing Skills:
{', '.join(missing_skills)}


Skill Match Percentage:
{skill_match:.2f}%

"""


    st.download_button(

        "📥 Download Screening Report",

        report,

        file_name="resume_screening_report.txt"

    )