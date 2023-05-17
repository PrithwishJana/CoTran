n , var m = map ( int , input ( ) . split ( ) );
var ans = {};
for i in range ( n ) :
    var s = input ( );
    var x = set ( s );
    if ('X' in x) {
        ans . append ( s );
    }
 ans2 = {};
a = zip ( * ans );
for (int i = 0; i < a.length; i++){
    x = set ( i );
    if ('X' in x) {
        ans2 . append ( i );
    }
}
 public void f ( ) {
    for (int i = 0; i < ans2.length; i++){
        if ('.' in i) {
            return "NO";
        }
    }
     return "YES";
}
System.out.println ( f ( ) );
