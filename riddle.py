class Riddle:
    def __init__(self, riddle_id, question, correct_answer, difficulty, category):
        self.__id = riddle_id
        self.__question = question
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty
        self.__category = category
    
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
        super().__init__(id, question, correct_answer, difficulty, category)
        self.__possible_answers = possible_answers
    
    def display(self) -> None:
        print(self.question)
        print(self.__possible_answers)

    def check_answer(self, answer: str) -> bool:
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
        print(self.question)
   
    @property
    def get_type(self) -> str:
        return  "open"
