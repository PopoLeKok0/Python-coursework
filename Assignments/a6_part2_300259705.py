class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
class Rectangle:
    'class that represents a Rectangle in the plane'

    def __init__(self,point1,point2,color='white'):
        '''(Rectangle, Point, Point, str) -> None'''
        self.point1=point1
        self.point2=point2
        self.color=color
    def __repr__(self):
        '''(Rectangle) -> str'''
        return "Rectangle("+str(self.point1)+","+str(self.point2)+","+"'"+self.color+"')"
    def get_color(self):
        '''(Rectangle) -> str'''
        return self.color
    def get_bottom_left(self):
        '''(Rectangle) -> Point'''
        return self.point1
    def get_top_right(self):
        '''(Rectangle) -> Point'''
        return self.point2
    def reset_color(self,new_color):
        '''(Rectangle,str) -> None'''
        self.color=new_color
    def move(self,dx,dy):
        '''(Rectangle,number,number) -> None'''
        Point.move(self.point1,dx,dy) 
        Point.move(self.point2,dx,dy)
    def __str__(self):
        '''(Rectangle) -> str'''
        return "I am a "+str(self.color)+ " rectangle with bottom left corner at "+str(Point.get(self.point1))+" and top right corner at "+str(Point.get(self.point2))+"."
    def __eq__(self,other):
        '''(Rectangle,Rectangle) -> bool()'''
        if self.point1==other.point1 and self.point2==other.point2 and self.color==other.color:
            return True
        else:
            return False
    def get_perimeter(self):
        '''(Rectangle) -> number'''
        return 2*(self.point2.x-self.point1.x+self.point2.y-self.point1.y)
    def get_area(self):
        '''(Rectangle) -> number'''
        return (self.point2.x-self.point1.x)*(self.point2.y-self.point1.y)
    def contains(self,dx,dy):
        '''(Rectangle,number,number) -> bool()'''
        if dx>=self.point1.x and dx<=self.point2.x and dy>=self.point1.y and dy<=self.point2.y:
            return True
        else:
            return False
    def intersects(self,other):
        '''(Rectangle,Rectangle) -> bool()'''
        if self.point2.x<other.point1.x or self.point2.y<other.point1.y or other.point2.x<self.point1.x or other.point2.y<self.point1.y:
            return False
        else:
            return True
class Canvas:
    'class that represents canvas of Rectangles in the plane'

    def __init__(self):
        '''() -> None'''
        self.lis=[]
    def add_one_rectangle(self,other):
        '''(Rectangle) -> None'''
        self.lis.append(other)
    def total_perimeter(self):
        '''() -> Number'''
        total=0
        for Rec in self.lis:
            total+=Rectangle.get_perimeter(Rec)
        return total
    def min_enclosing_rectangle(self):
        '''() -> str'''
        min_x=[]
        min_y=[]
        max_x=[]
        max_y=[]
        for Rec in self.lis:
            min_x.append(Rec.point1.x)
            min_x=sorted(min_x)
            min_y.append(Rec.point1.y)
            min_y=sorted(min_y)
            max_x.append(Rec.point2.x)
            max_x=sorted(max_x)
            max_y.append(Rec.point2.y)
            max_y=sorted(max_y)
        return Rectangle(Point(min_x[0], min_y[0]), Point(max_x[-1], max_y[-1]), "grey")
    def __len__(self):
        '''() -> int'''
        return len(self.lis)
    
    def __repr__(self):
        '''(Canvas) -> str'''
        return 'Canvas('+str(self.lis)+')'
    def count_same_color(self,color):
        '''(str) -> int'''
        counter=0
        for i in range(len(self.lis)):
            if self.lis[i].color==color:
                counter+=1
        return counter
    def common_point(self):
        '''() -> boolean'''
        for ch in self.lis:
            for ch2 in self.lis:
                if ch!=ch2:
                    if ch.intersects(ch2):
                        pass
                    else:
                        return False
        return True
