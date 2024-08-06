import argparse
import openai
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

def generate_business_plan(history, theme):
    business_plan = f"# Business Plan for {theme}\n\n"
    for role, response in history:
        business_plan += f"## {role}\n\n{response}\n\n"
    return business_plan

def deepen_ideas(business_plan_content, iterations):
    plan_sections = business_plan_content.split('## ')
    role = "LLM_A"
    debate_history = []

    for section in plan_sections[1:]:  # Skip the title section
        title, content = section.split('\n', 1)
        prompt = f"Based on the section '{title.strip()}', provide more detailed ideas and improvements:\n\n{content.strip()}"
        response = get_llm_response(prompt, role)
        debate_history.append((role, response))

        for i in range(iterations):
            if i % 2 == 0:
                response_a = get_llm_response(response, role)
                debate_history.append((role, response_a))
            else:
                response_b = get_llm_response(response_a, role)
                debate_history.append((role, response_b))

            response = response_b if i % 2 == 0 else response_a

        business_plan_content += f"\n### Deepened ideas for {title.strip()}\n\n{response}\n"

    return business_plan_content

def main(args):
    if args.file:
        with open(args.file, 'r') as file:
            business_plan_content = file.read()
        
        iterations = args.iterations if args.iterations else 5
        deepened_business_plan_content = deepen_ideas(business_plan_content, iterations)
        
        # Output deepened business plan in markdown format
        deepened_business_plan_path = "deepened_business_plan.md"
        with open(deepened_business_plan_path, "w") as file:
            file.write(markdown2.markdown(deepened_business_plan_content))
        
        print("Deepened business plan generated and saved as 'deepened_business_plan.md'")
    
    elif args.theme:
        iterations = args.iterations if args.iterations else 5
        debate_history = debate_on_theme(args.theme, iterations)
        
        business_plan_content = generate_business_plan(debate_history, args.theme)
        
        # Output initial business plan in markdown format
        business_plan_path = "business_plan.md"
        with open(business_plan_path, "w") as file:
            file.write(markdown2.markdown(business_plan_content))
        
        print("Initial business plan generated and saved as 'business_plan.md'")
        
        # Deepen ideas based on the generated business plan
        deepened_business_plan_content = deepen_ideas(business_plan_content, iterations)
        
        # Output deepened business plan in markdown format
        deepened_business_plan_path = "deepened_business_plan.md"
        with open(deepened_business_plan_path, "w") as file:
            file.write(markdown2.markdown(deepened_business_plan_content))
        
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
