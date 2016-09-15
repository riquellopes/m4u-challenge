// Start app
var express = require("express");

var app = exports.app = express();
var body_parser = require('body-parser');
var mongoose = require('mongoose');
var log4js = require('log4js');

var port = process.env.PORT || 5000;

var mongo_uri = process.env.MONGO_URI;

// Get logger
var logger = log4js.getLogger("booklog");

// Get views
var user = require("./views/user");
// var bookmark = require("./views/bookmark");

app.use(log4js.connectLogger(logger, { level: 'auto' }));
app.use(body_parser.urlencoded({ extended: true }));
app.use(body_parser.json());

app.set('json spaces', 2);
app.use("/user", user);
// app.use("/bookmark", bookmark);

// to connect
mongoose.connect(mongo_uri);

app.listen(port);
console.log('Start bookmark api on port ' + port);
