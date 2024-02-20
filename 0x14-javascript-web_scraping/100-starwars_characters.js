#!/usr/bin/node
const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/";
request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++)
    {
      request(characters[i], function (error, response, body) {
	if (error) console.log(error);
	else if (response.statusCode === 200) {
	  const character = JSON.parse(body);
	  console.log(character.name);
	}
      })
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
