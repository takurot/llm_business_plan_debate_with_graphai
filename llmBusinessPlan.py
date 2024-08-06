import argparse
import openai
import graphai
import markdown2

openai.api_key = 'your_openai_api_key'

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

def deepen_ideas(business_plan_path):
    with open(business_plan_path, 'r') as file:
        business_plan = file.read()

    plan_sections = business_plan.split('## ')
    role = "LLM_A"
    
    for section in plan_sections[1:]:  # Skip the title section
        title, content = section.split('\n', 1)
        prompt = f"Based on the section '{title.strip()}', provide more detailed ideas and improvements:\n\n{content.strip()}"
        response = get_llm_response(prompt, role)
        print(f"Deepened ideas for section '{title.strip()}': {response}\n")
        
        business_plan += f"\n### Deepened ideas for {title.strip()}\n\n{response}\n"

    return business_plan

def main(args):
    if args.file:
        deepened_business_plan = deepen_ideas(args.file)
        
        # Output deepened business plan in markdown format
        deepened_business_plan_path = "deepened_business_plan.md"
        with open(deepened_business_plan_path, "w") as file:
            file.write(markdown2.markdown(deepened_business_plan))
        
        print("Deepened business plan generated and saved as 'deepened_business_plan.md'")
    
    elif args.theme:
        iterations = args.iterations if args.iterations else 5
        debate_history = debate_on_theme(args.theme, iterations)
        visualize_debate(debate_history)
        
        business_plan = generate_business_plan(debate_history, args.theme)
        
        # Output initial business plan in markdown format
        business_plan_path = "business_plan.md"
        with open(business_plan_path, "w") as file:
            file.write(markdown2.markdown(business_plan))
        
        print("Initial business plan generated and saved as 'business_plan.md'")
        
        # Deepen ideas based on the generated business plan
        deepened_business_plan = deepen_ideas(business_plan_path)
        
        # Output deepened business plan in markdown format
        deepened_business_plan_path = "deepened_business_plan.md"
        with open(deepened_business_plan_path, "w") as file:
            file.write(markdown2.markdown(deepened_business_plan))
        
        print("Deepened business plan generated and saved as 'deepened_business_plan.md'")
    else:
        print("Please provide either a theme or a file path for business plan.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Debate Business Plan Generator")
    parser.add_argument('--theme', type=str, help='The theme for the business plan')
    parser.add_argument('--file', type=str, help='Path to an existing business plan file to deepen ideas')
    parser.add_argument('--iterations', type=int, default=5, help='Number of debate iterations (default: 5)')
    
    args = parser.parse_args()
    main(args)
