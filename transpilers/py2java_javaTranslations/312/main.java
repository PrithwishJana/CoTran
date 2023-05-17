import collections.defaultdict;
n , var m = map ( int , input ( ) . split ( ) );
var al = list ( map ( int , input ( ) . split ( ) ) );
var modd = defaultdict ( int );
var s = 0;
for (int a = 0; a < al.length; a++){
    s += a;
    s %= m;
    modd { s } += 1;
}
ans = 0;
for i in modd . values ( ) :
    ans += i * ( i - 1 ) // 2;
ans += modd { 0 };
System.out.println ( ans );
