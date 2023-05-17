class Dice {
    protected void init__ ( this , eyes ) {
        this . var _eyes = { 'dummy' } + eyes;
    }
    @ property;
    public void eye ( this ) {
        return this . _eyes { 1 };
    }
    public void roll ( this , direction ) {
        a = this . _eyes;
        if (direction == 'N') {
            this . _eyes = { 'dummy' , a [ 2 } , a { 6 } , a { 3 } , a { 4 } , a { 1 } , a { 5 } ];
        }
         else if (direction == 'S'){
            this . _eyes = { 'dummy' , a [ 5 } , a { 1 } , a { 3 } , a { 4 } , a { 6 } , a { 2 } ];
        }
        else if (direction == 'W'){
            this . _eyes = { 'dummy' , a [ 3 } , a { 2 } , a { 6 } , a { 1 } , a { 5 } , a { 4 } ];
        }
        else if (direction == 'E'){
            this . _eyes = { 'dummy' , a [ 4 } , a { 2 } , a { 1 } , a { 6 } , a { 5 } , a { 3 } ];
        }
        else{
            raise ValueError ( 'NEWS箱推し' );
        }
    }
}
var eyes = input ( ) . split ( );
var dice = Dice ( eyes );
var direction_text = input ( );
for (int d = 0; d < direction_text.length; d++){
    dice . roll ( d );
}
System.out.println ( dice . eye );
