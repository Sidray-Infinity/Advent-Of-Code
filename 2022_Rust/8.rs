use std::cmp::max;
use std::fs;

fn is_visible_from_left(mat: &Vec<Vec<u32>>, i: usize, j: usize) -> bool {
    for y in 0..j {
        if mat[i][j] <= mat[i][y] {
            return false;
        }
    }
    return true;
}

fn num_visible_from_left(mat: &Vec<Vec<u32>>, i: usize, j: usize) -> u32 {
    let mut res: u32 = 1;
    for y in (1..j).rev() {
        if mat[i][j] <= mat[i][y] {
            return res;
        }
        res += 1;
    }
    return res;
}

fn is_visible_from_top(mat: &Vec<Vec<u32>>, i: usize, j: usize) -> bool {
    for x in 0..i {
        if mat[i][j] <= mat[x][j] {
            return false;
        }
    }
    return true;
}

fn num_visible_from_top(mat: &Vec<Vec<u32>>, i: usize, j: usize) -> u32 {
    let mut res: u32 = 1;
    for x in (1..i).rev() {
        if mat[i][j] <= mat[x][j] {
            return res;
        }
        res += 1;
    }
    return res;
}

fn is_visible_from_right(mat: &Vec<Vec<u32>>, i: usize, j: usize, w: usize) -> bool {
    for y in (j+1..w).rev() {
        if mat[i][j] <= mat[i][y] {
            return false;
        }
    }
    return true;
}

fn num_visible_from_right(mat: &Vec<Vec<u32>>, i: usize, j: usize, w: usize) -> u32 {
    let mut res: u32 = 1;
    for y in j+1..w-1 {
        if mat[i][j] <= mat[i][y] {
            return res;
        }
        res += 1;
    }
    return res;
}

fn is_visible_from_bottom(mat: &Vec<Vec<u32>>, i: usize, j: usize, h: usize) -> bool {
    for x in (i+1..h).rev() {
        if mat[i][j] <= mat[x][j] {
            return false;
        }
    }
    return true;
}

fn num_visible_from_bottom(mat: &Vec<Vec<u32>>, i: usize, j: usize, h: usize) -> u32 {
    let mut res: u32 = 1;
    for x in i+1..h-1 {
        if mat[i][j] <= mat[x][j] {
            return res;
        }
        res += 1;
    }
    return res;
}

fn main() {
    let file_path = "8.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let rows: Vec<&str> = contents.split("\n").collect();
    let height: usize = rows.len();
    let width: usize = rows[0].len();
    let mut mat = vec![vec![0; height]; width];
    for (i, row) in rows.iter().enumerate() {
        let col_values: Vec<char> = row.chars().collect();
        for (j, col_value) in col_values.iter().enumerate() {
            mat[i][j] = col_value.to_digit(10).unwrap();
        }
    }

    let mut part1: usize = 0;
    for i in 1..(height - 1) {
        for j in 1..(width - 1) {
            if is_visible_from_left(&mat, i, j) {
                part1 += 1;
                continue;
            }
            if is_visible_from_top(&mat, i, j) {
                part1 += 1;
                continue;
            }
            if is_visible_from_right(&mat, i, j, width) {
                part1 += 1;
                continue;
            }
            if is_visible_from_bottom(&mat, i, j, height) {
                part1 += 1;
                continue;
            }
        }
    }
    println!("Part1: {}", part1);
    let mut part2: u32 = 0;
    for i in 1..(height - 1) {
        for j in 1..(width - 1) {
            let left_num: u32 = num_visible_from_left(&mat, i, j);
            let top_num: u32 = num_visible_from_top(&mat, i, j);
            let right_num: u32 = num_visible_from_right(&mat, i, j, width);
            let bottom_num: u32 = num_visible_from_bottom(&mat, i, j, height);

            let score: u32 = left_num * top_num * right_num * bottom_num;
            part2 = max(part2, score);
        }
    }
    println!("Part2: {}", part2);
}
