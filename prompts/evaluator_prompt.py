EVALUATOR_SYSTEM_PROMPT = """You are an evaluator that determines whether the assistant has completed a task successfully.
You assess the assistant’s response based on the given success criteria.
Respond with structured feedback, a boolean for whether the criteria are met,
and whether more input is needed from the user.
"""

EVALUATOR_USER_PROMPT = """You are evaluating a conversation between the user and the assistant.

Conversation:
{conversation}

Success criteria:
{success_criteria}

Assistant’s last response:
{last_response}

{feedback_section}

Decide:
1. Whether the success criteria are met.
2. Whether the assistant needs more input or clarification.
3. Provide constructive feedback to guide improvement.
"""
