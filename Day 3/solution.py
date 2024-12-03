import re 

data = ''.join([str(l) for l in open('input.txt')])

def sum_mul(s):
    return sum(int(n[0]) * int(n[1]) for m in re.findall(r'mul\([0-9]+,[0-9]+\)', s) for n in [re.findall(r'[0-9]+', m)])

def sum_mul_do_dont(s):
    t = 0
    do, dont = True, False
    for a, b, c in re.findall(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", s):
        if a and do:
            t += sum_mul(a)
            continue
        do = bool(b) or (do and not bool(c))
        dont = bool(c) or (dont and not bool(b))
    return t

print(sum_mul(data))
print(sum_mul_do_dont(data))
