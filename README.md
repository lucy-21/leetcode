## About
leetcode 문제 풀이
- 사용 언어 : Python 3.8
- 참고 : [(책) 파이썬 알고리즘 인터뷰](https://github.com/onlybooks/algorithm-interview)

## Note
### 1) `enumerate`
- list, set, tuple 등의 자료형을 index를 포함한 enumerate 객체로 리턴
```python
for i, v in enumerate(a):
    print(i, v)
```

### 2) 나누기 연산자 : `/` 와 `//`의 차이
- `/` : 정수형 나누면 실수형 리턴
- `//` : 정수형 나눌때 동일한 정수형 리턴 + 내림 연산자 역할 = 몫 구하는 연산자
```python
>>> 5 / 3
1.666666667
>>> type(5 / 3)
<class 'float'>

>>> 5 // 3
1
>>> type(5 // 3)
<class 'int'>
```

### 3) `locals`
- 로컬에 선언된 모든 변수 조회 (디버깅 용이)
```python
import pprint
pprint.pprint(locals())


# 결과 예시
{'nums': [2, 7, 11, 15],
 'pprint': <module 'pprint' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/pprint.py'>,
 'target': 9}
[0, 1]
```

### 4) 명시적 또는 암시적 비교
- 암시적 (ex. `not`) : bool 비교, 존재 여부 확인
- 명시적 (ex. `==`) : 정수 비교
```python
# good
if not users: ...
if foo == 0: ...
if i % 10 == 0: ...

# bad
if len(users) == 0: ...
if foo is not None and not foo: ...
if not i % 10: ...
```

### 5) Big-O
- 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 **계산 복잡도**를 표기하는 대표적인 방법
- 시간 복잡도 외에 공간 복잡도를 표현하는 데에도 널리 쓰임 (시간과 공간은 trade-off 관계)
- 최고차항만을 표기하며, 계수는 무시
- 주어진(최선/최악/평균) 경우의 수행 시간의 **상한(upper bound = 가장 늦게 실행될 때)** 을 나타냄
- 입력값에 따른 알고리즘의 실행 시간의 추이를 살필 수 있음
- 종류
  - **O(1)**: 해시 테이블의 조회 및 삽입
  - **O(logn)**: 이진 검색
  - **O(n)**: 정렬되지 않은 리스트에서 최댓값/최솟값 찾기
  - **O(nlogn)**: 병합 정렬
  - **O(n^2)**: 버블 정렬
  - **O(2^n)**: 피보나치 수를 재귀로 계산하는 알고리즘
  - **O(n!)**: 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제를 브루트 포스로 풀이할 때

### 6) 임의 정밀도
- 무제한 자릿수를 제공하는 정수형
- 정수를 숫자의 배열로 간주, 자릿수 단위로 쪼개어 배열 형태로 표현
- 장점: 숫자를 단일형으로 처리하여 언어를 매우 단순한 구조로 만들 수 있음, 오버플로 고민할 필요 없음
- 단점: 계산 속도 저하됨
- Python은 버전 3부터 `int` 타입이 임의 정밀도 지원

### 7) 타입 선언시 괄호 사용
- `list` : 대괄호(`[]`)
- `set`과 `dict` : 둘 다 중괄호(`{}`) 사용, `set`은 `{1}` 처럼 key 없이 value만 선언)
- `tuple` : 소괄호(`()`)
```python
# set
a = {'a', 'b', 'c'}

# dict
a = {'a': 'A', 'b': 'B', 'c': 'C'}
```

### 8) 객체의 불편과 가변
- Python은 모든 것이 객체, 심지어 문자와 숫자까지도!
- 변수 할당 = 해당 객체에 대해 **참조**
- 불변 객체(immutable object) : bool, int, float, tuple, str
- 가변 객체(mutable object) : list, set, dict

### 9) `is` 와 `==`
- `is` : `id()` 값을 비교하는 함수
- `==` : 값을 비교하는 연산자 (`None`은 값 자체가 정의되어 있지 않으므로, 비교 불가능)
```python
if a is None: pass

>>> a = [1, 2, 3]
>>> a == a
True
>>> a == list(a) # 별도의 객체로 복사되면서 다른 id 갖게 됨
True
>>> a is a
True
>>> a is list(a) # id가 다르므로 false!
False
```

### 10) 속도
- 파이썬의 객체 구조, 원시 타입이 없음 -> 느린 속도의 중요한 이유 중 하나
  - 객체 값을 꺼내는 데만 해도 `var->PyObject_HEAD` 에서 타입코드를 찾는 등 여러 단계의 부가 작업 필요
- `numpy` : C로 만든 모듈이라 빠른 속도로 유명, 내부적으로 리스트를 C의 원시 타입으로 처리

### 11) 리스트
- 순서대로 저장하는 시퀀스, 변경 가능한 목록(mutable list)
- 특징
  - 내부적으로 동적 배열로 구현됨
  - 연결 리스트에 대한 포인터 목록 관리 -> 다양한 자료형을 단일 리스트에 관리할 수 있음
  - 스택과 큐에서 사용 가능한 모든 연산을 함께 제공
- 주요 연산의 시간 복잡도
  - **O(1)**
    - `len(a)`
    - `a[i]`
    - `a.append(elem)`
    - `a.pop()`
  - **O(n)**
    - `elem in a`
    - `a.count(elem)`
    - `a.index(elem)`
    - `a.pop(0)` : 큐 연산 (첫번째 요소 추출) -> 큐 연산을 주로 사용한다면, O(1)에 가능한 데크(deque) 자료형 사용 권장
    - `del a[i]`
    - `min(a), max(a)`
    - `a.reverse()`
  - **O(nlogn)**
    - `a.sort()` : 팀소트(timsort) 사용, 최선의 경우 O(n)
- 사용 예시    
```python
>>> a = list() # 초기화
>>> a = []
>>> a = [1, 2, 3]
>>> a.append(4) # 삽입
>>> a
[1, 2, 3, 4]
>>> a.insert(3, 5) # 특정 위치에 삽입 - (위치, 요소)
>>> a
[1, 2, 3, 5, 4]
>>> a.append('안녕') # 다양한 타입 삽입 가능
>>> a
[1, 2, 3, 5, 4, '안녕']
>>> a.append(True)
>>> a
[1, 2, 3, 5, 4, '안녕', True]
>>> a[3] # 조회
5
>>> a[1:3]
[2, 3]
>>> del a[1] # 인덱스로 삭제
>>> a
[1, 3, 5, 4, '안녕', True]
>>> a.remove(3) # 값으로 삭제
>>> a
[1, 5, 4, '안녕', True]
>>> a.pop(3) # 추출 (반환값 존재)
'안녕'
>>> a
[1, 5, 4, True]
```

### 12) 딕셔너리
- key/value 구조로 이루어짐
- 특징
  - 내부적으로 해시 테이블로 구현됨
  - 다양한 타입을 key로 사용할 수 있음
  - Python 3.7 부터 입력 순서 유지됨 (이전에는 `collections.OrderedDict()` 사용) -> 버전을 정확히 확인할 수 없을 때는 입력 순서 유지된다고 가정하는 것을 권장하지 않음
- 딕셔너리를 효율적으로 생성하기 위한 추가 모듈
  - `collections.OrderedDict()` : 항상 입력 순서 유지
  - `collections.defaultdict(default_value)` : 조회시 디폴트 값 생성해 키 오류 방지
  - `collections.Counter()` : 값을 key로 하고, 개수를 value로 만들어 카운팅
```python
>>> import collections
>>> a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
>>> b = collections.Counter(a)
>>> b
Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
>>> b.most_common() # 가장 빈도수 높은 순서대로 추출
[(5, 3), (6, 2), (1, 1), (2, 1), (3, 1), (4, 1)]
>>> b.most_common(2)
[(5, 3), (6, 2)]
```
- 주요 연산의 시간 복잡도
  - **O(1)**
    - `len(a)`
    - `a[key]`
    - `a[key] = value`
    - `key in a`
- 사용 예시    
```python
>>> a = dict() # 초기화
>>> a = {}
>>> a = {'key1': 'value1', 'key2': 'value2'}
>>> a
{'key1': 'value1', 'key2': 'value2'}
>>> a['key3'] = 'value3' # 삽입
>>> a
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
>>> a['key1']
'value1'
>>> a['key4'] # 없는 key일 경우 에러 발생
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key4'
>>> del a['key4'] # 삭제
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key4'
>>> 'key4' in a # 조회
False
>>> for k, v in a.items(): # 순회
...     print(k, v)
... 
key1 value1
key2 value2
key3 value3
>>> del a['key1']
>>> a
{'key2': 'value2', 'key3': 'value3'}
```

### 13) 객체 복사
- Python은 모든 것이 객체
- 별도로 값을 복사하지 않는 한, 변수에 값을 할당하는 모든 행위는 객체에 대한 참조가 됨
- 참조가 가리키는 원래 값 변경하면 모든 참조 변수의 값 또한 함께 변경됨
- 참조가 되지 않도록 값 자체를 복사하는 법
```python
>>> a = [1, 2, 3]
>>> b = a[:]
>>> c = a.copy()
>>> id(a), id(b), id(c)
(4325340288, 4325340224, 4325340352)

# 복잡하게 중첩된 리스트 복사
>>> import copy
>>> a = [1, 2, [3, 5], 4]
>>> b = copy.deepcopy(a)
>>> id(a), id(b)
(4325641600, 4325195392)
```
