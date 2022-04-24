# no block scope meaning variables in if statements have same scope as enclosing unction or global if not in function
# game_level = 3
#
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
#
# create_enemy()

enemies = 1

# To change global variable must call global
# def increase_enemies():
#     global enemies
#     for enemy in range(3):
#         enemies += 1
#     print(enemies)
#
# increase_enemies()


def increase_enemies():
    return enemies + 1


enemies = increase_enemies()
print(enemies)

