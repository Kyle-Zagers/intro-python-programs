a = input()

area_code, prefix, line_num = a.split()
# or area_code = a.split()[0], line_num = a.split()[1], ect.

area_code = int(area_code)
prefix = int(prefix)
line_num = int(line_num)

print("Country  Phone Number")
print("-"*7 + "  " + "-"*12)
print(f'U.S.     +1 ({area_code}){prefix}-{line_num}')
print(f'Brazil   +55 ({area_code}){prefix+100}-{line_num}')
print(f'Croatia  +385 ({area_code}){prefix}-{line_num+50}')
print(f'Egypt    +20 ({area_code+30}){prefix}-{line_num}')
print(f'France   +33 ({prefix}){area_code}-{line_num}')


# substring:
# s = "5554572345"
# print(s[0:3])