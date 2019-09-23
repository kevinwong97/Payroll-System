# validation_test.py
# France Cheong
# 20/12/2018

# Import file/class to test
from validation import Validation


def test_is_numeric(validation):
    print("\n1.Testing is_numeric()") 
    
    # True
    assert (validation.is_numeric(10))

    # False
    assert (not validation.is_numeric(10.002))
    assert (not validation.is_numeric("abc"))
    assert (not validation.is_numeric("10abc"))

def test_is_alphabetic(validation):
    print("\n2. Testing is_alphabetic()")

    # True
    assert (validation.is_alphabetic("abc"))

    # False
    assert (not validation.is_alphabetic(10))    
    assert (not validation.is_alphabetic(10.002)) 
    assert (not validation.is_alphabetic("10abc"))

def test_is_alphanumeric(validation):
    print("\n3. Testing is_alphanumeric()")

    # True
    assert (validation.is_alphanumeric(10))  
    assert (validation.is_alphanumeric("abc")) 
    assert (validation.is_alphanumeric("10abc")) 

    # False 
    assert (not validation.is_alphanumeric(10.02))
    assert (not validation.is_alphanumeric("_")) 
    assert (not validation.is_alphanumeric(" "))
    assert (not validation.is_alphanumeric(".")) 

def test_is_phone_number(validation):
    print("\n4. Testing is_phone_number()")

    # True
    assert (validation.is_phone_number("02 9999 9999")) 

    # False
    assert (not validation.is_phone_number("(02) 9999 9999"))
    assert (not validation.is_phone_number("0299999999"))
    assert (not validation.is_phone_number("02-9999-9999"))
    assert (not validation.is_phone_number("02.9999.9999"))
    assert (not validation.is_phone_number("+61 2 9999 9999"))
    assert (not validation.is_phone_number("0413 888 888"))

def test_is_email(validation):
    print("\n5. Testing is_email()")

    # True
    assert  (validation.is_email("xyz@abc.def")) 
    assert (validation.is_email("xyz@abcdef"))

    # False
    assert (not validation.is_email("xyzabcdef"))
    assert (not validation.is_email("@abcdef"))
        

if __name__ == '__main__':
    
    print("\nTesting ...")

    # Instantiate a validation object
    validation = Validation()

    test_is_numeric(validation)

    test_is_alphabetic(validation)

    test_is_alphanumeric(validation)

    test_is_phone_number(validation)

    test_is_email(validation)