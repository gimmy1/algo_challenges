def sunset_views(nums, view):
    sunset = [0]
    for idx, num in enumerate(nums[1:], start=1):
        val = sunset[-1]
        if view == "EAST":
            if num >= nums[val]:
                while len(sunset) > 0:
                    val = sunset[-1]
                    if num >= nums[val]:
                        sunset.pop()
                    else:
                        break
        else:
            if num <= nums[val]:
                continue
        
        sunset.append(idx)
    
    return sunset

if __name__ == "__main__":
    print(sunset_views([1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], "WEST"))

