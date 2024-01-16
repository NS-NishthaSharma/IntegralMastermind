import sympy as sp
import random

def problem_gen():
    x = sp.symbols('x')
    question_type = random.choice(['integral', 'derivative'])

    if question_type == 'integral':
        a = random.randint(1, 5)
        b = random.randint(6, 10)
        expr = random.choice([sp.sin(x), sp.cos(x), sp.exp(x), x**2])
        problem = sp.integrate(expr, (x, a, b))
        prompt = f"Please solve the integral of the following expression {expr} from {a} to {b}:\n"

    else:  # 'derivative'
        expr = random.choice([sp.sin(x), sp.cos(x), sp.exp(x), x**2])
        problem = sp.diff(expr, x)
        prompt = f"Please find the derivative of the following expression {expr} with respect to x:\n"

    return prompt, problem

def main():
    print("Welcome to the Integral Mastermind Game! Please solve each question to unlock levels.")
    score = 0
    num_levels = 5

    for level in range(1, num_levels + 1):
        print(f"\n----- Level {level} -----")
        num_problems = 3 + level 

        for _ in range(num_problems):
            prompt, actual_solution = problem_gen()

            user_answer = input(prompt)

            try:
                user_answer = sp.sympify(user_answer)
                if user_answer == actual_solution:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Sorry, the correct answer is {actual_solution}\n")
            except sp.SympifyError:
                print("Invalid input. Please enter a valid mathematical expression.\n")

    print(f"Congratulations! You completed the game. Final score: {score}/{num_levels * (num_problems)}")

if __name__ == "__main__":
    main()
