# class A:
#     def f(self):
#         print("A")

# class B(A):
#     def f(self):
#         print("B")
#         super().f()

# class C(A):
#     def f(self):
#         print("C")
#         super().f()

# class D(C, B):
#     pass

# print(D.mro())


class X:
    def f(self):
        print("X")

class Y(X):
    def f(self):
        print("Y")
        super().f()

class Z(X):
    def f(self):
        print("Z")
        super().f()

class W(Y, Z):
    pass
print(Z.mro())