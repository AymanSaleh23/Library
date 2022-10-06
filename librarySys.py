# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:58:45 2022

@author: as292
"""
state = ("Idle", "Rented",  "Not found")
bookNumbers = 0

books = {
 
    }

while (True):
    print("---------------------------------")
    print("1. View All Available Books")
    print("2. Add Book")
    print("3. Modify Book")
    print("4. Test Book state")
    print("5. Exit")
    print("---------------------------------")
    
    choice = str(input("Choice: "))
    
    if choice == '1':
        for i in books.values():
            print(i)
    
    elif choice == '2':
        bookName = str(input("Get Book Name : ")).upper()
        bookPages = str(input("Get Book Pages: "))
        bookAuther = str(input("Get Book Auther: ")).upper()
        bookNumbers = bookNumbers +1
        books[bookNumbers] = [bookName, bookPages, bookAuther, state[0] ]
        
        print ("Book is added Succssfully"+ str(books[bookNumbers]))
        
        
    elif choice == '3':
        modify = int(input("Id of Book to modify"))
        
        if modify in books.keys():
            print("---------------------------------")
            print("1. Modify Name")
            print("2. Modify Pages")
            print("3. Modify Auther")
            print("---------------------------------")
            
            modifyChoice = str(input("Choice: "))
    
            if modifyChoice == '1':
                modifyName = str(input("New Name: ")).upper()
                books[modify] == modifyName
                print("Book name Updated")
                
            elif modifyChoice == '2':
                modifyPage = str(input("New Pages: "))
                books[modify] == modifyPage
                print("Book Page Updated")
                
            elif modifyChoice == '3':
                modifyAuther= str(input("New Auther: "))
                books[modify] == modifyAuther
                print("Book Auther Updated")
        
            else:
                print("Book isn't Found")
                
                
                
    elif choice == '4':
        test = int(input("Id of Book to Get Status"))
        if test in books.keys():
            print (books[test][3])
        else:
             print("Book isn't Found")
             
    elif choice == '5':
            break
        
      