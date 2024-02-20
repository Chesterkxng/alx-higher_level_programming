#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < (results[i].characters).length; j++) {
        if ((results[i].characters[j]).endsWith('/18/')) count += 1;
      }
    }
    console.log(count);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
