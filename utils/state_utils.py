def initial_state(message, success_criteria):
    return {
        "messages": message,
        "success_criteria": success_criteria or "The answer should be clear and accurate",
        "feedback_on_work": None,
        "success_criteria_met": False,
        "user_input_needed": False
    }
