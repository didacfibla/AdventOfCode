def prepare_game():
    f = open("input.txt", "r")
    lines = [linea.rstrip('\n') for linea in f]

    game = {}

    for line in lines:
        game_id, numbers = line.split(":")
        game_numbers = []
        part1, part2 = numbers.split("|")
        p1 = set()
        p2 = set()
        for n in part1.split(" "):
            if n.isdigit():
                p1.add(int(n))

        for n in part2.split(" "):
            if n.isdigit():
                p2.add(int(n))

        game_numbers.append(p1)
        game_numbers.append(p2)

        game_numer = int(game_id.split()[-1])
        game[game_numer] = game_numbers

    return game


def calculate_score(game):
    total = 0

    for k in game.keys():
        game_total = 0
        print(f"{k}: {game[k]}")

        intersection_set = game[k][0].intersection(game[k][1])

        if len(intersection_set) > 0:
            game_total = 1
            for i in range(1, len(intersection_set)):
                game_total *= 2

        print("Total:", game_total)
        total += game_total
        print()

    print("Total:", total)


def win_card(game: dict, card: int) -> list[int]:
    cards_winned = []
    intersection_set = game[card][0].intersection(game[card][1])
    new_card = card
    for _ in intersection_set:
        new_card += 1
        cards_winned.append(new_card)

    return cards_winned


def calculate_number_of_card(game):
    # Metemos las cartas iniciales a la pila
    cards = [card for card in game]

    # Por cada carta obtenemos las cartas que ganamos
    for card in cards:
        winned_cards = win_card(game, card)
        for winned_card in winned_cards:
            cards.append(winned_card)

    print(len(cards))


def part1(game):
    calculate_score(game)


def part2(game):
    calculate_number_of_card(game)


if __name__ == "__main__":
    game = prepare_game()
    # part1(game)
    part2(game)
