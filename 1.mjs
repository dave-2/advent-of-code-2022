import { open } from 'node:fs/promises';

async function main() {
  const file = await open('1.input');
  const calories = await parseInput(file);
  console.log('Part One:', part1(calories));
  console.log('Part Two:', part2(calories));
}

async function parseInput(file) {
  const allCalories = [];
  let currentCalories = [];

  for await (const line of file.readLines()) {
    if (!line) {
      allCalories.push(currentCalories);
      currentCalories = [];
      continue;
    }
    currentCalories.push(parseInt(line));
  }
  allCalories.push(currentCalories);

  return allCalories;
}

function part1(calories) {
  return Math.max(...calories.map(cal => cal.reduce((a, b) => a + b, 0)));
}

function part2(calories) {
  const summedCalories = calories.map(cal => cal.reduce((a, b) => a + b, 0));
  const sortedCalories = summedCalories.sort((a, b) => b - a);
  return sortedCalories[0] + sortedCalories[1] + sortedCalories[2];
}

main();
