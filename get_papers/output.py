import csv
from typing import List, Tuple

def write_to_csv(data: List[Tuple[str, str, str, str, str]], filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PubmedID", "Title", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
        writer.writerows(data)
