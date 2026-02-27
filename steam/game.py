class Game:
    """
    Representa um jogo da Steam.
    Aplicação de encapsulamento (POO).
    """

    def __init__(self, app_id, name, release_date, price, playtime):
        self.app_id = app_id
        self.name = name
        self.release_date = release_date
        self.price = float(price) if price else 0.0
        self.playtime = float(playtime) if playtime else 0.0

    def is_free(self):
        """Verifica se o jogo é gratuito."""
        return self.price == 0