import csv
from config import INTERACTION_FILE


def check_interactions(meds):

    warnings = []

    with open(INTERACTION_FILE) as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["drug1"].lower() in meds and row["drug2"].lower() in meds:

                warnings.append(
                    f"{row['drug1']} + {row['drug2']} risk: {row['risk']}"
                )

    return warnings