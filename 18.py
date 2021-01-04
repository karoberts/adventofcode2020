from collections import deque

class Token:
    def __init__(self, vint:int, vop:str):
        self.intval:int = vint
        self.opval:str = vop
        pass

    def __repr__(self):
        return str(self.intval) if self.intval is not None else self.opval

"""
class Node:
    def __init__(self, a:Element, op:str, b:Element):
        self.a = a
        self.op = op
        self.b = b

    def __repr__(self):
        return '{} {} {}'.format(self.a, self.oper, self.b)
"""

def parse(expr):
    cur_num = ''
    tokens:List[Token] = []
    for c in expr:
        if c.isdigit():
            cur_num += c
        else:
            if len(cur_num) != 0:
                tokens.append(Token(int(cur_num), None))
                cur_num = ''
            if c == ' ':
                continue
            if c in ['+', '*', '(', ')']:
                tokens.append(Token(None, c))
    if len(cur_num) != 0:
        tokens.append(Token(int(cur_num), None))
    return tokens

def eval(tokens,pos,depth=0):
    val = None
    oper = None
    tgt = 0
    p = pos
    while p < len(tokens):
        t = tokens[p]
        if t.intval is not None:
            if val is None:
                val = t.intval
            elif oper == '*':
                #print(depth * ' ', '{} * {}'.format(val, t.intval))
                val *= t.intval
            elif oper == '+':
                #print(depth * ' ', '{} + {}'.format(val, t.intval))
                val += t.intval
        elif t.opval in ['*', '+']:
            oper = t.opval
        elif t.opval == '(':
            #print(depth * ' ', '(')
            if val is None:
                (val, p) = eval(tokens, p + 1, depth + 1)
            elif oper == '*':
                (x, p) = eval(tokens, p + 1, depth + 1)
                #print(depth * ' ', '{} * {}'.format(val, x))
                val *= x
            elif oper == '+':
                (x, p) = eval(tokens, p + 1, depth + 1)
                #print(depth * ' ', '{} + {}'.format(val, x))
                val += x
            #print(depth * ' ', ')')
        elif t.opval == ')':
            return (val, p)
        p += 1
    return (val, len(tokens))

def eval2(tokens,pos,depth=0,stopdepth=-1):
    val = None
    oper = None
    tgt = 0
    p = pos
    while p < len(tokens):
        t = tokens[p]
        if t.intval is not None:
            if val is None:
                val = t.intval
            elif oper == '+':
                #print(depth * ' ', '{} + {}'.format(val, t.intval))
                val += t.intval
        elif t.opval == '+':
            oper = t.opval
        elif t.opval == '*':
            oper = t.opval
            (x, p) = eval2(tokens, p + 1, depth, depth - 1)
            val *= x
        elif t.opval == '(':
            #print(depth * ' ', '(')
            if val is None:
                (val, p) = eval2(tokens, p + 1, depth + 1)
            elif oper == '+':
                (x, p) = eval2(tokens, p + 1, depth + 1)
                #print(depth * ' ', '{} + {}'.format(val, x))
                val += x
            #print(depth * ' ', ')')
        elif t.opval == ')':
            return (val, p)
        p += 1

        if depth == stopdepth:
            return (val, p)
    return (val, len(tokens))
                
def infix_to_postfix(expr: str) -> list:
    precedence_order = {'+': 1, '*': 0}
    clean_infix = list(expr.replace(' ', ''))

    i = 0
    postfix = []
    operators = "+*"
    stack = deque()
    while i < len(clean_infix):
        char = clean_infix[i]
        if char in operators:
            if len(stack) == 0 or stack[0] == '(':
                stack.appendleft(char)
                i += 1
            else:
                top_element = stack[0]
                if precedence_order[char] == precedence_order[top_element]:
                    popped_element = stack.popleft()
                    postfix.append(popped_element)
                elif precedence_order[char] > precedence_order[top_element]:
                    stack.appendleft(char)
                    i += 1
                elif precedence_order[char] < precedence_order[top_element]:
                    popped_element = stack.popleft()
                    postfix.append(popped_element)
        elif char == '(':
            stack.appendleft(char)
            i += 1
        elif char == ')':
            top_element = stack[0]
            while top_element != '(':
                popped_element = stack.popleft()
                postfix.append(popped_element)
                top_element = stack[0]
            stack.popleft()
            i += 1
        else:
            postfix.append(char)
            i += 1

    if len(stack) > 0:
        for i in range(len(stack)):
            postfix.append(stack.popleft())

    return postfix

def eval_infix(infix):
    stack = deque()
    val = 0
    for i in infix:
        if i.isdigit():
            stack.appendleft(int(i))
        else:
            v1 = stack.popleft()
            v2 = stack.popleft()
            if i == '*':
                stack.appendleft(v1 * v2)
            else:
                stack.appendleft(v1 + v2)
    return stack.popleft()

"""
expr = '1 + 2 * 3 + 4 * 5 + 6'
expr = '2 * 3 + (4 * 5)'
expr = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
expr = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
#expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2'

infix = infix_to_postfix(expr)
print(infix)
val = eval_infix(infix)
print(val)
quit()

tokens = parse(expr)
print(tokens)
v = eval2(tokens, 0)
print('v', v[0])

quit()
"""

with open("18.txt") as f:
    val = 0
    val2 = 0
    for line in (l.strip() for l in f):
        val += eval(parse(line), 0)[0]
        val2 += eval_infix(infix_to_postfix(line))
    print('part1', val)
    print('part2', val2)
