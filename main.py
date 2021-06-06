if __name__ == '__main__':
    import random
    import sqlite3

    def lyhn(_nomer):
        _hui = _nomer[-1]
        _sum = 0
        if len(_nomer) <= 15:
            return False
        else:
            for _i in range(0, 15):
                if _i % 2 == 0:
                    if int(_nomer[_i]) * 2 >= 10:
                        _sum += int(_nomer[_i]) * 2 - 9
                    else:
                        _sum += int(_nomer[_i]) * 2
                else:
                    _sum += int(_nomer[_i])
            return _hui == str((10 - _sum % 10) % 10)


    def generate():
        _number = '400000'
        _sum = 0
        while True:
            for _ in range(0, 9):
                _number += str(random.randint(0, 9))
            for _i in range(0, 15):
                if _i % 2 == 0:
                    if int(_number[_i]) * 2 >= 10:
                        _hui = int(_number[_i]) * 2 - 9
                    else:
                        _hui = int(_number[_i]) * 2
                else:
                    _hui = int(_number[_i])
                _sum += _hui
            _number += str((10 - _sum % 10) % 10)
            cur.execute('select number from card where number = \"{0}\" ;'.format(_number))
            if cur.fetchone():
                continue
            else:
                break
        return _number


    def generate_pin():
        _pin = ''
        for _ in range(0, 4):
            _pin += str(random.randint(0, 9))
        return _pin


    def in_acc():
        while True:
            print(' ',
                  '1. Balance',
                  '2. Add income',
                  '3. Do transfer',
                  '4. Close account',
                  '5. Log out',
                  '0. Exit',
                  sep='\n')
            _choice = input()
            if _choice == '1':  # BALANCE
                cur.execute(
                    'select balance from card where number = \"{0}\" ;'.format(inp_number))
                (_babos,) = cur.fetchone()
                print('')
                print('Balance: ' + str(_babos))
            # -------------------------------------
            elif _choice == '2':  # ADD INCOME
                _inc = int(input('Enter income: '))
                cur.execute(
                    'update card set balance = balance + {1} where number = \"{0}\" ;'.format(inp_number, _inc))
                conn.commit()
                print('Income was added!')
            # -------------------------------------
            elif _choice == '3':  # DO TRANSFER
                _trans = input('Enter card number: ').strip()
                if inp_number == _trans:
                    print('Ti dyrak')
                    continue
                if lyhn(_trans):
                    cur.execute('select number from card where number = \"{0}\" ;'.format(_trans))
                    if cur.fetchone():
                        _trans_value = int(input('Enter how much money you want to transfer: '))
                        cur.execute(
                            'select balance from card where number = \"{0}\" ;'.format(inp_number, inp_pin))
                        (_babos,) = cur.fetchone()
                        if _trans_value > _babos:
                            print('Not enough money!')
                            continue
                        else:
                            cur.execute(
                                'update card set balance = balance - {0} where number = \"{1}\" ;'.format(
                                    _trans_value, inp_number))
                            cur.execute(
                                'update card set balance = balance + {0} where number = \"{1}\" ;'.format(
                                    _trans_value, _trans))
                            conn.commit()
                            print('Success!')
                    else:
                        print('Such a card does not exist ebalai')
                else:
                    print('Probably you made a mistake in the card number. Please try again ebalai!')
                    continue
            # -----------------------------------
            elif _choice == '4':  # CLOSE ACCOUNT
                print('And it\'s gone!')
                cur.execute('delete from card where number = \"{0}\" ;'.format(inp_number))
                conn.commit()
                return 2
            # -----------------------------------
            elif _choice == '5':  # LOG OUT
                print(f'Logging out',
                      ' ',
                      sep='\n')
                return 2
            # -----------------------------------
            elif _choice == '0':  # EXIT
                return 3


    random.seed()
    cards = {}
    # -------- S T A R T --------

    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()

    cur.execute('create table if not exists card (id integer, number TEXT,'
                'pin TEXT,' 
                'balance integer default 0'
                ');')

    while True:
        print(f'1. Create an account',
              '2. Log into account',
              '0. Exit',
              sep='\n')
        main_choice = input().strip()
        if main_choice == '0':
            print('Bye')
            break
        if main_choice == '1':
            iks = generate()
            igrik = generate_pin()
            cur.execute('insert into card (number, pin) values ("' + iks + '", "' + igrik + '") ;')
            conn.commit()
            print(f' ',
                  'Your card has been created',
                  'Your card number:',
                  iks,
                  'Your card PIN:',
                  igrik,
                  ' ',
                  sep='\n')
        elif main_choice == '2':
            inp_number = input('Enter your card number: ').strip()
            inp_pin = input('Enter your PIN: ').strip()
            cur.execute(
                'select number, pin from card where number = \"{0}\" and pin = \"{1}\" ;'.format(inp_number, inp_pin))
            if cur.fetchone():
                print('You have successfully logged in!')
                in_acc_result = in_acc()
                if in_acc_result == 2:
                    continue
                elif in_acc_result == 3:
                    print('Bye')
                    break
            else:
                print(f'Huewrong',
                      ' ',
                      sep='\n')
    cur.close()
    conn.close()
