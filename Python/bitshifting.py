# shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, 
# shifting one bit to the right is like dividing by two
# 17 // 2 → 8 (shifting to the right by one bit is the same as integer division by two)
# 17 * 4 → 68 (shifting to the left by two bits is the same as integer multiplication by four)

var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)