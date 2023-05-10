
import subprocess

result = subprocess.run(['ls', '-larth', '/motion/photo'], capture_output=True)

list = result.stdout.decode().splitlines()
list1 = []

for i in range(len(list)):
  if list[i].find('phillip') != -1:
    #print(list[i])
    continue
  else:
    print(list[i])
    #list.pop(i)
    list1.append(i)

print('\n\n')
#print(list)
print(list[-1])
print(list1.reverse())

print('DEMARC')
for i in list1:
  print(i)
  list.pop(i)

bob = list[-1].split()

print(bob[8])

