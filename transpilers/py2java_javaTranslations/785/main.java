a , var b = map ( int , input ( ) . split ( ) );
var x = a;
var h = 0;
var s = 0;
while (x > 0) {
    x -= 1;
    h += 1;
    s += 1;
}
 while (s // b != 0) {
    h += 1;
    s = s - b + 1;
}
 System.out.println ( h );
