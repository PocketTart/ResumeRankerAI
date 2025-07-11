import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="mistral-medium",
    openai_api_key=os.getenv("MISTRAL_API_KEY"),
    openai_api_base="https://api.mistral.ai/v1",
    temperature=0.2
)

prompt_template = PromptTemplate(
    input_variables=["jd_text"],
    template="""
You are an HR assistant. Read the job description and **infer** the following:

1. Bullet list of REQUIRED skills  
2. Bullet list of PREFERRED (nice-to-have) skills  

Even if the skills aren't explicitly written, guess based on the responsibilities and context.

Job Description:
---
{jd_text}
---
"""
)


def extract_skills_from_jd(jd_text: str) -> str:
    """
    Extracts skills from a JD using Mistral API via LangChain.
    Returns a clean bullet-format string.
    """
    prompt = prompt_template.format(jd_text=jd_text)
    response = llm.invoke([
        SystemMessage(content="You are an HR assistant skilled in parsing job descriptions."),
        HumanMessage(content=prompt)
    ])
    return response.content
