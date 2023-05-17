while (1) {
    var n = int ( input ( ) );
    if n == 0 : break;
    var d = {};
    for _ in { 0 } * n :
        k , v = input ( ) . strip ( ) . split ( );
        d { k } = v;
    for _ in { 0 } * int ( input ( ) ) :
        e = input ( ) . strip ( );
        System.out.println ( d { e } if e in d else e , end = '' );
    System.out.println ( );
}
 