# ResumeRanker AI - Intelligent Resume Screening System

**ResumeRanker AI** is a smart and modular resume screening tool designed to streamline candidate evaluation based on job descriptions (JD). Using NLP and optional LLM-powered insights, it ranks resumes by relevance, provides feedback, and generates a downloadable leaderboard — all through an interactive web UI.

---

## 🔍 Project Highlights

- Developed with **Streamlit** for a seamless web interface
- Uses **TF-IDF / keyword matching** for skill-based scoring
- Integrates **LLM (e.g., Mistral/OpenAI)** for enhanced JD understanding
- Generates detailed **feedback for each candidate**
- Ranks resumes using a **priority queue system**
- Allows **CSV export** of final leaderboard

---

## ✨ Key Features

- Job description analysis with LLM-based skill extraction
- Resume text extraction from uploaded PDFs
- Matching and scoring using NLP overlap or transformer-based embeddings
- Feedback generation using custom logic or LLMs
- Leaderboard view with scores and candidate insights
- Modular architecture with reusable agents and tools

---

## 📁 Project Structure
ResumeRankerAI/
├── app.py # Main Streamlit application
├── requirements.txt # Required Python dependencies
├── sample_data/ # Example resumes and job descriptions
├── output/
│ └── results.csv # Final leaderboard (generated)
│
├── agents/
│ ├── jd_agent.py # Extracts key skills from JD using LLM
│ └── screening_agent.py # Provides feedback and scores for resumes
│
├── tools/
│ ├── extract_text.py # PDF to raw text converter
│ └── nlp_matcher.py # Skill-matching logic (TF-IDF / keywords)
│
├── utils/
│ ├── leaderboard.py # Builds ranked leaderboard
│ └── preprocess.py # Text preprocessing functions

yaml
Copy
Edit

---
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PocketTart/ResumeRankerAI.git
cd ResumeRankerAI
2. Set Up Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # or .\venv\Scripts\activate on Windows

pip install -r requirements.txt
3. Configure API Key (Optional)
To use LLM-based JD skill extraction and resume evaluation:

bash
Copy
Edit
# .env file (in root directory)
MISTRAL_API_KEY=your_key_here
MISTRAL_API_BASE=https://api.mistral.ai/v1
🚀 Run the Application
bash
Copy
Edit
streamlit run app.py
Then open your browser at http://localhost:8501

🧪 Sample Workflow
Upload a Job Description (PDF)

Upload multiple candidate resumes (PDFs)

The app extracts text, evaluates matches, ranks candidates, and shows:

Name

Score (relevance to JD)

Feedback

Download the full leaderboard as CSV



📌 Dependencies
streamlit

pdfplumber

scikit-learn

python-dotenv

openai 

nltk

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributions
Contributions are welcome. Feel free to open issues or pull requests for enhancements, bug fixes, or new features.


Copy
Edit

---