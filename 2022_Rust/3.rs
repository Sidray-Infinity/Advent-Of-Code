use std::collections::HashSet;
use std::convert::TryInto;
use std::fs;

fn get_priority(c: &char) -> i32 {
    let c_code = *c as i32;
    if c_code >= 97 && c_code <= 122 {
        return c_code - 96;
    }
    if c_code >= 65 && c_code <= 90 {
        return c_code - 64 + 26;
    }
    return 0;
}

fn main() {
    let file_path = "3.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let ruck_sacks = contents.split("\n");
    let mut sum_priorities: i32 = 0;
    for ruck_sack in ruck_sacks.clone() {
        let crate_1: String = ruck_sack
            .chars()
            .skip(0)
            .take(ruck_sack.len() / 2)
            .collect();
        let crate_2: String = ruck_sack
            .chars()
            .skip(ruck_sack.len() / 2)
            .take(ruck_sack.len())
            .collect();
        let mut crate_1_set = HashSet::<char>::new();
        let mut crate_2_set = HashSet::<char>::new();
        for c1 in crate_1.chars() {
            crate_1_set.insert(c1);
        }
        for c2 in crate_2.chars() {
            crate_2_set.insert(c2);
        }
        let common = crate_1_set.intersection(&crate_2_set);
        for common_char in common {
            sum_priorities += get_priority(common_char);
        }
    }
    println!("Part1: {}", sum_priorities);
    let vec_ruck_sacks = ruck_sacks.collect::<Vec<&str>>();
    let mut i: usize = 0;
    sum_priorities = 0;
    while i + 2 < vec_ruck_sacks.len().try_into().unwrap() {
        let ruck_sack_1 = vec_ruck_sacks[i];
        let ruck_sack_2 = vec_ruck_sacks[i + 1];
        let ruck_sack_3 = vec_ruck_sacks[i + 2];
        let mut ruck_sack_1_set = HashSet::<char>::new();
        let mut ruck_sack_2_set = HashSet::<char>::new();
        let mut ruck_sack_3_set = HashSet::<char>::new();
        for c1 in ruck_sack_1.chars() {
            ruck_sack_1_set.insert(c1);
        }
        for c2 in ruck_sack_2.chars() {
            ruck_sack_2_set.insert(c2);
        }
        for c3 in ruck_sack_3.chars() {
            ruck_sack_3_set.insert(c3);
        }

        let mut sets: Vec<HashSet<char>> = vec![ruck_sack_1_set, ruck_sack_2_set, ruck_sack_3_set];
        let (intersection, others) = sets.split_at_mut(1);
        let intersection = &mut intersection[0];
        for other in others {
            intersection.retain(|e| other.contains(e));
        }
        for common_char in intersection.iter() {
            sum_priorities += get_priority(common_char);
        }

        i += 3
    }
    println!("Part2: {}", sum_priorities);
}
