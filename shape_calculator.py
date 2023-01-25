class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = ( ( self.width ** 2 + self.height ** 2 ) ** 0.5 )
        return self.diagonal

    def get_picture(self):
        self.picture = str()
        ind = 0
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            while ind < self.height:
                self.picture = self.picture + (self.width*"*") + "\n"
                ind += 1
            return self.picture

    def get_amount_inside(self, shape):
        self.num_width = int(self.width/shape.width)
        self.num_height = int(self.height/shape.height)
        self.num_fits = self.num_width*self.num_height
        return self.num_fits


    def __repr__(self):
        return "Rectangle(width=%s, height=%s)"%(self.width,self.height)





class Square(Rectangle):
    def __init__(self, length):
        self.height = length
        self.width = length

    def set_side(self, new_length):
        self.width = new_length
        self.height = new_length

    def __repr__(self):
        return "Square(side=%s)" % self.width

