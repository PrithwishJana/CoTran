import collections.Counter;
public void most_frequent ( List ) {
    var occurence_count = Counter ( List );
    return occurence_count . most_common ( 1 ) { 0 } { 0 };
}
var list = list ( map ( int , input ( ) . split ( ) ) );
var o = 0;
a1 = {};
b = most_frequent ( list );
for (int num = 0; num < list.length; num++){
    if (num == b) {
        o = o + 1;
    }
     else{
        a1 . append ( num );
    }
}
if (o == 6) {
    System.out.println ( 'Elephant' );
}
 if (o == 5) {
    System.out.println ( 'Bear' );
}
 if (o == 4) {
    if (a1 { 0 } == a1 { 1 }) {
        System.out.println ( 'Elephant' );
    }
     else{
        System.out.println ( 'Bear' );
    }
}
 if (4 > o) {
    System.out.println ( 'Alien' );
}
 