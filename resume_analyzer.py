print("SMART RESUME SKILL ANALYZER")
print("----------------------------")

resume_text = input("Paste your resume text here:\n")

skills = [
    "python",
    "java",
    "html",
    "css",
    "sql",
    "ai",
    "machine learning",
    "data science",
    "communication"
]

found_skills = []

for skill in skills:
    if skill in resume_text.lower():
        found_skills.append(skill)

print("\nSkills Found in Resume:")
if len(found_skills) == 0:
    print("No skills detected")
else:
    for s in found_skills:
        print("-", s.capitalize())

skill_count = len(found_skills)

print("\nResume Analysis Result:")
if skill_count >= 5:
    print("Resume Strength: EXCELLENT")
elif skill_count >= 3:
    print("Resume Strength: GOOD")
else:
    print("Resume Strength: NEEDS IMPROVEMENT")
    print("Suggestion: Add more technical skills")
