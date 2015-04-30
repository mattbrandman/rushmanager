var app = angular.module('EventManagement', ['ui.bootstrap']);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

	app.controller('EventController', ['$http', function($http) {
		this.rushList = [];
		var _this = this;
		var promise = $http.post('/api/events/', )
		promise.success(function(data) {
			_this.rushList = data;
		});
		this.addRush = function(rush) {
			var promise = $http.post('/api/events/', )
		};
	}]);