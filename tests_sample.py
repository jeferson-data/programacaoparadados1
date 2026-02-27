from steam.game import Game

def test_game_is_free():
    game = Game("1", "Teste", "Jan 1, 2020", "0", "100")
    assert game.is_free() is True