'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def in_order(nums):
    # Type your code here.
    newlist = []
    copied_list = nums.copy()
    for _ in range(0, len(copied_list)):
        newlist.append(min(copied_list))
        copied_list.remove(min(copied_list))
    if newlist == nums:
        return(True)
    #print(newlist)
    #print(nums)



        



if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
