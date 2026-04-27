import sys

class Variable:
    def __init__(self, value, type_str):
        self.value = value
        self.type_str = type_str 

class VirtualMachine:
    def __init__(self, input_path):
        self.memory = {}
        self.stack = []
        self.instructions = self.load_instructions(input_path)
        self.labels = {}
        self.pc = 0  
        self.preprocess_labels()

    def load_instructions(self, ipath):
        with open(ipath, "r") as f:
            lines = f.readlines()
            res = []

            for line in lines:
                res.append(line.strip())

            return res 

    def preprocess_labels(self):
        for i, instruction in enumerate(self.instructions):
            if instruction.startswith('label'):
                parts = instruction.split()
                self.labels[int(parts[1])] = i

    def parse_value(self, type_str, raw):
        if type_str == 'I': return int(raw)
        if type_str == 'F': return float(raw)
        if type_str == 'B': return raw == 'true'
        if type_str == 'S': return raw  

    def run(self):
        self.pc = 0
        while self.pc < len(self.instructions):
            instruction = self.instructions[self.pc]
            parts = instruction.split(' ', 2)
            op = parts[0].lower()

            if op == 'push':
                type_str = parts[1]
                raw = parts[2]
                self.stack.append(Variable(self.parse_value(type_str, raw), type_str))

            elif op == 'pop':
                self.stack.pop()

            elif op == 'load':
                name = parts[1]
                if name not in self.memory:
                    raise Exception(f'Variable {name} not found!')
                self.stack.append(self.memory[name])

            elif op == 'save':
                name = parts[1]
                self.memory[name] = self.stack.pop()

            elif op == 'add':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value + right.value, left.type_str))

            elif op == 'sub':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value - right.value, left.type_str))

            elif op == 'mul':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value * right.value, left.type_str))

            elif op == 'div':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value / right.value, 'F'))

            elif op == 'mod':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value % right.value, 'I'))

            elif op == 'uminus':
                val = self.stack.pop()
                self.stack.append(Variable(-val.value, val.type_str))

            elif op == 'concat':
                right = self.stack.pop()
                left = self.stack.pop()

                l = left.value.strip('"')
                r = right.value.strip('"')
                self.stack.append(Variable(f'"{l}{r}"', 'S'))

            elif op == 'and':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value and right.value, 'B'))

            elif op == 'or':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value or right.value, 'B'))

            elif op == 'not':
                val = self.stack.pop()
                self.stack.append(Variable(not val.value, 'B'))

            elif op == 'gt':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value > right.value, 'B'))

            elif op == 'lt':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value < right.value, 'B'))

            elif op == 'eq':
                right = self.stack.pop()
                left = self.stack.pop()
                self.stack.append(Variable(left.value == right.value, 'B'))

            elif op == 'itof':
                val = self.stack.pop()
                self.stack.append(Variable(float(val.value), 'F'))

            elif op == 'label':
                pass  

            elif op == 'jmp':
                self.pc = self.labels[int(parts[1])]
                continue  

            elif op == 'fjmp':
                val = self.stack.pop()
                if not val.value:
                    self.pc = self.labels[int(parts[1])]
                    continue

            elif op == 'print':
                n = int(parts[1])
                items = self.stack[-n:]
                del self.stack[-n:]
                for item in items:
                    if item.type_str == 'S':
                        print(item.value.strip('"'), end=' ')

                    elif item.type_str == 'B':
                        print('true' if item.value else 'false', end=' ')

                    elif item.type_str == 'F':
                        print(f'{item.value:g}', end=' ')

                    else:
                        print(item.value, end=' ')
                print() 

            elif op == 'read':
                type_str = parts[1]
                raw = input()
                self.stack.append(Variable(self.parse_value(type_str, raw), type_str))

            self.pc += 1

def project_exec(instructions_file):
    machine = VirtualMachine(instructions_file)
    machine.run()

if __name__ == '__main__':
    instructions_file = sys.argv[1]
    project_exec(instructions_file)