from character import Character


class Battle:
    """Manages turn-based combat between two characters"""

    def __init__(self, hero: Character, enemy: Character, max_rounds: int = 1000) -> None:
        """
        Initialise the Battle
        Args:
        hero (Character): The character that attacks first each round.
        enemy (Character): The character that attacks second each round.
        max_rounds (int): Upper limit on rounds, so a battle where nobody
            can deal damage does not run forever (default = 1000)
        """
        self.hero = hero
        self.enemy = enemy
        self.max_rounds = max_rounds
        self.rounds_played = 0

    def play_round(self) -> None:
        """Play one round: hero attacks enemy, and enemy strikes back if still alive"""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
        self.rounds_played += 1

    def simulate_battle(self, verbose: bool = True) -> Character | None:
        """
        Run rounds until one character is no longer alive

        Args:
        verbose (bool): Print the HP of both characters after each round (default = True)

        Returns:
        The winning character, or None if max_rounds is reached without a winner.
        """
        while self.hero.is_alive and self.enemy.is_alive and self.rounds_played < self.max_rounds:
            self.play_round()
            if verbose:
                print(f"Round {self.rounds_played}: "
                      f"{self.hero.name} {self.hero.hp} HP, {self.enemy.name} {self.enemy.hp} HP")

        if self.hero.is_alive and self.enemy.is_alive:
            winner = None
        elif self.hero.is_alive:
            winner = self.hero
        else:
            winner = self.enemy

        if verbose:
            if winner is None:
                print(f"No winner after {self.rounds_played} rounds.")
            else:
                print(f"{winner.name} wins after {self.rounds_played} rounds!")
        return winner

    def __repr__(self) -> str:
        """Representation of battle object"""
        return f"Battle(hero={self.hero!r}, enemy={self.enemy!r}, rounds_played={self.rounds_played})"