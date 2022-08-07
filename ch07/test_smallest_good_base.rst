>>> from ch07 import smallest_good_base_math as smallest_good_base
>>> from ch07 import good_base_math as good_base

# start snippet gb
>>> good_base(13, 3)
True

>>> good_base(13, 2)
False

>>> good_base(4681, 8)
True

# end snippet gb


# start snippet sgb
>>> smallest_good_base("13")
'3'

>>> smallest_good_base("4681")
'8'

>>> smallest_good_base("1000")
'999'

# end snippet sgb
