import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_DB = {
    "python", "java", "c++", "sql", "fastapi", "flask",
    "machine learning", "deep learning", "nlp",
    "docker", "aws", "git", "linux"
}

def extract_skills(text):
    doc = nlp(text.lower())

    found = set()

    for token in doc:
        if token.text in SKILL_DB:
            found.add(token.text)

    return list(found)