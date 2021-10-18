import math

p_1_carrot = 108/2115
p_2_carrot = 141/2994
p_carrot = (108+141)/(2115+2994)
n_1 = 2115
n_2 = 2994

numer = p_1_carrot - p_2_carrot
denomer = math.sqrt(p_carrot*(1-p_carrot)*((1/n_1)+(1/n_2)))

Z_c = numer/denomer

print(Z_c)