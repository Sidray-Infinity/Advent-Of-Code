use std::cmp::min;
use std::convert::TryInto;
use std::fs;

#[derive(Debug)]
struct Node {
    data: char,
    next: Option<Box<Node>>,
}

impl Node {
    fn new(data: char) -> Node {
        Node { data, next: None }
    }
}

#[derive(Debug)]
struct Stack {
    top: Option<Node>,
}

impl Stack {
    fn new() -> Stack {
        Stack { top: None }
    }
    fn push(&mut self, data: char) {
        let mut node = Node::new(data);
        if let Some(top) = std::mem::replace(&mut self.top, None) {
            node.next = Some(Box::new(top));
        }
        self.top = Some(node);
    }
    fn pop(&mut self) -> Option<char> {
        if let Some(top) = std::mem::replace(&mut self.top, None) {
            self.top = match top.next {
                Some(n) => Some(*n),
                None => None,
            };
            Some(top.data)
        } else {
            None
        }
    }
    fn peek(&self) -> Option<char> {
        match &self.top {
            None => None,
            Some(node) => Some(node.data),
        }
    }
}

fn parse_stack_line(line: &str, total_num_stacks: i32, stacks: &mut Vec<Stack>) {
    let num_chars: i32 = total_num_stacks * 4;
    let mut i: i32 = 0;
    let mut stack_num: usize = 0;
    while i < num_chars {
        let u: usize = (i + 4)
            .try_into()
            .expect("Expected to convert i32 to usize");
        let u_max: usize = min(line.len(), u);
        let stack_ele = &line[(i as usize)..(u_max as usize)].trim();
        if stack_ele.len() > 0 {
            stacks[stack_num].push(stack_ele.chars().nth(1).expect("Expected to get 1st char"));
        }

        i += 4;
        stack_num += 1;
    }
}

fn parse_stacks(stack_string: &str) -> Vec<Stack> {
    let mut stacks: Vec<Stack> = Vec::<Stack>::new();
    let stack_string_lines: Vec<&str> = stack_string.split("\n").collect();
    let num_stacks: i32 = stack_string_lines[stack_string_lines.len() - 1 as usize]
        .split("   ")
        .collect::<Vec<&str>>()
        .len() as i32;
    for _ in 0..num_stacks {
        let stack: Stack = Stack::new();
        stacks.push(stack);
    }

    for i in (0..stack_string_lines.len() - 1).rev() {
        parse_stack_line(stack_string_lines[i], num_stacks, &mut stacks);
    }

    return stacks;
}

fn main() {
    let file_path = "5.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let split_contents: Vec<&str> = contents.split("\n\n").collect();
    let stack_config: &str = split_contents[0];
    let moves: &str = split_contents[1];
    let mut stacks = parse_stacks(stack_config);
    let commands: Vec<&str> = moves.split("\n").collect();
    for command in commands.clone() {
        let ind_commands: Vec<&str> = command.split(" ").collect();
        let num_moves: usize = ind_commands[1]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        let from: usize = ind_commands[3]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        let to: usize = ind_commands[5]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        for _ in 0..num_moves {
            let poped = stacks[from - 1].pop().expect("Expected a char");
            stacks[to - 1].push(poped);
        }
    }
    let mut top_str_part1: String = String::new();
    for stack in stacks {
        top_str_part1 += &stack.peek().expect("Expected char").to_string();
    }
    println!("Part1: {}", top_str_part1);
    let mut temp_stack: Stack = Stack::new();
    stacks = parse_stacks(stack_config);
    for command in commands.clone() {
        let ind_commands: Vec<&str> = command.split(" ").collect();
        let num_moves: usize = ind_commands[1]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        let from: usize = ind_commands[3]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        let to: usize = ind_commands[5]
            .parse::<usize>()
            .expect("Expected to parse to usize");
        for _ in 0..num_moves {
            temp_stack.push(stacks[from - 1].pop().expect("Expected a char"));
        }
        loop {
            match temp_stack.pop() {
                None => break,
                Some(node) => stacks[to - 1].push(node),
            }
        }
    }
    let mut top_str_part2: String = String::new();
    for stack in stacks {
        top_str_part2 += &stack.peek().expect("Expected char").to_string();
    }
    println!("Part2: {}", top_str_part2);
}
