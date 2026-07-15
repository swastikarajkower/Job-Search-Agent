from search import search_jobs
from utils import remove_duplicates, save
from ranker import rank_job

print("Searching Internet...")

jobs = search_jobs()

jobs = remove_duplicates(jobs)

analysis = []

for i,row in jobs.iterrows():

    print(f"Ranking {i+1}/{len(jobs)}")

    analysis.append(

        rank_job(row)

    )

jobs["AI Analysis"] = analysis

save(jobs)

print()

print("Finished")

print()

print(jobs.head())
