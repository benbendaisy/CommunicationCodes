from typing import List


class Solution:
    """

    """
    def imageSmoother1(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        # Create a new image of the same dimension as the input image.
        smooth_img = [[0] * n for _ in range(m)]
        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                sums = 0
                count = 0
                # Iterate over all plausible nine indices
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        if 0 <= x < m and 0 <= y < n:
                            sums += img[x][y]
                            count += 1
                smooth_img[i][j] = sums // count
        return smooth_img

    def imageSmoother(self, img):
        rows = len(img)
        cols = len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total_sum = 0
                count = 0

                for l in range(max(0, i-1), min(rows, i+2)):
                    for k in range(max(0, j-1), min(cols, j+2)):
                        total_sum += img[l][k]
                        count += 1

                result[i][j] = total_sum // count

        return result