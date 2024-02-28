$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    for (const movie of movies) {
      const title = movie.title;
      $('UL#list_movies').append('<li>' + title + '</li>');
    }
  });
});
