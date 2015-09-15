(function() {
var app = angular.module('directives', ['ui.bootstrap', 'ui.select', 'ngSanitize']);
	app.config(['$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'x-CSRFToken';
    $locationProvider.html5Mode(true);
}]);