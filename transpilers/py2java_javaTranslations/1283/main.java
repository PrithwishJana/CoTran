var lst = {};
for _ in range ( 3 ) :
    lst += { list ( map ( int , input ( ) . split ( ) ) ) };
var total = 0;
for i in range ( 3 ) :
    for j in range ( 3 ) :
        total += lst { i } { j };
total = total // 3;
var flag = true;
for i in range ( 3 ) :
    a = lst { 0 } { i % 3 } + lst { 1 } { ( i + 1 ) % 3 } + lst { 2 } { ( i + 2 ) % 3 };
    if (a != total) {
        flag = false;
    }
 a = lst { 0 } { 0 } + lst { 1 } { 2 } + lst { 2 } { 1 };
if (a != total) {
    flag = false;
}
 a = lst { 1 } { 1 } + lst { 0 } { 2 } + lst { 2 } { 0 };
if (a != total) {
    flag = false;
}
 a = lst { 2 } { 2 } + lst { 1 } { 0 } + lst { 0 } { 1 };
if (a != total) {
    flag = false;
}
 if (flag) {
    System.out.println ( 'Yes' );
}
 else{
    System.out.println ( 'No' );
}
