class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        lost_once = []

        for match in matches:
            winners[match[0]] = winners.get(match[0], 0) + 1
            losers[match[1]] = losers.get(match[1], 0) + 1

        result = [player for player, wins in winners.items() if player not in losers]

        for player, losses in losers.items():
            if losses == 1:
                lost_once.append(player)

        return [sorted(result), sorted(lost_once)]
