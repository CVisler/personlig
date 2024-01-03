const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('Pattern: ', (user_pattern) => {
  rl.question('Height: ', (user_height) => {
    create_pyramid(user_pattern, user_height)
    rl.close();
  });
});


function create_pyramid(patt, h) {
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < i+1; j++) 
      process.stdout.write(patt);
    console.log('')
  }
}
