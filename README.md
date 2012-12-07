Докуметация
===========

Вычисление квадратного корня по итерационной формуле Герона

Вычисление производится по формуле
![alt text](http://upload.wikimedia.org/math/e/0/e/e0e036e9acd6c986d8ec8ce47e7556ce.png)

```python
from tkinter import *

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

if __name__ == "__main__":
    top = Tk()

    def compute():
        try:
            str = top.E1.get()
            n = gsqrt(float(str))
            top.L1["text"] = n
        except:
            top.L1["text"] = "ошибка"
        
    top.L1 = Label(top, text="0")
    top.L1.pack()
    top.E1 = Entry(top, textvariable = "0")
    top.E1.pack()
    top.B1 = Button(top, text="compute", command=compute)
    top.B1.pack(fill = 'x')

    top.mainloop()
 ```
 
работу выполняли: Пенкин Александр, Никита Плехов, Микаелян Андрей