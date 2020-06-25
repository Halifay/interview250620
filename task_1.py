def search_pairs(array, k):
    ret = []
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        s = array[left] + array[right]
        if s == k:
            ret.append((array[left], array[right]))
        if s <= k:
            left += 1
            if left >= right:
                break
            while array[left-1] == array[left]:
                left += 1
                if left >= right:
                    break

        if s >= k:
            right -= 1
            if right <= left:
                break
            while array[right + 1] == array[right]:
                right -= 1
                if right <= left:
                    break

    return ret


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
