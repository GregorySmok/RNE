import string
alf = string.digits + string.ascii_uppercase
alf = alf[:29]
for x in alf:
    d = int(f'42{x}158', 29) + int(f'16{x}234', 29)
    if d % 28 == 0:
        print(d/28)
        break
