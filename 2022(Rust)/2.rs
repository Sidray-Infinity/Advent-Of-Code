use std::collections::HashMap;
use std::fs;

fn game_result(opp_move: &str, own_move: &str) -> i32 {
    // draw
    if (opp_move == "A" && own_move == "X")
        || (opp_move == "B" && own_move == "Y")
        || (opp_move == "C" && own_move == "Z")
    {
        return 3;
    }
    // loss
    if (opp_move == "A" && own_move == "Y")
        || (opp_move == "B" && own_move == "Z")
        || (opp_move == "C" && own_move == "X")
    {
        return 6;
    }
    // win
    return 0;
}

fn expected_result(opp_move: &str, result: &str, scores: &HashMap<&str, i32>) -> i32 {
    // draw
    if result == "X" {
        // loss
        match opp_move {
            "A" => return scores.get("Z").copied().expect("Expected move to be found"),
            "B" => return scores.get("X").copied().expect("Expected move to be found"),
            "C" => return scores.get("Y").copied().expect("Expected move to be found"),
            &_ => return 0,
        }
    } else if result == "Y" {
        // draw
        match opp_move {
            "A" => return 3 + scores.get("X").copied().expect("Expected move to be found"),
            "B" => return 3 + scores.get("Y").copied().expect("Expected move to be found"),
            "C" => return 3 + scores.get("Z").copied().expect("Expected move to be found"),
            &_ => return 0,
        }
    } else {
        // win
        match opp_move {
            "A" => return 6 + scores.get("Y").copied().expect("Expected move to be found"),
            "B" => return 6 + scores.get("Z").copied().expect("Expected move to be found"),
            "C" => return 6 + scores.get("X").copied().expect("Expected move to be found"),
            &_ => return 0,
        }
    }
}

fn main() {
    let file_path = "2.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut scores = HashMap::new();
    scores.insert("X", 1);
    scores.insert("Y", 2);
    scores.insert("Z", 3);

    let strategies = contents.split("\n");
    let mut total_score: i32 = 0;
    let mut correct_total_score: i32 = 0;
    for strategy in strategies {
        let moves: Vec<&str> = strategy.split(" ").collect();

        let move_score = scores
            .get(moves[1])
            .copied()
            .expect("Expected move to be found");
        total_score += move_score + game_result(moves[0], moves[1]);
        correct_total_score += expected_result(moves[0], moves[1], &scores);
    }
    println!("Part1: {:?}", total_score);
    println!("Part2: {:?}", correct_total_score);
}
