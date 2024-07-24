#<p>An irrational decimal fraction is created by concatenating the positive integers:
#$$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$</p>
#<p>It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.</p>
#<p>If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
#$$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$</p>

con = ""
i = 1
val = 1
conval = ""
d = [10**i for i in range(1,7)]

while len(con) < 1000000:
    con += str(i)
    i += 1

for i in d:
    conval += con[i-1]
    val *= int(con[i-1])

print(val)