import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "fastapi",
    "tensorflow",
    "pytorch",
    "docker",
    "postgresql",
    "c++",
    "java",
    "html",
    "css",
    "javascript",
    "mysql",
    "flask",
    "git",
    "github"
]

def extract_skills(text):

    found = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found.append(skill)

    return found