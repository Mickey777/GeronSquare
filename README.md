Докуметация
===========

Вычисление квадратного корня по итерационной формуле Герона

Вычисление производится по формуле
![alt text](http://upload.wikimedia.org/math/e/0/e/e0e036e9acd6c986d8ec8ce47e7556ce.png)

```python
def gsqrt(a):
    """Возвращает квадратный корень по методу Герона

    Keyword arguments:
    a -- значение, корень из которого надо извлечь
    
    """
    def lsqrt(a, oldn, iters):
        """Возвращает квадратный корень по методу Герона

        Keyword arguments:
        a -- значение, корень из которого надо извлечь
        oldn -- число, используемое для итерации (n-1 в формуле) 
        iters -- количество итераций алгоритма
        
        """
        # вычисляем следующее число итерации
        n = 0.5*(oldn + a/oldn)
        # проверяем, нужно ли продолжать итерацию
        if iters == 0:
            return n
        else:
            return lsqrt(a, n, iters - 1)
    return lsqrt(a, 1, 100)

while(True):
    try:
        msg = 'Введиче число, из которого надо извлечь корень или break для выхода: '
        str = input(msg).replace('\n', '') # получение ввода
        if str.lower() == "break": # проверка необходимости завершения работы
            print("Работа завершена")
            break
        num = float(str)
        print(gsqrt(num)) # печать квадратного корня
    except:
        print("Введены неверные данные")
 ```
 
работу выполняли: Пенкин Александр, Никита Плехов, Микаелян Андрей