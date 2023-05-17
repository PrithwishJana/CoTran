var n = int ( input ( ) );
var x = input ( );
var s = "";
count = 0;
for i in range ( 0 , len ( x ) - 1 , 2 ) :
    k = x { i : i + 2 };
    if (k . count ( "a" ) == 2 or k . count ( "b" ) == 2) {
        k = "ab";
        count = count + 1;
    }
     s = s + k;
System.out.println ( count );
System.out.println ( s );
