from multipledispatch import dispatch

class hardening:
    def __init__(self, thickness: int, color: str, **kwargs) -> None:
        self.thickness = thickness
        self.color = color
        super().__init__(**kwargs)

class stamina:
    def __init__(self, transform_times: int, duration: int, **kwargs) -> None:
        self.transform_times = transform_times
        self.duration = duration
        super().__init__(**kwargs)
    
    def jump(self) -> str:
        return 'Can Jump'
    
    
    def fly(self) -> str:
        return 'Can fly'

class edurance:
    def _init_(self, speed: int, jump_height: int):
        self.speed = speed
        self.jump_height = jump_height
    
    def info(self):
        return f'Speed: {self.speed} Jump Height: {self.jump_height}'

class titan(hardening, stamina):
    def __init__(self, name: str, ability: str, height: int, thickness: int, color: str, transform_times: int, duration: int, **kwargs) -> None:
        self.name = name
        self.ability = ability
        self.height = height
        super().__init__(thickness=thickness, color=color, transform_times=transform_times, duration=duration, **kwargs)
        
    def info(self) -> str:
        info = f'Name: {self.name} | Ability: {self.ability} | Height: {self.height} | Thickness: {self.thickness} | Color: {self.color} | Number of Transformations: {self.transform_times} | Duration {self.duration}'
        return info
    
    @dispatch(int)
    def fly(self, dive: int) -> str:
        self.dive = dive
        return f'Can only Glide {self.dive}'

if __name__ == '__main__':
    armored_titan = titan('Armored Titan', 'Covered in thick hardening', 50, 5, 'black', 3, 5)

    print(armored_titan.info())
    print(armored_titan.fly(6))
    print(armored_titan.info())



    