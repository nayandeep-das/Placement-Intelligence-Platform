import os
import joblib

MODEL_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models"
)


def load_models():

    placement_model = joblib.load(
        os.path.join(
            MODEL_DIR,
            "placement_model.pkl"
        )
    )

    scaler = joblib.load(
        os.path.join(
            MODEL_DIR,
            "scaler.pkl"
        )
    )

    label_encoder = joblib.load(
        os.path.join(
            MODEL_DIR,
            "label_encoder.pkl"
        )
    )

    return (
        placement_model,
        scaler,
        label_encoder
    )


def load_feature_columns():

    return [

        "CGPA",
        "CodingScore",
        "DSASolved",
        "Projects",
        "Internships",
        "CommunicationScore",
        "AptitudeScore",
        "SkillCount",
        "TechnicalScore",
        "AcademicScore",
        "ExperienceScore",
        "OverallScore"

    ]