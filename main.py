import argparse
import logging
from quiz import Quiz
from results import Results

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="Advanced Basic Quiz Application")
    parser.add_argument(
        '-t', '--time', type=int, help="Set a time limit for the quiz in seconds."
    )
    args = parser.parse_args()

    # Start the quiz with optional timer
    quiz = Quiz(timer=args.time)
    quiz.start()

    # Show final results
    results = Results(score=quiz.score, total_questions=len(quiz.questions))
    results.show()

if __name__ == '__main__':
    main()
