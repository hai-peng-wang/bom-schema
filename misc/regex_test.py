import re

pattern = re.compile("^(0|[1-9][0-9]*|[0-9]*[A-Za-z-]+[0-9A-Za-z-]*)$")
#pattern = re.compile("^[0-9]*$")

def test_string(s, expected):
    if pattern.match(s):
        if expected:
          print("pass: %s" % s)
        else:
          print("fail: %s" % s)
    else:
        if not expected:
          print("pass: %s" % s)
        else:
          print("fail: %s" % s)

test_string("0", True)
test_string("1", True)
test_string("2", True)
test_string("10", True)
test_string("90", True)
test_string("900", True)
test_string("933", True)
test_string("800", True)
test_string("888", True)
test_string("alpha", True)
test_string("alpha01", True)
test_string("blah08", True)
test_string("10alpha", True)
test_string("01alpha", True)
test_string("01alpha01", True)
test_string("08blah08", True)
test_string("-", True)
test_string("--", True)
test_string("a-x", True)
test_string("a--x", True)
test_string("8-blah", True)
test_string("08-blah", True)
test_string("08-08", True)
test_string("x08-08x", True)

test_string("xxx%%", False)
test_string("^^", False)
test_string("hello.", False)
test_string("..", False)
test_string(".", False)
test_string("*", False)
test_string("#", False)
test_string("$", False)
test_string("1!", False)
test_string("01", False)
test_string("001", False)
test_string("0808", False)

