import csv
from rapidfuzz import process
from config import MEDICINE_FILE


def load_medicines():

    meds = []

    with open(MEDICINE_FILE) as f:

        reader = csv.reader(f)

        for r in reader:
            meds.append(r[0].lower())

    return meds


medicine_list = load_medicines()


def detect_medicines(words):

    found = []

    for w in words:

        w = w.lower()

        match, score, _ = process.extractOne(
            w,
            medicine_list
        )

        if score > 70:
            found.append(match)

    return list(set(found))