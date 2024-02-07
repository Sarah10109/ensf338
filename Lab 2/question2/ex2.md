## 1. Mention at least two aspects that make interpolation search better than binary search [0.1 pts]

Two aspects that make interpolation search better than binary search:
    a. Interpolation search is more efficient than binary search. Rather than starting from the middle point of an array,  it picks a point closer to where the item of interest is likely to be found.
    
    b. Interpolation search works better for a sorted array. If the item of interest is known to be near the middle of the array, for example, the search will start by choosing a point closer to the right side of the array. It requires less steps to find the item as well.

## 2. Interpolation search assumes that data is uniformly distributed What happens this data follows a different distribution? Will the performance be affected? Why? [0.2 pts]

If the data does not follow a uniform distribution, the interpolation will be less precise in pinpointing where the item to be searched is likely to occurr. This can potentially lead to requiring more steps to find the item and increased complexity.

## 3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? [0.1 pts]

From the code provided, the line pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))) would be affected. If the search follows a different distribution, then a different method has to be used to estimate the position.

## When comparing linear, binary and interpolation search:
## 4. When is linear search your only option for searching data as binary and interpolation search may fail? [0.2 pts]

Linear search may be the only option when searching for items from non-numeric data, such as an array of strings. Interpolation works for searching numeric data, and while binary search may work for non-numeric data, linear search would be simpler in some contexts.


## 5. In which case will linear search outperform both binary and interpolation search, and why? [0.2 pts]

Linear search may perform better for very small sets of data, allowing for a more straightforward approach rather than applying a divide-and-conquer method. It also works well for best-case scenarios, when the data might be in the first array index or near the beginning. For binary search, this would be the worst case scenario. 

## 6. Is there a way to improve binary and interpolation search to solve this issue? [0.2 pts]

The formula used to estimate the position of the data can be adjusted in interpolation search to enable it to work better for different arrangements of data. This can potentially make interpolation search more efficient for identifying best case scenarios and working with small sets of data. For improving how binary search handles worst case scenarions, one option is to use an exponential search method, which first finds a range for where the item is present, and performs binary search within that range. It can improve the handling of cases where the data is near the beginning or the end of an array instead of in the middle.