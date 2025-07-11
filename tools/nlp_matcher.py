import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def clean_text(text: str) -> str:
    """
    Lowercase, remove special chars, and normalize whitespace.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def match_resume_to_jd(resume_text: str, jd_skills_text: str) -> float:
    """
    Returns cosine similarity between resume and JD skill descriptions.
    """
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_skills_text)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_clean, resume_clean])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(float(similarity[0][0]), 2)
