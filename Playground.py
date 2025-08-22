from typing import Optional
from datetime import datetime


class a:
    def __inti__(self, firstname: str, lastname: str, DOB: Optional[str]):
        self.firstname = firstname
        self.lastname = lastname

    
    def full_name(self):
        return f'Full Name: {self.firstname} {self.lastname}'
    

    def can_drink(self):
        current_year = datetime.now().year
        