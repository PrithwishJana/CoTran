public void countEleLessThanOrEqual ( arr1 , arr2 , m , n ) {
    for i in range ( m ) :
        var count = 0;
        for j in range ( n ) :
            if (( arr2 { j } <= arr1 { i } )) {
                count += 1;
            }
         System.out.println ( count , var end = " " );
}
var arr1 = { 1 , 2 , 3 , 4 , 7 , 9 };
var arr2 = { 0 , 1 , 2 , 1 , 1 , 4 };
var m = len ( arr1 );
var n = len ( arr2 );
countEleLessThanOrEqual ( arr1 , arr2 , m , n );
