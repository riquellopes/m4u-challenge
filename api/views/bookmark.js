// Bookmark views
var router = require('express').Router();
var log4js = require('log4js');

// Get logger
var logger = log4js.getLogger("booklog");

// Get middleware
var user = require("../middlewares/user");

// Model
var Bookmark = require("../models/bookmark");

router.use(user.UserMiddleware);


var hide_fields = "-user -__v";

// List all
router.get("/", function(request, response){
    var user = request.user;

    Bookmark.find({user:user}, hide_fields, function(error, list){
        if( error ){
            logger.error("Error");
        }

        logger.info("Bookmark size :: user", list.length, user._id);
        response.json(list);
    });

});

// Get specific bookmark
router.get("/:id_bookmark", function(request, response){
    var user = request.user;
    var id_bookmark = request.params.id_bookmark;

    logger.info("Get bookmark", id_bookmark, user._id);

    Bookmark.findOne({_id:id_bookmark, user:user}, hide_fields, function(error, document){
        if(error){
            logger.error("Error");
            return response.status(404).json({message: "not found"});
        }

        response.json(document);
    });
});

// Delete specific bookmark
router.delete("/:id_bookmark", function(request, response){
    var user = request.user;
    var id_bookmark = request.params.id_bookmark;

    Bookmark.remove({_id:id_bookmark, user:user}, function(error, document){
        if(error){
            logger.error("Error");
            return response.json({message: "Error."});
        }

        response.json({message: "Bookmark "+id_bookmark+" removed."});
    });
});

// Save bookmark
router.post("/", function(request, response){
    var bookmark = new Bookmark();
        bookmark.user = request.user;
        bookmark.url = request.body.url;

        bookmark.save(function(error, document){
            if( error ){
                return response.status(500).json({message: "Error ..."});
            }

            response.status(201).json({message: "successfull created."});
        });
});

// Update bookmark
router.put("/:id_bookmark", function(request, response){
    var user = request.user;
    var id_bookmark = request.params.id_bookmark;

    Bookmark.findOneAndUpdate({_id:id_bookmark, user:user}, {url:url}, function(error, document){
        if( error ){
            logger.error("Error put");
            return response.status(500).json({message: "Error ..."});
        }

        response.status(201).json({message: "successfully updated."})
    });
});

module.exports = router;
