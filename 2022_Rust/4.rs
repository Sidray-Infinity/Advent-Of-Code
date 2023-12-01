use std::fs;

fn is_fully_contained(l0: i32, u0: i32, l1: i32, u1: i32) -> bool {
    // if range 1 is contained in range 0
    if l0 <= l1 && u0 >= u1 {
        return true;
    }
    // if range 0 is contained in range 1
    if l1 <= l0 && u1 >= u0 {
        return true;
    }
    return false;
}

fn check_if_overlap(l0: i32, u0: i32, l1: i32, u1: i32) -> bool {
    if l0 <= l1 && l1 <= u0 {
        return true;
    }
    if l1 <= l0 && l0 <= u1 {
        return true;
    }
    return false;
}

fn main() {
    let file_path = "4.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let pairs: Vec<&str> = contents.split("\n").collect();
    let mut full_contained_pairs: i32 = 0;
    let mut overlap_pairs: i32 = 0;
    for pair in pairs {
        let ranges: Vec<&str> = pair.split(",").collect();
        let range_1: Vec<&str> = ranges[0].split("-").collect();
        let range_2: Vec<&str> = ranges[1].split("-").collect();
        let l0: i32 = range_1[0]
            .parse()
            .expect("Should have been able to conver to i32");
        let l1: i32 = range_2[0]
            .parse()
            .expect("Should have been able to conver to i32");
        let u0: i32 = range_1[1]
            .parse()
            .expect("Should have been able to conver to i32");
        let u1: i32 = range_2[1]
            .parse()
            .expect("Should have been able to conver to i32");
        if is_fully_contained(l0, u0, l1, u1) {
            full_contained_pairs += 1;
        }
        if check_if_overlap(l0, u0, l1, u1) {
            overlap_pairs += 1;
        }
    }
    println!("Part1: {}", full_contained_pairs);
    println!("Part2: {}", overlap_pairs);
}
