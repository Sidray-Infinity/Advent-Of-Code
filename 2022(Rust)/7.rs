use std::collections::HashMap;
use std::fs;

fn get_file_path(file_system: &Vec<String>, dir: String) -> String {
    // Parentdir + currDir
    let mut res: String = String::new();
    if !file_system.is_empty() {
        res.push_str(file_system[file_system.len() - 1].as_str());
    }
    res.push_str(dir.as_str());
    return res;
}

fn main() {
    let file_path = "7.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut file_system: Vec<String> = Vec::<String>::new();
    let mut dir_sizes: HashMap<String, u64> = HashMap::<String, u64>::new();

    for line in contents.split("\n") {
        if &line[0..4] == "$ cd" {
            if &line[5..] == ".." {
                _ = file_system.pop();
            } else {
                let dir_name: String = line[5..].to_string();
                let file_path: String = get_file_path(&file_system, dir_name);
                if !dir_sizes.contains_key(&file_path) {
                    dir_sizes.entry(file_path.clone()).or_insert(0);
                }
                file_system.push(file_path);
            }
        } else if &line[0..4] == "$ ls" {
        } else if line.len() >= 3 && &line[0..3] == "dir" {
        } else {
            let values: Vec<&str> = line.split(" ").collect();
            let file_size: u64 = values[0]
                .parse::<u64>()
                .expect("Expected to convert to u64");

            for dir in &file_system {
                let dir_size: &mut u64 = dir_sizes.get_mut(dir).expect("Expected to find dir");

                *dir_size += file_size;
            }
        }
    }

    let mut part1_total: u64 = 0;
    for key in dir_sizes.keys() {
        if dir_sizes.get(key).unwrap() <= &100000 {
            part1_total += dir_sizes.get(key).unwrap();
        }
    }
    println!("Part1: {:?}", part1_total);
    let min_space_needed: u64 = 30000000 - (70000000 - dir_sizes.get("/").unwrap());
    let mut values: Vec<&u64> = dir_sizes.values().collect();
    values.sort();
    for value in values {
        if *value > min_space_needed {
            println!("Part2: {:?}", *value);
            break;
        }
    }
}
