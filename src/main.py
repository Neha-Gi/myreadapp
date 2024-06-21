from typing import Optional
from src.db.models.reader  import Reader 

class MenuDisplay:
    @staticmethod
    def display_main_menu():
        print(
            """
        WELCOME TO MY READ APP
        MENU
        ----------
        1.DATA MANIPULATION
        2.DATA QUERY
        00.QUIT
        """
        )

    @staticmethod
    def display_DM_menu():
        print(
            """
        1.INSERT READER
        2.INSERT BOOK
        3.INSERT MYREAD
        99.BACK
        """
                )


class DataInput():
    @staticmethod
    def input_for_reader_insert()-> dict[str,str]:
        username = input('Enter your username: ')
        title = input ('Enter title (Mr,Ms ,Dr):')
        first_name = input ('Enter fist name : ')
        last_name = input("enter last name : ")
        return{
            "username":username,
            "title": title,
            "first_name" : first_name,
            "last_name" : last_name
        }
def main() :
    while True:
        MenuDisplay.display_main_menu()
        option:int = int(input("Choose an option to continue : "))

        if option == 1:
            #TODO:OPERATION FOR MANIPULATION
            while True:
                MenuDisplay.display_DM_menu()
                option:int = int(input("Choose an option to continue : "))

                if option == 1:
                    # TODO:INSERT BOOK
                    reader_detail:dict [str,str] = DataInput.input_for_reader_insert()
                    reader:Optional[Reader] = Reader.insert_data(**reader_detail) 

                    if reader :
                        print(f'Reader with username:{reader.username}inserted succesfully')
                    else:
                        print('Insertion failed')
                elif option ==2:
                    #TODO :INSERT BOOK
                    pass
                elif option == 3:    
                    #TODO :INSERT MYREAD
                    pass
                elif option == 99:
                    break
                else:
                    print('Option not recognized.Please,try again')


                #TODO: OPERATIONS FOR QUERY
                pass

        elif option == 0:
            print('Program is QUITTING')    
            break
        else:
            print('Option not recognized. Please try again')


if __name__ == '__main__':
   main()