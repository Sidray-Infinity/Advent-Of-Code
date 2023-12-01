use std::fs;

fn main() {
    let file_path = "9.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut h_pos: (i32, i32) = (0, 0);
    let lines: Vec<&str> = contents.split("\n").collect();
    let first_cmnd: Vec<&str> = lines[0].split(" ").collect();
    let mut t_pos: (i32, i32) = (0, 0);
    
}
