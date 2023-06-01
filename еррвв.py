class ParentA:
    def __init__(self):
        self.attribute_a = "Attribute A from ParentA"

    def method_a(self):
        print("Method A from ParentA")


class ParentB:
    def __init__(self):
        self.attribute_b = "Attribute B from ParentB"

    def method_b(self):
        print("Method B from ParentB")


class Child(ParentA, ParentB):
    def __init__(self):
        ParentA.__init__(self)
        ParentB.__init__(self)
        self.attribute_c = "Attribute C from Child"

    def method_c(self):
        print("Method C from Child")



child = Child()


print(child.attribute_a)
print(child.attribute_b)
print(child.attribute_c)
child.method_a()
child.method_b()
child.method_c()