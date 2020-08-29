class Street_fighter():
    def __init__(self, name,life,nomal_attack,special_fight):
        self.name=name
        self.speed=life
        self.strength=nomal_attack
        self.special_fight=special_fight
        self.winning_record=0
        self.lose_record=0


fighter_1 = Street_fighter('chunli', 80, 3, 'fire Kicking')
fighter_2 = Street_fighter('sagat', 90, 4, 'super blade')
fighter_3 = Street_fighter('ryu',85,5,'long blow')
fighter_4 = Street_fighter('bison',95,5,'blue blaze')
selected_fighter_1 = ""
selected_fighter_2 = ""

def select_fighter():
    print('Please select the following fighters.\n1.Chunli\n2.Sagat\n3.Ryu\n4.Bison')
    selection=int(input('Input the number of the first fighter'))


    if selection == 1:
        selected_fighter_1 = fighter_1.name.title()
        print(f'\nThe first fighter is {selected_fighter_1}.')
    elif selection == 2:
        selected_fighter_1 = fighter_2.name.title()
        print(f'\nThe first fighter is {selected_fighter_1}.')
    elif selection == 3:
        selected_fighter_1 = fighter_3.name.title()
        print(f'\nThe first fighter is {selected_fighter_1}.')
    elif selection == 4:
        selected_fighter_1 = fighter_4.name.title()
        print(f'\nThe first fighter is {selected_fighter_1}.')



def select_another_fighter():
    print('\nPlease select the second fighter.\n1.Chunli\n2.Sagat\n3.Ryu\n4.Bison')
    second_selection = int(input('Input the number of the second fighter'))

    if second_selection == 1:
        selected_fighter_2 = fighter_1.name.title()
        print(f'\nThe second fighter is {selected_fighter_2}.')
    elif second_selection == 2:
        selected_fighter_2 = fighter_2.name.title()
        print(f'\nThe second fighter is {selected_fighter_2}.')
    elif second_selection == 3:
        selected_fighter_2 = fighter_3.name.title()
        print(f'\nThe second fighter is {selected_fighter_2}.')
    elif second_selection == 4:
        selected_fighter_2 = fighter_4.name.title()
        print(f'\nThe second fighter is {selected_fighter_2}.')



select_fighter()
select_another_fighter()
