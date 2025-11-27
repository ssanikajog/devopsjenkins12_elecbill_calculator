import sys
if len(sys.argv) == 2:
  unit = float(sys.argv[1])
else:
  unit = 120

total = unit * 5

print("Units: ", unit)
print("Total Bill: ", total)
