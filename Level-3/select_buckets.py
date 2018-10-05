def select_buckets(n, k, b, selections):
  if not (n or b):
    return selections

  for val in range(k, -1, -1):
    if n - val >= 0:
      selections.append(val)
      return select_buckets(n - val, k - 1, b - 1, selections)


selections = []
print select_buckets(12, 7, 2, selections)
