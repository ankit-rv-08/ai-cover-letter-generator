
# 📝 Cover Letter Generator AI

An AI-powered agent that auto-generates personalized cover letters using your resume summary and job descriptions. Powered by the **LLaMA model via Ollama API**, this tool is perfect for job seekers who want fast, tailored cover letters.

---

## 🚀 Features

- 🔍 **Summarizes your resume & job description**
- ✍️ **Generates a professional cover letter using LLaMA**
- 🧠 Runs locally via [Ollama](https://ollama.com/) — no OpenAI key required
- 📄 Simple terminal output (future: export to .txt or .pdf)
- 💻 Minimal setup with Python 3.10+

---

## 🧰 Tech Stack

- Python 3.10+
- Ollama (LLaMA model)
- `requests` library

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cover_letter_ai.git
cd cover_letter_ai
2. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install and Run Ollama
Make sure Ollama is installed from https://ollama.com

Then, in a separate terminal, run:

bash
Copy
Edit
ollama run llama3
Leave this running — it serves the local LLaMA model at http://localhost:11434

🧪 Usage
1. Modify cover_letter_agent.py
Fill in the sample details:

python
Copy
Edit
name = "John Doe"
job_desc = "We are looking for a software engineer who is passionate about AI..."
resume_summary = "I am a final-year BTech student at NITK with experience in Python, GPT, and AI tools..."
2. Run the Script
bash
Copy
Edit
python cover_letter_agent.py
✅ Output:
Your cover letter will be generated and printed in the terminal:

plaintext
Copy
Edit
📄 Generated Cover Letter:

Dear Hiring Manager...
📄 Sample Output
Dear Hiring Manager,
I am excited to apply for the Software Engineer role. With a strong background in Python, GPT-based tools, and practical AI applications...

🧠 Future Improvements
 Streamlit UI to allow user input and file download

 Export as .txt or .pdf

 Save output history

 Add language/tone options

📜 License
MIT License
© 2024 Ankit R.V. — All rights reserved.

👤 Author
Ankit R.V.
GitHub: @ankit-rv-08
Email: ankith8804@gmail.com
