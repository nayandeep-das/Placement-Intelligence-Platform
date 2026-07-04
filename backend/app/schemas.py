from pydantic import BaseModel


class StudentInput(BaseModel):

    branch_name: str

    preferred_role: str

    cgpa: float

    coding_score: int

    dsa_solved: int

    projects: int

    internships: int

    communication_score: int

    aptitude_score: int
    
    skill_count: int

    skills: list[int]

class PredictionResponse(BaseModel):

    Branch: str

    PreferredRole: str

    PlacementPrediction: str

    PlacementProbability: float

    PlacementReadiness: str


class RecommendationResponse(BaseModel):

    RecommendedRole: str

    RecommendationScore: float

    PlacementProbability: float

    SkillMatch: float

    MatchedSkills: list[str]

    MissingSkills: list[str]

    RecommendedCompanies: list[str]


class GuidanceResponse(BaseModel):

    PlacementPrediction: str

    PlacementProbability: float

    PlacementReadiness: str

    RecommendedRole: str

    RecommendationScore: float

    Guidance: list[str]