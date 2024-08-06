import openai
import graphai
from markdown2 import markdown

openai.api_key = 'your_openai_api_key' # replace with your OpenAI API key

def get_llm_response(prompt, role):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{role}: {prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def debate_on_theme(theme, iterations):
    role_a = "LLM_A"
    role_b = "LLM_B"
    initial_prompt = f"Develop a business plan for the theme: {theme}"
    
    response_a = get_llm_response(initial_prompt, role_a)
    print(f"{role_a}: {response_a}")

    response_b = get_llm_response(response_a, role_b)
    print(f"{role_b}: {response_b}")

    debate_history = [(role_a, response_a), (role_b, response_b)]

    for i in range(iterations):
        if i % 2 == 0:
            response_a = get_llm_response(response_b, role_a)
            print(f"{role_a}: {response_a}")
            debate_history.append((role_a, response_a))
        else:
            response_b = get_llm_response(response_a, role_b)
            print(f"{role_b}: {response_b}")
            debate_history.append((role_b, response_b))

    return debate_history

def visualize_debate(history):
    # Use GraphAI tools to visualize the debate
    graph = graphai.Graph()
    for idx, (role, response) in enumerate(history):
        graph.add_node(f"{role}_{idx}", label=response)
        if idx > 0:
            graph.add_edge(f"{role}_{idx-1}", f"{role}_{idx}")

    graph.visualize()

def generate_business_plan(history, theme):
    business_plan = f"# Business Plan for {theme}\n\n"
    for role, response in history:
        business_plan += f"## {role}\n\n{response}\n\n"
    return business_plan

if __name__ == "__main__":
    theme = "Sustainable Energy Solutions" # change the theme to your desired business idea
    iterations = 5  # number of iterations for the debate, increase number to deepen the debate
    debate_history = debate_on_theme(theme, iterations)
    visualize_debate(debate_history)
    
    business_plan = generate_business_plan(debate_history, theme)
    
    # Output business plan in markdown format
    with open("business_plan.md", "w") as file:
        file.write(markdown(business_plan))
    
    print("Business plan generated and saved as 'business_plan.md'")
