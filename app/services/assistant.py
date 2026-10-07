from app.data.knowledge_base import knowledge_base


def find_solution(question: str):

    question = question.lower()

    for error_code, problem in knowledge_base.items():

        for keyword in problem["keywords"]:

            if keyword in question:

                return {
                    "error_code": error_code,
                    "problem": problem["title"],
                    "solution": problem["solution"]
                }

    return {
        "error_code": None,
        "problem": "Unknown",
        "solution": "I couldn't identify the problem."
    }