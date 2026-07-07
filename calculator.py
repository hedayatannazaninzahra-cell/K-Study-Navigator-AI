def calculate_score(gpa, ielts, korean, projects):

    academic = (gpa / 20) * 40

    language = (
        (ielts / 9) * 30
        +
        (korean / 6) * 20
    )

    portfolio = min(projects * 2, 10)

    total = academic + language + portfolio


    if total >= 85:
        level = "Excellent Candidate ⭐"

    elif total >= 70:
        level = "Strong Candidate 👍"

    else:
        level = "Needs Improvement 📚"


    return {
        "score": round(total, 2),
        "level": level
    }