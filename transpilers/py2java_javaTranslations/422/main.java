public void frequencyOfSmallest ( n , arr ) {
    var mn = arr { 0 };
    freq = 1;
    for i in range ( 1 , n ) :
        if (( arr { i } < mn )) {
            mn = arr { i };
            var freq = 1;
        }
         else if (( arr { i } == mn )){
            freq += 1;
        }
    return freq;
}
if (var __name__ == '__main__') {
    var N = 5;
    var arr = { 3 , 2 , 3 , 4 , 4 };
    System.out.println ( frequencyOfSmallest ( N , arr ) );
}
 