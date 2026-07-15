from openai import OpenAI

client = OpenAI()

SYSTEM = """
You are a career coach.

Given a job posting,
return only

Score : 1-10

Reason :

Skills Required :
"""

def rank_job(job):

    prompt = f"""

Title:
{job['title']}

Description:

{job['snippet']}

"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role":"system",
                "content":SYSTEM
            },

            {
                "role":"user",
                "content":prompt
            }

        ]

    )

    return response.choices[0].message.content
