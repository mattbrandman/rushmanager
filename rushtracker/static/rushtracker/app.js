(function(){

	var app = angular.module('RushApp', ['RushFactory', 'ngTable']);
	
	

	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}]);

	app.controller('RushTableController', ['Rush', 'NgTableParams', function(Rush, NgTableParams){
		var vm = this;
		this.rushes = Rush.query();
		this.tableParams = new NgTableParams({page: 1, count:10}, {getData: function($defer, params) {
			this.r
		}});
	}]);

})();