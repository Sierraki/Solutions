class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        energy_cnt = experience_cnt = 0

        if sum(energy) + 1 > initialEnergy:
            energy_cnt = sum(energy) + 1 - initialEnergy

        # print(energy_cnt)

        for i in experience:
            if initialExperience <= i:
                experience_cnt += i + 1 - initialExperience
                initialExperience = 2 * i + 1
            else:
                initialExperience += i
        # print(experience_cnt)
        return experience_cnt + energy_cnt
