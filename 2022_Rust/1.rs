use std::fs;

fn main() {
    let file_path = "1.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let batches = contents.split("\n\n");
    let mut biggest_batch_size: i32 = 0;
    let mut second_biggest_batch_size: i32 = 0;
    let mut third_biggest_batch_size: i32 = 0;
    for batch in batches {
        let nums = batch.split("\n");
        let mut batch_sum: i32 = 0;
        for num in nums {
            batch_sum += num
                .parse::<i32>()
                .expect("Should have been able to convert to i32");
        }
        if batch_sum > biggest_batch_size {
            third_biggest_batch_size = second_biggest_batch_size;
            second_biggest_batch_size = biggest_batch_size;
            biggest_batch_size = batch_sum;
        } else if batch_sum > second_biggest_batch_size {
            third_biggest_batch_size = second_biggest_batch_size;
            second_biggest_batch_size = batch_sum;
        } else if batch_sum > third_biggest_batch_size {
            third_biggest_batch_size = batch_sum;
        }
    }
    println!("Part1: {}", biggest_batch_size);
    println!("Part2: {}", biggest_batch_size + second_biggest_batch_size + third_biggest_batch_size);
}
