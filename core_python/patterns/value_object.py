from dataclasses import dataclass
from typing import Any,Self

class Discount(float):

    def __new__(cls,value:Any)->Self:
        val = float(value)
        if value < 0 or value > 100:
            raise ValueError("not possible")
        return super().__new__(cls,val)
    



def apply_discount(price:int , discount:Discount):
    return price- ((price/100)*discount)

if __name__ == '__main__':
    print(apply_discount(100,Discount(value=29)))