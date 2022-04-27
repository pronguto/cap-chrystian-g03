class KeysError(Exception):
    def __init__(self, expected, recived, message= None, status_code: int= 422):
        
        self.status_code= status_code

        if not message:
            self.message= {
                "expected keys": list(expected), 
                "recived keys": list(recived)
            }
        else:
            self.message= message