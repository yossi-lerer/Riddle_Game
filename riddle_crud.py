import json
from riddle import FourAnswerRiddle, MultipleChoiceRiddle, OpenRiddle, TwoAnswerRiddle, Riddle
class RiddleRepository:

    def __init__(self, file_path):
        self.__file_path = file_path
    
    def load_riddles(self):
        with open(self.__file_path, "r") as file:
            data = json.load(file)
        return data

    def add_riddle(self, riddle_id, question, correct_answer, type, possible_answers, difficulty, category) -> None:
        riddles = self.load_riddles()
        riddles.append({
    "id": riddle_id,
    "question": question,
    "correct_answer": correct_answer,
    "type": type,
    "possible_answers": possible_answers,
    "difficulty": difficulty,
    "category": category
  })
        print(riddles)
        with open(self.__file_path, "w") as file:
            json.dump(riddles, file)
    
    def get_all_riddles(self) -> list[Riddle]:
        riddle_list = []
        riddles = self.load_riddles()
        for riddle in riddles:
            if riddle["type"] == "multiple_4":
                riddle_list.append(FourAnswerRiddle(riddle["id"], riddle["question"], riddle["correct_answer"], riddle["difficulty"], riddle["category"],riddle["possible_answers"]))
            elif riddle["type"] == "multiple_2":
                riddle_list.append(TwoAnswerRiddle(riddle["id"], riddle["question"], riddle["correct_answer"], riddle["difficulty"], riddle["category"],riddle["possible_answers"]))
            elif riddle["type"] == "open":
                riddle_list.append(OpenRiddle(riddle["id"], riddle["question"], riddle["correct_answer"], riddle["difficulty"], riddle["category"]))
        return riddle_list
    def get_riddle_by_id(self, riddle_id: int) -> Riddle | None:
        pass
    def update_riddle(self, riddle_id: int, new_data: dict) -> bool:
        pass
    def delete_riddle(self, riddle_id: int) -> bool:
        pass


        def save_riddles(self, riddles: list[Riddle]) -> None:
            pass
# ridd.add_riddle(12, "Who was the first president of the United States?", "George Washington", "open", [], "hard", "history")
# print(ridd.load_riddles())
# print(ridd.get_all_riddles())