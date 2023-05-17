public void findMinDifference ( arr , n ) {
    if (( arr { 0 } < arr { 1 } )) {
        var min__ = secondMax = arr { 0 };
    }
     else{
        min__ = secondMax = arr { 1 };
    }
    if (( arr { 0 } < arr { 1 } )) {
        max__ = secondMin = arr { 1 };
    }
     else{
        max__ = secondMin = arr { 0 };
    }
    for i in range ( 2 , n ) :
        if (( arr { i } > max__ )) {
            secondMax = max__;
            max__ = arr { i };
        }
         else if (( arr { i } > secondMax )){
            secondMax = arr { i };
        }
        else if (( arr { i } < min__ )){
            secondMin = min__;
            min__ = arr { i };
        }
        else if (( arr { i } < secondMin )){
            var secondMin = arr { i };
        }
    var diff = min ( max__ - secondMin , secondMax - min__ );
    return diff;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 4 , 3 , 4 };
    var n = len ( arr );
    System.out.println ( findMinDifference ( arr , n ) );
}
 