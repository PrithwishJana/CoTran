var t = int ( input ( ) );
var l = sorted ( list ( map ( int , input ( ) . split ( ) ) ) );
var s = sum ( l );
if (s % var 2 == 0) {
    System.out.println ( s );
}
 else{
    for (int i = 0; i < l.length; i++){
        if (i % 2 != 0) {
            System.out.println ( s - i );
            break;
        }
    }
 }
