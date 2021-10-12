#Jessica 
#Books
title = ["Apprentice in Death","Razor Girl","The Underground Railroad","A Great Reckoning","The Woman in Cabin 10"]
author = ["J. D. Robb","Carl Hiaasen","Colson Whitehead","Louise Penny","Ruth Ware"]
cost = [17.19,17.02,21.56,17.56,15.66]
revenue = [1727595.00,1706255.00,2156000.00,1751610.00,1558170.00]


def main():
    return calc()

def enter(expense,expense2,book,book2,):
    bt = input("Enter the book title: ")
    ba = input("Enter the author of the book: ")
    bc = float(input("Enter the cost of the book: "))
    gr = float(input("Enter the gross revenue of he book: "))
    title1 = title.append(bt)
    author1 = author.append(ba)
    cost1 = cost.append(bc)
    revenue1 = revenue.append(gr)
    return calc()

    


def calc():
    expense = max(cost)
    expense2 = min(cost)
    index = cost.index(expense)
    index2 = cost.index(expense2)
    book = title[index]
    book2 = title[index2]
    return display(expense,expense2,index,index2,book,book2)


def display(expense,expense2,index,index2,book,book2):
    print ("The most expensive book is:",expense)
    print ("Name of book:",book)
    print ("The least expensive book:",expense2)
    print ("Name of book:",book2)
    again = input("Do you have another book? Y or N: ")
    if again.lower() == "y":
        return enter(expense,expense2,book,book2)



main()
