import mysql.connector
import pandas as pd

from app.config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)

connection = mysql.connector.connect(

    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME

)

def load_table(table_name):

    query = f"SELECT * FROM {table_name}"

    return pd.read_sql(
        query,
        connection
    )



def get_roles():
    return load_table("Roles")

def get_skills():
    return load_table("Skills")

def get_role_skills():
    return load_table("RoleSkills")

def get_companies():
    return load_table("Companies")

def get_company_roles():
    return load_table("CompanyRoles")

def get_students():
    return load_table("Students")

def get_student_skills():
    return load_table("StudentSkills")

