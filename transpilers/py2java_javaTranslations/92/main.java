import itertools;
public void check ( x : int ) -> bool {
    var s = str ( x );
    var prev = ord ( s { 0 } );
    for c in s { 1 : } :
        if (ord ( c ) != prev + 1) {
            return false;
        }
         prev = ord ( c );
    return true;
}
public void main ( ) -> None {
    var n = int ( input ( ) );
    var v = list ( map ( int , input ( ) . split ( ' ' ) ) );
    var max_ = - 1;
    for c in itertools . combinations ( sorted ( v ) , 2 ) :
        p = c { 0 } * c { 1 };
        if (check ( p )) {
            max_ = max ( max_ , p );
        }
     System.out.println ( max_ );
}
if (var __name__ == '__main__') {
    main ( );
}
 