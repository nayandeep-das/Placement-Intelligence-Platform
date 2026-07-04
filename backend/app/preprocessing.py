import pandas as pd

from app.config import (
    MAX_DSA_SOLVED,
    MAX_SKILL_COUNT
)


def create_features(

    cgpa,
    coding_score,
    dsa_solved,
    projects,
    internships,
    communication_score,
    aptitude_score,
    skill_count

):

    technical_score = (
        0.4 * coding_score +
        0.4 * (dsa_solved / MAX_DSA_SOLVED * 100) +
        0.2 * (skill_count / MAX_SKILL_COUNT * 100)
    )

    academic_score = (
        0.7 * (cgpa * 10) +
        0.3 * aptitude_score
    )

    experience_score = (
        projects +
        internships
    )

    overall_score = (
        0.4 * technical_score +
        0.4 * academic_score +
        0.2 * communication_score
    )

    return {

        "CGPA": cgpa,
        "CodingScore": coding_score,
        "DSASolved": dsa_solved,
        "Projects": projects,
        "Internships": internships,
        "CommunicationScore": communication_score,
        "AptitudeScore": aptitude_score,
        "SkillCount": skill_count,
        "TechnicalScore": technical_score,
        "AcademicScore": academic_score,
        "ExperienceScore": experience_score,
        "OverallScore": overall_score

    }


def create_input_dataframe(

    feature_dict,
    feature_columns

):

    input_df = pd.DataFrame([feature_dict])

    input_df = input_df[
        feature_columns
    ]

    return input_df