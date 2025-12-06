def binary_search_first(nums, target):
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid          # guardo candidato
            right = mid - 1       # sigo buscando más a la izquierda
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == "__main__":
    nums = [1, 2, 4, 4, 4, 7, 9]
    print(binary_search_first(nums, 4))   # imprime 2 (primera aparición)
