# src/student_model.py
import json

class StudentModel:
    """
    Manages the student's knowledge state.

    This class tracks the student's proficiency for various knowledge
    components (KCs). Proficiency is represented as a score between 0 and 1.
    """
    def __init__(self, knowledge_components):
        """
        Initializes the student model.

        Args:
            knowledge_components (list): A list of strings representing the
                                         knowledge components for the subject.
        """
        # Initialize proficiency for each KC to a starting value (e.g., 0.1)
        # This assumes the student has some minimal prior knowledge.
        self.proficiency = {kc: 0.1 for kc in knowledge_components}
        print("StudentModel initialized with KCs:", knowledge_components)

    def get_proficiency(self, kc):
        """
        Retrieves the proficiency score for a given knowledge component.

        Args:
            kc (str): The knowledge component to check.

        Returns:
            float: The proficiency score, or None if the KC is not found.
        """
        return self.proficiency.get(kc)

    def update_proficiency(self, kc, is_correct):
        """
        Updates the proficiency for a KC based on the student's answer.

        This uses a simple learning rate update rule. If the answer is correct,
        proficiency increases. If incorrect, it decreases.

        Args:
            kc (str): The knowledge component related to the question.
            is_correct (bool): True if the student's answer was correct, False otherwise.
        """
        if kc not in self.proficiency:
            print(f"Warning: Knowledge component '{kc}' not found in model.")
            return

        # Learning rate determines how much proficiency changes after one problem.
        learning_rate = 0.1
        current_proficiency = self.proficiency[kc]

        if is_correct:
            # Increase proficiency, moving it closer to 1.
            self.proficiency[kc] += learning_rate * (1 - current_proficiency)
        else:
            # Decrease proficiency, moving it closer to 0.
            self.proficiency[kc] -= learning_rate * current_proficiency

        # Ensure proficiency stays within the [0, 1] bounds.
        self.proficiency[kc] = max(0, min(1, self.proficiency[kc]))

        print(f"Updated proficiency for '{kc}': {self.proficiency[kc]:.2f}")

    def get_mastery_summary(self):
        """
        Returns a summary of the student's mastery across all KCs.

        Returns:
            dict: A dictionary with KCs as keys and proficiency scores as values.
        """
        return self.proficiency

