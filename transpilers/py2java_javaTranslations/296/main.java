var R = lambda : map ( int , input ( ) . split ( ) );
n , m , s , var f = R ( );
if (s < f) {
    var d = 1;
    c = 'R';
}
 else{
    d = - 1;
    var c = 'L';
}
var res = "";
var i = 1;
j = s;
t , l , r = R ( );
k = 1;
while (j != f) {
    if (i > t and k < m) {
        t , l , r = R ( );
        k += 1;
    }
     if (i == t and ( l <= j <= r or l <= j + d <= r )) {
        res += 'X';
    }
     else{
        res += c;
        j += d;
    }
    i += 1;
}
 System.out.println ( res );
