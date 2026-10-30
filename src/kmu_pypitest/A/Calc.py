"""두수의 덧셈 곱셈 함수를 제공하는 모듈입니다."""

def add(a:int,b:int) -> int:
    """두 정수를 더하는 함수입니다.

    Args:
        a: 첫번째 정수 
        b: 두번째 정수

    Returns:
        int: a와 b를 더한 결과
    
    Examples:
        >>> add(1,2)
        3
    """
    return a + b

def mul(a:int,b:int) -> int:
    """두 정수를 곱하는 함수입니다.

    Args:
        a: 첫번째 정수
        b: 두번째 정수
    
    Returns:
        int: a와 b를 곱한 결과
    
    Examples:
        >>> mul(1,2)
        2
    """
    return a * b

def add_mul(a:int,b:int) -> tuple[int,int]:
    """두 정수를 곱하고 더하는 함수입니다.

    Args:
        a: 첫번째 정수
        b: 두번째 정수
  
    Returns:
        tuple[int, int]: 아래 요소를 담은 튜플
            - added (int): add함수 결과
            - muled (int): mul함수 결과
    
    Examples:
        >>> add_mul(1,2)
        (3, 2)
    """
    added = add(a,b)
    muled = mul(a,b)

    return added,muled