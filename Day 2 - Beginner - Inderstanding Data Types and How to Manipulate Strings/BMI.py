
height = input()
weight = input()

weighy_as_int = int(weight)
height_as_int = float(height)

bmi = weighy_as_int / height_as_int ** 2

print( bmi )