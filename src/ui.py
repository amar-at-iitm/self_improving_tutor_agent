# src/ui.py
import json

class CommandLineUI:
    """
    Handles the command-line interaction with the student.
    """
    def __init__(self, agent):
        """
        Initializes the Command Line UI.

        Args:
            agent (TutorAgent): The tutoring agent to interact with.
        """
        self.agent = agent
        print("Command Line UI initialized.")

    def start_session(self, num_questions):
        """
        Starts a tutoring session for a fixed number of questions.

        Args:
            num_questions (int): The number of questions to ask in the session.
        """
        print("\n--- Welcome to your personalized tutoring session! ---")
        print(f"We will go through {num_questions} problems. Type 'quit' at any time to exit.")

        for i in range(num_questions):
            print(f"\n----- Question {i + 1} -----")

            # Agent selects the next exercise
            exercise = self.agent.select_exercise()

            if exercise is None:
                print("Congratulations, you have completed all available exercises!")
                break

            print(f"Topic: {exercise['kc']}")
            print(f"Question: {exercise['question']}")

            # Get student's answer
            student_answer = input("Your answer: ")

            if student_answer.lower() == 'quit':
                print("Exiting session.")
                break

            # Agent processes the answer
            feedback, is_correct = self.agent.process_answer(exercise, student_answer)

            # Display feedback
            print(feedback)

        self.show_summary()

    def show_summary(self):
        """
        Displays a summary of the student's performance at the end of the session.
        """
        print("\n--- Session Summary ---")
        mastery = self.agent.student_model.get_mastery_summary()
        print("Final Proficiency Scores:")
        for kc, score in mastery.items():
            print(f"- {kc}: {score:.2f}")

        # Save session data to a file for analysis
        with open("data/student_logs/session_log.json", "w") as f:
            json.dump(self.agent.session_history, f, indent=2)
        print("\nSession log saved to data/student_logs/session_log.json")

