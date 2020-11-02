# https://leetcode.com/problems/high-five/
# TODO: Avg 5 scores instead of all scores
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = []
        items.sort()
        currentStudent = items[0][0]
        numScores = 0
        sumScores = 0
        for score in items:
            if score[0] == currentStudent:
                sumScores += score[1]
                numScores += 1
            else:
                scores.append([currentStudent, sumScores/numScores])
                sumScores = 0
                currentStudent = score[0]
        scores.append([currentStudent, sumScores/numScores])
        return scores
