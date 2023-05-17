x , var y = map ( int , input ( ) . split ( ) );
var gr1 = { 2 };
var gr2 = { 4 , 6 , 9 , 11 };
if (x in gr1) {
    var x_gr = 1;
}
 else if (x in gr2){
    x_gr = 2;
}
else{
    x_gr = 3;
}
if (y in gr1) {
    y_gr = 1;
}
 else if (y in gr2){
    y_gr = 2;
}
else{
    y_gr = 3;
}
if (x_gr == y_gr) {
    System.out.println ( 'Yes' );
}
 else{
    System.out.println ( 'No' );
}
