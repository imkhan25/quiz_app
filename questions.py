import random

# List of questions for the quiz application
QUESTIONS = [
    {
        'category': 'General Knowledge',
        'type': 'multiple_choice',
        'question': 'Which is the largest planet in our solar system?',
        'options': ['Earth', 'Jupiter', 'Saturn', 'Mars'],
        'answer': 'Jupiter'
    },
    {
        'category': 'Science',
        'type': 'true_false',
        'question': 'The atomic number of oxygen is 8.',
        'answer': True
    },
    {
        'category': 'Geography',
        'type': 'short_answer',
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    {
        'category': 'History',
        'type': 'multiple_choice',
        'question': 'Who was the first president of the United States?',
        'options': ['George Washington', 'Thomas Jefferson', 'Abraham Lincoln', 'John Adams'],
        'answer': 'George Washington'
    },
    {
        'category': 'Science',
        'type': 'true_false',
        'question': 'Water boils at 90 degrees Celsius.',
        'answer': False
    }
]

def get_random_questions():
    """Get a randomized list of questions for the quiz."""
    random.shuffle(QUESTIONS)
    return QUESTIONS
