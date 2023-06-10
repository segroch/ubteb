import pandas as pd

def get_centers_from_csv(examCenter):
    df = pd.read_csv(examCenter)
    centers = [(center, center) for center in df['CenterName'].tolist()]
    return centers


def get_districts_from_csv(districts):
    df = pd.read_csv(districts)
    cities = [(district, district) for district in df['District'].tolist()]
    return cities


def get_programs_from_csv(programs):
    df = pd.read_csv(programs)
    courses = [(program, program) for program in df['ProgramName'].tolist()]
    return courses