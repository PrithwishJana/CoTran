public void getCount ( arr , n , num1 , num2 ) {
    for i in range ( 0 , n ) :
        if (( arr { i } == num1 )) {
            break;
        }
     if (( i >= n - 1 )) {
        return 0;
    }
     for j in range ( n - 1 , i + 1 , - 1 ) :
        if (( arr { j } == num2 )) {
            break;
        }
     if (( var j == i )) {
        return 0;
    }
     return ( j - i - 1 );
}
var arr = { 3 , 5 , 7 , 6 , 4 , 9 , 12 , 4 , 8 };
var n = len ( arr );
var num1 = 5;
var num2 = 4;
System.out.println ( getCount ( arr , n , num1 , num2 ) );
