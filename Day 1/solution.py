from collections import Counter

a, b = [], []
with open('input.txt', 'r') as file:
    for line in file:
        l = line.replace('\n', '').split()
        a.append(int(l[0]))
        b.append(int(l[1]))

def find_distance_between_lists(a, b):
    return sum(list(map(lambda x, y: abs(x - y), sorted(a), sorted(b))))

def compute_similarity_score(a, b):
    c = Counter(b)
    return sum(map(lambda x: x * c[x], a))
    
print(find_distance_between_lists(a, b))
print(compute_similarity_score(a, b))