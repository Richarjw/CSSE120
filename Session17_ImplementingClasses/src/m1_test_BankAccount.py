"""
Tests the   BankAccount  class
that is defined in the imported   m1_BankAccount   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Jack Richard.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1_BankAccount as ba
from m1_BankAccount import BankAccount


def main():
    """
    Tests the   BankAccount   class
    defined in the imported   m1_BankAccount   module.

    See   UML_BankAccount.pdf   for BankAccount's UML class diagram.
    """
    # TODO: With your instructor, add code below
    #   (at the appropriate places) to test the   BankAccount   class
    #   that is defined in the imported  m1_BankAccount   module
    #   and whose UML class diagram is shown in   UML_BankAccount.pdf.

    print('--------------------------------------')
    print('Testing __init__:')

    test = BankAccount(500)
    print(test.balance, test.transactions)

    print('\n--------------------------------------')
    print('Testing __repr__:')

    print(test)

    print('\n--------------------------------------')
    print('Testing deposit:')

    test.deposit(500)
    print(test.balance)

    print('\n--------------------------------------')
    print('Testing withdraw:')

    test.withdraw(100)
    print(test.balance)

    print('\n--------------------------------------')
    print('Testing number_of_deposits:')

    print(test.number_of_deposits())

    print('\n--------------------------------------')
    print('Testing number_of_withdrawals:')

    print(test.number_of_withdrawals())

    print('\n--------------------------------------')
    print('Testing number_of_refused_withdrawals:')

    test.withdraw(100000)
    print(test.number_of_refused_withdrawals())

    print('\n--------------------------------------')
    print('Testing transfer_from:')

    test2 = BankAccount(100)
    test.transfer_from(test2)
    print(test.balance)

    print('\n--------------------------------------')
    print('Testing transfer_into:')

    test.transfer_into(test2)
    print(test2.balance)

    print('\n--------------------------------------')
    print('Testing richer:')

    print(test.richer(test2))

    print('\n--------------------------------------')
    print('Testing transfer_to_new_account:')

    account = test2.transfer_to_new_account()
    print(account)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
