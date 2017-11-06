from sidekick import opt
from types import SimpleNamespace
from getch import getche

ctx = SimpleNamespace(tokens=[], indent=1)

def construct(ctx, source):

    data = [0]
    ptr = 0
    code_ptr = 0
    breakpoints = []

    while code_ptr < len(source):
        cmd = source[code_ptr]

        if cmd == '+':
            data[ptr] = (data[ptr] + 1) % 256
            x = ptr
            # ctx.tokens.append('data[' + str(x) + '] += 1;\n')
        elif cmd == '-':
            data[ptr] = (data[ptr] - 1) % 256
            x = ptr
            # ctx.tokens.append('data[' + str(x) + '] -= 1;\n')
        elif cmd == '>':
            ptr += 1
            if ptr >= len(data):
                data.append(0)
        elif cmd == '<':
            ptr -= 1
        elif cmd == '.':
            ctx.tokens.append('cout << "' + chr(data[ptr]) + '";\n')
        elif cmd == ',':
            data[ptr] = ord(getche())
            ctx.tokens.append('cin >> data["' + str(x) + '"];\n')
        elif cmd == '[':
            if data[ptr] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_ptr += 1
                    if source[code_ptr] == '[':
                        open_brackets += 1
                    elif source[code_ptr] == ']':
                        open_brackets -= 1

            else:
                breakpoints.append(code_ptr)
        elif cmd == ']':
            # voltar para o colchete correspondente
            code_ptr = breakpoints.pop() - 1

        code_ptr += 1

    return ''.join(ctx.tokens)


source = '''

HELLO BRAINF*CK!

8: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
>
5: +++++++++++++++++++++++++++++++++++++++++++++++++++++.
<

[->+<]

>
.

'''

print(construct(ctx, source))
