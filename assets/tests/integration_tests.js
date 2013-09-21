module('integration tests', {
    setup: function() {
        Ember.run(function() {
            App.reset();
        });
    },
    teardown: function() {
        $.mockjaxClear();
    }
});

test("user gives bad credentials and receives error message", function() {
    var login_response = {success: false, message: "bad user!", user_id: null}
    httpStub('/session/', login_response);

    visit("/").then(function() {
        fillIn(".username", "dustin");
        fillIn(".password", "wrong");
        return click(".submit");
    }).then(function() {
        equal(find(".text-danger").text(), "bad user!", "error message was not detected")
    })
});

test("user logs in and receives welcome message", function() {
    var dustin = {id: 1, username: "dustin", first_name: "Dustin", last_name: "Farris"}
    var login_response = {success: true, user_id: 1}
    httpStub('/session/', login_response);
    httpStub('/api/users/1/', dustin);

    visit("/").then(function() {
        fillIn(".username", "dustin");
        fillIn(".password", "right");
        return click('.submit');
    }).then(function() {
        equal(find("p.welcome").text(), "Welcome back, Dustin!", "welcome message was not detected");
    });
});
