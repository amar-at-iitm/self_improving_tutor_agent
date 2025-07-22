
# Self-Improving Tutor Agent

This project is an adaptive tutoring agent designed to provide a personalized learning experience for students. The agent diagnoses misunderstandings, adjusts the difficulty and style of teaching, and tracks progress over time. It uses a data-driven approach to optimize lesson plans and improve learning outcomes.

## Problem Statement
The goal is to design and build an adaptive tutoring agent for a specific subject (e.g., Calculus or Linear Algebra). This agent will interact with a learner to:

- Diagnose misunderstandings by evaluating their answers to exercises.
- Adapt the difficulty and teaching style based on their performance.
- Log progress and update a model of the learner's knowledge.
- Provide tailored feedback and propose subsequent exercises to maximize learning.

The project also includes a component to run A/B experiments to compare the effectiveness of this adaptive tutoring system against a fixed (non-adaptive) curriculum, measuring the learning gains.

## Features & Deliverables
- **Interactive Interface:** A web-based UI or a Command-Line Interface (CLI) for students to take lessons and complete exercises.
- **Dynamic Student Model:** Tracks mastery for each concept (Knowledge Component) using methods like Bayesian Knowledge Tracing or proficiency scores.
- **Adaptive Agent Logic:** Intelligently selects the next exercise based on the student's current mastery and recent error patterns.
- **Logging & Analytics:** A system for logging all interactions and a dashboard to visualize performance, progress, and learning gains (e.g., pre-test vs. post-test scores).
- **Experimental Framework:** A setup to run experiments with real or simulated students to compare adaptive vs. static lesson sequences.
- **Privacy-First Design:** All student data is anonymized to protect privacy, and the system is designed to operate offline or with a local LLM.

## Architecture
The system is built around a few key components:

- **Knowledge Components (KCs):** The subject matter (e.g., Calculus) is broken down into a hierarchy of fundamental concepts or skills. For example, in Calculus, KCs could be 'limits', 'derivatives', and 'integrals', with sub-KCs like 'product rule' or 'chain rule'.
- **Exercise Bank:** A collection of 50–200 parameterized problems. Each problem is tagged with the specific KCs it assesses and includes an auto-grader for symbolic or numeric evaluation.
- **Adaptation Policy:** The core logic that determines the next best action (e.g., which exercise to present). This can be implemented using a multi-armed bandit algorithm or a heuristic approach that aims to select exercises maximizing the expected learning gain.
- **Feedback Generation:** A module, potentially using a local Large Language Model (LLM), that generates clear, targeted explanations based on the specific type of error a student makes.
- **Student Model:** A persistent profile for each student that stores their estimated mastery level for every KC. This model is continuously updated after each interaction.

## Repository Structure

```

/math_tutor/
├── README.md
├── exercises/
│   ├── calculus_exercises.json
│   └── ...
├── data/
│   ├── student_logs/
│   └── experiment_results/
└── src/
├── agent.py          # Core adaptive logic and decision-making
├── student_model.py  # Manages student proficiency data
├── grader.py         # Evaluates student answers
├── ui.py             # Handles user interaction (CLI or Web)
└── main.py           # Main entry point to run the application

````

## Getting Started


### Installation
Clone the repository:
```bash
git clone https://github.com/amar-at-iitm/math_tutor
cd math_tutor
````

Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Tutor

To start an interactive session:

```bash
python src/main.py
```

## Evaluation Metrics

The success of the agent is measured by:

* **Normalized Learning Gain:**
  Calculated from pre-test and post-test scores to measure knowledge improvement.

  ```
  Gain = (Post-test Score - Pre-test Score) / (Max Score - Pre-test Score)
  ```

* **Engagement Metrics:** Time spent on tasks, number of hints requested, and session completion/dropout rates.

* **Adaptivity Effectiveness:** Direct comparison of the learning gains between the group receiving adaptive tutoring and the control group with a static lesson plan.


