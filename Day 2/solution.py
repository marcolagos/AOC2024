from copy import deepcopy

reports = [[*map(int, l.split())] for l in open('input.txt')]

def isSafe(l):
    g = 1 if l[0] < l[-1] else -1
    l.append(l[-1]+g)
    for i in range(len(l) - 1):
        d = l[i+1]*g - l[i]*g
        if d < 1 or d > 3:
            return 0
    return 1

def countSafeReports(r):
    return sum(map(lambda x: isSafe(x), r))

def isSafeWithError(l, e=0):
    l = list(l)
    def IsIncreasing(q):
        c = 0
        for i in range(1, len(q) - 1):
            c += 1 if q[i] > q[i-1] else -1
        return c > 0
    c, g = 0, 1 if IsIncreasing(l) else -1
    z = []
    l.append(l[-1]+g)
    for i in range(len(l) - 1):
        d = l[i+1]*g - l[i]*g
        if d < 1 or d > 3:
            c += 1
            z.append(i)
            if c > e:
                return 0, []
    if c > 0:
        return 0, z
    return 1, z

def countSafeReportsWithProblemDampener(r):
    m = {i: isSafeWithError(r[i], 2) for i in range(len(r))}
    for k, v in m.items():
        z = v[1]
        if len(z):
            kc = deepcopy(r[k])
            if len(z) == 1:
                if z[0] == len(kc) - 2:
                    kc.pop(z[0]+1)  
                else:
                    kc.pop(z[0])
            elif len(z) == 2 and z[1] - z[0] == 1:
                kc.pop(z[1])
            m[k] = isSafeWithError(kc, 0)
    return sum(map(lambda x: m[x][0], m))

print(countSafeReports(deepcopy(reports)))
print(countSafeReportsWithProblemDampener(deepcopy(reports)))