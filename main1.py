#FOR VS WHILE
import time


def forloop():
  for i in range(100):
    print(i)


def whileloop():
  i = 0
  while i < 100:
    i += 1
    print(i)


init1 = time.time()
forloop()
t1 = time.time() - init1

init2 = time.time()
whileloop()
t2 = time.time() - init2

print(f"For loop time {t1:.5f} sec")
print(f"While loop time {t2:.5f} sec")
if t1 < t2: print("(For loop takes less time than while loop)")
else: print("(While loop takes less time than for loop)")