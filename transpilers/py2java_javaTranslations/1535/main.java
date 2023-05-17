var s = input ( );
var num_0 = 0;
var num_1 = 0;
for i in range ( len ( s ) ) :
    if (s { i } == "0") {
        num_0 += 1;
    }
     else{
        num_1 += 1;
    }
System.out.println ( min ( num_0 , num_1 ) * 2 );
