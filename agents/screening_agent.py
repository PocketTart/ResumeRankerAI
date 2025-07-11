import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

llm = ChatOpenAI(
    model="mistral-medium",
    openai_api_key=os.getenv("MISTRAL_API_KEY"),
    openai_api_base="https://api.mistral.ai/v1",
    temperature=0.3
)

# Prompt Template
feedback_prompt = PromptTemplate.from_template("""
You are an expert HR recruiter.

Given the following job description and a candidate's resume, provide a concise and professional feedback.

Mention:
- Key strengths of the candidate relevant to the JD
- Any major skill gaps or missing experience
- How well the resume matches the JD overall

Job Description:
{jd_text}

Resume:
{resume_text}

Your feedback (1-2 sentences):
""")

# LLM Chain
screening_agent = LLMChain(llm=llm, prompt=feedback_prompt)

# Function to evaluate resume against JD
def evaluate_resume(jd_text: str, resume_text: str) -> str:
    """
    Uses LLM to generate HR feedback comparing resume with JD.
    """
    input_data = {
        "jd_text": jd_text[:2500],        # truncate to keep under token limits
        "resume_text": resume_text[:2500]
    }
    feedback = screening_agent.invoke(input_data)
    return feedback["text"].strip()
