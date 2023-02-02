import itertools

def calculate_point(hand):

    # Create a mapping from card values to points
    values = {1: 1, 10: 10}
    for i in range(2, 10):
        values[i] = i

    # Get all possible combinations of 3 cards
    combs = [sorted(comb) for comb in itertools.combinations(hand, 3)]

    # Calculate the point for each combination
    points = []
    selected_cards = []
    remaining_cards = []
    for comb in combs:
        point = sum(comb) % 60
        if point % 10 == 0:
            remaining = [card for card in hand if card not in comb]
            point = sum(remaining)
            if point > 10:
                point = point - 10
            points.append(point)
            selected_cards.append(comb)
            remaining_cards.append(remaining)

    if not points:
        return -1, None, None

    min_point = min(points)
    index = points.index(min_point)
    return min_point, selected_cards[index], remaining_cards[index]

def get_max_point(hand):
  hand = get_hand_points(hand)
  hands = [hand, [6 if x==3 else 3 if x==6 else x for x in hand]]
  results = [calculate_point(h) for h in hands]
  max_point, selected_cards, remaining_cards = max(results, key=lambda x: x[0])
  return max_point, selected_cards, remaining_cards

def get_hand_points(hand):

    mapping = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    return [mapping[card] if card in mapping else int(card) for card in hand]