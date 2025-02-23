# SmartCodeAI
SmartCode AI is an AI-powered IDE assistant that automates code generation, bug detection, and test case creation. Using transformer-based models like OpenAI Codex or CodeT5, it provides intelligent autocomplete, real-time bug fixes, and automated test generation.
An AI-powered coding assistant that enhances developer productivity by:
- Generating intelligent code suggestions
- Detecting bugs in Python code
- Automatically creating test cases

## Features
✅ AI-powered code generation using OpenAI API  
✅ Simple bug detection analysis  
✅ Automatic unit test case generation  

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/smartcode-ai.git
    cd smartcode-ai
    ```
2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install openai
    ```

## Usage

1. Set your OpenAI API Key:
    ```sh
    export OPENAI_API_KEY="your-api-key"
    ```
2. Run the assistant:
    ```sh
    python smartcode_ai.py
    ```
3. Enter a prompt like:
    ```
    Write a Python function to calculate the factorial of a number.
    ```
4. View the generated code, bug detection report, and test cases.

## Example Output
```sh
Generated Code Suggestion:
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

Bug Detection Report:
No obvious issues detected.

Generated Test Cases:
import unittest

class TestFunction(unittest.TestCase):
    def test_case(self):
        # TODO: Add test cases
        self.assertEqual(1, 1)  # Replace with actual test

if __name__ == '__main__':
    unittest.main()
```

## Contributing
Feel free to submit issues and pull requests for improvements.

## License
MIT License
