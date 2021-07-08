# 목적 : heapq 모듈에서 지원하는 최소 힙 연산을 list 만으로 동일하게 구현


class BinaryHeap(object):
    """참고
    1. 이진 힙의 인덱스 위치 계산 수도코드
        - parent(i) : ceil((i - 1) / 2) (ceil = 올림)
        - left(i) : 2i
        - right(i) : 2i + 1

    """

    def __init__(self):
        self.items = [None]  # 0번 인덱스 사용 X (트리의 배열 표현의 경우, 인덱스 계산을 편하게 하기 위해 인덱스 1부터 사용)

    def __len__(self):
        return len(self.items) - 1  # 마지막 요소의 인덱스 가져옴

    ## 삽입 -> O(logn) : parent를 i // 2 로 약 절반씩 줄여나감
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):  # heap 모듈의 heapq.heappush()와 동일
        self.items.append(k)
        self._percolate_up()

    ## 추출 -> O(logn) : 추출 자체는 O(1) 이지만, 추출 후 다시 힙의 특성 유지하는 작업 필요
    def _percolate_down(self, idx):
        left = idx * 2  # left node
        right = idx * 2 + 1  # right node
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = (
                self.items[smallest],
                self.items[idx],
            )
            self._percolate_down(smallest)

    def extract(self):  # heap 모듈의 heapq.heappop()과 동일
        extracted = self.items[1]  # root 반환
        self.items[1] = self.items[len(self)]  # 맨 마지막 요소를 비어 있는 루트에 올림
        self.items.pop()
        self._percolate_down(1)
        return extracted
