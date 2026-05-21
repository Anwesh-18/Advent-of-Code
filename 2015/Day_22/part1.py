lines = open("input.txt").read().strip().splitlines()
boss_hp = int(lines[0].split()[-1])
boss_damage = int(lines[1].split()[-1])

SPELLS = {
    "Magic Missile": (53, 0),
    "Drain": (73, 0),
    "Shield": (113, 6),
    "Poison": (173, 6),
    "Recharge": (229, 5),
}

BEST = float("inf")


def apply_effects(player_hp, player_mana, boss_hp,
                  shield, poison, recharge):
    armor = 0

    if shield > 0:
        armor = 7
        shield -= 1

    if poison > 0:
        boss_hp -= 3
        poison -= 1

    if recharge > 0:
        player_mana += 101
        recharge -= 1

    return player_hp, player_mana, boss_hp, shield, poison, recharge, armor


def dfs(player_hp, player_mana, boss_hp,
        shield, poison, recharge,
        mana_spent, player_turn):
    global BEST

    if mana_spent >= BEST:
        return

    player_hp, player_mana, boss_hp, shield, poison, recharge, armor = \
        apply_effects(player_hp, player_mana, boss_hp,
                      shield, poison, recharge)

    if boss_hp <= 0:
        BEST = min(BEST, mana_spent)
        return

    if player_turn:
        for spell, (cost, timer) in SPELLS.items():
            if player_mana < cost:
                continue

            if spell == "Shield" and shield > 0:
                continue
            if spell == "Poison" and poison > 0:
                continue
            if spell == "Recharge" and recharge > 0:
                continue

            n_player_hp = player_hp
            n_player_mana = player_mana - cost
            n_boss_hp = boss_hp
            n_shield, n_poison, n_recharge = shield, poison, recharge

            if spell == "Magic Missile":
                n_boss_hp -= 4
            elif spell == "Drain":
                n_boss_hp -= 2
                n_player_hp += 2
            elif spell == "Shield":
                n_shield = timer
            elif spell == "Poison":
                n_poison = timer
            elif spell == "Recharge":
                n_recharge = timer

            dfs(n_player_hp, n_player_mana, n_boss_hp,
                n_shield, n_poison, n_recharge,
                mana_spent + cost, False)

    else:
        damage = max(1, boss_damage - armor)
        player_hp -= damage

        if player_hp <= 0:
            return

        dfs(player_hp, player_mana, boss_hp,
            shield, poison, recharge,
            mana_spent, True)


# Start fight
dfs(50, 500, boss_hp, 0, 0, 0, 0, True)
print(BEST)
