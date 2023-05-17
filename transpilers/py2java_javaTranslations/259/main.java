public void findAllSequences ( diff , out , start , end ) {
    if (( abs ( diff ) > ( end - start + 1 ) // 2 )) {
        return ;;
    }
     if (( start > end )) {
        if (( var diff == 0 )) {
            System.out.println ( '' . join ( list ( out ) ) , var end = " " ) ;;
        }
         return ;;
    }
     out { start } = '0' ;;
    out { end } = '1' ;;
    findAllSequences ( diff + 1 , out , start + 1 , end - 1 ) ;;
    out { start } = out { end } = '1' ;;
    findAllSequences ( diff , out , start + 1 , end - 1 ) ;;
    out { start } = out { end } = '0' ;;
    findAllSequences ( diff , out , start + 1 , end - 1 ) ;;
    out { start } = '1' ;;
    out { end } = '0' ;;
    findAllSequences ( diff - 1 , out , start + 1 , end - 1 ) ;;
}
var n = 2 ;;
var out = { "" } * ( 2 * n ) ;;
findAllSequences ( 0 , out , 0 , 2 * n - 1 );
System.out.println ( );
