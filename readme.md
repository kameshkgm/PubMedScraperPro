# 📄 PubMed Pharma Paper Extractor

A command-line tool that fetches research papers from PubMed using a search query, filters papers with pharmaceutical or biotech affiliations, and outputs the results to a CSV file.

---

## 🚀 Installation

1. **Clone this repository**
```bash
git clone https://github.com/kameshkgm/PubMedScraperPro.git
cd pubmed-pharma-extractor
```

2. **Install Poetry**
```bash
# On Windows
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

3. **Set Python Version (Make sure you have Python >= 3.10)**
```bash
poetry env use C:/path/to/your/python3.12/python.exe
```

4. **Install dependencies**
```bash
poetry install
```

---

## 🛠️ Usage

```bash
poetry run get-papers-list --query "cancer drug discovery" --debug --file results.csv
```

### Available Flags

- `-q` or `--query`: PubMed search query (required)
- `-f` or `--file`: Filename to save results to CSV (optional)
- `-d` or `--debug`: Enable debug logging
- `-h` or `--help`: Show usage

---

## 📁 Project Structure

```
.
├── cli.py                 # Command-line interface logic
├── get_papers
│   ├── __init__.py
│   ├── fetch.py           # PubMed fetch functions
│   ├── filter.py          # Data filtering and heuristic logic
│   └── output.py          # CSV writer
├── pyproject.toml         # Poetry project definition
├── README.md              # This file
```

---

## 📦 Packaging & Script Setup

`pyproject.toml` includes this:

```toml
[tool.poetry.scripts]
get-papers-list = "cli:main"
```

Run the script using:

```bash
poetry run get-papers-list --query "your search"
```

---

## 📚 Dependencies

- [Biopython](https://biopython.org/) - To access PubMed via Entrez
- [Pandas](https://pandas.pydata.org/) - Data formatting (optional but used internally)
- [Poetry](https://python-poetry.org/) - Dependency management

---

## 🧠 Built With Help From

- [PubMed API (Entrez)](https://www.ncbi.nlm.nih.gov/books/NBK25499/)

---

## 🧪 To Publish on Test PyPI (Optional Bonus)

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry build
poetry publish -r test-pypi
```

---

## 📜 License

MIT License © Kamesh S