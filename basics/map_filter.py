class MapAndFilter:
    def __init__(self,numbers):
        self.numbers=numbers     
    def get_squares(self):    
        try:
         squares=list(map(lambda x:x*x , self.numbers))
         return squares
        except Exception as e:
         print(f"An Error Occured :{e}")
    def get_even(self):
        even=list(filter(lambda x: x%2==0,self.numbers))
        return even
use_map_filter=MapAndFilter([1,2,3,4,5])
squares=use_map_filter.get_squares()
print(squares)
even_numbers=use_map_filter.get_even()
print(even_numbers)