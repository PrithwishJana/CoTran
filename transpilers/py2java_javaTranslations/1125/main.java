var t = int ( input ( ) );
while (t > 0) {
    t -= 1;
    var S = input ( );
    var s = list ( S );
    stack = {};
    pos = {};
    var check0 = 0;
    for i in range ( 0 , len ( s ) ) :
        j = len ( s ) - i - 1;
        stack . append ( { j , int ( s [ j } ) ] );
        if (s { j } == "0") {
            if (check0 == 0) {
                if (not pos) {
                    stack . pop ( );
                    pos . append ( j );
                }
                 else{
                    if (pos { - 1 } - j > 1) {
                        stack . pop ( );
                        pos . append ( j );
                    }
                 }
                if (stack) {
                    if (stack { - 1 } { 1 } == 0) {
                        check0 = 1;
                    }
                 }
             }
         }
         if (check0 == 1) {
            if (s { j } == "1") {
                if (pos { - 1 } - j > 1) {
                    stack . pop ( );
                    pos . append ( j );
                }
             }
         }
     var stack2 = {};
    var check = 0;
    for i in range ( 0 , len ( stack ) - 1 ) :
        if (stack { i } { 1 } < stack { i + 1 } { 1 }) {
            check = 1;
        }
     if (check == 1) {
        System.out.println ( "NO" );
    }
     else{
        System.out.println ( "YES" );
    }
}
 