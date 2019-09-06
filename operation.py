# -*- coding: utf-8 -*-
"""
Created on Fri Sep 2019

@author: Neetu Ghosh
"""
"""
Finds the minimum number from an array
"""
        
def binary_search(arr, low, high):
    """
    
    Purpose : This function divide the array into smallest possible size required for comparison and returs the smallest element
    
    Input : 
        arr  : The array from which the smallest element has to be returned
        low  : Starting index of the array
        high : End index of the array  
        
    Output : Smallest element
    
    """ 
    if (low > high):
        raise IndexError('list is empty')
    
    while(low < high):
        mid = (low + (high-low)//2)
        
        if arr[mid] < arr[mid+1]:
            high = mid
        else:
            low = mid + 1
    print (low)
    return arr[low]    
              
        
        
def minimum(array):
    """
    
    Purpose : This function returns the minimum element in an array
    
    Input : 
        array  : The array from which the smallest element has to be returned
        
    Output : Smallest element
    
    """   
    
    arr_len = len(array)
    low = 0
    high = arr_len-1
    
    return binary_search(array, low, high)
        