class A:
    def __init__(self, name):
        self.name=name

class B(A):
    gene = 'XX'

class C(A):
    gene = 'XY'

class D(B,C):
    pass

baby = D('baby')
print(baby.gene)