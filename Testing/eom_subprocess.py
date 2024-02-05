import subprocess


cmd = 'lscpu | grep "CPU(s):"'

result = subprocess.check_output(["ssh"] + ['192.168.68.10', cmd]).decode("utf-8").strip()
##result = subprocess.check_output(["ssh"] + ['192.168.68.10', cmd])

a = result.split('\n')

print(len(result))
print(len(a))

#print(result[0])
#print(result[1])
#print(result[10])

print(f"result: {result}")
print('\n')

print(a[0])

print(a[1])
print('\n')

a[1] = a[1][:0] + "  " + a[1][0:]
print(a[1])

x = a[0].split()
print(len(x))
print(x[0])
print(x[1])
