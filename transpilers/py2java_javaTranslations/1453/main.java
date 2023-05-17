public void countPairs ( arr , n ) {
    var odd = 0;
    var even = 0;
    for i in range ( n ) :
        if (( arr { i } % var 2 == 0 )) {
            even += 1;
        }
         else{
            odd += 1;
        }
    var odd_pairs = odd * ( n - 1 );
    var even_pairs = even * ( n - 1 );
    System.out.println ( odd_pairs );
    System.out.println ( even_pairs );
}
if (var __name__ == '__main__') {
    var arr = { 2 , 3 , 4 , 5 };
    var n = len ( arr );
    countPairs ( arr , n );
}
 