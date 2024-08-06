# LLM Debate Business Plan Generator

This project utilizes OpenAI's GPT models to create an application where specified LLMs debate and develop a business plan on a specified theme. The final business plan is output in Markdown format.

## Prerequisites

1. **Python**: Ensure Python is installed on your machine.
2. **Virtual Environment (optional but recommended)**: Create a virtual environment for this project.
3. **OpenAI API Key**: Obtain an API key from OpenAI and set it in the script.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/takurot/llm_business_plan_debate_with_graphai
    cd llm_business_plan_debate_with_graphai
    ```

2. **Install necessary libraries**:
    ```bash
    pip install openai markdown2
    ```

3. **Set up OpenAI API Key**: Replace `'your_openai_api_key'` in the script with your actual OpenAI API key.

## Usage

### Command-line Arguments

- **--theme**: The theme for the business plan. Use this to start a debate from a keyword.
- **--file**: Path to an existing business plan file to deepen ideas.
- **--iterations**: Number of debate iterations. Default is 5.

### Examples

1. **Start a new debate with a specific theme**:
    ```bash
    python llm_debate_business_plan.py --theme "Sustainable Energy Solutions" --iterations 10
    ```

2. **Deepen ideas from an existing business plan file**:
    ```bash
    python llm_debate_business_plan.py --file "business_plan.md"
    ```

### Output

- **Business Plan**: The initial business plan and the deepened business plan are saved as Markdown files.

## Example

1. **Set the Theme and Iterations**:
    ```bash
    python llm_debate_business_plan.py --theme "Sustainable Energy Solutions" --iterations 5
    ```

2. **Run the Script**:
    ```bash
    python llm_debate_business_plan.py --theme "Sustainable Energy Solutions" --iterations 5
    ```

3. **Generated Business Plan**:
    The business plan will be saved as `business_plan.md` and the deepened business plan will be saved as `deepened_business_plan.md` in the current directory.

## Code Explanation

### Main Functions

1. **get_llm_response(prompt, role)**: Interacts with the OpenAI API to get responses from the LLMs based on the prompt and role.
2. **debate_on_theme(theme, iterations)**: Initializes the debate with a given theme and iterates the debate between two LLMs.
3. **generate_business_plan(history, theme)**: Generates a business plan from the debate history in Markdown format.
4. **deepen_ideas(business_plan_path)**: Reads an existing business plan and generates deeper ideas and improvements for each section.

### Main Execution

- The main block of the script sets the theme and iterations, runs the debate, generates the business plan, and deepens the ideas based on the generated or existing business plan.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenAI](https://www.openai.com/)
- [Markdown2](https://github.com/trentm/python-markdown2)
