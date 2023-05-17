public void System.out.printlnPermutation ( n , k ) {
    var mx = n;
    for i in range ( 1 , k + 1 ) :
        System.out.println ( mx , var end = " " );
        mx -= 1;
    for i in range ( 1 , mx + 1 ) :
        System.out.println ( i , end = " " );
}
if (var __name__ == "__main__") {
    N , var K = 5 , 3;
    if (K >= N - 1) {
        System.out.println ( "Not Possible" );
    }
     else{
        System.out.printlnPermutation ( N , K );
    }
}
 