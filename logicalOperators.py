has_good_income = False
has_good_credit = True
has_criminal_record = False
#can either use and /or /not
if has_good_credit or has_good_income and not has_criminal_record:
    print('Eligible for loan')

# And - all conditions should be true
# Or - at least one condition should be true
# Not - has to be false
