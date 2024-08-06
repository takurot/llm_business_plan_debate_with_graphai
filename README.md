# llm_business_plan_debate_with_graphai (LLM Debate Business Plan Generator)

This project utilizes tools from the GraphAI GitHub repository and OpenAI's GPT models to create an application where specified LLMs debate and develop a business plan on a specified theme. The final business plan is output in Markdown format.

## Prerequisites

1. **Python**: Ensure Python is installed on your machine.
2. **Virtual Environment (optional but recommended)**: Create a virtual environment for this project.

## Installation

1. **Clone the GraphAI repository**:
    ```bash
    git clone https://github.com/receptron/graphai
    cd graphai
    ```

2. **Install necessary libraries**:
    ```bash
    pip install openai graphai markdown2
    ```

3. **Set up OpenAI API**: Obtain an API key from OpenAI and set it in the script.

## Usage

1. **Set up OpenAI API Key**: Replace `'your_openai_api_key'` in the script with your actual OpenAI API key.

2. **Run the Script**: Execute the script to generate a business plan.
    ```bash
    python llm_debate_business_plan.py
    ```

### Script Parameters

- **Theme**: The theme for the business plan. This can be set in the script (default is "Sustainable Energy Solutions").
- **Iterations**: The number of debate iterations between the LLMs. This can also be set in the script (default is 5).

### Output

- **Debate Visualization**: The debate process is visualized using GraphAI tools.
- **Business Plan**: The final business plan is saved as a Markdown file named `business_plan.md`.

## Example

1. **Set the Theme and Iterations**:
    ```python
    theme = "Sustainable Energy Solutions"
    iterations = 5
    ```

2. **Run the Script**:
    ```bash
    python llm_debate_business_plan.py
    ```

3. **Generated Business Plan**:
    The business plan will be saved as `business_plan.md` in the current directory.

## Code Explanation

### Main Functions

1. **get_llm_response(prompt, role)**: Interacts with the OpenAI API to get responses from the LLMs based on the prompt and role.
2. **debate_on_theme(theme, iterations)**: Initializes the debate with a given theme and iterates the debate between two LLMs.
3. **visualize_debate(history)**: Uses GraphAI tools to create and visualize the debate graphically.
4. **generate_business_plan(history, theme)**: Generates a business plan from the debate history in Markdown format.

### Main Execution

- The main block of the script sets the theme and iterations, runs the debate, visualizes it, and generates the business plan.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [GraphAI](https://github.com/receptron/graphai)
- [OpenAI](https://www.openai.com/)
- [Markdown2](https://github.com/trentm/python-markdown2)
