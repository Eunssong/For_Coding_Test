# Big-O Notation

O(1), O(log n), O(n^2)는 **알고리즘의 시간 또는 공간 복잡도를 설명하는 표기법 중 하나**인 빅 오 표기법입니다. 

각각의 의미는 다음과 같습니다:

- O(1): 이 표기법은 **입력 크기에 관계없이 알고리즘이 일정한 시간 또는 공간을 사용한다는 것**을 나타냅니다. 다시 말해, 알고리즘의 실행 시간이나 필요한 메모리가 입력의 크기에 의존하지 않습니다. 이는 상수 시간 또는 공간을 사용하는 것을 의미합니다. 예를 들어, 배열에서 특정 인덱스의 요소를 찾는 것과 같은 작업은 O(1) 시간에 수행될 수 있습니다.

- O(log n): 이는 입력 크기에 대한 로그 함수의 복잡도를 나타냅니다. **입력 크기가 증가함에 따라 알고리즘의 실행 시간 또는 공간이 로그 함수에 비례하여 증가**합니다. 로그 시간 복잡도를 가진 알고리즘은 **입력이 커져도 비교적 느리게 증가**하는 경향이 있습니다. 예를 들어, **이진 검색 알고리즘이 O(log n) 시간에 수행**됩니다.

- O(n^2): 이는 **입력 크기의 제곱에 비례하는 복잡도**를 나타냅니다. 입력이 커질수록 알고리즘의 실행 시간 또는 공간이 입력 크기의 제곱에 비례하여 증가합니다. 이러한 알고리즘은 **입력이 커질수록 실행 시간이 빠르게 증가**할 수 있습니다. 예를 들어, **이차 시간 복잡도를 가진 이중 반복문을 사용하는 알고리즘은 O(n^2)** 입니다.

이러한 **빅 오 표기법은 알고리즘의 성능과 효율성을 분석하고 비교하는 데 사용**됩니다.   
**일반적으로 알고리즘을 설계할 때 가능한 한 시간과 공간 복잡도를 최소화하는 것이 이상적입니다.**