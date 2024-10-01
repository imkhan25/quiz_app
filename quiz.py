import time
import logging
from questions import get_random_questions

logging.basicConfig(level=logging.INFO)

class Quiz:
    def __init__(self, timer: int = None):
        self.questions = get_random_questions()
        self.score = 0
        self.timer = timer  # Optional timer in seconds
        self.start_time = None

    def start(self):
        """Starts the quiz."""
        self.start_time = time.time()
        logging.info("Quiz started.")
        for question in self.questions:
            if self.timer and time.time() - self.start_time > self.timer:
                print("\nTime's up! The quiz has ended.")
                break
            self.ask_question(question)
        logging.info("Quiz ended.")
        self.show_results()

    def ask_question(self, question):
        """Display a question and handle user input."""
        print(f"\nCategory: {question['category']}")
        print(f"Question: {question['question']}")
        
        if question['type'] == 'multiple_choice':
            for idx, option in enumerate(question['options'], start=1):
                print(f"{idx}. {option}")
            user_answer = input("Choose the correct option (1-4): ")
            try:
                selected_option = question['options'][int(user_answer) - 1]
            except (IndexError, ValueError):
                print("Invalid input. Skipping question.")
                return
            if selected_option == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")

        elif question['type'] == 'true_false':
            user_answer = input("True or False? (t/f): ").lower()
            if (user_answer == 't' and question['answer'] is True) or (user_answer == 'f' and question['answer'] is False):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")

        elif question['type'] == 'short_answer':
            user_answer = input("Your answer: ").strip()
            if user_answer.lower() == question['answer'].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")

    def show_results(self):
        """Displays the final score and performance breakdown."""
        print(f"\nQuiz Completed!\nYour total score is: {self.score}/{len(self.questions)}")
        if self.timer:
            elapsed_time = time.time() - self.start_time
            print(f"Time taken: {elapsed_time:.2f} seconds")

