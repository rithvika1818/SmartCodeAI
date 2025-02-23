from openai import Client
import os

# Initialize the OpenAI client
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

def generate_code_suggestion(prompt, model="gpt-3.5-turbo"):
    """
    Uses OpenAI API to generate a code suggestion based on the given prompt.
    """
    response = client.chat_completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an AI coding assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

def detect_bug(code_snippet):
    """
    Dummy function to detect bugs in Python code.
    """
    if "print(" not in code_snippet:
        return "Warning: No print statements found. Consider adding debugging logs."
    return "No obvious issues detected."

def generate_test_cases(function_code):
    """
    Simple logic to generate a unit test for a given function.
    """
    return f"""import unittest

class TestFunction(unittest.TestCase):
    def test_case(self):
        # TODO: Add test cases for:
        {function_code}
        self.assertEqual(1, 1)  # Replace with actual test

if __name__ == '__main__':
    unittest.main()"""

if __name__ == "__main__":
    user_prompt = "Write a Python function to calculate the factorial of a number."
    suggestion = generate_code_suggestion(user_prompt)
    print("Generated Code Suggestion:\n", suggestion)

    bug_check = detect_bug(suggestion)
    print("Bug Detection Report:\n", bug_check)

    test_case = generate_test_cases(suggestion)
    print("Generated Test Cases:\n", test_case)
