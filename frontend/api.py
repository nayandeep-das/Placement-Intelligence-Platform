import requests

BASE_URL = "http://127.0.0.1:8000"


def predict_student(student_data):

    response = requests.post(

        f"{BASE_URL}/predict",

        json=student_data

    )

    return response.json()


def recommend_student(student_data):

    response = requests.post(

        f"{BASE_URL}/recommend",

        json=student_data

    )

    return response.json()


def guidance_student(student_data):

    response = requests.post(

        f"{BASE_URL}/guidance",

        json=student_data

    )

    return response.json()