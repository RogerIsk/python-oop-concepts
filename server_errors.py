# Complete these classes

class OK:
    def __init__(self, error_object):
        self.error_object = error_object
    
    def status(self):
        print(f"Error code: {self.error_object} \nError message: Yo mama is hot (200)")

class NotFound:
    def __init__(self, error_object):
        self.error_object = error_object
    
    def status(self):
        print(f"Error code: {self.error_object} \nError message: Yo mama so big, the camera said 'not found(404)' when I took her photo.")

class ServerError:
    def __init__(self, error_object):
        self.error_object = error_object
    
    def status(self):
        print(f"Error code: {self.error_object} \nError message: Yo mama so big, when I uploaded her photo to Facebook their server broke down (500)")