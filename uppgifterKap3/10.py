number = 8

if number < 5:
    print('Less than 5')
if number < 10:
    print('Less than 10')
if number < 100:
    print('Less than 100')

# All conditions are checked, even if earlier ones are true.
# Multiple outputs can happen.
# Use this when more than one condition can be true and all should be evaluated.

if number < 5:
    print('Less than 5')
elif number < 10:
    print('Less than 10')
elif number < 100:
    print('Less than 100')

# Only the first true condition runs, the rest are skipped.
# Use this when conditions are mutually exclusive