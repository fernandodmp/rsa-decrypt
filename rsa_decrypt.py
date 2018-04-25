lista = open("info.txt", "r")
info = map(lambda s: int(s.split(":")[1].split(" ")[1]), lista)

info_list = list(info)
print(info_list)

#The encrypted Message
c = info_list[0]
#The prime numbers
p = info_list[1]
q = info_list[2]
#dp = d mod p-1
dp = info_list[3]
#dq = d mod q-1
dq = info_list[4]

#Extended Euclidean Algorithm to find the GCD
def egcd(a, b):
 if a == 0:
     return (b, 0, 1)
 else:
     g, y, x = egcd(b % a, a)
     return (g, x - (b // a) * y, y)


#Computees q^-1 mod p
def modinv(a, m):
 g, x, y = egcd(a, m)
 if g != 1:
     raise Exception('modular inverse does not exist')
 else:
     return x % m


qinv = modinv(q, p)
m1 = pow(c, dp, p)
m2 = pow(c, dq, q)
h = (qinv * (m1 - m2)) % p
#Decrypted message as a int
m = m2 + h * q
#Converts the number to hexcode and remove the 0x from beginning
txt = hex(m).split("0x")[1]
#Iterates of the txt transforming every 2 character into hexadecimal integers then converts it into characters
message = ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])
print(message)
