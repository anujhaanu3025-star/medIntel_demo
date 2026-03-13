import requests


def explain_medicine(name):

    prompt = f"""
    Explain medicine {name} in simple language.
    Include use, dose, warning.
    """

    # fake response for hackathon
    # replace with API later

    return f"{name} is commonly used medicine. Take as prescribed."