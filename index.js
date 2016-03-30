
//<!-- SVG Size -->

var w = 1280,
    h = 800;

//<!-- Randomized Node Radius -->

//random data list (to test for now)
dem_data=[['Alabama', '63.0', '6.0', '69.0'], ['Alaska', '19.0', '5.0', '24.0'], ['American Samoa', '6.0', '6.0', '12.0'], ['Arizona', '70.0', '10.0', '80.0'], ['Arkansas', '47.0', '8.0', '55.0'], ['California', '547.0', '62.0', '609.0'], ['Colorado', '72.0', '14.0', '86.0'], ['Connecticut', '73.0', '15.0', '88.0'], ['Delaware', '23.0', '10.0', '33.0'], ['Democrats Abroad', '15.0', '4.0', '19.0'], ['District of Columbia', '22.0', '23.0', '45.0'], ['Florida', '276.0', '24.0', '300.0'], ['Georgia', '110.0', '14.0', '124.0'], ['Guam', '7.0', '5.0', '12.0'], ['Hawaii', '26.0', '9.0', '35.0'], ['Idaho', '27.0', '4.0', '31.0'], ['Illinois', '189.0', '26.0', '215.0'], ['Indiana', '96.0', '9.0', '105.0'], ['Iowa', '54.0', '11.0', '65.0'], ['Kansas', '49.0', '4.0', '53.0'], ['Kentucky', '66.0', '7.0', '73.0'], ['Louisiana', '64.0', '8.0', '72.0'], ['Maine', '31.0', '6.0', '37.0'], ['Maryland', '97.0', '27.0', '124.0'], ['Massachusetts', '110.0', '26.0', '136.0'], ['Michigan', '183.0', '20.0', '203.0'], ['Minnesota', '91.0', '16.0', '107.0'], ['Mississippi', '40.0', '5.0', '45.0'], ['Missouri', '89.0', '13.0', '102.0'], ['Montana', '24.0', '7.0', '31.0'], ['Nebraska', '38.0', '6.0', '44.0'], ['Nevada', '36.0', '8.0', '44.0'], ['New Hampshire', '28.0', '7.0', '35.0'], ['New Jersey', '153.0', '19.0', '172.0'], ['New Mexico', '39.0', '11.0', '50.0'], ['New York', '337.0', '47.0', '384.0'], ['North Carolina', '139.0', '18.0', '157.0'], ['North Dakota', '22.0', '5.0', '27.0'], ['Ohio', '174.0', '17.0', '191.0'], ['Oklahoma', '45.0', '5.0', '50.0'], ['Oregon', '70.0', '14.0', '84.0'], ['Pennsylvania', '228.0', '22.0', '250.0'], ['Puerto Rico', '60.0', '7.0', '67.0'], ['Rhode Island', '32.0', '8.0', '40.0'], ['South Carolina', '56.0', '6.0', '62.0'], ['South Dakota', '22.0', '7.0', '29.0'], ['Tennessee', '82.0', '9.0', '91.0'], ['Texas', '260.0', '27.0', '287.0'], ['Unassigned', '0.0', '0.0', '0.0'], ['Utah', '29.0', '5.0', '34.0'], ['Vermont', '18.0', '9.0', '27.0'], ['Virgin Islands', '7.0', '6.0', '13.0'], ['Virginia', '106.0', '18.0', '124.0'], ['Washington', '105.0', '15.0', '120.0'], ['West Virginia', '36.0', '11.0', '47.0'], ['Wisconsin', '100.0', '11.0', '111.0'], ['Wyoming', '18.0', '4.0', '22.0'],]

dataList = [3,3,3,3,3,3,3,33,3,3,3,3,3,3,3, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12, 22, 20, 30, 23, 12, 23, 12];
//Making list of dem_total_delegates
var demTotalList = function(){
    //console.log(Number(dem_data[i][3]));
    var result = [];
    for (var counter = 0; counter<dem_data.length;counter++){
	result.push(Number(dem_data[counter][3]));
    }
    return result;
}
console.log(demTotalList());

var i = 0;
var getDataElement = function(){
    i++;
    return demTotalList()[i]+3; //Note: minimum number for circle radius = 3
}

var nodes = d3.range(demTotalList().length-1).map(
    function() { 
	//return {radius: Math.random() * 12 + 4};
	//return {radius: getDataElement()};
	var d = {};
	d["radius"] = getDataElement();
	return d;
    }),
    //color = d3.scale.category10(); //Note: COLOR IS HERE

var force = d3.layout.force()
    .gravity(0.05)
    .charge(function(d, i) { return i ? 0 : -2000; })
    .nodes(nodes)
    .size([w, h]);

var root = nodes[0];
root.radius = 0;
root.fixed = true;

force.start();

var svg = d3.select("#body").append("svg:svg")
    .attr("width", w)
    .attr("height", h);

svg.selectAll("circle")
    .data(nodes.slice(1))
  .enter().append("svg:circle")
    .attr("r", function(d) { return d.radius - 2; })
    .style("fill", function(d, i) { return color(i % 3); });

force.on("tick", function(e) {
  var q = d3.geom.quadtree(nodes),
      i = 0,
      n = nodes.length;

  while (++i < n) {
    q.visit(collide(nodes[i]));
  }

  svg.selectAll("circle")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
});

svg.on("mousemove", function() {
  var p1 = d3.svg.mouse(this);
  root.px = p1[0];
  root.py = p1[1];
  force.resume();
});

function collide(node) {
  var r = node.radius + 16,
      nx1 = node.x - r,
      nx2 = node.x + r,
      ny1 = node.y - r,
      ny2 = node.y + r;
  return function(quad, x1, y1, x2, y2) {
    if (quad.point && (quad.point !== node)) {
      var x = node.x - quad.point.x,
          y = node.y - quad.point.y,
          l = Math.sqrt(x * x + y * y),
          r = node.radius + quad.point.radius;
      if (l < r) {
        l = (l - r) / l * .5;
        node.x -= x *= l;
        node.y -= y *= l;
        quad.point.x += x;
        quad.point.y += y;
      }
    }
    return x1 > nx2
        || x2 < nx1
        || y1 > ny2
        || y2 < ny1;
  };
}

