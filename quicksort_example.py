# arr1 = [11, 45, 23, 81, 28, 34]
# arr2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#
#
# def quicksort(arr, l, r):
#     if l < r:  # l != r : 오른쪽 값이랑 왼쪽 값이 같으면 터지는걸 제외하기 위해서
#         pivot = partition(arr, l, r)
#         # 피봇 왼쪽 값
#         # 왼쪽 값 안에서도 계속 피봇을 만들어 나누고 또 나누고 진행해야하니 재귀
#         quicksort(arr, l, pivot - 1)
#         # 피봇 오른쪽 값
#         # 오른쪽 값 안에서도 계속 피봇을 만들어 나누고 또 나누고 진행해야하니 재귀
#         quicksort(arr, pivot + 1, r)
#
#
# def partition(arr, l, r):
#     # 피봇값
#     pivot = arr[l]  # 피봇값을 일단 왼쪽으로 잡음
#     i = l  # i는 왼쪽
#     j = r  # j는 오른쪽
#
#     # i와 j가 교차할 때까지 반복
#     while i <= j:  # 만날 때까지는 교차가 아님
#         # i를 먼저 이동을 시켜준다 ( 피봇보다 더 큰값이 나올 때까지 )
#         while i <= j and arr[i] <= pivot: i += 1  # i가 j보다 작거나 같고, i번째 요소가 피봇보다 작거나 같을 때: i는 오른쪽으로 이동
#         while i <= j and arr[j] >= pivot: j -= 1  # i가 j보다 작거나 같고, j번째 요소가 피봇보다 작거나 같을 때: j는 왼쪽으로 이동
#         if i < j: arr[i], arr[j] = arr[j], arr[i]  # swap
#
#     arr[l], arr[j] = arr[j], arr[l]  # 피봇 위치를 중앙에 넣어주기
#     return j  # 피봇 위치(인덱스)를 반환
#
#
# quicksort(arr1, 0, len(arr1) - 1)
# quicksort(arr2, 0, len(arr2) - 1)
# quicksort(arr3, 0, len(arr3) - 1)
#
# print(arr1)
# print(arr2)
# print(arr3)

