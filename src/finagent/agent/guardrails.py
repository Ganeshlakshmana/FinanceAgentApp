def basic_input_guardrails(user_input: str) -> None:
    if not user_input or not user_input.strip():
        raise ValueError("Query cannot be empty.")
