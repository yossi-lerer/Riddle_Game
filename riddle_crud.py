import json
from riddle import FourAnswerRiddle, MultipleChoiceRiddle, OpenRiddle, TwoAnswerRiddle, Riddle
class RiddleRepository:

    def __init__(self, file_path):
        self.__file_path = file_path
    
    def load_riddles(self):
        with open(self.__file_path, "r") as file:
            data = json.load(file)
        return data

    def add_riddle(self) -> None:
        riddles = self.load_riddles()
        riddles.append({
    "id": 11,
    "question": "Who was the first president of the United States?",
    "correct_answer": "George Washington",
    "type": "open",
    "possible_answers": [],
    "difficulty": "hard",
    "category": "history"
  })
        print(riddles)
        with open(self.__file_path, "w") as file:
            json.dump(riddles, file)
    
    def get_all_riddles(self) -> list[Riddle]:
        pass
    def get_riddle_by_id(self, riddle_id: int) -> Riddle | None:
        pass
    def update_riddle(self, riddle_id: int, new_data: dict) -> bool:
        pass
    def delete_riddle(self, riddle_id: int) -> bool:
        pass


        def save_riddles(self, riddles: list[Riddle]) -> None:
            pass
ridd = RiddleRepository("answers.json")
ridd.add_riddle()
# print(ridd.load_riddles())