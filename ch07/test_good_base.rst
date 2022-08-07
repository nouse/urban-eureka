>>> from ch07 import good_base, smallest_good_base

# start snippet test
>>> good_base(13, 3)
True

>>> good_base(13, 2)
False

>>> good_base(4681, 8)
True

# end snippet test


# start snippet test_sgb
>>> smallest_good_base("13")
'3'

>>> smallest_good_base("4681")
'8'

>>> smallest_good_base("1000")
'999'

# end snippet test_sgb
