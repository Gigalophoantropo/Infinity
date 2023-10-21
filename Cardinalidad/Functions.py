from manim import *
import sympy as simp


def SternsDiatomicSeries(n:int):
    DP = [0]*(n+2)
    DP[0] = 0
    DP[1] = 1

    for i in range(2, n+1):
        if int(i % 2) == 0:
            DP[i] = DP[int(i/2)]
        else:
            DP[i] = DP[int((i-1)/2)] + DP[int((i+1)/2)]

    return DP[n]


def NtoQplus(n: int):
    return SternsDiatomicSeries(n)/(SternsDiatomicSeries(n + 1))


def ZtoQ(n: int):
    if n >= 0:
        return SternsDiatomicSeries(n)/(SternsDiatomicSeries(n + 1))
    else:
        return -SternsDiatomicSeries(abs(n))/(SternsDiatomicSeries(abs(n) + 1))


def NtoQ(n: int):
    return ZtoQ(int((1 + ((-1)**n)*(2*n-1))/4))

def summation(func: Callable[[int], Any], i: int, n=None):
    """This is a sigma summation.

    Parameters
    ----------

    func
        The formula for the terms.
    i
        The starting index.
    n
        The last index value. 

        If you want that n approaches infinity it needs to be ``None`` (the default).
    
    """
    sigma = 0
    if n is None:
        # Infinity Sum
        while True:
            if func(i) == 0:
                break
            sigma += func(i)
            i += 1
    else:
        # Finity Sum
        for x in range(i, n + 1):
            sigma += func(x)
    return sigma

def derivative(func):
    x = simp.symbols("x")
    h = simp.symbols("h")
    return simp.Lambda(x, simp.limit((func(x+h)-func(x))/h, h, 0))

def Squares(n: int):
    S = Square()

def construct(self):
    def ChangeSkin(GoofyAhhObject: ImageMobject, GoofyAhhObject2: ImageMobject, times: list):
        for d in times:
            for e in range(d):
                self.remove(GoofyAhhObject), self.add(GoofyAhhObject2), self.wait(0.1)
                self.remove(GoofyAhhObject2), self.add(GoofyAhhObject), self.wait(0.1)
            if d != times[-1]:
                self.wait(0.4)

    def SpeakButWhitMove(GoofyAhhSpeaker: ImageMobject, Text: list):
        for b in Text:
            for c in range(b):
                self.play(GoofyAhhSpeaker.animate.shift(UP/8), run_time = 0.1)
                self.play(GoofyAhhSpeaker.animate.shift(DOWN/8), run_time = 0.1)
            if b != Text[-1]:
                self.wait(0.4)