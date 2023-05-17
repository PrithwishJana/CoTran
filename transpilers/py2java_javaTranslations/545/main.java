public void fromStart ( inp , del11 ) {
    var inp1 = inp { 0 : del1 - 1 } ;;
    inp2 = inp { del1 : len ( inp ) } ;;
    return inp1 + inp2 ;;
}
public void fromEnd ( inp , del1 ) {
    inp1 = inp { 0 : len ( inp ) - del1 } ;;
    var inp2 = inp { len ( inp ) - del1 + 1 : len ( inp ) } ;;
    return inp1 + inp2 ;;
}
var in1 = 1234 ;;
var inp = str ( in1 ) ;;
var del1 = 3 ;;
System.out.println ( "num_after_deleting_from_starting" , fromStart ( inp , del1 ) ) ;;
System.out.println ( "num_after_deleting_from_ending" , fromEnd ( inp , del1 ) ) ;;
