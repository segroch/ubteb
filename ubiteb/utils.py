import pandas as pd

def get_centers_from_csv(examCenter):
    df = pd.read_csv(examCenter)
    centers = [(center, center) for center in df['CenterName'].tolist()]
    return centers
