class Car:
    def __init__(self, color: str, price: float, size: str = "Unknown"):
        self.color = color
        self.price = price
        self.setSize(size)
        
    def getColor(self):
        return self.color
    
    def getPrice(self):
        return self.price
    
    def getSize(self):
        return self.size
    
    def checkIfSizeValid(self, size):
        if size == 'S' or size == 'M' or size == 'L':
            return size
        
    def checkCarSize(self, size):
        if size == 'S':
            return "small"
        elif size == 'M':
            return 'medium'
        elif size == 'L':
            return 'large'
        
    def setColor(self, color):
        self.color = color
        
    def setPrice(self, price):
        self.price = price
        
    def setSize(self, size):
        self.size = self.checkIfSizeValid(size).upper()
            
    def __str__(self):
        string = (f"Car ({self.color}) - P{self.price:.2f} - {self.checkCarSize(self.size)}")
        return string
    
def main():
    car1 = Car("red", 19999.85, 'M')
    car2 = Car("blue", 50000.00, 'L')
    car3 = Car("green", 12345.67, 'S')
    print(car1.__str__())
    print(car2.__str__())
    print(car3.__str__())
    
main()