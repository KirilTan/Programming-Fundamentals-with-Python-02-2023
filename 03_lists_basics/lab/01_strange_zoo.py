# Inputs
tail = input()
body = input()
head = input()

# Re-arranging
meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

# Output
print(meerkat)
