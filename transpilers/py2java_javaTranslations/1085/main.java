public void bit ( n ) {
    var count = 0;
    while (( n )) {
        count += 1;
        var n = n & ( n - 1 );
    }
     return count;
}
public void maxSumOfBits ( arr , n ) {
    for i in range ( n ) :
        arr { i } = bit ( arr { i } );
    incl = arr { 0 };
    excl = 0;
    for i in range ( 1 , n ) :
        if (incl > excl) {
            excl_new = incl;
        }
         else{
            excl_new = excl;
        }
        incl = excl + arr { i } ;;
        excl = excl_new;
    if (incl > excl) {
        return incl;
    }
     else{
        return excl;
    }
}
if (__name__ == "__main__") {
    arr = { 1 , 2 , 4 , 5 , 6 , 7 , 20 , 25 };
    n = len ( arr );
    System.out.println ( maxSumOfBits ( arr , n ) );
}
 