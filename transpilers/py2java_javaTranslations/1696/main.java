public void countSubarrays ( a , n , x ) {
    var count = 0;
    number = 0;
    for i in range ( n ) :
        if (( a { i } > x )) {
            count += 1;
        }
         else{
            number += ( count ) * ( count + 1 ) / 2;
            count = 0;
        }
    if (( count )) {
        number += ( count ) * ( count + 1 ) / 2;
    }
     return int ( number );
}
if (var __name__ == '__main__') {
    var a = { 3 , 4 , 5 , 6 , 7 , 2 , 10 , 11 };
    var n = len ( a );
    var k = 5;
    System.out.println ( countSubarrays ( a , n , k ) );
}
 