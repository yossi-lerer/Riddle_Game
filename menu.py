import questionary

class Menu:
    def __init__(self, RiddleGame, RiddleRepository):
        self.riddleGame = RiddleGame
        self.riddleRepository = RiddleRepository

    def menu_selection(self):
        choice = questionary.select("Would you like to start a quiz or edit questions?", ["Start a quiz", "Edit the puzzles"]).ask()
        if choice == "Start a quiz":
            result = self.riddleGame.start()
            print(result.average_time_by_category())
            print(result.average_time_by_type())

        elif choice == "Edit the puzzles":
            choice_edit = questionary.select("What action would you like to take?", ["add", "edit", "delete"]).ask()
            if choice_edit == "add":
                riddle = questionary.text("Write a riddle").ask()
                correct_answer = questionary.text("Write the correct answer.").ask()
                question_type = questionary.select("question type", ["open"]).ask()
                level = questionary.select("question type", ["easy", "medium", "hard"]).ask()
                category = questionary.select("category", ["math", "english", "geography", "science", "history"]).ask()
                self.riddleRepository.add_riddle(len(self.riddleRepository.load_riddles()) + 1, riddle, correct_answer, question_type, [], level, category)