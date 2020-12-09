# A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
# it conforms to the integer vs. float rule.