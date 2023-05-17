var n = int ( input ( ) );
var l = { int ( i ) for i in input ( ) . split ( ) };
l . sort ( var reverse = true );
for i in range ( 1 , n ) :
    if (l { i } >= l { i - 1 }) {
        if (l { i - 1 } == 0) {
            l { i } = 0;
        }
         else{
            l { i } = l { i - 1 } - 1;
        }
    }
     else{
        l { i } = l { i };
    }
System.out.println ( sum ( l ) );
