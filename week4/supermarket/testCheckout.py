import pytest
from supermarketcheckout import Checkout

def test_instantiateCheckoutClass():
    co = Checkout()

def test_addItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)

def test_addItem():
    co = Checkout()
    co.addItem("a")

def test_calculateTotal():
    co = Checkout()
    co.addItemPrice("a", 1)
    co.addItem("a")
    assert co.calculateTotal() == 1

def test_getCorrectTotalMultipleItems():
    co = Checkout()
    co.addItemPrice("a", 1)
    co.addItemPrice("b", 2)
    co.addItem("a")
    co.addItem("b")
    assert co.calculateTotal() == 3

def test_addDiscount():
    co = Checkout()
    co.addDiscount("a", 3, 2)

def test_canApplyDiscount():
    co = Checkout()
    co.addDiscount("a", 3, 2)
    co.addItem("a")
    co.addItem("a")
    co.addItem("a")

    assert co.calculateTotal() == 2

def test_ExceptionNoItem():
    co = Checkout()
    with pytest.raises(Exception):
        co.addItem("c")







