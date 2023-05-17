public void LiesInsieRectangle ( a , b , x , y ) {
    if (( x - y - b <= 0 and x - y + b >= 0 and x + y - 2 * a + b <= 0 and x + y - b >= 0 )) {
        return true;
    }
     return false;
}
if (var __name__ == "__main__") {
    a , b , x , var y = 7 , 2 , 4 , 5;
    if (LiesInsieRectangle ( a , b , x , y )) {
        System.out.println ( "Given point lies inside" " the rectangle" );
    }
     else{
        System.out.println ( "Given point does not lie" " on the rectangle" );
    }
}
 