public void reverse ( str1 , x ) {
    var n = ( len ( str1 ) - x ) // 2;
    for i in range ( n ) :
        System.out.println ( str1 { i } , var end = "" );
    for i in range ( n + x - 1 , n - 1 , - 1 ) :
        System.out.println ( str1 { i } , end = "" );
    for i in range ( n + x , len ( str1 ) ) :
        System.out.println ( str1 { i } , end = "" );
}
var str1 = "geeksforgeeks";
var x = 3;
reverse ( str1 , x );
