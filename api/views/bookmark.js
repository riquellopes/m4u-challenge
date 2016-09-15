// Bookmark views
var router = require('express').Router();

// Get middleware
var user = require("./middleware/user");

// Model
var Bookmark = require("../models/bookmark");

// List all
router.get("/", function(request, response){

});

// Get specific bookmark
router.get("/:id_bookmark", function(request, response){

});

// Delete specific bookmark
router.delete("/:id_bookmark", function(request, response){

});

// Save bookmark
router.post("/", function(request, response){

});

// Update bookmark
router.put("/:id_bookmark", function(){

});

router.use(user.UserMiddleware);
