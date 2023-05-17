public void merge ( ar1 , ar2 , m , n ) {
    for i in range ( n - 1 , - 1 , - 1 ) :
        var last = ar1 { m - 1 };
        var j = m - 2;
        while (( j >= 0 and ar1 { j } > ar2 { i } )) {
            ar1 { j + 1 } = ar1 { j };
            j -= 1;
        }
         if (( j != m - 2 or last > ar2 { i } )) {
            ar1 { j + 1 } = ar2 { i };
            ar2 { i } = last;
         }
 }
var ar1 = { 1 , 5 , 9 , 10 , 15 , 20 };
var ar2 = { 2 , 3 , 8 , 13 };
var m = len ( ar1 );
var n = len ( ar2 );
merge ( ar1 , ar2 , m , n );
System.out.println ( "After Merging \nFirst Array: " , var end = ""  );
System.out.println ( ar1 );
System.out.println ( "Second Array: " , end = "" );
System.out.println ( ar2 );
