# Job-Search-Agent
# 🤖 AI Job Search Agent

An AI-powered job search agent that searches the internet for recently posted AI/ML-related job opportunities, collects relevant information, removes duplicate listings, and exports the results to a CSV file.

This project was developed as part of the **Summer PEP (Professional Enhancement Program) Assignment** for the **AI & ML Cohort**.

---

## 📌 Project Overview

The AI Job Search Agent automates the process of discovering newly posted job opportunities by searching multiple web queries related to AI, Machine Learning, Data Science, and Python development.

The agent:
- Searches the web for relevant job postings.
- Collects job titles, links, and descriptions.
- Removes duplicate results.
- Stores the final dataset in CSV format.
- (Optional) Uses an LLM to rank and analyze jobs based on relevance.

---

## 🚀 Features

- 🔍 Automated internet-based job search
- 📅 Focus on recently posted jobs
- 📄 Extracts:
  - Job Title
  - Job URL
  - Job Description/Snippet
- 🧹 Duplicate removal
- 📊 CSV export for further analysis
- 🤖 Optional AI-powered job ranking

---

## 🛠️ Tech Stack

- Python
- DuckDuckGo Search API (`duckduckgo-search`)
- Pandas
- OpenAI API *(optional for AI ranking)*
- python-dotenv

---

## 📂 Project Structure

```
job-agent/
│
├── agent.py          # Main program
├── search.py         # Searches jobs from the internet
├── ranker.py         # AI-based job ranking (optional)
├── utils.py          # Helper functions
├── jobs.csv          # Generated output
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Job-Search-Agent.git

cd AI-Job-Search-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install duckduckgo-search
pip install pandas
pip install openai
pip install python-dotenv
```

---

## ▶️ Usage

Run the agent using:

```bash
python agent.py
```

The agent will:

1. Search the internet using predefined job-related queries.
2. Collect job information.
3. Remove duplicate entries.
4. Rank jobs (optional).
5. Generate a `jobs.csv` file containing the results.

---

## 📄 Sample Output

| Title | URL | Description |
|-------|-----|-------------|
| Machine Learning Engineer | https://... | Job summary... |
| AI Engineer | https://... | Job summary... |
| Python Developer | https://... | Job summary... |

---

## 📈 Future Enhancements

- Resume-based job matching
- Semantic search using embeddings
- Email notifications
- Daily scheduled job search
- Support for additional job portals
- Interactive web dashboard
- SQLite/PostgreSQL database integration
- AI-generated job recommendations

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python programming
- AI agent workflow design
- Web search automation
- Data collection and processing
- CSV data generation
- Modular software development
- Optional LLM integration

---

## 📚 Academic Context

This project was completed as part of the **Summer Professional Enhancement Program (PEP)** for the **AI & ML Cohort** to explore the development of intelligent automation agents using Python.

---

## 👩‍💻 Author

**Swastika Raj Kower**

MCA (Hons.) – Artificial Intelligence & Machine Learning

GitHub: https://github.com/swastikarajkower


---

## 📜 License

This project is intended for educational and learning purposes.
