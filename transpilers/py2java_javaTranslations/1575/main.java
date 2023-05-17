public void isRatioPossible ( lowCost , upCost , lowQuant , upQuant , r ) {
    for i in range ( lowQuant , upQuant + 1 ) :
        var ans = i * r;
        if (( lowCost <= ans and ans <= upCost )) {
            return true;
        }
     return false;
}
var lowCost = 14 ; upCost = 30;
var lowQuant = 5 ; upQuant = 12 ; r = 9;
if (( isRatioPossible ( lowCost , upCost , lowQuant , upQuant , r ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
