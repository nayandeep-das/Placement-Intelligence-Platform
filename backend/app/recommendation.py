from app.database import (

    get_roles,
    get_skills,
    get_role_skills,
    get_companies,
    get_company_roles,
    get_student_skills

)

from app.config import (
    SKILL_MATCH_WEIGHT,
    PLACEMENT_WEIGHT,
    PREFERRED_ROLE_WEIGHT,
    BRANCH_WEIGHT
)

from app.prediction import (
    predict_new_student
)

BRANCH_ROLE_MAPPING = {

    "Computer Science and Engineering": [
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
        "Technology Consultant",
        "Consultant",
        "Risk Analyst",
        "Quant Analyst",
        "Network Engineer",
        "Cybersecurity Engineer"
    ],

    "Mechanical Engineering": [
        "Mechanical Engineer",
        "Design Engineer",
        "Production Engineer",
        "Process Engineer",
        "Project Engineer"
    ],

    "Electrical Engineering": [
        "Electrical Engineer",
        "Embedded Engineer",
        "Firmware Engineer"
    ],

    "Civil Engineering": [
        "Civil Engineer"
    ],

    "Chemical Engineering": [
        "Chemical Engineer"
    ],

    "Metallurgical Engineering": [
        "Metallurgical Engineer"
    ]
}

# Load tables from the database

roles_df = get_roles()

skills_df = get_skills()

role_skills_df = get_role_skills()

companies_df = get_companies()

company_roles_df = get_company_roles()

student_skills_df = get_student_skills()


# Skill Lookup Dictionary

skill_lookup = dict(
    zip(
        skills_df["SkillID"],
        skills_df["SkillName"]
    )
)


def calculate_skill_match(
    student_skill_ids,
    role_skill_ids
):

    if not role_skill_ids:

        return {

            "SkillMatch": 0.0,

            "MatchedSkills": [],

            "MissingSkills": []

        }
    
    matched_skill_ids = (
        student_skill_ids.intersection(
            role_skill_ids
        )
    )

    missing_skill_ids = (
        role_skill_ids.difference(
            student_skill_ids
        )
    )

    matched_skills = [

        skill_lookup[skill_id]

        for skill_id in matched_skill_ids

    ]

    missing_skills = [

        skill_lookup[skill_id]

        for skill_id in missing_skill_ids

    ]

    skill_match = (

        len(matched_skill_ids)
        /
        len(role_skill_ids)

    ) * 100

    skill_match = round(
        skill_match,
        2
    )

    return {

        "SkillMatch": skill_match,

        "MatchedSkills": matched_skills,

        "MissingSkills": missing_skills

    }


def recommend_role(
    student_skill_ids,
    branch_name,
    preferred_role,
    placement_probability
):

    best_role = None

    best_match = -1

    best_result = None

    for role_id in roles_df["RoleID"]:

        role_skill_ids = set(

            role_skills_df[
                role_skills_df["RoleID"] == role_id
            ]["SkillID"]

        )

        
        if not role_skill_ids:
            continue

        
        role_name = roles_df.loc[

            roles_df["RoleID"] == role_id,

            "RoleName"

        ].iloc[0]

        
        result = calculate_skill_match(

            student_skill_ids,

            role_skill_ids

        )

        
        preferred_role_score = (

            100

            if role_name == preferred_role

            else 0

        )

        
        branch_score = (

            100

            if role_name in BRANCH_ROLE_MAPPING.get(
                branch_name,
                []
            )

            else 0

        )

        
        final_score = (

            result["SkillMatch"] * SKILL_MATCH_WEIGHT

            +

            placement_probability * PLACEMENT_WEIGHT

            +

            preferred_role_score * PREFERRED_ROLE_WEIGHT

            +

            branch_score * BRANCH_WEIGHT

        )

        final_score = round(
            final_score,
            2
        )

        
        if final_score > best_match:

            best_match = final_score

            best_result = result

            best_role = role_name

    return {

        "RecommendedRole": best_role,

        "RecommendationScore": best_match,

        **best_result

    }


def recommend_company(role_name):

    
    role_id = roles_df.loc[
        roles_df["RoleName"] == role_name,
        "RoleID"
    ].iloc[0]

    
    company_ids = company_roles_df[
        company_roles_df["RoleID"] == role_id
    ]["CompanyID"]

    
    recommended_companies = companies_df[
        companies_df["CompanyID"].isin(company_ids)
    ]["CompanyName"].tolist()

    return recommended_companies


def recommend_student(

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

    prediction_result = predict_new_student(

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

    placement_probability = prediction_result[
    "PlacementProbability"
    ]

    role_result = recommend_role(

    student_skill_ids,

    branch_name,

    preferred_role,

    placement_probability

    )

    recommended_companies = recommend_company(
        role_result["RecommendedRole"]
    )

    return {

    "RecommendedRole": role_result["RecommendedRole"],

    "RecommendationScore": role_result["RecommendationScore"],

    "PlacementProbability": placement_probability,

    "SkillMatch": role_result["SkillMatch"],

    "MatchedSkills": role_result["MatchedSkills"],

    "MissingSkills": role_result["MissingSkills"],

    "RecommendedCompanies": recommended_companies[:5]

    }