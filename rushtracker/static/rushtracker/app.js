(function(){

	var app = angular.module('RushApp', ['RushFactory', 'ngTable']);
	
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}]);

	app.controller('RushTableController', ['Rush', 'NgTableParams' function(Rush, NgTableParams){
		var vm = this;
		var self = this;
		this.rushes = Rush.query();
		var data = this.rushes;
		self.tableParams = new NgTableParams({}, {data: data});
	}]);
})();