var n = int ( input ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
public void loveTriangle ( idx , seen ) {
    if (idx in seen) {
        if (len ( seen ) == 3) {
            return idx;
        }
         return - 1;
    }
     return loveTriangle ( arr { idx - 1 } , seen | set ( { idx } ) );
}
var istrue = false;
for i in range ( 1 , n + 1 ) :
    if (i == loveTriangle ( arr { i - 1 } , set ( { i } ) )) {
        istrue = true;
        break;
    }
 if (istrue) {
    System.out.println ( 'YES' );
}
 else{
    System.out.println ( 'NO' );
}
