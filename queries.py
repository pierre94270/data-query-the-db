# pylint:disable=C0111,C0103
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()


def query_orders(db):
    # return a list of orders displaying each column
    query="""
        SELECT *
        FROM OrderDetails od
        ORDER BY OrderID DESC
    """
    db.execute(query)
    results = db.fetchall()
    #liste.append(i[0]) for i in results2
    return [x[0] for x in results]

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query="""
         SELECT * 
         FROM Orders o  
         WHERE OrderDate > ? AND OrderDate < ?
         ORDER BY OrderDate DESC
    """
    db.execute(query, (date_from, date_to))
    results = db.fetchall()
    return [x[0] for x in results]
    
    pass  # YOUR CODE HERE

def get_waiting_time(db):
    query="""
          SELECT *  
          FROM Orders o  
          ORDER BY ShippedDate  ASC
    """
    db.execute(query)
    results = db.fetchall()
    return [x[0] for x in results]
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    pass  # YOUR CODE HERE
