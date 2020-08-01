class A:
    a=5
    def __init__(self):
        self.a=6


class B(A):
    a=7
    def __init__(self):
        # super().__init__()
        self.a=8
        super().__init__()

b=B()
print(b.a)