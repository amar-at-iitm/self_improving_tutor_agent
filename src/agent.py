# src/agent.py
import random

class TutorAgent:
    """
    The core agent that drives the tutoring session.

    It selects exercises, provides feedback, and interacts with the
    student model and grader.
    """
    def __init__(self, exercise_bank, student_model, grader):
        """
        Initializes the Tutor Agent.

        Args:
            exercise_bank (list): A list of exercise dictionaries.
            student_model (StudentModel): An instance of the student model.
            grader (Grader): An instance of the grader.
        """
        self.exercise_bank = exercise_bank
        self.student_model = student_model
        self.grader = grader
        self.session_history = []
        print("TutorAgent initialized.")

    def select_exercise(self):
        """
        Selects the next exercise for the student based on their proficiency.

        Adaptation Policy:
        1. Find the KC with the lowest proficiency score above a minimum threshold.
           This targets areas where the student is struggling but has some foundation.
        2. If all KCs are mastered, select a random one for review.
        3. Filter the exercise bank for problems related to the chosen KC.
        4. Return one of these problems.

        Returns:
            dict: The selected exercise, or None if no suitable exercise is found.
        """
        proficiencies = self.student_model.get_mastery_summary()

        # Find KCs that are not fully mastered.
        non_mastered_kcs = {kc: p for kc, p in proficiencies.items() if p < 0.9}

        if not non_mastered_kcs:
            # If all KCs are mastered, pick a random one for review.
            target_kc = random.choice(list(proficiencies.keys()))
            print("All KCs mastered! Selecting a random KC for review:", target_kc)
        else:
            # Select the KC with the lowest proficiency.
            target_kc = min(non_mastered_kcs, key=non_mastered_kcs.get)
            print(f"Targeting KC with lowest proficiency: {target_kc} (Score: {proficiencies[target_kc]:.2f})")

        # Get all exercises for the target KC that haven't been answered correctly yet.
        answered_correctly_ids = {
            item['exercise_id'] for item in self.session_history if item['is_correct']
        }

        candidate_exercises = [
            ex for ex in self.exercise_bank
            if ex['kc'] == target_kc and ex['id'] not in answered_correctly_ids
        ]

        if not candidate_exercises:
            # If no unseen exercises for this KC, try any other non-mastered KC.
            all_unseen_exercises = [
                ex for ex in self.exercise_bank if ex['id'] not in answered_correctly_ids
            ]
            if not all_unseen_exercises:
                print("No more exercises available.")
                return None
            return random.choice(all_unseen_exercises)

        return random.choice(candidate_exercises)


    def process_answer(self, exercise, student_answer):
        """
        Processes the student's answer, grades it, and updates the model.

        Args:
            exercise (dict): The exercise that was given.
            student_answer (str): The student's response.

        Returns:
            tuple: A tuple containing a feedback string and a boolean indicating correctness.
        """
        is_correct = self.grader.grade(student_answer, exercise['answer'])
        kc = exercise['kc']

        # Update the student model based on the result.
        self.student_model.update_proficiency(kc, is_correct)

        # Log the interaction.
        self.session_history.append({
            'exercise_id': exercise['id'],
            'kc': kc,
            'answer': student_answer,
            'is_correct': is_correct
        })

        # Generate feedback.
        if is_correct:
            feedback = "Correct! Great job."
        else:
            feedback = f"Not quite. The correct answer is {exercise['answer']}. Let's keep practicing this topic."

        return feedback, is_correct

