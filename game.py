import time

class RiddleGame:
    def __init__(self, Player, Riddle):
        self.__player =  Player
        self.__riddles = Riddle
        self.__results = []

    def start(self):
        start = time.time()
        print(self.__player.get_username())
        for riddle in self.__riddles:
            riddle.display()
            while True:
                answer = input("enter answer ")
                if riddle.check_answer(answer):
                    break
            end = time.time()
            total_time = end - start
            self.__results.append(QuestionResult(riddle.riddle_id, riddle.get_type, riddle.category, total_time))

        print(self.__results[0].__dict__)
        return GameResult(self.__player.get_username(), self.__results)

    def ask_riddle(self, riddle: Riddle) -> QuestionResult:
        pass

    def print_summary(self, result: GameResult) -> None:
        pass
    
class Player:
    def __init__(self, username):
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def rename(self, new_username: str) -> None:
        pass

class QuestionResult:
    def __init__(self, riddle_id: int, riddle_type: str, category: str, time_taken: float):
        self.__riddle_id = riddle_id
        self.__riddle_type = riddle_type
        self.__category = category
        self.__time_taken = time_taken

    @property
    def riddle_type(self):
        return self.__riddle_type
    @property
    def category(self):
        return self.__category
    @property
    def time_taken(self):
        return self.__time_taken
    
class GameResult:
    def __init__(self, user, question_results):
        self.__username = user
        self.__date = time.strftime("%Y-%m-%d")
        self.__total_time = 0
        self.__question_results = question_results


    def get_total_riddles(self) -> int:
        return len(self.__question_results)
    
    def average_time_by_type(self) -> dict[str, float]:
        average = {}
        for question in self.__question_results:
            if question.riddle_type in average:
                average[question.riddle_type][0] += question.time_taken
                average[question.riddle_type][1] += 1
            else:
                average[question.riddle_type] = [question.time_taken, 1]
        for avg in average:
            average[avg] = f"{average[avg][0] / average[avg][1]:.2f}"
        return average

    def average_time_by_category(self) -> dict[str, float]:
        average = {}
        for question in self.__question_results:
            if question.category in average:
                average[question.category][0] += question.time_taken
                average[question.category][1] += 1
            else:
                average[question.category] = [question.time_taken, 1]
        for avg in average:
            average[avg] = f"{average[avg][0] / average[avg][1]:.2f}"
        return average
    
    
    def to_csv_row(self) -> list:
        pass