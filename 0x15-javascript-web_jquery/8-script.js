$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const res of data.results) {
    $('UL#list_movies').append('<li>' + res.title + '</li>');
  }
});
