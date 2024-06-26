#Day 13: Abstract Classes


from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
# Soluton Starts Here
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price=str(price)
        
    def display(self):
        print("Title: "+self.title)
        print("Author: "+self.author)
        print("Price: "+self.price)
# Solution Ends Here
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
