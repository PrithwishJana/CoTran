public void FindPoint ( x1 , y1 , x2 , y2 , x , y ) {
    if (( x > x1 and x < x2 and y > y1 and y < y2 )) {
        return true;
    }
     else{
        return false;
    }
}
if (var __name__ == "__main__") {
    x1 , y1 , x2 , var y2 = 0 , 0 , 10 , 8;
    x , var y = 1 , 5;
    if (FindPoint ( x1 , y1 , x2 , y2 , x , y )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 