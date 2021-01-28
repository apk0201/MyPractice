class A:
    def m1(self):
        print("hello All.. This is from M1 Method...")

        # self.obj = self.B()
        # self.obj.f1()

        def m2():
            print("This is from the M2 Method...")

            def a1():
                print("This is from A1 Method....")

            a1()
            return a1

        return m2


class B(A):
    def b1(self):
        print("hello All.. This is from B1 Method...")


obj = A()
x = obj.m1()
y = x()
y()
o1 = B()
o1.b1()
