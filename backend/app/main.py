from fastapi import FastAPI

from app.schemas import (

    StudentInput,

    PredictionResponse,

    RecommendationResponse,

    GuidanceResponse

)

from app.prediction import (
    predict_new_student
)

from app.recommendation import (
    recommend_student
)

from app.schemas import (
    RecommendationResponse
)

from app.guidance import (
    generate_guidance
)


app = FastAPI(

    title="Placement Intelligence Platform API",

    description="Backend API for Placement Prediction and Recommendation System",

    version="1.0.0"

)


@app.get("/")
def home():

    return {

        "message": "Placement Intelligence Platform API is Running"

    }


@app.post(

    "/predict",

    response_model=PredictionResponse

)
def predict(

    student: StudentInput

):

    result = predict_new_student(

        branch_name=student.branch_name,

        preferred_role=student.preferred_role,

        cgpa=student.cgpa,

        coding_score=student.coding_score,

        dsa_solved=student.dsa_solved,

        projects=student.projects,

        internships=student.internships,

        communication_score=student.communication_score,

        aptitude_score=student.aptitude_score,

        skill_count=student.skill_count

    )

    return result



@app.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(
    student: StudentInput
):

    student_skill_ids = set(student.skills)

    result = recommend_student(

        student_skill_ids=student_skill_ids,

        branch_name=student.branch_name,

        preferred_role=student.preferred_role,

        cgpa=student.cgpa,

        coding_score=student.coding_score,

        dsa_solved=student.dsa_solved,

        projects=student.projects,

        internships=student.internships,

        communication_score=student.communication_score,

        aptitude_score=student.aptitude_score,

        skill_count=student.skill_count

    )

    return result



@app.post(
    "/guidance",
    response_model=GuidanceResponse
)
def guidance(
    student: StudentInput
):

    student_skill_ids = set(student.skills)

    result = generate_guidance(

        student_skill_ids=student_skill_ids,

        branch_name=student.branch_name,

        preferred_role=student.preferred_role,

        cgpa=student.cgpa,

        coding_score=student.coding_score,

        dsa_solved=student.dsa_solved,

        projects=student.projects,

        internships=student.internships,

        communication_score=student.communication_score,

        aptitude_score=student.aptitude_score,

        skill_count=student.skill_count

    )

    return result