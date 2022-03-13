from typing import Any, List, Optional

from pydantic import BaseModel


class DataInputSchema(BaseModel):
    city: Optional[str]
    city_development_index: Optional[float]
    gender: Optional[str]
    relevent_experience: Optional[str]
    enrolled_university: Optional[str]
    education_level: Optional[str]
    major_discipline: Optional[str]
    experience: Optional[str]
    company_size: Optional[str]
    company_type: Optional[str]
    last_new_job: Optional[str]
    training_hours: Optional[int]


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "city": "city_41",
                        "city_development_index": 0.8270000000000001,
                        "gender": "Male",
                        "relevent_experience": "Has relevent experience",
                        "enrolled_university": "Full time course",
                        "education_level": "Graduate",
                        "major_discipline": "STEM",
                        "experience": "9",
                        "company_size": "<10",
                        "company_type": "Funded Startup",
                        "last_new_job": "1",
                        "training_hours": 21
                    }
                ]
            }
        }