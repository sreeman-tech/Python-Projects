import random

lower = "abcdefghijklmnopqustuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols ="!@#$%^&*?.()"

string= lower + upper + numbers + symbols
length = 8
password = "".join(random.sample(string,length))

print("Generated-Password:" + password)