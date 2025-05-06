def f(pos_only_1, /, pos_or_kwd, *, kwd_only_1):
    print("Positional-only argument:", pos_only_1)
    print("Positional-or-keyword argument:", pos_or_kwd)
    print("Keyword-only argument:", kwd_only_1)

f(1, 2, kwd_only_1="Hello")