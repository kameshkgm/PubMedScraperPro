import argparse
from get_papers.fetch import search_pubmed, fetch_paper_details
from get_papers.filter import extract_affiliation_info
from get_papers.output import write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech author affiliations.")
    parser.add_argument("--query", "-q", required=True, help="PubMed search query")
    parser.add_argument("--file", "-f", help="Filename to save CSV results (e.g., results.csv)")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Searching PubMed for query: {args.query}")

    pubmed_ids = search_pubmed(args.query)
    raw_data = fetch_paper_details(pubmed_ids)
    results = extract_affiliation_info(raw_data)

    if not results:
        print("No relevant papers found.")
        return

    if args.file:
        write_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        for row in results:
            print(" | ".join(row))

if __name__ == "__main__":
    main()
