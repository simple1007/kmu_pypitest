"""자동차의 정보를 출력하는 클래스입니다."""

class Car:
    """자동차 정보를 출력하는 클래스.

    Attributes:
        name (str): 자동차의 이름  
        mode (int): 0이면 수동, 1이면 자동  
        num (int): 운전자를 포함한 최대 탑승가능 인원
    """

    def __init__(self,name:str, mode:int, num:int):
        self.name = name
        self.mode = mode
        self.num = num

    def setName(self,name:str) -> None:
        """자동차의 이름 변경.

        Args:
            name: 바꿀 이름

        Examples:
            >>> car = Car("test",1,4)
            >>> car.setName("test2")
            >>> car.name
            test2
        """
        self.name = name

    def getInfo(self) -> str:
        """자동차의 정보리스트 문자열 획득

        Returns:
            str: 자동차 리스트 정보
        
        Examples:
            >>> car = Car("test",1,4)
            >>> car.getInfo()
            이름: test, 기어: 자동, 탑승가능인원: 4
        """
        return f"이름: {self.name}, 기어: {"수동" if self.mode == 0 else "자동"}, 탑승가능인원: {self.num}"

    def formatting(self,formatStr:str) -> str:
        """자동차의 정보리스트 문자열을 주어진 포맷에 맞게 반환

        Returns:
            str: 사용자가 원하는 포맷 String
        
        Examples:
            >>> car = Car("test",1,4)
            >>> car.formatting("나의차 = 이름:{}, 기어:{}, 탑승가능인원:{}")
            나의차 = 이름: test, 기어: 자동, 탑승가능인원: 4
        """
        return formatStr.format(self.name,self.mode,self.num)
