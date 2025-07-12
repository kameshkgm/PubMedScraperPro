from Bio import Entrez

Entrez.email = "skameshtamilan@gmail.com" 

def search_pubmed(query: str, max_results: int = 20) -> list[str]:
    with Entrez.esearch(db="pubmed", term=query, retmax=max_results) as handle:
        data = Entrez.read(handle)
    return data.get("IdList", [])

def fetch_paper_details(ids: list[str]) -> str:
    if not ids:
        return ""
    with Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline", retmode="text") as handle:
        return handle.read()
