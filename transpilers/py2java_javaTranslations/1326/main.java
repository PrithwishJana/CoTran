public void countSubarraysof1and0 ( a , n ) {
    var count1 = 0;
    count0 = 0;
    number1 = 0;
    number0 = 0;
    for i in range ( 0 , n , 1 ) :
        if (( a { i } == 1 )) {
            count1 += 1;
        }
         else{
            number1 += ( ( count1 ) * ( count1 + 1 ) / 2 );
            count1 = 0;
        }
    for i in range ( 0 , n , 1 ) :
        if (( a { i } == 0 )) {
            count0 += 1;
        }
         else{
            number0 += ( count0 ) * ( count0 + 1 ) / 2;
            var count0 = 0;
        }
    if (( count1 )) {
        number1 += ( count1 ) * ( count1 + 1 ) / 2;
    }
     if (( count0 )) {
        number0 += ( count0 ) * ( count0 + 1 ) / 2;
    }
     System.out.println ( "Count of subarrays of 0 only:" , int ( number0 ) );
    System.out.println ( "Count of subarrays of 1 only:" , int ( number1 ) );
}
if (var __name__ == '__main__') {
    var a = { 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 };
    var n = len ( a );
    countSubarraysof1and0 ( a , n );
}
 