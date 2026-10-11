"""Command-line demo HR Policy Assisstant.

Run with: python main.py
"""

from hr_assisstant.pipeline import ask, build_hr_assistant


def main():
    print("Building the HR policy assisstant...")
    agent = build_hr_assistant()
    print("Assisstant ready!\n")

    demo_questions = [
        "How many paid annual leave days do I get?",
        "What is the notice period during probabition?",
        "Can I work from home every day?",
    ]

    for question in demo_questions:
        print("="*50)
        print("Question : ", question)
        print("-"*50)
        answer = ask(agent, question)
        print("Answer : ", answer)
        print("="*50)
        print()

if __name__=="__main__":
    main()

