public void findMin ( V ) {
    var deno = { 1 , 2 , 5 , 10 , 20 , 50 , 100 , 500 , 1000 };
    var n = len ( deno );
    ans = {};
    i = n - 1;
    while (( i >= 0 )) {
        while (( V >= deno { i } )) {
            V -= deno { i };
            ans . append ( deno { i } );
        }
         i -= 1;
    }
     for i in range ( len ( ans ) ) :
        System.out.println ( ans { i } , end = " " );
}
if (__name__ == '__main__') {
    n = 93;
    System.out.println ( "Following is minimal number" , "of change for" , n , ": " , var end = "" );
    findMin ( n );
}
 