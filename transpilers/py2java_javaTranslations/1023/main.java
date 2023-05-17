import sys;
import sys.stdin;
import operator.itemgetter;
var input = stdin . readline;
public void solve ( data ) {
    data . sort ( var key = itemgetter ( 1 ) );
    var top2 = data { : 2 };
    var others = data { 2 : };
    return top2 , others;
}
public void main ( args ) {
    others_results = {};
    for _ in range ( 3 ) :
        round_results = {};
        for _ in range ( 8 ) :
            id , time = input ( ) . split ( );
            round_results . append ( { int ( id ) , float ( time ) } );
        top2 , others = solve ( round_results );
        others_results . extend ( others );
        for id , time in top2 :
            System.out.println ( '{} {}' . format ( id , time ) );
    top2 , others = solve ( others_results );
    for id , time in top2 :
        System.out.println ( '{} {}' . format ( id , time ) );
}
if (var __name__ == '__main__') {
    main ( sys . argv { 1 : } );
}
 