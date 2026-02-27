import csv
import zipfile
from .game import Game
from .exceptions import SteamDataError


class SteamRepository:
    """
    Responsável por carregar os dados (princípio da responsabilidade única).
    Suporta CSV normal ou CSV dentro de arquivo ZIP.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.games = []

    def load(self):

        try:
            if self.file_path.endswith(".zip"):

                with zipfile.ZipFile(self.file_path, 'r') as z:
                    file_name = z.namelist()[0]

                    with z.open(file_name) as file:
                        reader = csv.DictReader(
                            (line.decode("utf-8") for line in file)
                        )

                        for row in reader:
                            self._create_game(row)

            else:
                with open(self.file_path, encoding="utf-8") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        self._create_game(row)

        except Exception as e:
            raise SteamDataError(f"Erro ao carregar dados: {e}")

    def _create_game(self, row):
        try:
            game = Game(
                row["AppID"],
                row["Name"],
                row["Release date"],
                row["Price"],
                row["Average playtime forever"]
            )
            self.games.append(game)
        except:
            pass

    def __len__(self):
        return len(self.games)