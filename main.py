from riddle import FourAnswerRiddle
from game import RiddleGame, Player

yossi = Player("yossi")
quistion = FourAnswerRiddle(10, "what is the main city of frach", "hi", "hard", "country", ["hi", "hello"])
quistion1 = FourAnswerRiddle(10, "what is the main city1 of frach", "hi", "hard", "country", ["hi", "hello"])
quistion2 = FourAnswerRiddle(10, "what is the main city2 of frach", "hi", "hard", "country", ["hi", "hello"])
run_game = RiddleGame(yossi, [quistion, quistion1, quistion2])
result = run_game.start()
print(result.average_time_by_category())