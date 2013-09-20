module.exports = function(karma) {
    karma.set({
        basePath: 'assets',

        files: [
          "vendor/jquery.js",
          "vendor/handlebars.js",
          "vendor/ember.js",
          "vendor/ember-data.js",
          "vendor/adapter.js",
          "vendor/jquery.mockjax.js",
          "js/app.js",
          "tests/*.js",
          "js/templates/*.handlebars"
        ],

        logLevel: karma.LOG_ERROR,
        browsers: ['PhantomJS'],
        singleRun: true,
        autoWatch: false,

        frameworks: ["qunit"],

        plugins: [
            'karma-qunit',
            'karma-chrome-launcher',
            'karma-ember-preprocessor',
            'karma-phantomjs-launcher'
        ],

        preprocessors: {
            "**/*.handlebars": 'ember'
        }
    });
};
