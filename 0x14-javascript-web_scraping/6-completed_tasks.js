#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const array = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < array.length; i++) {
      const task = array[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) completed[task.userId] = 1;
        else completed[task.userId]++;
      }
    }
    console.log(completed);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
