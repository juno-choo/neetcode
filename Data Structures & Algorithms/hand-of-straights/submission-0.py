class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False

        hand.sort()
        freq = defaultdict(int)

        for card in hand:
            freq[card] += 1

        for card in hand:
            if freq[card] == 0: continue
            for i in range(card, card + groupSize):
                if i not in freq:
                    return False

                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]

        return True