class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")
        super().f()

class C(A):
    def f(self):
        print("C")
        super().f()

class D(B):
    def f(self):
        print("D")
        super().f()

class E(C):
    def f(self):
        print("E")
        super().f()

class F(D, E):
    pass
