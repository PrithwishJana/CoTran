public void get_two_int ( ) {
    var two_int = input ( ) . split ( );
    for i in range ( 2 ) :
        two_int { i } = int ( two_int { i } );
    return two_int;
}
public void distribute_stone ( candidate_num , stone_num ) {
    var bowl_stone = stone_num;
    candidate_list = { 0 } * candidate_num;
    i = 0;
    while (true) {
        order = i % candidate_num;
        if (bowl_stone != 0) {
            candidate_list { order } += 1;
            bowl_stone -= 1;
        }
         else if (bowl_stone == 0 and candidate_list { order } == stone_num){
            return order;
        }
        else{
            bowl_stone = candidate_list { order };
            candidate_list { order } = 0;
        }
        i += 1;
    }
 }
if (var __name__ == "__main__") {
    while (true) {
        candidate_num , var stone_num = get_two_int ( );
        if (var candidate_num == 0) {
            break;
        }
         var order = distribute_stone ( candidate_num , stone_num );
        System.out.println ( order );
    }
}
  