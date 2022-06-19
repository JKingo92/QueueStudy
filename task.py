from celerytask import add
import time

result = []
for i in range(1, 10):
    print(i)
    result.append(add.delay(10, i).get())

print(result)
