from django.shortcuts import render

# Create your views here.
class Paren:
    pass

class Chil(Paren):
    def child(self):
        from p_basics.views import Person1

        p=Person1()
        return f'{p._name}, {p._age}, {p._protected()}'

class Other:
    def pa_class(self):
        from p_basics.views import Person1

        p=Person1()
        return f'{p._name}, {p._age}, {p._protected()}'