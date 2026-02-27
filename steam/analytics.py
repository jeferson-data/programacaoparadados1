from collections import Counter


class SteamAnalytics:
    """
    Responsável pelas análises dos dados.
    Separação de responsabilidades.
    """

    def __init__(self, games):
        self.games = games

    def percentual_free_vs_paid(self):

        total = len(self.games)
        free = sum(1 for g in self.games if g.is_free())
        paid = total - free

        return {
            "Gratuitos (%)": round((free / total) * 100, 2) if total else 0, sep="\n"
            "Pagos (%)": round((paid / total) * 100, 2) if total else 0
        }

    def year_with_most_games(self):

        years = []

        for g in self.games:
            if g.release_date:
                year = g.release_date[-4:]
                years.append(year)

        counter = Counter(years)

        if not counter:
            return []

        max_value = max(counter.values())

        return [year for year, count in counter.items() if count == max_value]

    def average_playtime_by_type(self):

        free_times = [g.playtime for g in self.games if g.is_free()]
        paid_times = [g.playtime for g in self.games if not g.is_free()]

        return {
            "Tempo médio - Gratuitos": round(sum(free_times) / len(free_times), 2) if free_times else 0, sep="\n"
            "Tempo médio - Pagos": round(sum(paid_times) / len(paid_times), 2) if paid_times else 0
        }

