from app.preprocessing import (
    create_features,
    create_input_dataframe
)

from app.config import (
    EXCELLENT_THRESHOLD,
    HIGH_THRESHOLD,
    MODERATE_THRESHOLD,
    DEVELOPING_THRESHOLD
)

from app.utils import (
    load_models,
    load_feature_columns
)


placement_model, scaler, label_encoder = load_models()

feature_columns = load_feature_columns()


def get_placement_readiness(probability):

    if probability >= EXCELLENT_THRESHOLD:
        return "Excellent"

    elif probability >= HIGH_THRESHOLD:
        return "High"

    elif probability >= MODERATE_THRESHOLD:
        return "Moderate"

    elif probability >= DEVELOPING_THRESHOLD:
        return "Developing"

    else:
        return "Needs Improvement"



def predict_new_student(

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

    # Create engineered features
    feature_dict = create_features(

        cgpa=cgpa,
        coding_score=coding_score,
        dsa_solved=dsa_solved,
        projects=projects,
        internships=internships,
        communication_score=communication_score,
        aptitude_score=aptitude_score,
        skill_count=skill_count

    )

    
    input_df = create_input_dataframe(

        feature_dict,
        feature_columns

    )

    
    scaled_input = scaler.transform(
        input_df
    )

    
    prediction = placement_model.predict(
        scaled_input
    )[0]

    prediction_label = label_encoder.inverse_transform(
        [prediction]
    )[0]

    # Predict probability
    probabilities = placement_model.predict_proba(
        scaled_input
    )[0]

    placement_probability = round(
        probabilities[1] * 100,
        2
    )

    
    placement_readiness = get_placement_readiness(
        placement_probability
    )

    
    return {

        "Branch": branch_name,
        "PreferredRole": preferred_role,
        "PlacementPrediction": prediction_label,
        "PlacementProbability": placement_probability,
        "PlacementReadiness": placement_readiness

    }

