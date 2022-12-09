use std::cmp::min;
use std::collections::HashSet;
use std::fs;

fn unique_chars(s: &str) -> bool {
    let v: Vec<char> = s.chars().collect();
    let mut v_set: HashSet<char> = HashSet::<char>::new();
    for c in v.clone() {
        v_set.insert(c);
    }
    v.len() == v_set.len()
}

fn main() {
    let file_path = "6.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut idx: usize = 0;

    while idx < contents.len() {
        let u: usize = min(contents.len(), idx + 4);
        if unique_chars(&contents.as_str()[idx..u]) {
            println!("Part1: {}", idx + 4);
            break;
        }
        idx += 1;
    }
    idx = 0;
    while idx < contents.len() {
        let u: usize = min(contents.len(), idx + 14);
        if unique_chars(&contents.as_str()[idx..u]) {
            println!("Part2: {}", idx + 14);
            break;
        }
        idx += 1;
    }
}
