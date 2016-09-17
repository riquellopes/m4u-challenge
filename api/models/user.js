// Model User
var mongoose = require('mongoose');
var bcrypt = require('bcrypt-nodejs');

var Schema = mongoose.Schema;

var UserSchema = new Schema({
    username:{
        type: String,
        unique: true,
        required: true
    },
    password:{
        type: String,
        required: true
    },
    create_at:{
        type: Date,
        default: Date.now
    },
    is_admin: {
        type: Boolean,
        default: false
    }
});

UserSchema.pre("save", function(next){
    var user = this;

    bcrypt.genSalt(5, function(error, salt){

        bcrypt.hash(user.password, salt, null, function(error, hash) {
            if (error){
                return next(err);
            }

            user.password = hash;
            next();
       });

    });

    next();
});

UserSchema.methods.validation = function(password, next){
    bcrypt.compare(password, this.password, function(error, isMatch){
        if( error ){
            return next(error);
        }

        next(isMatch);
    });
}

var user = module.exports = mongoose.model('User', UserSchema);
