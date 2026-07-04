from app.prediction import predict_new_student

from app.recommendation import recommend_student


def generate_guidance(

    student_skill_ids,

    branch_name,

    preferred_role,

    cgpa,

    coding_score,

    dsa_solved,

    projects,

    internships,

    communication_score,

    aptitude_score,

    skill_count

):
    

    prediction = predict_new_student(

    branch_name=branch_name,

    preferred_role=preferred_role,

    cgpa=cgpa,

    coding_score=coding_score,

    dsa_solved=dsa_solved,

    projects=projects,

    internships=internships,

    communication_score=communication_score,

    aptitude_score=aptitude_score,

    skill_count=skill_count

    )


    recommendation = recommend_student(

    student_skill_ids=student_skill_ids,

    branch_name=branch_name,

    preferred_role=preferred_role,

    cgpa=cgpa,

    coding_score=coding_score,

    dsa_solved=dsa_solved,

    projects=projects,

    internships=internships,

    communication_score=communication_score,

    aptitude_score=aptitude_score,

    skill_count=skill_count

    )


    guidance = []

    # Placement Readiness Guidance

    if prediction["PlacementReadiness"] == "Needs Improvement":

        guidance.append(
        "Focus on strengthening your core technical skills before placements."
    )

    elif prediction["PlacementReadiness"] == "Developing":

        guidance.append(
        "You are improving, but there is still room to increase your placement readiness."
    )

    elif prediction["PlacementReadiness"] == "Moderate":

        guidance.append(
        "You are on the right track. Continue improving your skills and projects."
    )

    elif prediction["PlacementReadiness"] == "High":

            guidance.append(
        "You are well prepared for placements. Focus on interview practice and consistency."
    )

    else:

        guidance.append(
        "Excellent placement readiness! Continue practicing interviews and advanced topics."
    )
        
    # CGPA Guidance

    if cgpa < 7.5:

        guidance.append(
        "Improve your CGPA to at least 7.5 to satisfy eligibility criteria of many companies."
    )

    # DSA Solved Guidance

    if dsa_solved < 300:

        guidance.append(
        "Solve more DSA problems. Aim for at least 300–500 solved problems."
    )

    # Projects Guidance

    if projects < 3:

        guidance.append(
        "Build more real-world projects to strengthen your portfolio."
    )

    # Internships Guidance

    if internships == 0:

        guidance.append(
        "Try to complete at least one internship before placement season."
    )

    # Communication Score Guidance

    if communication_score < 70:

        guidance.append(
        "Improve your communication skills through presentations, mock interviews and group discussions."
    )

    # Missing Skills Guidance

    if recommendation["MissingSkills"]:

        guidance.append(

        "Learn these important skills for your recommended role: "

        +

        ", ".join(recommendation["MissingSkills"])

    )

    # Positive Message

    guidance.append(

    f"Your recommended career path is {recommendation['RecommendedRole']}. Stay consistent and keep improving."

    )


    return {

    "PlacementPrediction": prediction["PlacementPrediction"],

    "PlacementProbability": prediction["PlacementProbability"],

    "PlacementReadiness": prediction["PlacementReadiness"],

    "RecommendedRole": recommendation["RecommendedRole"],

    "RecommendationScore": recommendation["RecommendationScore"],

    "Guidance": guidance

    }