def check_palindrome(x):
  x = "".join(x.upper().split())
  return x == x[::-1]