import os
from steam.repository import SteamRepository
from steam.analytics import SteamAnalytics


def run_analysis():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "steam_games.zip")

    repo = SteamRepository(file_path)
    repo.load()

    analytics = SteamAnalytics(repo.games)

    print("Total de jogos:", len(repo))
    
    print("\nPercentual de Jogos Gratuitos vs Pagos:")
    print(analytics.percentual_free_vs_paid())
    
    print("\nAno(s) com maior número de lançamentos:")
    print(analytics.year_with_most_games())
    
    print("\nTempo médio de jogo por tipo:")
    print(analytics.average_playtime_by_type())


if __name__ == "__main__":

    run_analysis()
