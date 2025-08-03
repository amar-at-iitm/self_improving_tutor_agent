# src/grader.py

class Grader:
    """
    Evaluates the student's answer for a given exercise.
    """
    def __init__(self):
        """
        Initializes the Grader.
        """
        print("Grader initialized.")

    def grade(self, student_answer, correct_answer):
        """
        Compares the student's answer with the correct answer.

        This is a simple implementation that checks for numerical equality.
        It can be extended to handle symbolic math, string matching, etc.

        Args:
            student_answer (str): The answer provided by the student.
            correct_answer (any): The correct answer from the exercise bank.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        try:
            # Attempt to convert student's answer to a float for comparison.
            # This handles most simple math problems.
            student_answer_float = float(student_answer)
            correct_answer_float = float(correct_answer)
            return abs(student_answer_float - correct_answer_float) < 1e-6
        except (ValueError, TypeError):
            # Fallback for non-numeric answers (e.g., string comparison)
            return str(student_answer).strip().lower() == str(correct_answer).strip().lower()

