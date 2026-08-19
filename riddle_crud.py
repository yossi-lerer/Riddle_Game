import json
from riddle import FourAnswerRiddle, OpenRiddle, TwoAnswerRiddle, Riddle
import questionary

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
        riddles = self.load_riddles()
        i = 0
        for riddle in riddles:
            if int(riddle["id"]) == riddle_id:
                return riddles[i]
            else:
                i += 1
    
    def update_riddle(self, riddle_id: int, new_data: dict) -> bool:
        riddles = self.load_riddles()
        i = 0
        for riddle in riddles:
            if int(riddle["id"]) == riddle_id:
                riddles[i] = new_data
                with open(self.__file_path, "w") as file:
                    json.dump(riddles, file)
            else:
                i += 1
    
    def delete_riddle(self, riddle_id: int) -> bool:
        riddles = self.load_riddles()
        i = 0
        for riddle in riddles:
            if int(riddle["id"]) == riddle_id:
                riddle_remove = riddles.pop(i)
                with open(self.__file_path, "w") as file:
                    json.dump(riddles, file)
                return riddle_remove
            else:
                i += 1

    def save_riddles(self, riddles: list[Riddle]) -> None:
       pass

    def menu_update_riddle(self, riddle_id: int):
        choices = []
        riddle_by_id = self.get_riddle_by_id(riddle_id)
        for feild in riddle_by_id:
            choices.append(feild)
        choice_change = questionary.select("wich feild you wont to update", choices).ask()
        change = questionary.text("say").ask()
        print(change)
        riddle_by_id[choice_change] = change
        self.update_riddle(riddle_id, riddle_by_id)
        print(choice_change)


        
# ridd.add_riddle(12, "Who was the first president of the United States?", "George Washington", "open", [], "hard", "history")
# print(ridd.load_riddles())
# print(ridd.get_all_riddles())