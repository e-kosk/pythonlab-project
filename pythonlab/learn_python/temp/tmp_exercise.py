def check_palindrome(x):
  y = "".join(x.upper().split())
  return y == y[::-1]