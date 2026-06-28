class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for i in range(iterations):
            derivitive = 2 * x
            x = x - learning_rate * derivitive
        return round(x, 5)
