# p,q=3,7
# n=p*q
# fi=(p-1)*(q-1)
# e=5
# test=5
# d=(test*e)%fi

# import struct

# # f = open("text.txt", 'rb')
# file = open("png.png", 'rb')
# # text = ''
# for b in file:
# 	# text += int.from_bytes(b, byteorder='big')
# 	print(int.from_bytes(b, byteorder='big'))
# 	print()


# def sqrt(n, q):
#     assert n < q
#     for i in range(1, q):
#         if i * i % q == n:
#             return (i, q - i)
#         pass
#     raise Exception("not found")

# x, a, b, q = 7, 1, 18, 19
# ysqrt = (x ** 3 + a * x + b) % q
# print(ysqrt)
# y, yreverse = sqrt(ysqrt, q)
# print(y, yreverse)

# def egcd(a, b):
# 	s0, s1, t0, t1 = 1, 0, 0, 1
# 	while b > 0:
# 		print(s0,s1,t0,t1)
# 		q, r = divmod(a, b)
# 		a, b = b, r
# 		s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
# 		pass
# 	return s0, t0, a

# result = egcd(240, 46)
# print(result)