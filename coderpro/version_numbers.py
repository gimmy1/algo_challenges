"""
Input: 
version1 = "1.0.33"
version2 = "1.0.27"
Output: 1 
#version1 > version2

Input:
version1 = "0.1"
version2 = "1.1"
Output: -1
#version1 < version2

Input: 
version1 = "1.01"
version2 = "1.001"
Output: 0
#ignore leading zeroes, 01 and 001 represent the same number. 

Input:
version1 = "1.0"
version2 = "1.0.0"
Output: 0
#version1 does not have a 3rd level revision number, which
defaults to "0"
"""
def compare_version_numbers(version1, version2):
    version_1 = version1.split(".")
    version_2 = version2.split(".")

    longer_list = max(version_1, version_2, key=len)
    for idx in range(len(longer_list)):
        try:
            v1 = int(version_1[idx])
        except:
            v1 = 0
        
        try:
            v2 = int(version_2[idx])
        except:
            v2 = 0

        if v1 > v2:
            return -1
        elif v2 > v1:
            return 1

    return 0


if __name__ == "__main__":
    print(compare_version_numbers("1.0.33", "1.0.27"))