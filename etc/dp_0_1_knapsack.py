"""
0-1 배낭 문제
- 총 무게가 capacity를 만족하면서 가장 가치가 높은 짐을 담아야 함 (반환 : 최대 가치)
- DP 타뷸레이션 이용
- 테이블 크기 = (짐의 최대 개수 + 1) * (배낭의 최대 용량 + 1) = 6 * 16 
"""


def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c],
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])

    return pack[-1][-1]


if __name__ == "__main__":
    cargo = [  # (가치, 무게)
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]
    result = zero_one_knapsack(cargo)
    print(result)
