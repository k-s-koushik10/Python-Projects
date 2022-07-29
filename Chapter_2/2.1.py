#2.1 - Covering a** with assertions

#Used as a debugging tool only for finding unknown error not for signalling expected errors/handling run-time errors

def apply_disc(prod,disc):
    price = int(prod['price'] * (1.0 - disc))
    assert 0 <= price <= prod['price']
    return price

product = {'name' : 'Shoes' , 'price' : 14000}
print(apply_disc(product,0.25))
#print(apply_disc(product,2.0)) --> AssertionError

#Common pitfalls #1 - Dont's user Assert for Data validation. Assert functions can be disabled by -0 or -00 command and hence assert does not provide us with error if unexpected, eading to bugs and security issue.

#Common pitfalls #2 - Asserts that never fail like below

counter = 5
assert counter == 10,"This Never Failed"

