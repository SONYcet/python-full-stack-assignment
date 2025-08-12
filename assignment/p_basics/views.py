import os
import re
from abc import abstractmethod, ABC

from django.db import models

from assignment import settings
from assignment.settings import BASE_DIR
from second.views import Chil, Other
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import sort
from .myclasses import ClassOne, ClassTwo
# Create your views here.
x=89
def print_name(request):
    x='Hi'
    context = {
        'a':5,
        'b':'sony',
        'c': True,
        'd':3.67,
        'e':65.678994667,
        'local_scope': x,
        'global_scope': globals()['x']

    }

    return render(request,'p_basics/basics.html', context)

def operators(request):
    var1=67
    var2=54
    if var1<var2:
        larger=var2
        smaller=var1
    else:
        larger=var1
        smaller=var2
    number=100
    add=var1+var2
    sub=var1-var2
    mult=var1*var2
    div=var1/var2
    incre=number+1
    decre=number-1
    are_equal=var1==var2
    context={
        'var1':var1,
        'var2':var2,
        'add':add,
        'sub': sub,
        'mult': mult,
        'div': div,
        'incre': incre,
        'decre': decre,
        'number':number,
        'are_equal':are_equal,
        'lt' :var1<var2,
        'lte': var1 <= var2,
        'gt': var1 > var2,
        'gte': var1 >= var2,
        'larger': larger,
        'smaller': smaller,

    }
    return render(request, 'p_basics/operators.html', context)
def loops(request):
    start=1
    start_do=1
    end_do=10
    start1=10
    num1=765
    num3=str(num1)
    num2=0
    end=20
    string1=""
    list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    pair=[(10,34),(100,100),(22,22),(54,43)]
    string2=""
    max1=[5,9,2]
    while start<=end:
        string1+=str(start)+'<br>'
        start+=1
    for i,j in pair:
        if i==j:
            string2+=(f"{i} == {j}-->equal <br>\n")
        else:
            string2+=(f"{i} != {j}--> are not equal <br>\n")
    str1=""
    str2=''
    str3=''
    str4=''
    list2=[]
    for l in list1:
        if l%2==0:
            str1+=str(l)+','
        else:
            str2+=str(l)+','
    str1=str1.strip(',')
    str2=str2.strip(',')
    max2=max(max1)
    while start1<=end:
        list2.append(start1)
        if start1%2==0:
            str3+=str(start1)+','
        start1+=1
    str3=str3.strip(',')
    while True:
        str4+=str(start_do)+','
        start_do+=1
        if start_do>end_do:
            break
    str4=str4.strip(',')
    for i in num3:
        num2+=int(i)**3
    a1 = 18
    list3 = []

    for j in range(2, a1 + 1):
        if a1 % j == 0:
            list3.append(j)
    a2 = "342"
    d2 = ''
    for i in a2:
        d2 = i + d2
    num3 = 45
    b2 = [0, 1]
    c2 = num3 % 2
    for i in b2:
        if i == c2:
            if i == 0:
                result = f'{num3} is even'
            else:
                result = f'{num3} is odd'
            break
    result2=''
    if request.method == 'POST':
        gender_input = request.POST.get('gender', '').upper()
        if gender_input == 'M':
            result2 = 'Gender is Male'
        elif gender_input == 'F':
            result2 = 'Gender is Female'
        else:
            result2 = 'Invalid input'
    context={
        'ten_times':range(10),
        'start':start,
        'end' : end,
        'list1':string1,
        'string2':string2,
        'str1':str1,
        'str2': str2,
        'max2':max2,
        'max1':max1,
        'list2': list2,
        'str3': str3,
        'str4': str4,
        'num1':num1,
        'num2':num2,
        'is_armstr':num1==num2,
        'list3': list3,
        'a1': a1,
        'a2':a2,
        'd2': d2,
        'resul': a2==d2,
        'result': result,
        'num3' : num3,
        'result2': result2,



    }
    return render(request, 'p_basics/loops.html', context)
def string1(request):
    str1="hi iam sony and iam 02"
    str2='Hello'
    str3='''are aare are are
            you you you you
            ready ready '''
    str4=" good morning  buddies      byeeee                   "
    type1=type(str1)
    a=765
    type11=type(a)
    b=str(a)
    type2=type(b)
    sub=str1[1:8]
    sear=str1.index('2')
    stri=''
    pattern=''
    result=''
    if request.method=="POST":
        stri=request.POST.get('string','')
        pattern= r'^[A-Za-z]+$'
        if re.fullmatch(pattern,stri):
            result='matching string'
        else:
            result=' no matching string'

    context={
        'str1' : str1,
        'str2': str2,
        'str3': str3,
        'type1' :str(type1),
        'con':str1+str2,
        'len1': len(str1),
        'sub' :sub,
        'sear':sear,
        'stri': stri,
        'pattern' :pattern,
        'result':result,
        'equal': str1==str2,
        'not_equal': str1 != str2,
        'less_than': str1 < str2,
        'greater_than': str1> str2,
        'lr_equal': str1 <= str2,
        'gr_equal': str1 >= str2,
        'starts_with': str1.startswith("Hello"),
        'ends_with': str1.endswith("02"),
        'str4': str4,
        'strip_fucn': str4.strip(),
        'replacing' : str4.replace("buddies", "friends"),
        'splitting' :str1.split(' '),
        'a' : a,
        'type_a' :str(type11),
        'b' : b,
        'type_b':str(type2),
        'upper_case' :str1.upper(),
        'lower_case' : str1.lower(),

    }
    return render(request,'p_basics/strings.html', context)
def arrays(request):
    list1 = [5, 4, 2, 7, 1]
    list2 = [5, 4, 2, 7, 1]
    list3=[34,65,12,78]
    list5=[67,45,32,87]
    list6=list5.copy()
    list7=[4,8,3,6,23]
    list8=list7.copy()
    a = 0
    b=4
    c=2
    d=7
    for i in list1:
        a += i
    length_is = len(list1)
    if b in list1:
        result = ' yes there is a match'
    else:
        result = ' no match'
    list5.insert(1, 98)
    list8.reverse()
    list9 = [5, 4, 2, 7, 5, 8, 3, 9, 4, 1]
    list10 = []
    set1 = set()
    for i in list9:
        if i not in set1:
            set1.add(i)
        else:
            list10.append(i)
    list11 = [5, 4, 2, 7, 5, 8, 3, 9, 4, 1]
    list12 = [6, 4, 2, 8, 6, 5, 3, 9]
    com = []
    set2 = set()
    for i in list11:
        if i not in set2:
            set2.add(i)
            if i in list12:
                com.append(i)
    list14 = [5, 4, 2, 7, 5, 8, 3, 9, 4, 1]
    list13 = []
    list15=[]
    for i in list14:
        if i not in list13:
            list13.append(i)
        else:
            list15.append(i)
    list17 = [5, 4, 2, 7, 73, 54, 8, 3, 65, 9, 1]
    e = sorted(list17)
    list18 = [5, 4, 2, 7, 73, 54, 8, 3, 65, 9, 1]
    even = []
    odd = []
    for i in list17:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    ma = max(e)
    mi = min(e)
    diff = ma - mi
    list19 = [5, 4, 12, 2, 7, 73, 54, 8, 23, 13, 65, 9, 1]
    li = [12, 23]
    if all(i in list19 for i in li):
        result1 = "two items are present"
    else:
        result1 = "12 and/or 23 sre missing"

    context = {
        'list1': list1,
        'list2': list2,
        'list3' : list3,
        'list6' : list6,
        'a':a,
        'b': b,
        'c' : c,
        'd' : d,
        'length_is' : length_is,
        'aver' : a / length_is,
        'index_value' : list1.index(d),
        'result' : result,
        'remo' : list2.remove(c),
        'list4' : list3.copy(),
        'list5' : list5,
        'min': min(list5),
        'max' : max(list5),
        'list7' : list7,
        'list8' : list8,
        'list10' : list10,
        'list9' : list9,
        'list11': list11,
        'list12' : list12,
        'com': com,
        'set2' : set2,
        'list13': list13,
        'list14': list14,
        'list15': list15,
        'list17' :list17,
        'e': e,
        'sec_lar' : e[-2],
        'list18' : list18,
        'even' : even,
        'odd' : odd,
        'num_even': len(even),
        'num_odd' : len(odd),
        'ma' : ma,
        'mi' : mi,
        'diff' : diff,
        'list19' : list19,
        'li': li,
        'result1':result1,

    }
    return render(request, 'p_basics/arrays.html', context)
def static_variable(request):
    class Student:
        school_name = 'sony indian school'

    prin1 = Student.school_name
    ins1 = Student()
    prin2 = ins1.school_name
    ins2=Student()
    ins2.school_name='Nithins indian school'

    class Stu1:
        school_name1 = 'sony indian school'

    Stu1.school_name1 = 'children indian school'
    ins3 = Stu1()
    ins4 = Stu1()
    prin3 = ins3.school_name1
    prin4 = ins4.school_name1
    context={
        'prin1': prin1,
        'school_var_name': 'school_name',
        'prin2': prin2,
        'ins2': ins2.school_name,
        'prin3': prin3,
        'prin4' :prin4,
        'class': Stu1.school_name1,

    }
    return render(request,'p_basics/static.html', context)

class Vehicle:
    def vehicle_method1(self):
        return "Vehicle: General method 1"
    def vehicle_method2(self):
        return "Vehicle: General method 2"
    def start(self):  # Common overridden method
        return "Vehicle starting..."
class Car(Vehicle):
    def car_method1(self):
        return "Car: Playing music"
    def car_method2(self):
        return "Car: Opening sunroof"
    def start(self):
        return "Car starting with key..."
class ElectricCar(Car):
    def electric_method1(self):
        return "ElectricCar: Battery at 100%"
    def electric_method2(self):
        return "ElectricCar: Charging port open"
    def start(self):
        return "ElectricCar starting silently..."
class Vehicle1:
    def start(self):
        return "Vehicle starting..."
class Car1(Vehicle1):
    def start(self):
        return super().start()  + " <br>Car starting with key..."
class ElectricCar1(Car1):
    def start(self):
        return super().start()  + "<br> ElectricCar starting silently..."
class Vehicle2:
    def __init__(self):
        self.engine=["vehicle engine"]
class Car2(Vehicle2):
    def __init__(self):
        super().__init__()
        self.engine.append("<br>car engine")
class ElectricCar2(Car2):
    def __init__(self):
        super().__init__()
        self.engine.append("<br>electric car engine")
def main_view(request):
    obj = ElectricCar()
    obj_v=Vehicle()
    obj_c = Car()
    obj_e = ElectricCar()
    e = ElectricCar1()
    e2 = ElectricCar2()

    context = {
        'v_m1': obj.vehicle_method1(),
        'v_m2': obj.vehicle_method2(),
        'c_m1': obj.car_method1(),
        'c_m2': obj.car_method2(),
        'e_m1': obj.electric_method1(),
        'e_m2': obj.electric_method2(),
        'e_m3': obj.start(),

        'v_m11': obj_v.vehicle_method1(),
        'v_m21': obj_v.vehicle_method2(),
        'v_m31': obj_v.start(),

        'c_m11': obj_c.car_method1(),
        'c_m21': obj_c.car_method2(),
        'c_m31': obj_c.start(),

        'e_m11': obj_e.electric_method1(),
        'e_m21': obj_e.electric_method2(),
        'e_m31': obj_e.start(),

        'super_methods': e.start(),
        'super_variables': e2.engine,

    }
    return render(request,'p_basics/inheritance.html', context)




class Person:
    def __init__(self):
        self.__name = 'sony'
        self.__age = 22

    def __private(self):
        return f'private method says : Hello {self.__name}'

    def main(self):
        return f'Name: {self.__name} and age: {self.__age}' + "\n" + self.__private()

class Student(Person):
    def access_private(self):
        result = ''
        try:
            result += f'<br>accessing private attribute :  {self.__name}'
        except AttributeError:
            result += f'<br>can not access the private attributes'
        try:
            result += self.__private()
        except AttributeError:
            result += f'<br>can not access the private method'
        return result

class Person1:
    def __init__(self):
        self._name = 'sony'
        self._age = 22

    def _protected(self):
        return f'protected  method says : Hello {self._name}'

class Student1:
    def pp_app(self):
        p = Person1()
        return f'{p._name} and {p._age} and {p._protected()}'

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def public(self):
        return f'public method says : Hello {self.name}'

class Student2:
    def __init__(self):
        self.per2 = Person2('nithin', 22)

    def show_person_info(self):
        return f'{self.per2.name} and {self.per2.age} and {self.per2.public()}'

def access_modifiers(request):

    p=Person()
    s=Student()
    p1 = Person1()
    s2 = Student1()
    c = Chil()
    o = Other()
    stu2=Student2()
    context={
        'p': p._Person__private(),
        'p1': p.main(),
        'p2': p._Person__name,
        'p3': p._Person__age,
        's': s.access_private(),
        's1':s.main(),
        'pro': p1._protected(),
        'pro1': p1._name,
        'pro2': p1._age,
        'pro_sa': s2.pp_app(),
        'op_c': c.child(),
        'op_o': o.pa_class(),
        'per2': stu2.per2.name,
        'per3': stu2.per2.age,
        'per4' : stu2.per2.public(),
        'stu2' : stu2.show_person_info(),

    }
    return render(request, 'p_basics/access.html', context)

def abstract1(request):
    class Animal(ABC):
        def __init__(self,name):
            self.name= name
        def sleep(self):
            return f'{self.name} is sleeping'
        @abstractmethod
        def speak(self):
            pass
    class Dog(Animal):
        def speak(self):
            return f'{self.name} says bow bow'
        def wag_tail(self):
            return f'{self.name} is wagging its tail'
    class Vehicle(ABC):
        def __init__(self, brand):
            self.brand = brand
        def start_engine(self):
            return f"{self.brand}'s engine has started"
        @abstractmethod
        def drive(self):
            pass
    class Car(Vehicle):
        def __init__(self, brand, model):
            super().__init__(brand)
            self.model = model
        def drive(self):
            return f'{self.brand} , {self.model} now started'

    class Vehicle1(ABC):
        def __init__(self, brand):
            self.brand = brand
        def start_engine(self):
            return f"{self.brand}'s engine has started"
        @abstractmethod
        def drive(self):
            pass
    class Car1(Vehicle1):
        def __init__(self, brand, model):
            super().__init__(brand)
            self.model = model
        def drive(self):
            return f'{self.brand} , {self.model} now started'
        @classmethod
        def create_demo_car(cls):
            return cls("Toyota", "Supra")

    d=Dog('max')
    mycar = Car('toyota', 'corolla')
    my_car = Car1.create_demo_car()
    my_car1= Car1.create_demo_car()

    context= {
        'd': d.name,
        'd1': d.speak(),
        'd2': d.sleep(),
        'd3': d.wag_tail(),
        'brand': mycar.brand,
        'model': mycar.model,
        'car_me': mycar.start_engine(),
        'car_me1': mycar.drive(),
        'brand1': my_car.brand,
        'model1': my_car.model,
        'car_me3': my_car.drive(),
        'brand2': my_car1.brand,
        'model2': my_car1.model,
        'car_me2': my_car1.start_engine(),

    }
    return render(request, 'p_basics/abstract1.html', context)

class StudentManager:
    def __init__(self):
        self.students= {
            '001': 'sony',
            '002': 'nitin',
            '003': 'bujji',
            '004': 'pandu',
            '005': 'vedhanush',

        }
        self.students1 = {
            '001': 'sony',
            '002': 'nitin',
            '003': 'bujji',
            '004': 'pandu',
            '005': 'vedhanush',
        }
        self.students2 = {
            '001': 'sony',
            '002': 'nitin',
            '003': 'bujji',
            '004': 'pandu',
            '005': 'vedhanush',
        }
        self.students3 = {
            '001': 'sony',
            '002': 'nitin',
            '003': 'bujji',
            '004': 'pandu',
            '005': 'vedhanush',

        }
        self.nested_students= {
            'S001': {'name': 'sujji', 'age': 20, 'grade': 'A'},
            'S002': {'name': 'suresh', 'age': 21, 'grade': 'B'},
            'S003': {'name': 'gouthami', 'age': 19, 'grade': 'A'},
            'S004': {'name': 'naveen', 'age': 22, 'grade': 'C'},
            'S005': {'name': 'chandu', 'age': 20, 'grade': 'B'}
        }

    def adding_value(self):
        self.students1['006']= 'ayyan'
        self.students1.update({'007':'arjun'})
        return self.students1

    def update_value(self):
        self.students2['001']= 'sonu'
        self.students2.update({'002':'chinnu'})
        return self.students2

    def accessing_value_students(self):
        name=self.students['004']
        return name

    def accessing_value_nested(self):
        name=self.nested_students['S004']['name']
        grade = self.nested_students['S003']['grade']
        return name, grade


    def keys_particular_dictionary(self):
        keys=list(self.students.keys())
        return keys

    def delete_value(self):
        if '004' in self.students3:
           del self.students3['004']
        return self.students3
def studentmanager(request):
    stu=StudentManager()
    context= {
        'adding': stu.adding_value(),
        'update': stu.update_value(),
        'accessing': stu.accessing_value_students(),
        'access_nested': stu.accessing_value_nested(),
        'keys': stu.keys_particular_dictionary(),
        'delete': stu.delete_value(),
        'dictionary': stu.students,
        'nested_dict': stu.nested_students,

    }
    return render(request,'p_basics/dict.html', context)

class StudentInfo:
    def display(self, *args):
        if len(args)==1:
            return f'<br>stu_name: {args[0]}'
        elif len(args)==2:
            return f'<br>stu_name: {args[0]} <br> grade: {args[1]}'
        else:
            return f'<br>stu_name: {args[0]} <br> grade: {args[1]} <br> age: {args[2]}'
class DataProcessor:
    def process_data(self, data):
        if isinstance(data, int):
            return f'integer_received  -- {data}:<br>the square of int: {data**2}'
        elif isinstance(data, str):
            return f'string_received  --  {data}: <br>the uppercase of string:{data.upper()}'
        elif isinstance(data, list):
            return f'list_received  --  {data}: <br>the length of list:{len(data)}'
        elif isinstance(data, dict):
            return f'dict_received  --  {data}:<br>the  keys: {data.keys()}'
class SimpleProcessor:
    def show_message(self,  msg1,msg2):
        if isinstance(msg1, str) and isinstance(msg2, str):
            return f'<br>Hi my name is {msg1} and i said {msg2}'

def student_view(request):
    student=StudentInfo()
    data=DataProcessor()
    same=SimpleProcessor()


    context={
        'result_1' : student.display('nithin'),
        'result_2': student.display('sony', "+A"),
        'result_3': student.display('sony','+A', '24'),
        'int': data.process_data(6),
        'str': data.process_data("sony"),
        'list': data.process_data([4, 6, 3, 8]),
        'dict': data.process_data({'a': 1, 'b': 2}),
        'str1': same.show_message("sony", 'good morning'),
        'str2': same.show_message("nithin", 'have a nice day'),

    }
    return render(request,'p_basics/method_oloading.html', context)

def testcalsses(request):
    obj1=ClassOne('sonu')
    obj2=ClassTwo('age')
    context={
        'obj1': obj1,
        'obj2': obj2,
    }
    return render(request, 'p_basics/packages.html', context)

def file_reading():
    file_path=os.path.join(BASE_DIR, 'django_remainders.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content=file.read()
    else:
        content= f'file not found'
    return content
def file_writing():
    file_path = os.path.join(BASE_DIR, 'schedule.txt')
    with open(file_path, 'a') as file:
        file.write("\nThis is a new line added to the file")
        return 'data added successfully '


def reading_file_stream():
    file_path=os.path.join(BASE_DIR,'html.txt')
    lines=[]
    try:
        with open(file_path,'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        lines=['file not found error']
    return lines
def random_access_read():
    file_path = os.path.join(settings.BASE_DIR, 'html.txt')
    with open(file_path, 'rb') as file:
        file.seek(10)
        data = file.read(20)
    return f"Random access read: {data.decode('utf-8', errors='ignore')}"
def seek_read():
    file_path = os.path.join(settings.BASE_DIR, 'html.txt')
    with open(file_path, 'r') as file:
        file.seek(5)
        data = file.read()
    return f"Read from position 5: <pre>{data}</pre>"

def check_permissions():
    file_path = os.path.join(settings.BASE_DIR, 'html.txt')
    can_read = os.access(file_path, os.R_OK)
    can_write = os.access(file_path, os.W_OK)
    return can_read, can_write



def read_text_file(request):

    content1 = file_writing()

    content=file_reading()
    file_stream_reading= reading_file_stream()
    binary_read= random_access_read()
    seek=seek_read()
    read, write= check_permissions()
    context={
        'content': content,
        'content1': content1,
        'stream_line': file_stream_reading,
        'binary_read' :  binary_read,
        'seek' : seek,
        'read': read,
        'write': write,


    }
    return render(request, 'p_basics/file_read.html', context)


def arithmetic_without_handling():
    numerator = 10
    denominator = 0
    if denominator != 0:
        result = numerator / denominator
    else:
        result = "Cannot divide by zero."
    return f"Result: {result}"
def arithmetic_with_handling():
    try:
        a = 10
        b = 0
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Arithmetic Exception: Cannot divide by zero."

def throwing_method():
    raise ZeroDivisionError("Manually thrown")
def call_throwing_method():
    try:
        throwing_method()
    except ZeroDivisionError as e:
        return HttpResponse(f"Caught a ZeroDivisionError: {e}")


def multiple_excepts():
    try:
        a = int("abc")
        b = 10 / 0
    except ZeroDivisionError:
        return "Caught ZeroDivisionError"
    except ValueError:
        return "Caught ValueError"
    except Exception as e:
        return f"Other Exception: {str(e)}"

def throw_custom_message(count=0):
    if count > 5:
        raise Exception("Custom Exception Caught: Too many recursive calls!")
    try:
        return throw_custom_message(count + 1)
    except Exception as e:
        return f"Custom Exception Caught: {e}"

result = throw_custom_message()
print(result)


class MyCustomException(Exception):
    pass

def custom_exception_view():

    try:
        raise MyCustomException("This is a user-defined exception.")
    except MyCustomException as e:
        return f"Caught custom exception: {e}"


def with_finally():
    try:
        a = 10 / 0
    except ZeroDivisionError:
        return HttpResponse("Caught division by zero.")
    finally:
        return "This always executes."
def generate_arithmetic_exception():
    denominator = 0
    if denominator == 0:
        result = "Cannot divide by zero!"
    else:
        result = 10 / denominator
    return f"Result: {result}"

def file_not_found():
    try:
        with open('non_existing_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found error handled!"
    return content


def simulate_class_not_found():
    try:
        __import__('non_existing_module')
    except ModuleNotFoundError:
        return "Simulated ClassNotFoundException (ModuleNotFoundError)"

def simulate_io_exception():
    try:
        with open('/root/protected.txt', 'w') as f:
            f.write("Trying to write")
    except IOError as e:
        return f"IOError occurred: {str(e)}"
class Dummy:
    name = "Test"

def no_such_field():
    d = Dummy()
    try:
        return d.non_existing_field
    except AttributeError:
        return "NoSuchFieldException simulated: Field does not exist"

def exceptions(request):
    arith= arithmetic_without_handling()
    arith_excep=arithmetic_with_handling()
    excep=call_throwing_method()
    multi_excep=multiple_excepts()
    cus_throw=throw_custom_message()
    cus_excep=custom_exception_view()
    with_fina=with_finally()
    gene_arith=generate_arithmetic_exception()
    file_nfound=file_not_found()
    simu_class_not=simulate_class_not_found()
    simu_io=simulate_io_exception()
    no_file=no_such_field()

    context ={
        'arith' : arith,
        'arith_excep' : arith_excep,
        'excep' : excep,
        'multi_excep' : multi_excep,
        'cus_throw' : cus_throw,
        'cus_excep' : cus_excep,
        'with_fina' : with_fina,
        'gene_arith' : gene_arith,
        'file_nfound' : file_nfound,
        'simu_class_not' : simu_class_not,
        'simu_io' : simu_io,
        'no_file' : no_file,

    }
    return render(request, 'p_basics/exceptions.html', context)

class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            self.message = "Default constructor called"
        elif b is None:
            self.message = f"One-argument constructor called with a={a}"
        else:
            self.message = f"Two-argument constructor called with a={a}, b={b}"
class SuperClass:
    def __init__(self, a=None):
        if a is None:
            self.message = "SuperClass default constructor"
        else:
            self.message = f"SuperClass argument constructor with a={a}"

class ChildClass(SuperClass):
    def __init__(self, a=None, b=None):
        if a is None:
            super().__init__()
        else:
            super().__init__(a)
        self.child_message = f"ChildClass constructor with b={b}"

class AccessModifiers:

    def __init__(self):
        self.public_message = "This is public"
        self._protected_message = "This is protected"  # Make sure this is here
        self.__private_message = "This is private"

    def call_private(self):
        return self.__private_message


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = f"Initialized Product: {self.name} at ${self.price}"
    def __str__(self):
        return f"{self.name} - ${self.price}"

def test_constructors():
    obj1 = MyClass()
    obj2 = MyClass(10)
    obj3 = MyClass(10, 20)
    c1 = ChildClass()
    c2 = ChildClass(100, 200)
    obj = AccessModifiers()
    public = obj.public_message
    protected = obj._protected_message
    private = obj.call_private()
    p = Product(name="Laptop", price=1200.00, available=True)


    return obj1, obj2, obj3, c1, c2, public, protected, private, p

def constructors(request):
    obj1, obj2, obj3, c1,c2, public, protected, private, p = test_constructors()
    context = {
        'obj11': obj1,
        'obj22': obj2,
        'obj33': obj3,
        'c1' : c1,
        'c2': c2,
        'public': public,
        'protected': protected,
        'private': private,
        'p': p,

    }
    return render(request, 'p_basics/constructors.html', context)










