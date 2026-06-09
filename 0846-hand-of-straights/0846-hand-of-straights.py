class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cards_count = Counter(hand)
        sorted_cards = sorted(cards_count.keys())

        for card in sorted_cards:
            count = cards_count[card]
            if count == 0:
                continue
            for i in range(groupSize):
                next_card = card + i
                if cards_count[next_card] < count:
                    return False
                cards_count[next_card] -= count
        return True
