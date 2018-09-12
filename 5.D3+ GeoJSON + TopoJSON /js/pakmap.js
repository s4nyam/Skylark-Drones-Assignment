var width = window.innerWidth,
height = window.innerHeight;

//D# DOCUMENTATION
//https://github.com/d3/d3/blob/master/API.md
var projection = d3.geo.albers()
	.center([0, 30])
	.rotate([-70, 0])
	.parallels([23, 37])
	.scale(2 * width)
	.translate([width * 0.3, height * 0.5]);

var path = d3.geo.path()
	.projection(projection)
	.pointRadius(2);

var svg = d3.select("body").append("svg")
	.attr("width", width)
	.attr("height", height);

var facName = svg.append("text")
	.attr("class", "display")
	.attr("x", "800px")
	.attr("y", "200px");

var facCov = svg.append("text")
	.attr("class", "display")
	.attr("x", "800px")
	.attr("y", "250px");

d3.json("pakistan.json", function(error, pak) {
	var provinces = topojson.feature(pak, pak.objects.provinces),
	districts = topojson.feature(pak, pak.objects.districts),
	subdistricts = topojson.feature(pak, pak.objects.subdistricts);

	svg.selectAll(".subdistrict")
			.data(subdistricts.features)
		.enter().append("path")
			.attr("class", function(d) { return "subdistrict " + d.properties.name3.replace(/[ .]/g, ""); })
			.attr("d", path)
			.style("fill", function(d) { return "rgb(" + Math.pow(Math.round(Math.random()*6), 3) + ",110,210)" });
//Random Colorzation
	svg.append("path")
		.datum(topojson.mesh(pak, pak.objects.subdistricts, function(a, b) { return a !== b; })) // return a !== b; for tangential borders only
		.attr("d", path)
		.attr("class", "subdistrict-boundary");

var places = [
  {
    name: "Zoi-Nari Tehsil",
    location: {
      latitude:  32.92507,
      longitude: 70.145
    }
  },
  {
    name: "Dray Nashthar",
    location: {
      latitude:  26.55,
      longitude: 79.9455
    }
  }//.................................. and many more
]
//places are the places from dataset. They are of no use here because we have already imported everything from "pak" handler 
	svg.selectAll(".pin")
    .data(places)
  .enter().append("circle", ".pin")
    .attr("r", 5)
    .attr("transform", function(d) {
      return "translate(" + projection([
        d.location.latitude,
        d.location.longitude
      ]) + ")"
    })



    
	svg.append("path")
		.datum(topojson.mesh(pak, pak.objects.districts, function(a, b) { return a !== b; })) // return a !== b; for tangential borders only
		.attr("d", path)
		.attr("class", "district-boundary");

	svg.append("path")
		.datum(topojson.mesh(pak, pak.objects.provinces, function(a, b) { return a !== b; })) // return a !== b; for tangential borders only
		.attr("d", path)
		.attr("class", "province-boundary");

	svg.selectAll(".province-label")
			.data(provinces.features)
		.enter().append("text")
			.attr("class", function(d) { return "province-label " + d.properties.name1.replace(/[ .]/g, ""); })
			.attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
			.attr("dy", ".35em")
			.text(function(d) { return d.properties.name; });
});


//https://stackoverflow.com/questions/14168023/d3-cant-call-svg-selectalltext-twice-on-a-same-svg-object
d3.json("newplots.json", function(error, fake) {
	var facilities = fake.facilities;

	svg.selectAll(".facility")
			.data(facilities)
		.enter().append("circle")
			.attr("class", function(d) { return "facility " + d.facility_name.replace(/[ .]/g, ""); })
			.attr("cx", function(d) { return projection([d.longitude, d.latitude])[0]; })
			.attr("cy", function(d) { return projection([d.longitude, d.latitude])[1]; })
			.attr("r", 20);

	svg.selectAll(".facility").on("click", function(fac) {
		svg.selectAll(".facility").transition()
			.attr("r", 20)
			.style("fill-opacity", 0);
		d3.select(this).transition()
			.attr("r", 40)
			.style("fill-opacity", .4);

		facName.text(fac.properties.name);
		facCov.text("Coverage: " + fac.properties.coverage + "%");
	});
});