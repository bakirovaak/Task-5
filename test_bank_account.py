import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Создание базовых тестовых счетов перед каждым тестом."""
        self.account1 = BankAccount("Алексей", "ACC-1001")
        self.account2 = BankAccount("Мария", "ACC-2002")

    def test_creation(self):
        """Проверка создания счёта с нулевым балансом."""
        self.assertEqual(self.account1.owner, "Алексей")
        self.assertEqual(self.account1.account_number, "ACC-1001")
        self.assertEqual(self.account1.balance(), 0.0)
        self.assertTrue(self.account1.is_empty())

    def test_deposit_success(self):
        """Проверка корректного пополнения счёта."""
        self.account1.deposit(1000.0)
        self.assertEqual(self.account1.get_balance(), 1000.0)
        self.assertFalse(self.account1.is_empty())

    def test_deposit_negative_or_zero_raises_error(self):
        """Проверка ошибки при пополнении на нулевую или отрицательную сумму."""
        with self.assertRaises(ValueError):
            self.account1.deposit(0)
        with self.assertRaises(ValueError):
            self.account1.deposit(-500)

    def test_withdraw_success(self):
        """Проверка успешного снятия средств."""
        self.account1.deposit(1000.0)
        self.account1.withdraw(400.0)
        self.assertEqual(self.account1.get_balance(), 600.0)

    def test_withdraw_insufficient_funds_raises_error(self):
        """Проверка ошибки при попытке снять больше имеющегося баланса."""
        self.account1.deposit(500.0)
        with self.assertRaises(ValueError):
            self.account1.withdraw(600.0)
        # Состояние счёта не должно измениться
        self.assertEqual(self.account1.get_balance(), 500.0)

    def test_withdraw_negative_or_zero_raises_error(self):
        """Проверка ошибки при попытке снять отрицательное значение."""
        self.account1.deposit(500.0)
        with self.assertRaises(ValueError):
            self.account1.withdraw(-100)

    def test_transfer_success(self):
        """Проверка успешного перевода между счетами."""
        self.account1.deposit(1000.0)
        self.account1.transfer(self.account2, 300.0)

        self.assertEqual(self.account1.get_balance(), 700.0)
        self.assertEqual(self.account2.get_balance(), 300.0)

    def test_transfer_insufficient_funds_leaves_accounts_unchanged(self):
        """Проверка: если перевод невозможен, балансы счетов не меняются."""
        self.account1.deposit(200.0)
        with self.assertRaises(ValueError):
            self.account1.transfer(self.account2, 500.0)

        # Состояния обоих счетов не меняются
        self.assertEqual(self.account1.get_balance(), 200.0)
        self.assertEqual(self.account2.get_balance(), 0.0)

    def test_is_empty(self):
        """Проверка работы флага пустого счёта."""
        self.assertTrue(self.account1.is_empty())
        self.account1.deposit(100.0)
        self.assertFalse(self.account1.is_empty())
        self.account1.withdraw(100.0)
        self.assertTrue(self.account1.is_empty())


if __name__ == "__main__":
    unittest.main()