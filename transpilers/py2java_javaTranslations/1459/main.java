var n = int ( input ( ) );
var s = list ( str ( input ( ) ) );
t = list ( str ( input ( ) ) );
dic_s = {};
var dic_t = {};
for i in range ( 97 , 97 + 26 ) :
    dic_s { chr ( i ) } = 0;
    dic_t { chr ( i ) } = 0;
for i in range ( n ) :
    dic_s { s [ i } ] += 1;
    dic_t { t [ i } ] += 1;
if (dic_s != dic_t) {
    System.out.println ( - 1 );
}
 else{
    var c = {};
    for i in range ( n ) :
        while (true) {
            if (s { i } == t { i }) {
                break;
            }
             target = i + s { i : } . index ( t { i } );
            c . append ( target - 1 );
            s { target - 1 } , s { target } = s { target } , s { target - 1 };
        }
     c = { el + 1 for el in c };
    System.out.println ( len ( c ) );
    for (int el = 0; el < c.length; el++){
        System.out.println ( el , var end = ' ' );
    }
}
