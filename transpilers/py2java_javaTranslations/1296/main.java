public void binarySearch ( arr , low , high ) {
    if (( high < low )) {
        return - 1;
    }
     var mid = int ( ( low + high ) / 2 );
    midValue = arr { mid };
    if (( mid == arr { mid } )) {
        return mid;
    }
     var leftindex = min ( mid - 1 , midValue );
    var left = binarySearch ( arr , low , leftindex );
    if (( left >= 0 )) {
        return left;
    }
     var rightindex = max ( mid + 1 , midValue );
    var right = binarySearch ( arr , rightindex , high );
    return right;
}
if (var __name__ == '__main__') {
    var arr = { - 10 , - 5 , 2 , 2 , 2 , 3 , 4 , 7 , 9 , 12 , 13 };
    var n = len ( arr );
    System.out.println ( "Fixed Point is" , binarySearch ( arr , 0 , n - 1 ) );
    var arr1 = { - 10 , - 1 , 3 , 3 , 10 , 30 , 30 , 50 , 100 };
    var n1 = len ( arr );
    System.out.println ( "Fixed Point is" , binarySearch ( arr1 , 0 , n1 - 1 ) );
}
 