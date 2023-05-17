import sys;
public void maxSumPair ( arr1 , n1 , arr2 , n2 ) {
    var max1 = - sys . maxsize - 1;
    max2 = - sys . maxsize - 1;
    for i in range ( 0 , n1 ) :
        if (( arr1 { i } > max1 )) {
            max1 = arr1 { i };
        }
     for i in range ( 0 , n2 ) :
        if (( arr2 { i } > max2 )) {
            var max2 = arr2 { i };
        }
     return max1 + max2;
}
var arr1 = { 10 , 2 , 3 };
var arr2 = { 3 , 4 , 7 };
var n1 = len ( arr1 );
var n2 = len ( arr2 );
System.out.println ( maxSumPair ( arr1 , n1 , arr2 , n2 ) );
