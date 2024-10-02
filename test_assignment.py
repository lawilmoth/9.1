import unittest
from assignment import Cat, create_cat, change_cat_age, BankAccount, create_bank_account, BankAccount2, BankAccount3, create_bank_account3

class TestAssignment(unittest.TestCase):

    def test_cat_class(self):
        cat = Cat("Whiskers", 3, "black")
        self.assertEqual(cat.name, "Whiskers")
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.color, "black")

    def test_create_cat(self):
        cat = create_cat()
        self.assertEqual(cat.name, "Whiskers")
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.color, "black")

    def test_change_cat_age(self):
        cat = Cat("Whiskers", 3, "black")
        change_cat_age(cat)
        self.assertEqual(cat.age, 4)

    def test_bank_account_class(self
                                ):
        account = BankAccount("123456", "Mr. Wilmoth")
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.account_holder, "Mr. Wilmoth")
        self.assertEqual(account.balance, 0)

    def test_create_bank_account(self):
        account = create_bank_account()
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.account_holder, "Mr. Wilmoth")
        self.assertEqual(account.balance, 0)

    def test_bank_account2_class(self):
        account = BankAccount2("123456", "Mr. Wilmoth")
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.account_holder, "Mr. Wilmoth")
        self.assertEqual(account.balance, 0)
        new_balance = account.deposit(100)
        self.assertEqual(new_balance, 100)
        self.assertEqual(account.balance, 100)

    def test_bank_account3_class(self):
        account = BankAccount3("123456", "Mr. Wilmoth")
        self.assertEqual(account.account_number, "123456")
        self.assertEqual(account.account_holder, "Mr. Wilmoth")
        self.assertEqual(account.balance, 0)
        account.deposit(100)
        self.assertEqual(account.balance, 100)
        new_balance = account.withdraw(50)
        self.assertEqual(new_balance, 50)
        self.assertEqual(account.balance, 50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

    def test_create_bank_account3(self):
        account = create_bank_account3()
        self.assertEqual(account.account_number, "314159")
        self.assertEqual(account.account_holder, "Mr. Orlando")
        self.assertEqual(account.balance, 50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

if __name__ == '__main__':
    unittest.main()
    