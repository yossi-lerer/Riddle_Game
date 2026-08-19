import questionary


class Riddle:
    def __init__(self, riddle_id, question, correct_answer, difficulty, category):
        difficul = ["easy", "medium", "hard"]
        category_possible  = ["math", "english", "geography", "science", "history"]
        if type(riddle_id) == int and type(question) == str and type(correct_answer) == str and difficulty in difficul and category in category_possible:
            self.__id = riddle_id
            self.__question = question
            self.__correct_answer = correct_answer
            self.__difficulty = difficulty
            self.__category = category
        else:
            print("we have a problem")
            exit()
    def display(self) -> None:
        raise NotImplementedError
    
    def check_answer(self, answer: str) -> bool:
        raise NotImplementedError
    
    def get_type(self) -> str:
        raise NotImplementedError

    def to_dict(self) -> dict:
        pass

    # getter
    @property
    def question(self):
        return self.__question

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def riddle_id(self):
        return self.__id

    @property
    def category(self):
        return self.__category

class MultipleChoiceRiddle(Riddle):
    def __init__(self, id, question, correct_answer, difficulty, category, possible_answers):
        if type(possible_answers) == list:
            super().__init__(id, question, correct_answer, difficulty, category)
            self.__possible_answers = possible_answers
        else:
            print("we have a problem")
            exit()

    def display(self) -> None:
        print(self.question)
        choices = []
        for answer in self.__possible_answers:
            choices.append(answer)
        return  questionary.select(self.question, choices).ask()
    def check_answer(self, answer: str) -> bool:
        print(answer)
        if answer == self.correct_answer:
            return True
        
    def get_possible_answers(self) -> list[str]:
        return list(self.__possible_answers)

class FourAnswerRiddle(MultipleChoiceRiddle):
    @property
    def get_type(self) -> str:
        return  "multiple_4"

class TwoAnswerRiddle(MultipleChoiceRiddle):
    @property    
    def get_type(self) -> str:
        return  "multiple_2"

class OpenRiddle(Riddle):
    def display(self) -> None:
        question = questionary.text(self.question).ask()
        return question
    def check_answer(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
            
    @property
    def get_type(self) -> str:
        return  "open"
