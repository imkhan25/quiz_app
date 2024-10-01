class Results:
    def __init__(self, score, total_questions):
        self.score = score
        self.total_questions = total_questions

    def show(self):
        """Display the quiz results."""
        print(f"\nYou answered {self.score} out of {self.total_questions} questions correctly.")
        percentage = (self.score / self.total_questions) * 100
        print(f"Your score: {percentage:.2f}%")
        if percentage >= 80:
            print("Excellent!")
        elif percentage >= 50:
            print("Good job!")
        else:
            print("Better luck next time!")
