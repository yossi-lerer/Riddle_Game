from riddle import FourAnswerRiddle, TwoAnswerRiddle, OpenRiddle
from game import RiddleGame, Player
from riddle_crud import RiddleRepository
ridd = RiddleRepository("answers.json")
yossi = Player("yossi")

run_game = RiddleGame(yossi, ridd.get_all_riddles())
result = run_game.start()
print(result.average_time_by_category())
print(result.average_time_by_type())