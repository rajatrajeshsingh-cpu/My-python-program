def days():
    d=['sun','mon','tue','wed','thu','fri','sat']
    i=0
    while True:
        yield d[i]
        i=(i+1)%7

m=days()

print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
