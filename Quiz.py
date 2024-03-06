class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.score = 0

    def run_quiz(self):
        for i in range(len(self.questions)):
            user_answer = input(f"Question {i + 1}: {self.questions[i]}? ").lower()
            if user_answer == self.answers[i].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {self.answers[i]}")

        print(f"\nQuiz complete! You scored {self.score} out of {len(self.questions)}.")

def main():
    questions = [
        "What is the capital of France",
        "What is the largest planet in our solar system",
        "Who wrote 'Romeo and Juliet'",
        "What is the chemical symbol for gold",
        "How many continents are there"
    ]

    answers = [
        "Paris",
        "Jupiter",
        "William Shakespeare",
        "Au",
        "7"
    ]

    quiz = Quiz(questions, answers)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
