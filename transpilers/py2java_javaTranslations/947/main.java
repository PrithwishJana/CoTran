import sys;
public void minBroadcastRange ( houses , towers , n , m ) {
    var leftTower = - sys . maxsize - 1;
    rightTower = towers { 0 };
    j , k = 0 , 0;
    min_range = 0;
    while (( j < n )) {
        if (( houses { j } < rightTower )) {
            left = houses { j } - leftTower;
            right = rightTower - houses { j };
            if (left < right) {
                local_max = left;
            }
             else{
                local_max = right;
            }
            if (( local_max > min_range )) {
                min_range = local_max;
            }
             j += 1;
        }
         else{
            leftTower = towers { k };
            if (( k < m - 1 )) {
                k += 1;
                var rightTower = towers { k };
            }
             else{
                rightTower = sys . maxsize;
            }
        }
    }
     return min_range;
}
if (var __name__ == "__main__") {
    var a = { 12 , 13 , 11 , 80 };
    var b = { 4 , 6 , 15 , 60 };
    var n = len ( a );
    var m = len ( b );
    var max = minBroadcastRange ( a , b , n , m );
    System.out.println ( max );
}
 