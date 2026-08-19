from riddle import FourAnswerRiddle, TwoAnswerRiddle, OpenRiddle
from game import RiddleGame, Player
from riddle_crud import RiddleRepository

ridd = RiddleRepository("answers.json")
# ridd.menu_update_riddle(7)
# print(ridd.get_riddle_by_id(5))
# print(ridd.delete_riddle)
# print(ridd.update_riddle(6,{'hi': "hi"}))

yossi = Player("yossi")
run_game = RiddleGame(yossi, ridd.get_all_riddles())
result = run_game.start()
print(result.average_time_by_category())
print(result.average_time_by_type())