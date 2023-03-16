import os
import file
import listfunk
import UI



def main():
    os.system('cls')
    ui.show_menu()
    try:
        choice = ui.choice_menu()
        print(choice)
        if choice==7:
            print(file.read_fale('data.csv'))

    except Exception as ex:
        print(str(ex))
        input()





        main()
