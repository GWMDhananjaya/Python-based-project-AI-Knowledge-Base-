"""
This module provides a simple AI knowledge base search functionality. 
It uses fuzzy matching to find close matches for user input.
"""

from fuzzywuzzy import process


def ai_knowledge_base():
    """
    This function implements an interactive search of AI terms using a 
    knowledge base. It utilizes fuzzy matching to find close matches 
    to user queries and prompts the user for further actions.
    """
    knowledge_base = {
        "Turing Test": (
            "Proposed by Alan Turing in 1950 to test a machine's ability to "
            "exhibit intelligent behavior."
        ),
        "Neural Networks": "A machine learning model inspired by the human brain.",
        "Deep Learning": (
            "A subset of machine learning based on neural networks with "
            "three or more layers."
        ),
        "AI Winter": (
            "A period in the history of AI when progress was slow, "
            "from 1974 to 1980."
        ),
        "Machine Learning": (
            "A subset of AI focused on enabling machines to learn from data."
        ),
        "Reinforcement Learning": (
            "An area of machine learning where agents learn to make "
            "decisions by taking actions in an environment to maximize a reward."
        ),
        "Natural Language Processing": (
            "A field of AI focused on the interaction between computers "
            "and humans using natural language."
        ),
        "Support Vector Machines": (
            "A supervised learning algorithm used for classification "
            "and regression tasks."
        ),
        "Gradient Descent": (
            "An optimization algorithm used to minimize the loss function "
            "in machine learning models."
        ),
        "Convolutional Neural Networks": (
            "A class of deep neural networks most commonly applied "
            "to analyzing visual imagery."
        ),
        "Generative Adversarial Networks": (
            "A class of machine learning models in which two neural networks "
            "contest with each other to generate new data."
        )
    }

    while True:
        query = input("Enter AI term to search: ").strip()

        # Find close matches based on the input query, regardless of case sensitivity or minor typos
        match, score = process.extractOne(query, knowledge_base.keys())

        if score > 80:  # If the match is sufficiently close
            print(f"{match}: {knowledge_base[match]}")
        else:
            print(f"{query} not found in the knowledge base.")
            print(f"Did you mean: {match}?")

            # Ask the user if they want to search for the suggested term
            while True:
                confirm = input(
                    "Do you want to search for the suggested term? (yes/no): "
                ).strip().lower()
                if confirm == 'yes':
                    print(f"{match}: {knowledge_base[match]}")
                    break
                elif confirm == 'no':
                    print("Okay, try another term.")
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

        # Ask the user if they want to search for another term
        while True:
            retry = input(
                "Do you want to search for another term? (yes/no): ").strip().lower()
            if retry == 'yes':
                break
            elif retry == 'no':
                return  # Exit the function and end the program
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == '__main__':
    ai_knowledge_base()
