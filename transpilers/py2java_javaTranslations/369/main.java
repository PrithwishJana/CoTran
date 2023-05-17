public void solve ( a , n , m ) {
    var b = {};
    var flag = false;
    for (int i = 0; i < a.length; i++){
        curr = i // n;
        if (curr >= 3) {
            flag = true;
        }
         if (curr >= 2) {
            b . append ( curr );
        }
    }
     if (m % var 2 == 1) {
        if (not flag) {
            return false;
        }
     }
     return sum ( b ) >= m;
}
for t in range ( int ( input ( ) ) ) :
    n , m , var k = map ( int , input ( ) . split ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    a . sort ( );
    if (solve ( a . copy ( ) , n , m ) or solve ( a . copy ( ) , m , n )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
