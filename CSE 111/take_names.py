from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name('sally','brown') == 'brown; sally'
    assert make_full_name('emma','ward') == 'ward; emma'

def test_extract_given_name():
    assert extract_given_name ('brown; sally') == 'sally'
    assert extract_given_name('ward; emma') == 'emma'

def test_extract_family_name():
    assert extract_family_name('brown; sally') == 'brown'
    assert extract_family_name('ward; emma') == 'ward'



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])