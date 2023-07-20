from typing import List


class Solution:
    """
    In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

    Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

    For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
    Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

    It is guaranteed an answer exists.

    Example 1:

    Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
    Output: [0,2]
    Example 2:

    Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    Output: [1,2]
    """
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_store = {skill:i for i, skill in enumerate(req_skills)}
        cand = []
        for skills in people:
            val = 0
            for skill in skills:
                val |= 1 << skill_store[skill]
            cand.append(val)
        @lru_cache(None)
        def helper(idx, mask):
            if mask == 0:
                return []
            if idx == len(people):
                return [0] * 100
            if not (mask & cand[idx]):
                return helper(idx + 1, mask)
            # either skip current candidate or 
            # take the candidate and filter out the skills that candidate has
            return min(helper(idx + 1, mask), [idx] + helper(idx + 1, mask & ~cand[idx]), key=len)
        return helper(0, (1 << len(req_skills)) - 1)