a = [2, 5, 7,3,4]
second = 0

biggest = max(a)

for i in range(0,a.len):
  if(a[i] != biggest): 
    second = a[i] if a[i] > second else second

print(biggest)
print(second)
