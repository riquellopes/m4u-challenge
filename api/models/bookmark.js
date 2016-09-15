// Model BookMark
var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var BookMarkSchema = new Schema({
    user:{
        type: Schema.ObjectId,
        ref: 'UserSchema'
        required: true
    },
    url: {
        type: String,
        required: true
    }
});


var bookmark = module.exports = mongoose.model('BookMark', BookMarkSchema);
