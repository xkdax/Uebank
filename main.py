if __name__ == '__main__':
    import random


    def generate():
        _number = '400000'
        _sum = 0
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
                  '2. Log out',
                  '0. Exit',
                  sep='\n')
            _choice = input()
            if _choice == '1':
                print('There is no money')
            elif _choice == '2':
                print(f'Logging out',
                      ' ',
                      sep='\n')
                return 2
            elif _choice == '0':
                return 3


    random.seed()
    cards = {}
    # -------- S T A R T --------

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
            cards = {iks: igrik}
            print(f' ',
                  'Your card has been created',
                  'Your card number:',
                  iks,
                  'Your card PIN:',
                  igrik,
                  ' ',
                  sep='\n')
        elif main_choice == '2':
            print('Enter your card number:')
            inp_number = input().strip()
            print('Enter your PIN:')
            inp_pin = input().strip()
            if inp_number in cards and cards.get(inp_number) == inp_pin:
                print('You have successfully logged in!')
                in_acc_result = in_acc()
                if in_acc_result == 2:
                    continue
                elif in_acc_result == 3:
                    print('Bye')
                    break
            else:
                print(f'No way dude',
                      ' ',
                      sep='\n')
