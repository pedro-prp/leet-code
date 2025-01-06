class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # Usando o método Newton-Raphson
        estimated = x / 2

        while True:
            new_estimated = (estimated + x / estimated) / 2

            # Aplica a tolerância esperada
            if abs(new_estimated - estimated) < 1e-6:
                break
            estimated = new_estimated

        return int(estimated)
