import re
from typing import List, Tuple

def extract_affiliation_info(text: str) -> List[Tuple[str, str, str, str, str]]:
    entries = text.strip().split("\n\n")
    filtered_papers = []

    for entry in entries:
        pubmed_id = re.search(r"PMID-\s*(\d+)", entry)
        title = re.search(r"TI\s+-\s+(.+)", entry)
        authors = re.findall(r"FAU - (.+)", entry)
        affiliations = re.findall(r"AD  - (.+)", entry)
        email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", entry)

        company_affils = [aff for aff in affiliations if any(keyword in aff.lower() for keyword in ["pharma", "biotech", "inc", "ltd", "corp", "llc"])]

        if company_affils:
            filtered_papers.append((
                pubmed_id.group(1) if pubmed_id else "N/A",
                title.group(1) if title else "N/A",
                ", ".join(authors),
                ", ".join(company_affils),
                email.group(0) if email else "N/A"
            ))
    return filtered_papers
