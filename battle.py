class Battle:
    """
    > All warfare is based on deception.

    This class deals with matters of life and death.
    """

    @staticmethod
    def attack(attacker, defendant):
        """
        Battle between two knights, return winning knight.
        """
        attack_score = attacker.base_attack + 0.5
        defend_score = defendant.base_defence

        if attacker.equipped:
            attack_score += attacker.equipped.attack

        if defendant.equipped:
            defend_score += defendant.equipped.defence

        return (
            (attacker, defendant)
            if attack_score > defend_score
            else (defendant, attacker)
        )

    @staticmethod
    def kill_knight(knight, status=1):
        """
        Kill knight and return loot.
        """
        equipped_item = knight.equipped

        knight.update_status(status)
        knight.pos = None
        knight.equipped = None
        knight.base_attack = 0
        knight.base_defence = 0

        return equipped_item
