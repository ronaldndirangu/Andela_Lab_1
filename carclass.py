class Car(object):
      
    def __init__(self, name=None, model=None, car_type=None, num_of_wheels=None, num_of_doors=None, speed=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = num_of_doors
        self.speed = 0
        if self.name is None and self.model is None:
            self.name = 'General'
            self.model = 'GM'
        
        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors=2
        else:
            self.num_of_doors= 4
        
        if self.car_type == 'trailer':
          self.num_of_wheels = 8
        else:
          self.num_of_wheels = 4
    
    def is_saloon(self):
        if self.car_type is not 'trailer' or self.car_type is None:
            self.car_type = 'saloon'
            return self
        else:
            self.car_type = 'trailer'
            return self
    
    def drive(self,gear):
        self.gear = gear
        if self.gear == 7 and self.car_type == 'trailer':
            self.speed = 77
            return self
        elif self.gear == 3 and self.name == 'Mercedes':
            self.speed = 1000
            return self
        else:
            return self