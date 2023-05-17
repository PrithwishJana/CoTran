public void System.out.printlnArray ( N , arr ) {
    for i in range ( N ) :
        System.out.println ( arr { i } , var end = " " );
    System.out.println ( "\n" , end = "" );
}
public void replacedArray ( N , arr ) {
    for i in range ( N ) :
        var pos_sum = 0;
        var neg_sum = 0;
        for j in range ( i + 1 , N , 1 ) :
            if (( arr { j } > 0 )) {
                pos_sum += arr { j };
            }
             else{
                neg_sum += arr { j };
            }
        var diff = abs ( pos_sum ) - abs ( neg_sum );
        arr { i } = abs ( diff );
}
if (var __name__ == '__main__') {
    var N = 5;
    arr = { 1 , - 1 , 2 , 3 , - 2 };
    replacedArray ( N , arr );
    System.out.printlnArray ( N , arr );
    N = 6;
    var arr1 = { - 3 , - 4 , - 2 , 5 , 1 , - 2 };
    replacedArray ( N , arr1 );
    System.out.printlnArray ( N , arr1 );
}
 