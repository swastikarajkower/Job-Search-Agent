from duckduckgo_search import DDGS
from datetime import datetime
import pandas as pd

SEARCHES = [
    "Machine Learning Engineer jobs India posted today",
    "AI Engineer jobs India last 24 hours",
    "Python Developer jobs India today",
    "Data Scientist jobs India posted today",
    "Generative AI jobs India today",
    "LLM Engineer jobs India today",
]

def search_jobs():

    jobs = []

    with DDGS() as ddgs:

        for query in SEARCHES:

            results = ddgs.text(
                query,
                max_results=25
            )

            for r in results:

                jobs.append({

                    "title": r["title"],
                    "url": r["href"],
                    "snippet": r["body"],
                    "query": query

                })

    return pd.DataFrame(jobs)
