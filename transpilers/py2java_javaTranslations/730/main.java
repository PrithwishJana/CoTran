var n = int ( input ( ) );
var A = { int ( x ) for x in input ( ) . split ( ) };
var m = int ( input ( ) );
var B = { int ( x ) for x in input ( ) . split ( ) };
var ans = 0;
for i in range ( min ( len ( A ) , len ( B ) ) ) :
    if (A { i } < B { i }) {
        ans = 1;
        break;
    }
     else if (A { i } > B { i }){
        break;
    }
else{
    if (len ( A ) < len ( B )) {
        ans = 1;
    }
 }
System.out.println ( ans );
