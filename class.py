class Car(object):
    def __init__(self,model,color,company,speed_limit):
     self.model=model 
     self.color=color
     self.company=company
     self.speed_limit=speed_limit
    def start(self):
       print("started")
    def stop(self):
       print("stopped")
    def accelarate(self):
       print("accelarating...")
       "accelarater functunality here"
    def change_gear(self,gear_type):
       print("gear changed")
       "gear relater fuctionality here"

audi=Car("a6", "red", "audi", 80)
print(audi.start())