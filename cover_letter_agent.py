import requests

def generate_cover_letter(name, job_desc, resume_summary):
    prompt = f"""
You are an expert resume and cover letter editor who specializes in FAANG-level applications and high-performing job candidates.

Generate a customized, professional cover letter based on the following details:

🔹 Candidate Name: {name}
🔹 Resume Summary: {resume_summary}
🔹 Job Description: {job_desc}

Guidelines:
- Assume the role is either tech, academic, or business based on the job description automatically.
- Write in a confident, concise, and results-driven tone.
- Match industry standards used at companies like Google, Amazon, Meta, or top-tier startups.
- Include: 
  - Greeting
  - Strong opening hook (1–2 sentences)
  - Brief relevant experience (mapped to job)
  - Matching keywords or technologies from job description
  - Enthusiastic & professional closing

Format:
- Output in plain text
- No markdown, no emojis
- 3–5 short, powerful paragraphs
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            headers={"Content-Type": "application/json"},
            json={
                "model": "llama3",  # Adjust if you're using a different model in Ollama
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            },
            timeout=60
        )
        return response.json().get("message", {}).get("content", "⚠️ No response from model.")
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ----------- Test Run Example -----------
if __name__ == "__main__":
    name = "Ankit"
    job_desc = (
        "We are seeking a backend engineer with experience in Python, REST APIs, and scalable infrastructure. "
        "Experience in cloud deployment, microservices, and databases preferred. Teamwork and agility are a must."
    )
    resume_summary = (
        "Final year EEE student at NITK with a passion for building AI agents and developer tools. "
        "Skilled in Python, API development, and streamlining automation workflows. "
        "Strong foundation in problem-solving and system thinking."
    )

    result = generate_cover_letter(name, job_desc, resume_summary)
    print("\n📄 Generated Cover Letter:\n")
    print(result)
