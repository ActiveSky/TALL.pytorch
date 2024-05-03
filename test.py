import argparse


class A:
    def __init__(self):
        self.age = 18
        self.name = 'Alice'
    def setAge(self, age):
        self.age = age
    def setName(self, name):    
        self.name = name
    def getAge(self):
        return self.age
    def getName(self):
        return self.name    

def test_class(model:A):
    model.setAge(20)
    model.setName('Bob')
    # print(model.age, model.name)

def parse_args():
    parser = argparse.ArgumentParser(description='Arg test')
    parser.add_argument("-n",'--name', default='Alice', type=str, help='name of the person')
    parser.add_argument("-a",'--age', default=18, type=int, help='age of the person')
    args = parser.parse_args()
    return args
def print_args(args):
    print(args.name, args.age)
if __name__ == '__main__':
    args = parse_args()
    print("hello world")
    print_args(args)
