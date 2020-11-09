from typing import List
import csv
import time
 
CSV = "menu.csv"

class Order:
    '''
    An order for the Pizza Parlour.

    Precondition: All instance variables that are of the str type are all lowercase.

    === Private Attributes ===
    order_id:
        The order's unique ID that the customer uses to change order or cancel order
    type:
        The type of pizza
    size:
        The size of the pizza
    extra_toppings:
        A list of extra toppings (prices calculated separately)
    drink:
        The drink accompanying the pizza
    delivery:
        The delivery method (ubereats / foodora / in-house)
    address:
        The address to deliver the pizza to

    '''
    _order_id: int
    _type: str
    _size: str
    _extra_toppings: List[str]
    _drink: str
    _delivery: str
    _addresss: str


    def __init__(self, type, size, extra_toppings, drink, delivery, address) :
        '''
        Creates a new order.
        '''
        self._order_id = self._timestamp()
        self._type = type
        self._size = size
        self._extra_toppings = extra_toppings
        self._address = address
        self._drink = drink
        self._delivery = delivery
        self._price = self._calculate_price()

    def _calculate_price(self) -> float:
        '''
        

        '''
        total = 0.0

        with open(CSV, newline="") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0].lower() == self._size or row[0].lower() == self._type or row[0].lower() == self._drink or row[0].lower() in self._extra_toppings:
                    
                    total += float(row[1])
        
        return total

    def _timestamp(self) -> int:
        '''
        NOBODY'S GONNA KNOW ;)
        they'er gonna knoW
        hOw wOUlD thEY knoW????
        '''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)

        return time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

    def get_price(self) -> int:
        '''
        '''
        return self._price
    
    def get_order_id(self) -> int:
        '''
        '''
        return self._order_id
    
    def get_toppings(self) -> List:
        '''
        '''
        return self._extra_toppings
    
    def set_price(self, new_price) -> None:
        '''
        '''
        self._price = new_price


if __name__ == "__main__":
    order = Order('cheese', 'small', ['feta cheese'], 'coke', 'ubereats', "123 fml street")

    print(order.get_price()) # 16.55