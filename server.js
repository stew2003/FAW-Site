var express = require('express');
var app = express();
var bodyParser = require("body-parser");
var server = require('http').createServer(app);
var mustache = require('mustache-express');


app.use(express.static('views'));
app.engine('html', mustache());
app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", function(request, response){
	response.render("main.html");
})


app.post("/generate", function(request, response){
    const {spawn} = require('child_process');
    const pyProg = spawn('python3', ['./views/markovclass.py', "./views/captions2.txt", parseInt(request.body['n-gram'])]);
    var yo = {};
    pyProg.stdout.on('data', function(data) {
    	yo.text = data.toString();
        response.render("generator.html", yo);
    });
});

app.get("*", function(request, response){
	response.redirect("/");
});

server.listen(8000, function() {
	console.log("Bruce Analyzer website listening on localhost:8080");
});
