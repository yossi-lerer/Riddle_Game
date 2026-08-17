from riddle import FourAnswerRiddle, TwoAnswerRiddle, OpenRiddle
from game import RiddleGame, Player

yossi = Player("yossi")
quistion = FourAnswerRiddle(10, "what is the main city of frach", "hi", "Easy", "Math", ["hi", "hello"])
quistion1 = FourAnswerRiddle(10, "what is the main city1 of frach", "hi", "Medium", "English", ["hi", "hello"])
quistion2 = OpenRiddle(10, "what is the main city2 of frach", "cc", "Medium", "English")
run_game = RiddleGame(yossi, [quistion, quistion1, quistion2])
result = run_game.start()
print(result.average_time_by_category())
print(result.average_time_by_type())