class Stats():
    """Статистика игры"""

    def __init__(self):
        """Инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('stats/high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Статистика изменяющаяся во время игры"""
        self.ship_live = 2
        self.score = 0
