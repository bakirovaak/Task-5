class BankAccount:
    """Класс для управления банковским счётом."""

    def __init__(self, owner: str, account_number: str):
        """Создание банковского счёта с начальным балансом 0.0."""
        self.owner = owner
        self.account_number = account_number
        self._balance = 0.0

    @property
    def balance(self) -> float:
        """Получить текущий баланс счёта."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Пополнить счёт на указанную сумму."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Снять денежные средства со счёта."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте.")
        self._balance -= amount

    def transfer(self, target_account: "BankAccount", amount: float) -> None:
        """Перевести денежные средства на другой счёт."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Счёт получателя должен быть экземпляром BankAccount.")
        
        # Снятие выполнит проверки суммы и баланса
        self.withdraw(amount)
        target_account.deposit(amount)

    def is_empty(self) -> bool:
        """Проверить, является ли счёт пустым (баланс равен нулю)."""
        return self._balance == 0