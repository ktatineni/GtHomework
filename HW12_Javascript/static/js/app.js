// from data.js
var tableData = data;

// YOUR CODE HERE!

function empty(e) {
  switch (e) {
    case "":
    case 0:
    case "0":
    case null:
    case false:
    case typeof this == "undefined":
      return true;
    default:
      return false;
  }
}


// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // document.getElementById("tbodyid").empty();
  var tbody = d3.select("tbody");
  // clear tbody
  tbody.html("");
  // Prevent the page from refreshing
  d3.event.preventDefault();

// Select the input element and get the raw HTML node
var inputDate = d3.select("#datetime");
if (empty(inputDate.property("value"))){
	filteredData_date = tableData;
} else {
	input_date = inputDate.property("value");
	filteredData_date = tableData.filter(data => data.datetime === input_date);
}

var inputCity = d3.select("#city");
if (empty(inputCity.property("value"))){
	filteredData_city = filteredData_date;
} else {
	input_city = inputCity.property("value").toLowerCase();
	filteredData_city = filteredData_date.filter(data => data.city === input_city);
}

var inputState = d3.select("#state");
if (empty(inputState.property("value"))){
	filteredData_state = filteredData_city;
} else {
	input_state = inputState.property("value").toLowerCase();
	filteredData_state = filteredData_city.filter(data => data.state === input_state);
}

var inputCountry = d3.select("#country");
if (empty(inputCountry.property("value"))){
	filteredData_country = filteredData_state;
} else {
	input_country = inputCountry.property("value").toLowerCase();
	filteredData_country = filteredData_state.filter(data => data.country === input_country);
}

var inputShape = d3.select("#shape");
if (empty(inputShape.property("value"))){
	filteredData_shape = filteredData_country;
} else {
	input_shape = inputShape.property("value").toLowerCase();
	filteredData_shape = filteredData_country.filter(data => data.shape === input_shape);
}


  // console.log(tableData);

  // console.log(filteredData_date);
  // console.log(filteredData_city);

// document.getElementById("tbodyid").empty();
var tbody = d3.select("tbody");

  filteredData_shape.forEach((data) => {
  var row = tbody.append("tr");
  Object.entries(data).forEach(([key, value]) => {
   var cell = row.append("td");
   cell.text(value);
  });
 });


});

