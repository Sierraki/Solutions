class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for i in image:
            left = 0
            right = n - 1
            while left <= right:
                i[left], i[right] = i[right], i[left]
                left += 1
                right -= 1
        for i in image:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
        return image
