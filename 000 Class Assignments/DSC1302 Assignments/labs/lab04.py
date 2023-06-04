#  TODO: Define BankAccount class
    # TODO: Define constructor with parameters to initialize instance attributes
    
    # TODO: Define deposit_checking()
    
    # TODO: Define deposit_savings()
    
    # TODO: Define withdraw_checking()
    
    # TODO: Define withdraw_savings()
    
    # TODO: Define transfer_to_savings()

class BankAccount:
    def __init__(self, name, checking_balance=0, saving_balance=0):
        self.checking_balance = checking_balance
        self.savings_balance = saving_balance
        self.name = name



    def withdraw_savings(self, amount):
        if amount > self.savings_balance:
            print('Cannot withdraw more than the amount in your savings account.')
            return False
        
        self.savings_balance -= amount
        print('Successful withdrawal from savings!')
        return True



    def withdraw_checking(self, amount):
        if amount > self.checking_balance:
            print('Cannot withdraw more than the amount in your checking account')
            return False

        self.checking_balance -= amount
        print('Successful withdrawal from checking!')
        return True
    

    def transfer_to_savings(self, balance):
        if balance > self.checking_balance:
            print('Unable to transfer, value is greater than amount in checking account')
            return False
        self.checking_balance -= balance
        self.savings_balance += balance
        print('Successful Transfer!') 
        return True




if __name__ == "__main__":
    account_name = input('Input a name for the account\n')
    account_checking = int(input('Input a checking balance for the account\n'))
    account_saving = int(input('Input an savings balance for the account\n'))
    account = BankAccount("Mickey", account_checking, account_saving)
    # account.checking_balance = 500
    # account.savings_balance = 500
    account.withdraw_savings(100)
    account.withdraw_checking(100)
    account.transfer_to_savings(300)

    print('START OF QUESTION 1-----------------------------------')
    print(account.name)
    print(f'${account.checking_balance:.2f}')
    print(f'${account.savings_balance:.2f}')
    print('END OF QUESTION 1------------------------')



class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes
    
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')
        print(f'   Edition: {self.edition}')
        print(f'   Number of Volumes: {self.num_volumes}')
        
        
    
    
    
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_volumes

    
    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class

if __name__ == "__main__":
    title = input('title: ')
    author = input('author: ')
    publisher = input('publisher: ')
    publication_date = input('publication_date: ')
    
    e_title = input('title: ')
    e_author = input('author: ')
    e_publisher = input('publisher: ')
    e_publication_date = input('pub. date: ')
    edition = input('edition: ')
    num_pages = int(input('num pages: '))
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()