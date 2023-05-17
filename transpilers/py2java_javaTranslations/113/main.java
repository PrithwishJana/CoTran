var COST = 3 ;;
public void maxItems ( x , y , z ) {
    var type1 = x // COST ;;
    x %= COST ;;
    var type2 = y // COST ;;
    y %= COST ;;
    var type3 = z // COST ;;
    z %= COST ;;
    var type4 = min ( x , min ( y , z ) ) ;;
    var maxItems = type1 + type2 + type3 + type4 ;;
    return maxItems ;;
}
if (var __name__ == "__main__") {
    var x = 4 ; y = 5 ; z = 6 ;;
    System.out.println ( maxItems ( x , y , z ) ) ;;
}
 