# a - значение, корень из которого надо извлечь
def gsqrt(a):
    # oldn - число, используемое для итерации
    # iters - количество итераций алгоритма
    def lsqrt(a, oldn, iters):
        # вычисляем следующее число итерации
        n = 0.5*(oldn + a/oldn)
        # проверяем, нужно ли продолжать итерацию
        if iters == 0:
            return n
        else:
            return lsqrt(a, n, iters - 1)
    return lsqrt(a, 1, 100)
print(gsqrt(2))