# src/main.py
import json
import os
from student_model import StudentModel
from grader import Grader
from agent import TutorAgent
from ui import CommandLineUI

def load_exercises(file_path):
    """Loads exercises from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Exercise file not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
        return []

def main():
    """
    Main function to run the tutoring system.
    """
    # --- Configuration ---
    EXERCISE_FILE = 'exercises/calculus_exercises.json'
    NUM_QUESTIONS_PER_SESSION = 5

    # --- Setup ---
    # Create data directories if they don't exist
    os.makedirs('data/student_logs', exist_ok=True)
    
    # Load the exercise bank
    exercise_bank = load_exercises(EXERCISE_FILE)
    if not exercise_bank:
        print("Exiting due to missing or invalid exercise file.")
        return

    # Get all unique knowledge components from the exercises
    knowledge_components = sorted(list(set(ex['kc'] for ex in exercise_bank)))

    # Initialize components
    student_model = StudentModel(knowledge_components)
    grader = Grader()
    agent = TutorAgent(exercise_bank, student_model, grader)
    cli = CommandLineUI(agent)

    # --- Run Session ---
    cli.start_session(NUM_QUESTIONS_PER_SESSION)

if __name__ == '__main__':
    main()

