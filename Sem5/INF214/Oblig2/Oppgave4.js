// The reasson why this code has such a buggy behavour is beacuse in line 31
// we find that the method does not return anything after running the function,
// which again mean that before the .then is run after line 31
// the .then will run in the login function which result that the validateLogin
// function will return an undefined object, which causes all the buggy behaviour.


function login(req, res) {
    validateLogin(req.nameOrEmail, req.password).then(
        (result) => {
            // (BUG) Why does `result` has value `undefined` here?
        }
    )
};

function validateLogin(nameOrEmail, password) {
    var errors = {};
    if (validator.isEmpty(nameOrEmail)) {
        errors.nameOrEmail = 'username is required';
    }
    if (validator.isEmpty(password)) {
        errors.password = 'password is required';
    }
    return db.User.find({$or:[{ username: nameOrEmail }, { email: nameOrEmail }]})
        .then(existingUser => {
            // Bug:
            if (existingUser.length > 0) {
                // user exists, check if password matches hash
                var user = existingUser[0];
                bcrypt.compare(password, user.password_digest)
                    .then(valid => {
                        if (!valid){
                            errors.password = 'Invalid Password';
                        }
                        return { isValid: isEmpty(errors), errors };
                    })
            } else {
                errors.nameOrEmail = 'username or email does not exist';
                return { isValid: isEmpty(errors), errors };
            }
            // Bug
        });

}
