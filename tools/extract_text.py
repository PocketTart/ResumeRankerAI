import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts and returns plain text from a PDF file using pdfplumber.
    
    Args:
        file_path (str): Path to the PDF file.
    
    Returns:
        str: The extracted plain text.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text.strip()
