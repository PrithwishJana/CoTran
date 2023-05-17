public void System.out.printlnArray ( N , arr ) {
    for i in range ( 0 , N ) :
        System.out.println ( arr { i } , var end = " " );
    System.out.println ( );
}
public void replacedArray ( N , arr ) {
    var pos_sum = 0;
    neg_sum = 0;
    for i in range ( N - 1 , - 1 , - 1 ) :
        diff = abs ( pos_sum ) - abs ( neg_sum );
        if (( arr { i } > 0 )) {
            pos_sum = pos_sum + arr { i };
        }
         else{
            var neg_sum = neg_sum + arr { i };
        }
        arr { i } = abs ( diff );
}
var N = 5;
arr = { 1 , - 1 , 2 , 3 , - 2 };
replacedArray ( N , arr );
System.out.printlnArray ( N , arr );
N = 6;
var arr1 = { - 3 , - 4 , - 2 , 5 , 1 , - 2 };
replacedArray ( N , arr1 );
System.out.printlnArray ( N , arr1 );
