import re


class ResumeAnalyzer:

    SKILLS = [
        "Azure",
        "Azure DevOps",
        "AWS",
        "Docker",
        "Kubernetes",
        "AKS",
        "Terraform",
        "Python",
        "Git",
        "GitHub",
        "Linux",
        "Jenkins",
        "Helm",
        "Prometheus",
        "Grafana",
        "SQL",
        "PostgreSQL",
        "FastAPI",
        "Azure Data Factory",
    ]

    @staticmethod
    def analyze(text: str):

        found_skills = []

        text_lower = text.lower()

        for skill in ResumeAnalyzer.SKILLS:
            if skill.lower() in text_lower:
                found_skills.append(skill)

        experience_match = re.search(
            r"(\d+)\+?\s+years",
            text,
            re.IGNORECASE,
        )

        experience = (
            experience_match.group(0)
            if experience_match
            else "Not Found"
        )

        ats_score = min(
            100,
            50 + len(found_skills) * 3,
        )

        recommendations = []

        if ats_score < 80:
            recommendations.append(
                "Add more technical keywords."
            )

        if "certification" not in text_lower:
            recommendations.append(
                "Mention certifications."
            )

        if "achievement" not in text_lower:
            recommendations.append(
                "Include measurable achievements."
            )

        missing_skills = [
            skill
            for skill in ResumeAnalyzer.SKILLS
            if skill not in found_skills
        ]

        return {
            "ats_score": ats_score,
            "experience": experience,
            "skills": found_skills,
            "missing_skills": missing_skills,
            "recommendations": recommendations,
        }