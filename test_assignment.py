import unittest
from assignment import Cat, create_cat, change_cat_age, BankAccount, create_bank_account, BankAccount2, BankAccount3, create_bank_account3

import pytest

class TestAssignment:

    def test_cat_class(self):
        cat = Cat("Whiskers", 3, "black")
        assert cat.name == "Whiskers"
        assert cat.age == 3
        assert cat.color == "black"

    def test_create_cat(self):
        cat = create_cat()
        assert cat.name == "Whiskers"
        assert cat.age == 3
        assert cat.color == "black"

    def test_change_cat_age(self):
        cat = Cat("Whiskers", 3, "black")
        change_cat_age(cat)
        assert cat.age == 4

    def test_bank_account_class(self):
        account = BankAccount("123456", "Mr. Wilmoth")
        assert account.account_number == "123456"
        assert account.account_holder == "Mr. Wilmoth"
        assert account.balance == 0

    def test_create_bank_account(self):
        account = create_bank_account()
        assert account.account_number == "123456"
        assert account.account_holder == "Mr. Wilmoth"
        assert account.balance == 0

    def test_bank_account2_class(self):
        account = BankAccount2("123456", "Mr. Wilmoth")
        assert account.account_number == "123456"
        assert account.account_holder == "Mr. Wilmoth"
        assert account.balance == 0
        new_balance = account.deposit(100)
        assert new_balance == 100
        assert account.balance == 100

    def test_bank_account3_class(self):
        account = BankAccount3("123456", "Mr. Wilmoth")
        assert account.account_number == "123456"
        assert account.account_holder == "Mr. Wilmoth"
        assert account.balance == 0
        account.deposit(100)
        assert account.balance == 100
        new_balance = account.withdraw(50)
        assert new_balance == 50
        assert account.balance == 50
        with pytest.raises(ValueError):
            account.withdraw(100)

    def test_create_bank_account3(self):
        account = create_bank_account3()
        assert account.account_number == "314159"
        assert account.account_holder == "Mr. Orlando"
        assert account.balance == 50
        with pytest.raises(ValueError):
            account.withdraw(100)

if __name__ == '__main__':
    unittest.main()
